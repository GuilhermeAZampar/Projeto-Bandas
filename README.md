# 🎸 Projeto Bandas

Aplicação web desenvolvida com Django para gerenciamento de bandas, integrantes e discos.

O projeto permite que usuários criem suas próprias contas e gerenciem bandas, integrantes e discografias, contando com autenticação, controle de permissões, busca e testes automatizados.

## 🚀 Funcionalidades

- Cadastro de usuários
- Login e logout
- Autenticação de usuários
- Controle de acesso com `@login_required`
- Cadastro de bandas
- Edição de bandas
- Exclusão de bandas
- Cadastro de integrantes
- Edição de integrantes
- Exclusão de integrantes
- Cadastro de discos
- Edição de discos
- Exclusão de discos
- Upload de imagens
- Busca de bandas por nome
- Mensagens de sucesso e erro
- Controle de permissões por usuário
- Interface responsiva

## 🔐 Autenticação e permissões

Cada banda é associada ao usuário responsável pelo seu cadastro.

A aplicação possui verificações de autorização para impedir que um usuário edite ou exclua bandas pertencentes a outro usuário.

As mesmas regras são aplicadas aos integrantes e discos relacionados às bandas.

Exemplo da relação entre os dados:

```text
Usuário
  └── Banda
       ├── Integrantes
       └── Discos
```

## 🔎 Sistema de busca

A página inicial possui uma barra de busca que permite pesquisar bandas pelo nome.

A busca utiliza `icontains`, permitindo pesquisas sem diferenciação entre letras maiúsculas e minúsculas.

Exemplo:

```text
metallica
Metallica
METALLICA
```

As três pesquisas podem encontrar a mesma banda.

## 🧪 Testes automatizados

O projeto possui uma suíte com **28 testes automatizados** utilizando o sistema de testes do Django.

Os testes verificam funcionalidades como:

- Carregamento da Home
- Templates utilizados pelas views
- Sistema de busca
- Busca sem resultados
- Cadastro de usuários
- Login com credenciais válidas
- Login com credenciais inválidas
- Logout
- Proteção de rotas com `@login_required`
- Criação de bandas
- Criação de integrantes
- Criação de discos
- Edição e exclusão
- Permissões entre diferentes usuários
- Persistência e exclusão dos dados no banco

Para executar todos os testes:

```bash
python manage.py test
```

Resultado atual:

```text
Found 28 test(s).
............................
Ran 28 tests

OK
```

## 🛠️ Tecnologias utilizadas

- Python
- Django
- HTML5
- CSS3
- JavaScript
- SQLite
- Django ORM
- Django Authentication
- Django TestCase

## 📁 Estrutura principal

```text
ProjetoBandas/
│
├── Projeto_Bandas/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── usuarios/
│   ├── templates/
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── config/
├── manage.py
└── README.md
```

## ⚙️ Como executar o projeto

Clone o repositório:

```bash
git clone URL_DO_SEU_REPOSITORIO
```

Entre na pasta:

```bash
cd ProjetoBandas
```

Crie um ambiente virtual:

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute as migrations:

```bash
python manage.py migrate
```

Inicie o servidor:

```bash
python manage.py runserver
```

A aplicação ficará disponível em:

```text
http://127.0.0.1:8000/
```

## 🧪 Executando os testes

Com o ambiente virtual ativado:

```bash
python manage.py test
```

O Django cria automaticamente um banco de dados separado para a execução dos testes e o remove após a finalização.

## 📚 Objetivo do projeto

Este projeto foi desenvolvido com foco no estudo e aplicação prática de desenvolvimento Back-end com Django.

Durante o desenvolvimento foram trabalhados conceitos como:

- Models e relacionamentos
- Django ORM
- Forms e ModelForms
- Function-Based Views
- Templates
- Arquivos estáticos
- Autenticação
- Sessões
- Permissões
- Upload de arquivos
- CRUD
- Busca
- Mensagens
- Testes automatizados
- Organização de aplicações Django

## 👨‍💻 Autor

**Guilherme Zampar**

Desenvolvedor Full Stack Python com foco em Back-end.

GitHub: GuilhermeAZampar
