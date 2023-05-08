from django.shortcuts import render, redirect
from .forms import CategoryCreateForm, MenuCreateForm
from .models import Category, Menu
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/authentication/login')
def menu_index(request):
    data = Menu.objects.all()
    categories = Category.objects.all()
    context = {"data": data, "categories": categories}
    if request.method == 'POST':
        if request.POST.get('id') is not None:
            filter_list = Menu.objects.filter(id=request.POST.get('id'))
        if request.POST.get('category_id') is not None:
            filter_list = Menu.objects.filter(category_id=request.POST.get('category_id'))

        context.update({"data":filter_list})


    return render(request, 'menus/index.html', context)

@login_required(login_url='/authentication/login')

def menu_add(request):
    menu_form = MenuCreateForm()
    context = {
        "form": menu_form,
        "title": "Menu Create Form"
    }

    if request.method == "POST":
        id = request.POST.get('category_id')
        category_id = Category.objects.get(id=id)

        # method one: non-argumented constructor
        # data = Menu()
        # data.menu_title = request.POST.get('menu_title')
        # data.menu_desc = request.POST.get('menu_desc')
        # data.menu_ingredient = request.POST.get('menu_ingredient')
        # data.menu_price = request.POST.get('menu_price')
        # data.category_id = category_id
        # data.save()
        
        # method two: argumented constructor
        # menu_title = request.POST.get('menu_title')
        # menu_desc = request.POST.get('menu_desc')
        # menu_ingredient = request.POST.get('menu_ingredient')
        # menu_price = request.POST.get('menu_price')

        # data = Menu(menu_title=menu_title, menu_desc=menu_desc,menu_ingredient=menu_ingredient,
        #             menu_price=menu_price)
        # data.save()

        # method three: form object
        data = MenuCreateForm(request.POST, request.FILES)
        if data.is_valid():
            data.save()

    return render(request, 'menus/create.html', context)


@login_required(login_url='/authentication/login')

def menu_update(request):
    if request.method == "POST":
        id = request.POST.get('category_id')
        category_id = Category.objects.get(id=id)

        data = Menu.objects.get(id=request.POST.get('id'))
        data.menu_title = request.POST.get('menu_title')
        data.menu_desc = request.POST.get('menu_desc')
        data.menu_ingredient = request.POST.get('menu_ingredient')
        data.menu_price = request.POST.get('menu_price')
        data.menu_img = request.FILES.get('menu_img')
        data.category_id = category_id
        data.save()

        return redirect("menu-list")


@login_required(login_url='/authentication/login')

def menu_edit(request, id):
    data = Menu.objects.get(id=id)
    categories = Category.objects.all()
    context = {"data": data, "categories": categories}
    return render(request, 'menus/edit.html', context)

def menu_show(request, id):
    data = Menu.objects.get(id=id)
    context = {"data": data}
    return render(request, 'menus/show.html', context)

def menu_delete(request, id):
    data = Menu.objects.get(id=id)
    data.delete()

    return redirect("menu-list")

# category views
@login_required(login_url='/authentication/login')
def category_create(request):
    form = CategoryCreateForm()
    context = {
        "form": form,
        "title": "Category Create Form"
    }
    return render(request, "menus/add_category.html", context)