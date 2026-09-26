from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Usuario


class AuthenticationService:
    @staticmethod
    def login(
        db_session: Session,
        email: str | None,
        senha: str | None,
    ) -> Usuario | None:
        return db_session.scalar(
            select(Usuario).where(
                Usuario.email == email,
                Usuario.senha == senha,
            )
        )