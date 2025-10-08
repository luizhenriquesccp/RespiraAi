# RespiraAi - Aplicação Flask

## Descrição

O RespiraAi é uma aplicação web desenvolvida em Flask para exercícios de respiração e bem-estar. A aplicação foi modificada para usar rotas Flask ao invés de JavaScript para navegação e funcionalidades.

## Funcionalidades

### Rotas Implementadas

- **`/`** - Página inicial com estatísticas e navegação
- **`/login`** - Página de login (GET e POST)
- **`/cadastro`** - Página de cadastro (GET e POST)
- **`/exercicios`** - Lista de exercícios disponíveis
- **`/exercicio/<id>`** - Exercício específico por ID
- **`/historico`** - Histórico de práticas do usuário
- **`/salvar_pratica`** - API para salvar práticas (POST)
- **`/api/estatisticas`** - API para obter estatísticas do usuário
- **`/estatisticas`** - Redireciona para página inicial com estatísticas
- **`/logout`** - Logout do usuário

### Modificações Realizadas

1. **Substituição de JavaScript por Flask**:
   - Removidos arquivos JS de login, cadastro e exercícios
   - Implementadas rotas Flask para processar formulários
   - Criada API para estatísticas usando Flask

2. **Atualização dos Templates HTML**:
   - Links de navegação agora usam `url_for()` do Flask
   - Formulários modificados para usar métodos POST do Flask
   - CSS links atualizados para usar `url_for('static')`

3. **Sistema de Sessões**:
   - Implementado sistema de login/logout com sessões Flask
   - Histórico de práticas vinculado ao usuário logado

4. **Banco de Dados Simulado**:
   - Dados armazenados em memória (dicionários Python)
   - Exercícios pré-definidos no código
   - Sistema de usuários e práticas em memória

## Como Executar

### Pré-requisitos

- Python 3.7+
- Flask

### Instalação

1. Navegue até o diretório do projeto:
```bash
cd respira_ai_flask
```

2. Instale as dependências:
```bash
pip install flask
```

3. Execute a aplicação:
```bash
python app.py
```

4. Acesse no navegador:
```
http://localhost:5000
```

## Estrutura do Projeto

```
respira_ai_flask/
├── app.py                 # Aplicação Flask principal
├── templates/             # Templates HTML
│   ├── index.html        # Página inicial
│   ├── login.html        # Página de login
│   ├── cadastro.html     # Página de cadastro
│   ├── ex.html           # Página de exercícios
│   └── h.html            # Página de histórico
├── static/               # Arquivos estáticos
│   ├── css/             # Arquivos CSS
│   └── js/              # Arquivos JS (ignorados)
└── README.md            # Este arquivo
```

## Funcionalidades Principais

### Sistema de Usuários
- Cadastro de novos usuários
- Login/logout com sessões
- Dados armazenados em memória

### Exercícios de Respiração
- 3 exercícios pré-definidos:
  - Respiração 4-7-8 (3 min)
  - Respiração Quadrada (5 min)
  - Respiração Alternada (5 min)

### Histórico e Estatísticas
- Registro de práticas realizadas
- Estatísticas por usuário
- Visualização de histórico

## Observações

- **Dados em Memória**: Os dados são armazenados em memória e serão perdidos ao reiniciar a aplicação
- **JavaScript Removido**: Conforme solicitado, os arquivos JavaScript foram ignorados e suas funcionalidades implementadas no Flask
- **Desenvolvimento**: A aplicação está configurada para modo de desenvolvimento (`debug=True`)

## Próximos Passos

Para uso em produção, considere:
- Implementar banco de dados real (SQLite, PostgreSQL, etc.)
- Adicionar validações de segurança
- Implementar hash de senhas
- Configurar para ambiente de produção
