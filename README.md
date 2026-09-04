# 🎸 Projeto Bandas

Aplicação web desenvolvida com Django para gerenciamento de bandas, integrantes e discos.

O projeto permite que usuários criem suas próprias contas e gerenciem bandas, integrantes e discografias, contando com autenticação, controle de permissões, uploads de arquivos, sistema de busca, mensagens de feedback, testes automatizados e containerização com Podman.

## 🚀 Funcionalidades

- Cadastro de usuários
- Login e logout
- Autenticação de usuários
- Proteção de rotas com `@login_required`
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
- Upload de arquivos de mídia
- Busca de bandas por nome
- Mensagens de sucesso e erro
- Controle de permissões por usuário
- Interface responsiva
- Testes automatizados
- Containerização com Podman

## 🔐 Autenticação e permissões

Cada banda é associada ao usuário responsável pelo seu cadastro.

A aplicação possui controle de autorização para impedir que um usuário edite ou exclua bandas pertencentes a outro usuário.

As mesmas regras são aplicadas aos integrantes e discos relacionados às bandas.

A estrutura principal dos relacionamentos é:

```text
Usuário
  └── Banda
       ├── Integrantes
       └── Discos
```

Dessa forma, integrantes e discos são protegidos de acordo com o proprietário da banda à qual pertencem.

As páginas responsáveis pela criação e gerenciamento dos dados também utilizam `@login_required`, impedindo o acesso de usuários não autenticados.

## 🎸 Gerenciamento de bandas

Usuários autenticados podem cadastrar suas próprias bandas.

Cada banda pode possuir informações como:

- Nome
- Estilo musical
- Descrição
- Imagem
- Links e redes sociais
- Integrantes
- Discos

O usuário responsável pela criação da banda é automaticamente associado a ela.

Somente o proprietário pode editar ou excluir seus dados.

## 👥 Gerenciamento de integrantes

Cada banda pode possuir diversos integrantes.

É possível:

- Cadastrar integrante
- Editar integrante
- Excluir integrante
- Definir nome
- Definir instrumento ou função

Os integrantes ficam relacionados diretamente à banda cadastrada.

## 💿 Gerenciamento de discos

As bandas também podem possuir discos cadastrados.

É possível:

- Cadastrar disco
- Editar disco
- Excluir disco
- Informar nome
- Informar ano
- Adicionar descrição
- Fazer upload da capa

Cada disco fica relacionado à sua respectiva banda.

## 🔎 Sistema de busca

A página inicial possui uma barra de busca para localizar bandas pelo nome.

A busca utiliza `icontains` do Django ORM, permitindo pesquisas sem diferenciação entre letras maiúsculas e minúsculas.

Por exemplo:

```text
metallica
Metallica
METALLICA
```

As três pesquisas podem localizar a mesma banda.

Quando nenhuma banda é encontrada, a aplicação informa ao usuário que não existem resultados para aquela pesquisa.

## 💬 Sistema de mensagens

A aplicação utiliza o sistema de mensagens do Django para fornecer feedback após determinadas operações.

Exemplos:

- Cadastro realizado com sucesso
- Login realizado com sucesso
- Logout realizado com sucesso
- Banda cadastrada com sucesso
- Banda atualizada com sucesso
- Banda excluída
- Integrante cadastrado
- Integrante atualizado
- Integrante excluído
- Disco cadastrado
- Disco atualizado
- Disco excluído
- Credenciais de login inválidas

As mensagens podem ser fechadas pelo usuário e também desaparecem automaticamente após alguns segundos.

## 🧪 Testes automatizados

O projeto possui uma suíte com **28 testes automatizados** utilizando `TestCase` do Django.

Os testes foram desenvolvidos para validar tanto o funcionamento das páginas quanto regras de negócio, autenticação, permissões e alterações realizadas no banco de dados.

Entre os cenários testados estão:

- Carregamento da Home
- Status HTTP das views
- Utilização do template correto
- Busca de bandas
- Busca sem resultados
- Busca ignorando maiúsculas e minúsculas
- Página de login
- Template de login
- Login com credenciais válidas
- Login com credenciais inválidas
- Verificação de usuário não autenticado após login inválido
- Página de cadastro
- Template de cadastro
- Criação de usuário
- Tentativa de cadastro com senhas diferentes
- Logout
- Proteção de rotas com `@login_required`
- Acesso de usuário autenticado
- Criação de bandas
- Associação da banda ao usuário autenticado
- Criação de integrantes
- Criação de discos
- Permissões para edição de bandas
- Permissões para edição de integrantes
- Permissões para edição de discos
- Exclusão de bandas
- Exclusão de integrantes
- Exclusão de discos
- Tentativas de alteração por usuários sem permissão
- Verificação dos dados diretamente no banco de testes

Para executar todos os testes localmente:

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

O Django cria automaticamente um banco separado para a execução dos testes e o remove após a finalização.

## 🛠️ Tecnologias utilizadas

- Python
- Django
- Django ORM
- Django Authentication
- Django TestCase
- SQLite
- HTML5
- CSS3
- JavaScript
- Pillow
- Podman
- Compose
- Dockerfile
- Git
- GitHub

## 📦 Dependências

As dependências do projeto estão disponíveis no arquivo:

```text
requirements.txt
```

Atualmente o projeto utiliza:

```text
asgiref==3.12.1
Django==6.1
pillow==12.3.0
sqlparse==0.5.5
tzdata==2026.3
```

Para instalar todas as dependências:

```bash
pip install -r requirements.txt
```

## 📁 Estrutura do projeto

```text
ProjetoBandas/
│
├── Projeto_Bandas/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── apps.py
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
│
├── media/
│
├── manage.py
├── db.sqlite3
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── compose.yml
└── README.md
```

## ⚙️ Executando localmente

Clone o repositório:

```bash
git clone SEU_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd Projeto-Bandas
```

Crie um ambiente virtual.

### Windows

```bash
python -m venv .venv
```

Ative o ambiente:

```bash
.venv\Scripts\activate
```

### Linux/macOS

```bash
python3 -m venv .venv
```

Ative o ambiente:

```bash
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

## 🐳 Executando com Podman

O projeto também possui suporte à execução em container utilizando Podman e Compose.

Primeiro, inicie a máquina do Podman:

```bash
podman machine start
```

Na raiz do projeto, construa a imagem e inicie o container:

```bash
podman compose up --build
```

Após a inicialização, a aplicação ficará disponível em:

```text
http://127.0.0.1:8000/
```

Para iniciar novamente sem reconstruir a imagem:

```bash
podman compose up
```

Para encerrar os containers:

```bash
podman compose down
```

## 🧪 Executando os testes no Podman

Com o container em execução, os testes também podem ser executados diretamente dentro dele:

```bash
podman compose exec web python manage.py test
```

A suíte completa também foi validada dentro do container:

```text
Found 28 test(s).
............................
Ran 28 tests

OK
```

Isso garante que a aplicação e seus testes funcionam corretamente no ambiente containerizado.

## 💾 Persistência durante o desenvolvimento

Durante o desenvolvimento, o diretório do projeto é montado dentro do container:

```yaml
volumes:
  - .:/app
```

Dessa forma, alterações feitas no código ficam imediatamente disponíveis dentro do container.

O banco SQLite e os arquivos armazenados no diretório `media/` também permanecem no diretório do projeto durante o ambiente de desenvolvimento.

Assim, executar:

```bash
podman compose down
```

e posteriormente:

```bash
podman compose up
```

não remove os dados armazenados no diretório local do projeto.

## 🐳 Containerização

O projeto utiliza os seguintes arquivos para containerização:

```text
Dockerfile
.dockerignore
compose.yml
requirements.txt
```

O `Dockerfile` é responsável por:

- Definir a imagem Python
- Configurar o diretório da aplicação
- Instalar as dependências
- Copiar os arquivos do projeto
- Expor a porta 8000
- Iniciar o servidor Django

O `compose.yml` facilita a construção e execução do container durante o desenvolvimento.

## 📚 Conceitos aplicados

Durante o desenvolvimento deste projeto foram aplicados conceitos como:

- Models
- Relacionamentos entre models
- Foreign Keys
- Django ORM
- Forms
- ModelForms
- Function-Based Views
- Templates
- Template inheritance
- Arquivos estáticos
- Upload de arquivos
- Autenticação
- Sessões
- Login e logout
- Controle de permissões
- `@login_required`
- CRUD
- Busca com Django ORM
- Query parameters
- Django Messages
- Testes automatizados
- Banco de dados de testes
- HTTP GET e POST
- Redirects
- Containerização
- Podman
- Compose
- Gerenciamento de dependências
- Git e GitHub

## 🎯 Objetivo do projeto

O Projeto Bandas foi desenvolvido com foco no aprendizado e aplicação prática de desenvolvimento Back-end com Python e Django.

O objetivo foi construir uma aplicação completa, passando desde a modelagem dos dados até autenticação, permissões, CRUD, testes automatizados e containerização.

O projeto também foi utilizado para aprofundar conhecimentos em organização de aplicações Django, segurança de acesso aos dados e testes de regras de negócio.

## 👨‍💻 Autor

**Guilherme Zampar**

Desenvolvedor Full Stack Python com foco em Back-end.

GitHub: GuilhermeAZampar
