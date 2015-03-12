# -*- coding: utf-8 -*-
'''
Created on Mar 7, 2015
@author: José David Fernández Curado
'''
from datetime import date
import hashlib
import logging

from timetoken.utils import base36_to_int

from .utils import int_to_base36


VERSION = (0, 1, 0)
__version__ = ''.join(str(i) for i in VERSION)

class TimeConstrainedTokenGenerator(object):
    base_date = date(2010, 1, 1)
    def __init__(self, hashf = 'sha512', password = ''):
        self.hashf = hashf
        self.password = password
    def hash(self, s):
        return hashlib.new(self.hashf, s).hexdigest()
    def _today(self):
        return date.today()
    def _days(self, dt = None):
        if not dt:
            dt = self._today()
        return (dt - date(2010, 1, 1)).days
    def text_value(self, user, cdate):
        return '%d:%s:%s:%d' % (
            user.id,
            user.password,
            self.password,
            cdate
        )
    def create_token(self, user):
        return '%s-%s' % (
            int_to_base36(self._days()),
            self.hash(self.text_value(user, self._days()))
        )
    def verify_token(self, user, token, days = 7):
        try:
            cdate, text = token.split('-')
            cdate = base36_to_int(cdate)
            days_passed = self._days(self._today()) - cdate
            gentext = self.hash(self.text_value(user, cdate))
            if text != gentext:
                logging.info('Token did not match: %s != %s' % (text, gentext))
                return False
            if days_passed > days:
                logging.info('Token has expired!')
                return False
            return True
        except Exception as e:
            logging.exception(e.message)
            return False
