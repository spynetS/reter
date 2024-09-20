#!/usr/bin/env python3

from core.controller import *
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

class TestController (Controller):
    # Define a data model using Pydantic
    @route('/add','POST')
    async def add(self,name: str = Form(...), password : str = Form(...)):
        await self.model.database.query(f"insert into users (name,password) values ('{name}','{password}')")
        return await self.add_GET()

    @route('/add','GET')
    async def add_GET(self):
        res = list(await self.model.database.query("select * from users"))
        name = await self.model.get_user("alfred")
        return HTMLResponse(self.render('add.html',{'res':res,'name':name[0][0]}))

    @route('/','GET')
    async def test(self):
        name = await self.model.get_name()
        return HTMLResponse(self.render('test/index.html',{'name': name}))
