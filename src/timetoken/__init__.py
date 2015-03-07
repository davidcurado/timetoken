# -*- coding: utf-8 -*-
'''
Created on Mar 7, 2015
@author: José David Fernández Curado
'''
from datetime import date

from .utils import int_to_base36


VERSION = (0, 1, 0)
__version__ = ''.join(str(i) for i in VERSION)

class TimeConstrainedTokenGenerator(object):
    def _today(self):
        return date.today()
    def _days(self, dt = None):
        if not dt:
            dt = self._today()
        return (dt - date(2010, 1, 1)).days
    def text_value(self, user):
        return '%d:%s:%d' (
            user.id,
            user.password,
            self._days()
        )
    def create_token(self, user):
        return '%s-%s' % (
            int_to_base36(self._days()),
            ''
        )
    def verify_token(self, user, days = 7):
        pass

    pass
