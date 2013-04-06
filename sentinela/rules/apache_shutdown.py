from sentinela.modules.monitors.new_log_entries import NewLogEntries
from sentinela.modules.actions.shutdown import Shutdown

apache_log = NewLogEntries('/var/log/apache2/access.log', 10)
shutdown = Shutdown()


def call_every_minute():
    if apache_log.call_every_minute():
        shutdown.do()
    