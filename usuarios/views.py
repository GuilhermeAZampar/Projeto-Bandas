from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages

# Create your views here.
def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Cadastro realizado com sucesso!')
            return redirect('login')

    else:
        form=UserCreationForm()

    contexto={'form':form}
    return render(request,'usuarios/cadastro.html',contexto)


def login_usuario(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password= request.POST.get('password')

        usuario=authenticate(request,username=username,password=password)
        if usuario is not None:
            login(request,usuario)
            messages.success(request,'Login realizado com sucesso! ')
            return redirect('home')
        else:
            messages.error(request,'Usuário ou senha incorretos!')
            return render(request,'usuarios/login.html')
    return render(request,'usuarios/login.html')



def logout_usuario(request):
    logout(request)
    messages.success(request,'Logout realizado com sucesso!')
    return redirect('home')