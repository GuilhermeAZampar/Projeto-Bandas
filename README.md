Projeto Bandas

Desenvolvi este projeto para colocar em prática meus estudos de back-end com Python e Django. A aplicação permite criar uma conta e cadastrar bandas, seus integrantes e discos, com informações como estilo musical, descrição, imagens e links.

Acesse a aplicação: Projeto Bandas

Cada usuário pode editar e excluir apenas as bandas que cadastrou, incluindo os integrantes e discos associados a elas. O sistema também conta com busca de bandas por nome, upload de imagens e arquivos de mídia, mensagens de sucesso e erro e uma interface adaptada para computadores e celulares.

Utilizei Django e SQLite no back-end, com HTML, CSS e JavaScript na interface. O projeto possui 28 testes automatizados para verificar funcionalidades, autenticação e permissões, além de configuração para execução em containers com Podman e Compose.

Para executar localmente, instale as dependências, aplique as migrations e inicie o servidor:

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Também é possível executar com Podman:

podman compose up --build

Localmente, a aplicação ficará disponível em http://127.0.0.1:8000/.

Para rodar os testes:

python manage.py test

Ou, com o container em execução:

podman compose exec web python manage.py test

Desenvolvido por Guilherme Zampar.
