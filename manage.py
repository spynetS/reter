#!/usr/bin/env python3
from flagser import *
import os
from fastapi import FastAPI
from mvc.model import Model

from test.controller import TestController

def create_app(args):
    os.mkdir(args[0])
    os.chdir(args[0])


def run(args):
    app = FastAPI()
    con = TestController(Model(None))
    app.include_router(con)

manager = FlagManager([
    Flag('createapp',"creates a new mvc app",onCall = create_app),
    Flag('run',"runs the server",onCall=run)
])

manager.check()
