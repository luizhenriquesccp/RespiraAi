"""Modelos ORM do banco de dados do RespiraAi."""

from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    """Classe base para todos os modelos da aplicação."""


class Exercicio(Base):
    """Exercício de respiração disponível para prática."""

    __tablename__ = "exercicio"

    id_exercicio: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    nome: Mapped[str | None] = mapped_column(String(100), nullable=True)
    descricao: Mapped[str | None] = mapped_column(String(1000), nullable=True)
    duracao: Mapped[int | None] = mapped_column(Integer, nullable=True)

    praticas: Mapped[list["Pratica"]] = relationship(
        back_populates="exercicio",
    )


class Usuario(Base):
    """Usuário cadastrado na aplicação."""

    __tablename__ = "usuario"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nome: Mapped[str | None] = mapped_column(String(50), nullable=True)
    email: Mapped[str | None] = mapped_column(String(50), nullable=True)
    senha: Mapped[str | None] = mapped_column(String(6), nullable=True)

    praticas: Mapped[list["Pratica"]] = relationship(
        back_populates="usuario",
    )


class Pratica(Base):
    """Registro de uma prática realizada por um usuário."""

    __tablename__ = "pratica"

    id_pratica: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )
    data: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    tempo_dedicado: Mapped[int | None] = mapped_column(Integer, nullable=True)
    id_usuario: Mapped[int | None] = mapped_column(
        ForeignKey("usuario.id"),
        nullable=True,
        index=True,
    )
    id_exercicio: Mapped[int | None] = mapped_column(
        ForeignKey("exercicio.id_exercicio"),
        nullable=True,
        index=True,
    )

    usuario: Mapped[Usuario | None] = relationship(
        back_populates="praticas",
    )
    exercicio: Mapped[Exercicio | None] = relationship(
        back_populates="praticas",
    )


__all__ = ["Base", "Exercicio", "Pratica", "Usuario"]
