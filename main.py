from fastapi import FastAPI
from core.database import Database, MySqlDataBase
from core.model import Model

from test.controller import TestController
from test.model import TestModel


DATABASE_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "my-secret-pw",
    "db": "rater",
}

# Initialize FastAPI app
app = FastAPI()

# Initialize the database object
database = MySqlDataBase()

# Define the controllers
con = TestController("test/views",TestModel(database))
app.include_router(con.router)


# Define FastAPI lifecycle events for connecting and disconnecting the database

@app.on_event("startup")
async def startup():
    # Connect to the database asynchronously when the app starts
    await database.connect(DATABASE_CONFIG)

@app.on_event("shutdown")
async def shutdown():
    # Disconnect from the database when the app shuts down
    await database.close()
