'''
new_log_entries.py

Copyright 2013 Andres Riancho

This file is part of w3af, http://w3af.org/ .

w3af is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation version 2 of the License.

w3af is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with w3af; if not, write to the Free Software
Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
'''
from sentinela.core.base_monitor import BaseMonitor


class NewLogEntries(BaseMonitor):
    
    def __init__(self, logfile, max_wait):
        super(NewLogEntries, self).__init__()
        self._log_lines = None
        
        # User configured
        self._log_file = logfile
        self._max_wait = max_wait
        
    def call_every_minute(self):
        '''
        Read the number of log lines in self._log_file and return True if that
        number does NOT change in self.max_wait.
        
        :return: False if there is any type of file read error.        
        '''
        current_file_lines = 0
        try:
            for _ in file(self._log_file).readline():
                current_file_lines += 1
        except:
            return False
        else:
            if self._log_lines is None:
                self._log_lines = current_file_lines
            elif self._log_lines == current_file_lines:
                self.clicks += 1
            elif self._log_lines > current_file_lines:
                # This is the case where we handle log rotation
                self.clicks = 0
            elif self._log_lines < current_file_lines:
                # A new log entry was written to the log file
                self.clicks = 0
            
            if self.clicks == self._max_wait:
                self.reset()
                return True
            
        return False
    
    def reset(self):
        self.clicks = 0
        self._log_lines = None
    
    def get_name(self):
        '''
        :return: The name of this monitor to use in log files
        '''
        return 'new_log_entries'
    