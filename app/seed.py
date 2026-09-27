from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models import Exercicio


DEFAULT_EXERCICIOS = (
    (
        "Respiração Diafragmática",
        "Sente-se ou deite-se confortavelmente. Coloque uma mão sobre o peito e "
        "outra no abdômen. Inspire profundamente pelo nariz, expandindo o "
        "abdômen. Expire lentamente pela boca, contraindo a barriga.",
        6,
    ),
    (
        "Respiração Quadrada",
        "Inspire contando até 4, segure o ar por 4 segundos, expire em 4 "
        "segundos e segure novamente por 4 segundos antes de inspirar de novo. "
        "Repita por alguns minutos.",
        1,
    ),
    (
        "Respiração Alternada",
        "Com o polegar direito, feche a narina direita e inspire pela esquerda. "
        "Depois, feche a esquerda e expire pela direita. Inverta o processo e "
        "repita.",
        5,
    ),
    (
        "Respiração 4-7-8",
        "Inspire pelo nariz por 4 segundos, segure o ar por 7 segundos e expire "
        "lentamente pela boca por 8 segundos. Excelente para relaxamento e sono.",
        3,
    ),
    (
        "Respiração Contada",
        "Inspire profundamente e conte até 5. Expire contando novamente até 5. "
        "Mantenha o ritmo e concentre-se apenas na contagem e na respiração.",
        5,
    ),
    (
        "Respiração de Atenção Plena",
        "Sente-se com a coluna ereta, feche os olhos e concentre-se apenas na "
        "entrada e saída do ar pelas narinas. Se pensamentos surgirem, apenas "
        "observe e volte ao foco.",
        1,
    ),
    (
        "Respiração Profunda com Alongamento",
        "Enquanto inspira profundamente, levante os braços lentamente acima da "
        "cabeça. Expire devagar abaixando-os. Repita várias vezes, coordenando "
        "respiração e movimento.",
        2,
    ),
)


def seed_exercicios(db_session: Session) -> int:
    nomes_existentes = set(db_session.scalars(select(Exercicio.nome)).all())
    exercicios_faltantes = [
        Exercicio(nome=nome, descricao=descricao, duracao=duracao)
        for nome, descricao, duracao in DEFAULT_EXERCICIOS
        if nome not in nomes_existentes
    ]

    if exercicios_faltantes:
        db_session.add_all(exercicios_faltantes)
        db_session.commit()

    return len(exercicios_faltantes)
