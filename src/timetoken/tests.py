# -*- coding: utf-8 -*-
'''
Created on Mar 7, 2015
@author: José David Fernández Curado
'''
import logging
import random
import unittest

from timetoken import TimeConstrainedTokenGenerator
from timetoken.utils import int_to_base36, base36_to_int


class User(object):
    def __init__(self, uid = 10, password = 'password'):
        self.id = uid
        self.password = password

class UtilsTest(unittest.TestCase):
    def setUp(self):
        logging.getLogger().setLevel(logging.CRITICAL)
        self.tg = TimeConstrainedTokenGenerator()
    def test_int_to_base36(self):
        self.assertEqual(int_to_base36(0), '0', 'int_to_base36(0)')
        self.assertEqual(int_to_base36(10), 'a', 'int_to_base36(10)')
        self.assertEqual(int_to_base36(36), '10', 'int_to_base36(36)')
        self.assertEqual(int_to_base36(72), '20', 'int_to_base36(72)')

    def test_base36_to_int(self):
        self.assertEqual(base36_to_int('0'), 0, "base36_to_int('0')")
        self.assertEqual(base36_to_int('a'), 10, "base36_to_int('a')")
        self.assertEqual(base36_to_int('10'), 36, "base36_to_int('10')")
        self.assertEqual(base36_to_int('20'), 72, "base36_to_int('20')")

    def test_tokens(self):
        n = 1000
        while n > 0:
            user = User(uid = random.randint(0, 1000), password = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(10)))
            token = self.tg.create_token(user)
            self.assertTrue(self.tg.verify_token(user, token, 1))
            n -= 1

    def test_weird_tokens(self):
        self.assertFalse(self.tg.verify_token(User(), 'fijidsolff'))
