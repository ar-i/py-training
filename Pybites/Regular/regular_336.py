#!/usr/bin/env python3
# https://codechalleng.es/bites/336/

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def default_endpoint():
    return {"message":  "Welcome to PyBites' FastAPI Learning Path 🐍 🎉"}
