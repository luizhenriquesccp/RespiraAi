import os
import secrets
from urllib.parse import quote_plus

from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configuração da aplicação e da conexão com o banco de dados."""

    CURRENT_DATABASE = os.getenv("CURRENT_DATABASE", "mysql").lower()
    DB_USERNAME = os.getenv("DB_USERNAME", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "labinfo")
    DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME", "setembroamarelo")
    SECRET_KEY = os.getenv("SECRET_KEY") or secrets.token_hex(16)

    if CURRENT_DATABASE == "mysql":
        SQLALCHEMY_DATABASE_URI = (
            f"mysql+mysqlconnector://{quote_plus(DB_USERNAME)}:"
            f"{quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )
    elif CURRENT_DATABASE == "postgresql":
        SQLALCHEMY_DATABASE_URI = (
            f"postgresql://{quote_plus(DB_USERNAME)}:"
            f"{quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )
    else:
        raise ValueError(
            "CURRENT_DATABASE deve ser 'mysql' ou 'postgresql'."
        )
