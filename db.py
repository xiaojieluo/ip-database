#!/usr/bin/env python
# coding=utf-8

from pymongo import MongoClient

class Db(object):

    def __init__(self, url='localhost', port=27017, database='database'):
        client = MongoClient(url, port)
        self.db = client[database]

db = Db().db
