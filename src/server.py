from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, status
from typing import List
from src.infra.sqlalchemy.config.database import get_db
from src.routers import rotas_produtos, rotas_usuarios



app = FastAPI()

#CORS 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Rotas PRODUTOS

app.include_router(rotas_produtos.router)



#Rotas USUARIOS

app.include_router(rotas_usuarios.router)