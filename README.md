Projeto Bandas

Desenvolvi esta aplicação para reunir informações de bandas, integrantes e discos em um só lugar. Cada usuário pode criar uma conta e gerenciar suas próprias bandas, com descrições, imagens, links e arquivos de mídia.

Implementei cadastro e login, busca por nome e controle de permissões para que apenas o responsável possa editar ou excluir seus registros. A interface é responsiva e exibe mensagens de sucesso e erro.

Utilizei Python, Django e SQLite no ambiente local, com HTML, CSS e JavaScript na interface. O projeto conta com 28 testes automatizados de funcionalidades, autenticação e permissões, além de execução com Podman e Compose.

Teste a aplicação: [Projeto Bandas](https://projeto-bandas-nine.vercel.app/)

Para executar localmente:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Acesse http://127.0.0.1:8000/. Também é possível executar com Podman:

```bash
podman compose up --build
```

Para rodar os testes:

```bash
python manage.py test
```

Desenvolvido por [Guilherme Zampar](https://github.com/GuilhermeAZampar).
