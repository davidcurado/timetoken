# -*- coding: utf-8 -*-
'''
Created on Mar 7, 2015
@author: José David Fernández Curado
'''
from datetime import date
import hashlib

from timetoken.utils import base36_to_int

from .utils import int_to_base36


VERSION = (0, 1, 0)
__version__ = ''.join(str(i) for i in VERSION)

class TimeConstrainedTokenGenerator(object):
    def hash(self, s):
        return hashlib.sha512(s).hexdigest()
    def _today(self):
        return date.today()
    def _days(self, dt = None):
        if not dt:
            dt = self._today()
        return (dt - date(2010, 1, 1)).days
    def text_value(self, user, cdate):
        return '%d:%s:%d' (
            user.id,
            user.password,
            cdate
        )
    def create_token(self, user):
        return '%s-%s' % (
            int_to_base36(self._days()),
            self.hash(self.text_value(user, self._days()))
        )
    def verify_token(self, user, token, days = 7):
        days, text = token.split('-')
        return text == self.text_value(user, base36_to_int(days))

def includeme(config):
    config.add_request_method(lambda: TimeConstrainedTokenGenerator(), 'token_generator', reify = True)