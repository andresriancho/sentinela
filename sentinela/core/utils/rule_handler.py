'''
rule_handler.py

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
import logging


def parse_rules(enabled_rules):
    '''
    Read all rules from the rule_path and return a list of all functors
    which need to be called every minute.
    
    :enabled_rules: A string list with rule names.
    '''        
    functors = []
    
    for rule in enabled_rules:

        '''
        Reminder:
        >>> __import__('sentinela.rules.apache_debug', fromlist=['apache_debug'])
        <module 'sentinela.rules.apache_debug' from 'sentinela/rules/apache_debug.pyc'>
        '''
        
        module_name = 'sentinela.rules.%s' % (rule)
        
        try:
            module_inst = __import__(module_name, fromlist=[rule])
        except Exception, e:
            msg = 'Failed to import the "%s" rule. Exception: "%s".'
            logging.exception(msg % (module_name, e))
        else:
            logging.debug('Imported %s' % module_name)
            
            cev = 'call_every_minute'
            functor = getattr(module_inst, cev, None)
            
            if functor is None:
                msg = 'The %s rule does NOT define the required %s'
                logging.error(msg % (module_name, cev))
                continue
            
            functors.append(functor)
    
    return functors

def get_enabled_rules(config_file):
    '''
    Read the config file and return the list of enabled rules.
    '''
    enabled_rules = []
    
    try:        
        config_file_handler = file(config_file)
    except:
        logging.exception('Failed to open sentinela config "%s"' % config_file)
    else:
    
        for rule_name in config_file_handler.readlines():
            rule_name = rule_name.strip()
            
            if rule_name.startswith('#'):
                continue
            
            if not rule_name:
                continue
            
            enabled_rules.append(rule_name)

    return enabled_rules