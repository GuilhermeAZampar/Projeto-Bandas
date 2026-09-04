from django.db.models import Model
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

import usuarios
from .models import Banda ,Integrantes,Discos


class HomeViewTest(TestCase):

    def setUp(self):
        self.usuario=User.objects.create_user(username='test',password='12345678')
        self.banda=Banda.objects.create(nome='Metallica', estilo='Thrash Metal', descricao_banda='Banda teste', usuario=self.usuario)
    def testar_home_200(self):
        response=self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)

    def test_usa_template_correto(self):
        response= self.client.get(reverse('home'))
        self.assertTemplateUsed(response,'Projeto_Bandas/home.html')

    def test_busca(self):
        response=self.client.get(reverse('home'),{'q':'Metallica'})
        self.assertContains(response,'Metallica')

    def test_busca_erro(self):
        response=self.client.get(reverse('home'),{'q':'System'})
        self.assertContains(response,'Nenhuma banda encontrada')

    def test_busca_com_letra_minuscula(self):
        response=self.client.get(reverse('home'),{'q':'metallica'})
        self.assertContains(response,'Metallica')



class LoginViewTest(TestCase):

    def setUp(self):
        self.usuario=User.objects.create_user(username='test',password='12345678')

    def test_tela_login(self):
        response=self.client.get(reverse('login'))
        self.assertEqual(response.status_code,200)

    def test_template_login(self):
        response=self.client.get(reverse('login'))
        self.assertTemplateUsed(response,'usuarios/login.html')


    def test_login_dados_corretos(self):
        response=self.client.post(reverse('login'),{'username':'test','password':'12345678'})
        self.assertRedirects(response,reverse('home'))


    def test_login_senha_incorreta(self):
        response=self.client.post(reverse('login'),{'username':'test','password':'senha_errada'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'Usuário ou senha incorretos!')
        self.assertFalse(response.wsgi_request.user.is_authenticated)


class CadastroViewTest(TestCase):
    def test_tela_cadastro(self):
        response=self.client.get(reverse('cadastro'))
        self.assertEqual(response.status_code,200)

    def test_tela_cadastro_template(self):
        response=self.client.get(reverse('cadastro'))
        self.assertTemplateUsed(response,'usuarios/cadastro.html')

    def test_cadastro(self):
        response=self.client.post(reverse('cadastro'),{'username':'Wesley','password1':'senha_forte123!','password2':'senha_forte123!'})
        self.assertTrue(User.objects.filter(username='Wesley').exists())
        self.assertRedirects(response,reverse('login'))

    def test_cadastro_senha_diferente(self):
        response=self.client.post(reverse('cadastro'),{'username':'Wesley','password1':'senha_forte123!','password2':'Senha_errada123!'})
        self.assertFalse(User.objects.filter(username='Wesley').exists())
        self.assertEqual(response.status_code,200)


class Logoutview(TestCase):
    def setUp(self):
        self.usuario=User.objects.create_user(username='test',password='test1234!')


    def test_logout(self):
        self.client.login(username='test',password='test1234!')

        response=self.client.get(reverse('logout'))
        self.assertRedirects(response,reverse('home'))

        self.assertFalse(response.wsgi_request.user.is_authenticated)



class PermissaoBandaTest(TestCase):
    def setUp(self):
        self.usuario_dono=User.objects.create_user(username='test',password='test1234!')

        self.outro_usuario=User.objects.create_user(username='juan',password='juan123!')

        self.banda=Banda.objects.create(nome='System',estilo='NuMetal',descricao_banda='banda de numetal',usuario=self.usuario_dono)


    def test_outro_usuario(self):
        self.client.login(username='juan',password='juan123!')
        response=self.client.get(reverse('editar_banda',args=[self.banda.id]))

        self.assertRedirects(response,reverse('home'))


    def test_usuario_dono_editando(self):
        self.client.login(username='test',password='test1234!')

        response=self.client.get(reverse('editar_banda',args=[self.banda.id]))

        self.assertEqual(response.status_code,200)

    def test_outro_usuario_excluido(self):
        self.client.login(username='juan',password='juan123!')
        response=self.client.get(reverse('excluir_banda',args=[self.banda.id]))
        self.assertRedirects(response,reverse('home'))


    def test_usuario_excluido(self):
        self.client.login(username='test',password='test1234!')
        response=self.client.get(reverse('excluir_banda',args=[self.banda.id]))
        self.assertEqual(response.status_code,200)

    def test_usuario_excluindo_banda(self):
        self.client.login(username='test',password='test1234!')
        response=self.client.post(reverse('excluir_banda',args=[self.banda.id]))
        self.assertRedirects(response,reverse('home'))
        self.assertFalse(Banda.objects.filter(id=self.banda.id).exists())

    def test_outro_usuario_excluindo_banda(self):
        self.client.login(username='juan',password='juan123!')
        response=self.client.post(reverse('excluir_banda',args=[self.banda.id]))
        self.assertRedirects(response,reverse('home'))
        self.assertTrue(Banda.objects.filter(id=self.banda.id).exists())


    class IntegrantesTest(TestCase):

        def setUp(self):
            self.usuario_dono=User.objects.create_user(username='test',password='test1234!')
            self.usuario_errado=User.objects.create_user(username='juan',password='juan123!')
            self.banda=Banda.objects.create(nome='Metallica',estilo='Trhash Metal',descricao_banda='banda de metal',usuario=self.usuario_dono)
            self.integrante=Integrantes.objects.create(nome='James Hetfield',intrumento='Guitarra',banda=self.banda)

        def test_criar_integrante(self):
            self.client.login(username='test',password='test1234!')
            response=self.client.post(reverse('novo_integrate',args=[self.banda.id]),{'nome':'Kirk','instrumento':'Guitarra'})
            self.assertTrue(response,Integrantes.objects.filter(nome='Kirk',banda=self.banda).exists())
            self.assertRedirects(response,reverse('detalhes',args=[self.banda.id]))

        def test_usario_errado_editando(self):
            self.client.login(username='juan',password='juan123!')
            response=self.client.get(reverse('editar_integrante',args=[self.integrante.id]))
            self.assertRedirects(response,reverse('home'))

        def test_dono_editando(self):
            self.client.login(username='test',password='test1234!')
            response=self.client.get(reverse('editar_integrante',args=[self.integrante.id]))
            self.assertEqual(response.status_code,200)

        def test_excluir_integrante_usuario_errado(self):
            self.client.login(username='juan',password='juan123!')
            response=self.client.post(reverse('excluir_integrante',args=[self.integrante.id]))
            self.assertRedirects(response,reverse('home'))
            self.assertTrue(Integrantes.objects.filter(id=self.integrante.id).exists())


        def test_excluir_integrate_dono(self):
            self.client.login(username='test',password='test1234!')
            response=self.client.post(reverse('excluir_integrante',args=[self.integrante.id]))
            self.assertRedirects(response,reverse('detalhes',args=[self.banda.id]))
            self.assertFalse(Integrantes.objects.filter(id=self.integrante.id).exists())


class DiscosTestView(TestCase):
    def setUp(self):
        self.usuario_dono=User.objects.create_user(username='test',password='test1234!')
        self.usuario_errado=User.objects.create_user(username='juan',password='juan123!')
        self.banda=Banda.objects.create(nome='Metallica',estilo='Trash',descricao_banda='bandade metal',usuario=self.usuario_dono)
        self.disco=Discos.objects.create(nome='Ride',descricao_disco='Disco',ano=1986,banda=self.banda)

    def test_criar_disco(self):
        self.client.login(username='test',password='test1234!')
        response=self.client.post(reverse('cadastrar_disco',args=[self.banda.id]),{'nome':'Master','descricao_disco':'Teste','ano':1987})
        self.assertTrue(Discos.objects.filter(nome='Master',banda=self.banda).exists())
        self.assertRedirects(response,reverse('detalhes',args=[self.banda.id]))

    def test_usuario_errado_editando(self):
        self.client.login(username='juan',password='juan123!')
        response=self.client.get(reverse('editar_disco',args=[self.disco.id]))
        self.assertRedirects(response,reverse('home'))


    def test_dono_editando(self):
        self.client.login(username='test',password='test1234!')
        response=self.client.get(reverse('editar_disco',args=[self.disco.id]))
        self.assertEqual(response.status_code,200)


    def test_excluir_disco_usuario_errado(self):
        self.client.login(username='juan',password='juan123!')
        response=self.client.post(reverse('excluir_disco',args=[self.disco.id]))
        self.assertRedirects(response,reverse('home'))
        self.assertTrue(Discos.objects.filter(id=self.disco.id).exists())


    def test_excluir_disco_usuario_dono(self):
        self.client.login(username='test',password='test1234!')
        response=self.client.post(reverse('excluir_disco',args=[self.disco.id]))
        self.assertRedirects(response,reverse('detalhes',args=[self.banda.id]))
        self.assertFalse(Discos.objects.filter(id=self.disco.id).exists())


class LoginRequiredTestView(TestCase):
    def setUp(self):
        self.usuario=User.objects.create_user(username='test',password='test1234!')

    def test_usuario_sem_logar(self):
        response=self.client.get(reverse('nova_banda'))
        self.assertRedirects(response,f"{reverse('login')}?next={reverse('nova_banda')}")

    def test_usuario_logado(self):
        self.client.login(username='test',password='test1234!')
        response=self.client.get(reverse('nova_banda'))
        self.assertEqual(response.status_code,200)

    def test_criar_banda(self):
        self.client.login(username='test',password='test1234!')
        response=self.client.post(reverse('nova_banda'),{'nome':'Megadeth','estilo':'Trash','descricao_banda':'bandade metal'})
        self.assertTrue(Banda.objects.filter(nome='Megadeth').exists())
        banda=Banda.objects.get(nome='Megadeth')
        self.assertEqual(banda.usuario,self.usuario)
        self.assertRedirects(response,reverse('home'))