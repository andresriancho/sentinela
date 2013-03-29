'''
base_action.py

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


class BaseAction(object):
    def do(self):
        '''
        Runs the action (shutdown, remove a file, wget a URL, etc.) that was
        intended to perform.
        
        :return: True if the action was successful.
        '''
        raise NotImplementedError
    
    def get_name(self):
        '''
        :return: The name of this action to use in log files
        '''
        return 'base_action'
    