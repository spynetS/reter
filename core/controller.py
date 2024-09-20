#!/usr/bin/env python3

from fastapi import APIRouter
from core.model import Model
import os

from jinja2 import Environment, FileSystemLoader

# Custom decorator to register routes
def route(path: str, method: str):
    def decorator(func):
        # Store route info in the function object for later use
        func._path = path
        func._method = method
        return func
    return decorator

class Controller:
    def __init__(self, views:str,model):
       self.model = model
       self.file_loader = FileSystemLoader(views)


       self.router = APIRouter()
       # Dynamically register routes after the class is instantiated
       for attr_name in dir(self):
           attr = getattr(self, attr_name)
           if hasattr(attr, "_path") and hasattr(attr, "_method"):
               self.router.add_api_route(attr._path, attr, methods=[attr._method])#

    def render(self,template_name,data):
        # Create an environment that loads templates from the file system
        env = Environment(loader=self.file_loader)
        # # Load the template by its filename
        template = env.get_template(template_name)
        # # Render the template with the provided data
        return template.render(data)
