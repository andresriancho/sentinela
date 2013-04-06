'''
disk_usage.py

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
import psutil

from sentinela.core.base_monitor import BaseMonitor


class DiskUsage(BaseMonitor):
    
    def __init__(self, max_usage):
        super(DiskUsage, self).__init__()
        
        # User configured
        self._max_usage = max_usage
        
    def call_every_minute(self):
        '''
        :return: Read the disk usage and compare it with self._max_usage, 
                 return True when the disk usage is greater than max_usage.
        '''
        # usage(total=213786, used=48097, free=154828, percent=22.5)
        usage = psutil.disk_usage('/')
        
        if usage.percent > self._max_usage:
                return True
            
        return False
    
    def reset(self):
        pass
    
    def get_name(self):
        '''
        :return: The name of this monitor to use in log files
        '''
        return 'disk_usage'
    