#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @namespace pyfortified_logging
"""
Helpers: Singleton
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        # print('Singleton', cls.__name__, '__call__')
        if cls not in cls._instances:
            new_instance = super(Singleton, cls).__call__(*args, **kwargs)
            cls._instances[cls] = new_instance

        instance = cls._instances[cls]
        # print('Singleton', cls.__name__, id(instance))
        return instance
