from fastapi import FastAPI
from fastapi.responses import JSONResponse
from starlette.requests import Request

app = FastAPI()

@app.get("/")
def main():
    return "RAIZ API -Metodo GET"

@app.get("/hello/")
def hello():
    return "Este es el API Inicial del ITI-621"

@app.get("/api/personas/")
def getPersonas():
    return {"id":"208490055", "Nombre":"Eithel", "telefono":"84599184" }