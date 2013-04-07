'''
sentinela.py

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
import os
import sys
import time
import logging

import daemon

from core.utils.rule_handler import parse_rules, get_enabled_rules
from core.utils.operating_system import check_if_root, change_working_directory
from core.utils.log_handler import configure_logging
from core.sentinela import Sentinela

DELAY = 60
LOOPS = 0

def should_stop(max_loops):
    '''
    :return: True when the sentinela_loop should stop.
    '''
    if max_loops is None:
        return False
    
    if LOOPS >= max_loops:    
        return True
    
    return False

def log_alive():
    if LOOPS % 60 == 0:
        logging.debug('Sentinela is alive')

def inc_loop_counter():
    global LOOPS
    LOOPS += 1
    
def sentinela_loop(delay=DELAY, max_loops=None):
    '''
    :delay: Seconds to wait between each click()
    '''
    curr_dir = os.path.dirname(os.path.realpath(__file__))
    sentinela_cfg = os.path.join(curr_dir, 'config', 'sentinela.cfg')
    
    enabled_rules = get_enabled_rules(sentinela_cfg)
    rules = parse_rules(enabled_rules)
    
    st = Sentinela(rules)
    
    logging.info('Successfully started')
    
    while True:
        
        inc_loop_counter()
        if should_stop(max_loops): break
        
        try:
            st.click()
        except KeyboardInterrupt:
            logging.info('Received signal, exiting')
            break
        else:
            time.sleep(delay)
            log_alive()
    
def main():
    '''
    Project's main method that enters and infinite loop waiting for delay
    seconds each time.
    '''
    check_if_root()
    sentinela_root = change_working_directory()
        
    with daemon.DaemonContext(working_directory=sentinela_root):
        configure_logging()
        
        sentinela_loop()
    
    logging.info('Exit with code 0')
    sys.exit(0)
    
if __name__ == '__main__':
    main()