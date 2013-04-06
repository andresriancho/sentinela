Sentinela
=========
[![Build Status](https://travis-ci.org/andresriancho/sentinela.png?branch=master)](https://travis-ci.org/andresriancho/sentinela)

Sentinela is a highly configurable operating system watchdog which can take actions based on pre-configured rules.

The initial motivation was to create a daemon that would monitor a set of log files and if no activity was present shutdown the operating system. This was extremely useful for making sure my ec2 instances were shut down after a specified idle time.

Given Sentinela's modular nature, you can also extend it to monitor network traffic, processes, disk usage, etc. and run any actions such as sending an email, send a SNMP alert, etc.

Basic configuration
===================

Sentinela configured using the `config/sentinela.cfg` file, which allows you to enable rules which are going to be run.

Rules are defined in python code and are found in the `rules/` directory. In most cases rules use two different types of modules:
 * `modules/monitors/`: Once every minute read from a resource and store it's status. When required return `True` to trigger an action.
 * `modules/actions/`: Actions will run a command, send an email or any other python defined code you can imagine.

Running Sentinela
=================

To start sentinela you need to run:
```
sudo python sentinela.py
```

You can monitor all sentinela actions by reading the `/var/log/sentinela.log` file. A regular sentinela log file looks like this:

```
[2013-03-29 11:41:20,440][INFO] Successfully started
[2013-03-29 11:41:20,441][DEBUG] Imported rules.apache_shutdown
[2013-03-29 12:51:50,480][DEBUG] Sentinela is alive
...
[2013-03-29 12:58:34,009][DEBUG] Going to execute command "shutdown now -h".
```

Creating your own rules
=======================

Creating your own rules is easy. Lets understand the basics by looking at this example rule:

```
1: from modules.monitors.new_log_entries import NewLogEntries
2: from modules.actions.debug_print import DebugPrint
3: 
4: apache_log = NewLogEntries('/var/log/apache2/access.log', 10)
5: debug_print = DebugPrint()
6:
7:
8: def call_every_minute():
9:     if apache_log.call_every_minute():
10:        debug_print.do(apache_log)
```

Common rules will have a monitor and an action, in this case they `NewLogEntries` and `DebugPrint` (lines 1 and 2).

Both of them need to be instanciated at the module level (lines 4 and 5) in order to be able to keep state. If you create your monitor or action instances inside the `call_every_minute` a new instance is going to be created each time and no state will be kept.

Monitors and actions can have parameters, in this line 4 we see how the `NewLogEntries` monitor takes two parameters:
 * The log file to monitor for changes
 * How many minutes of inactivity it will wait until returning `True`

The `call_every_minute` function (line 8) needs to be defined for a rule to be valid. This function, as the name indicates, will be called every minute by sentinela. You could define any actions to be run in this context, but we decide to call the monitor's `call_every_minute` method and based on it's return value call the action with the `apache_log` instance as parameter.

`apache_log.call_every_minute()` will return `True` only if the file passed as parameter doesn't have any new entries in 10 minutes.

`debug_print.do` will print the name of the monitor passed as parameter.

To sum up, we can say that this rule will 'Print the name of the monitor to sentinela's log file when the `/var/log/apache2/access.log` logfile is inactive during 10 minutes'.

Once you've created your own rule, you'll have to follow these steps to run them:
 * Copy your `.py` file to the `rules/` directory in the sentinela installation
 * Update the `config/sentinela.cfg` to include your rule name (without the extension)
 * Restart the sentinela daemon

