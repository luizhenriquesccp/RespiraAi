from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import Config
from app.models import Base, Exercicio, Pratica, Usuario


app = Flask(__name__)
app.config.from_object(Config)

engine = create_engine(
    app.config["SQLALCHEMY_DATABASE_URI"],
    pool_pre_ping=True,
)
SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False,
)


def create_tables() -> None:
    """Cria as tabelas mapeadas caso ainda não existam."""
    Base.metadata.create_all(bind=engine)


__all__ = [
    "Base",
    "Exercicio",
    "Pratica",
    "SessionLocal",
    "Usuario",
    "app",
    "create_tables",
    "engine",
]
