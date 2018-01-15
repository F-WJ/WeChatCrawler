# _*_ coding: utf-8 _*_
__author__ = 'FWJ'
__date__ = 2018 / 1 / 13

from mongoengine import connect

connect('test', host='localhost', port=27017)