#!/usr/bin/env python3
from core.model import Model

class TestModel(Model):
    name = "alfred"

    async def get_user(self,name):
        res = await self.database.query(f"select * from users where name='{name}'")
        print(res)
        return res
