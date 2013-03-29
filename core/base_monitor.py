'''
base_monitor.py

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


class BaseMonitor(object):
    
    def __init__(self):
        # Internal counter useful for keeping track of "how many times X
        # happen", where X is measured in call_every_minute
        self.clicks = 0
    
    def call_every_minute(self):
        '''
        Monitors a resource and returns True when the configured actions should
        be called. The core will call this method every minute, which is useful
        for creating monitors that "run actions if there is no X in Y minutes".
        
        :return: True when a log file is full, there is too much RAM being
                 used, etc.
        '''
        raise NotImplementedError

    def reset(self):
        '''
        :return: None, just reset the self.clicks and other internal variables
                 It should be called by call_every_minute before returning True
        '''
        raise NotImplementedError
    
    def get_name(self):
        '''
        :return: The name of this monitor to use in log files
        '''
        return 'base_monitor'
    