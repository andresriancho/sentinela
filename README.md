Sentinela
=========

Sentinela is a highly configurable operating system watchdog which can take actions based on pre-configured rules.

The initial motivation was to create a daemon that would monitor a set of log files and if no activity was present shutdown the operating system. This was extremely useful for making sure my ec2 instances were shut down after a specified idle time.

Given Sentinela's modular nature, you can also extend it to monitor network traffic, processes, disk usage, etc. and run any actions such as sending an email, send a SNMP alert, etc.

Usage
=====

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

