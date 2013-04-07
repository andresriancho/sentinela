'''
test_sentinela.py

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

from mock import MagicMock

from sentinela.core.sentinela import Sentinela

    
class TestSentinela(unittest.TestCase):
    
    def test_clicks(self):
        rule_click = MagicMock()

        rules = [rule_click,]
        
        s = Sentinela(rules)
        s.click()
        
        self.assertEqual(rule_click.call_count, 1)
        s.click()
        
        self.assertEqual(rule_click.call_count, 2)

    def test_clicks_exception(self):
        rule_click = MagicMock(side_effect=Exception())

        rules = [rule_click,]
        
        s = Sentinela(rules)
        s.click()
        
        self.assertEqual(rule_click.call_count, 1)
        s.click()
        
        self.assertEqual(rule_click.call_count, 1)
