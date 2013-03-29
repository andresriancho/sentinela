'''
main.py

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
import sys
import time
import logging

import daemon

from core.utils.rule_handler import parse_rules, get_enabled_rules
from core.utils.operating_system import check_if_root
from core.utils.log_handler import configure_logging
from core.sentinela import Sentinela

def main():
    check_if_root()

    with daemon.DaemonContext(working_directory='.',):
        configure_logging()
        
        # TODO: The 'rules/' should be a command line argument
        enabled_rules = get_enabled_rules()
        rules = parse_rules('rules/', enabled_rules)
        
        st = Sentinela(rules)
        
        logging.info('Successfully started')
        is_alive = 0
        
        while True:
            try:
                st.click()
                time.sleep(60)
            except KeyboardInterrupt:
                logging.info('Received signal. Exiting')
                break
            else:
                is_alive += 1
                if is_alive == 60:
                    logging.debug('Sentinela is alive')
                    is_alive = 0
    
    sys.exit(0)
    
if __name__ == '__main__':
    main()