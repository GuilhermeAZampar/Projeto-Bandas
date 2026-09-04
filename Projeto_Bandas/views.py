from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Banda,Integrantes,Discos
from .forms import BandaForm,IntegranteForm,DiscoForm
from django.contrib import messages


def home(request):
    busca = request.GET.get('q')
    bandas=Banda.objects.all()
    if busca:
        bandas=bandas.filter(nome__icontains=busca)

    contexto={'bandas':bandas,'busca':busca}

    return render(request,'Projeto_Bandas/home.html',contexto)


def detalhes(request,id):
    banda=get_object_or_404(Banda,id=id)
    contexto={'banda':banda}
    return render(request,'Projeto_Bandas/detalhes.html',contexto)


@login_required
def nova_banda(request):
    if request.method=='POST':
        form=BandaForm(request.POST,request.FILES)
        if form.is_valid():
            banda=form.save(commit=False)
            banda.usuario=request.user
            banda.save()
            messages.success(request,'Banda cadastrada com sucesso!!')
            return redirect('home')

    else:
        form=BandaForm()

    contexto={'form':form}

    return render(request,'Projeto_Bandas/nova_banda.html',contexto)




@login_required
def editar_banda(request,id):
    banda=get_object_or_404(Banda,id=id)
    if banda.usuario != request.user:
        return redirect('home')
    if request.method=='POST':
        form = BandaForm(request.POST,request.FILES,instance=banda)
        if form.is_valid():
            form.save()
            messages.success(request,'Banda atualizada com sucesso!')
            return redirect('detalhes',id=banda.id)
    else:
        form = BandaForm(instance=banda)

    contexto={'form':form,'banda':banda}
    return render(request,'Projeto_Bandas/editar_banda.html',contexto)





@login_required
def excluir_banda(request,id):
    banda=get_object_or_404(Banda,id=id)
    if banda.usuario != request.user:
        return redirect('home')

    if request.method=='POST':
        banda.delete()
        messages.success(request,'Banda excluida com sucesso! ')
        return redirect('home')

    contexto={'banda':banda}
    return render(request,'Projeto_Bandas/excluir_banda.html',contexto)



@login_required
def novo_integrante(request,id):
    banda=get_object_or_404(Banda,id=id)
    if banda.usuario != request.user:
        return redirect ('home')

    if request.method=='POST':
        form =IntegranteForm(request.POST)
        if form.is_valid():
            integrante=form.save(commit=False)
            integrante.banda=banda
            integrante.save()
            messages.success(request,"Integrante cadastrado com sucesso!")
            return redirect('detalhes',id=banda.id)
    else:
        form=IntegranteForm()


    contexto={'form':form,'banda':banda}
    return render(request,'Projeto_Bandas/novo_integrante.html',contexto)


@login_required
def editar_integrante(request,id):
    integrante=get_object_or_404(Integrantes,id=id)
    banda=integrante.banda
    if banda.usuario != request.user:
        return redirect('home')
    if request.method=="POST":
        form=IntegranteForm(request.POST,instance=integrante)
        if form.is_valid():
            form.save()
            messages.success(request,'Integrante atualizado com sucesso!')
            return redirect('detalhes',id=banda.id)
    else:
        form=IntegranteForm(instance=integrante)

    contexto={'form':form,'integrante':integrante,'banda':banda}
    return render(request,'Projeto_Bandas/editar_integrante.html',contexto)




@login_required
def excluir_integrante(request,id):
    integrante=get_object_or_404(Integrantes,id=id)
    banda=integrante.banda
    if banda.usuario != request.user:
        return redirect('home')
    if request.method=="POST":
        integrante.delete()
        messages.success(request,'integrante excluido com sucesso')
        return redirect('detalhes',id=banda.id)

    contexto = {'integrante':integrante,'banda':banda}
    return render(request,'Projeto_Bandas/excluir_integrante.html',contexto)


@login_required
def cadastrar_disco(request,id):
    banda=get_object_or_404(Banda,id=id)
    if banda.usuario != request.user:
        return redirect('home')
    if request.method=="POST":
        form=DiscoForm(request.POST,request.FILES)
        if form.is_valid():
            disco=form.save(commit=False)
            disco.banda=banda
            disco.save()
            messages.success(request,'Disco cadastrado com sucesso!')
            return redirect('detalhes',id=banda.id)

    else:
        form=DiscoForm()

    contexto={'form':form,'banda':banda}
    return render(request,'Projeto_Bandas/cadastrar_disco.html',contexto)



@login_required
def editar_disco(request,id):
    disco=get_object_or_404(Discos,id=id)
    banda=disco.banda
    if banda.usuario != request.user:
        return redirect('home')
    if request.method == "POST":
        form = DiscoForm(request.POST,request.FILES,instance=disco)
        if form.is_valid():
            form.save()
            messages.success(request,'Disco editado com sucesso!')
            return redirect('detalhes',id=banda.id)
    else:
        form=DiscoForm(instance=disco)

    contexto ={'form':form,'disco':disco,'banda':banda}
    return render(request,'Projeto_Bandas/editar_disco.html',contexto)



@login_required
def excluir_disco(request,id):
    disco=get_object_or_404(Discos,id=id)
    banda=disco.banda
    if banda.usuario != request.user:
        return redirect('home')
    if request.method == "POST":
        disco.delete()
        messages.success(request,'Disco excluido com sucesso!')
        return redirect('detalhes',id=banda.id)

    contexto={'disco':disco,'banda':banda}
    return render (request,'Projeto_Bandas/excluir_disco.html',contexto)
