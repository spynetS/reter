#!/usr/bin/env python3
import aiomysql

# abastract class for databasees
class Database():
    def __init__(self):
        self.connection = None

    async def connect(self,args: dict):
        pass
    async def close(self):
        pass
    async def query(self,_query:str):
        pass

# mysql database from Database
class MySqlDataBase(Database):
    async def connect(self,args:dict):
        self.connection = await aiomysql.connect(**args)

    async def query(self, _query:str):
        async with self.connection.cursor() as cursor:
            await cursor.execute(_query)
            result = await cursor.fetchall()
            return result

    async def close(self):
        await self.connection.close()
