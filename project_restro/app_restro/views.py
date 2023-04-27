from django.shortcuts import render
from .forms import CategoryCreateForm, MenuCreateForm
from .models import Category, Menu

# Create your views here.
def menu_index(request):
    return render(request, 'menus/index.html')

def menu_add(request):
    menu_form = MenuCreateForm()
    context = {
        "form" : menu_form,
        "title" : "Menu Create Form"
    }
    
    if request.method == "POST":
        id = request.POST.get('category_id')
        category_id = Category.objects.get(id=id)

        # Method-one: non-argumented constructor
        # data = Menu()
        # data.menu_title = request.POST.get('menu_title')
        # data.menu_desc = request.POST.get('menu_desc')
        # data.menu_ingredient = request.POST.get('menu_ingredient')
        # data.menu_price = request.POST.get('menu_price')
        # data.category_id = category_id
        # data.save()
        # context.update({
        #     "desc" : data.menu_desc
        #     })
        
        # # Method-two: argumented constructor
        # menu_title = request.POST.get('menu_title')
        # menu_desc = request.POST.get('menu_desc')
        # menu_ingredient = request.POST.get('menu_ingredient')
        # menu_price = request.POST.get('menu_price')

        # data = Menu(menu_title=menu_title, menu_desc=menu_desc,
        #             menu_ingredient=menu_ingredient, menu_price=menu_price)
        # data.save()

        # Method-three: form object
        data = MenuCreateForm(request.POST)
        if data.is_valid():
            data.save()


        
    return render(request, 'menus/create.html', context)

def menu_edit(request):
    return render(request, 'menus/edit.html')

def menu_show(request):
    return render(request, 'menus/show.html')

#category views
def category_create(request):
    form = CategoryCreateForm()
    context = {
        "form" : form,
        "title" : "Category Create Form"
    }
    return render(request, "menus/add_category.html", context)