from flask import abort, request, session


PERMISSOES_ROTAS = {
	"adicionar_exercicio": ["ADMIN"],
	"editar_exercicio": ["ADMIN"],
	"painel_administrador": ["ADMIN"],
	"excluir_usuario": ["ADMIN"],
}


def autorizar(lista_permissoes):
	"""Verifica se o perfil da sessão possui uma das permissões informadas."""
	if session.get("administrador"):
		perfil = "ADMIN"
	elif session.get("usuario"):
		perfil = "USUARIO"
	else:
		perfil = None

	if perfil not in lista_permissoes:
		abort(403)

	return None


def verificar_autorizacao():
	"""Aplica as permissões cadastradas para a rota atual."""
	lista_permissoes = PERMISSOES_ROTAS.get(request.endpoint)

	if lista_permissoes is None:
		return None

	return autorizar(lista_permissoes)
