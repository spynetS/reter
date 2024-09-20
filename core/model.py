#!/usr/bin/env python3

from core.database import Database


class Model:
    def __init__(self, database: Database):
        self.database = database
