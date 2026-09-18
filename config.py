import os
from urllib.parse import quote_plus


class Config:
    """Configuração da aplicação e da conexão com o banco de dados."""

    SECRET_KEY = os.getenv("SECRET_KEY", "respira-ai-development-key")

    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_NAME = os.getenv("DB_NAME", "setembroamarelo")

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        (
            f"mysql+mysqlconnector://{quote_plus(DB_USER)}:"
            f"{quote_plus(DB_PASSWORD)}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        ),
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
