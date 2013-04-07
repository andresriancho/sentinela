'''
test_rule_handler.py

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
import unittest
import tempfile
import os
import types

from sentinela.core.utils.rule_handler import get_enabled_rules, parse_rules


class TestRuleHandler(unittest.TestCase):
    def test_get_enabled_rules(self):
        temp_rules_file_name = tempfile.mktemp()
        
        temp_rules_file = file(temp_rules_file_name, 'w')
        temp_rules_file.write('# comment\n')
        temp_rules_file.write('rule1\n')
        temp_rules_file.write('# comment2\n')
        temp_rules_file.write('rule2\n')
        temp_rules_file.close()
        
        rules = get_enabled_rules(temp_rules_file_name)
        
        self.assertEqual(set(rules), set(['rule1', 'rule2']))
        
        os.remove(temp_rules_file_name)
        
    def test_parse_rules(self):
        functors = parse_rules(['apache_debug',])
        
        self.assertEqual(len(functors), 1)
        
        functor = functors[0]
        self.assertIsInstance(functor, types.FunctionType)
        