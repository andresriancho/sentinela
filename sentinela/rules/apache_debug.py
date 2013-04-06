from sentinela.modules.monitors.new_log_entries import NewLogEntries
from sentinela.modules.actions.debug_print import DebugPrint

apache_log = NewLogEntries('/var/log/apache2/access.log', 10)
debug_print = DebugPrint()


def call_every_minute():
    if apache_log.call_every_minute():
        debug_print.do(apache_log)
    