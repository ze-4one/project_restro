from django.shortcuts import render, redirect
from .forms import CategoryCreateForm, MenuCreateForm
from .models import Category, Menu

# Create your views here.
def menu_index(request):
    data = Menu.objects.all()
    context = {"data": data}
    return render(request, 'menus/index.html', context)

# def menu_add(request):
#     menu_form = MenuCreateForm()
#     context = {
#         "form": menu_form,
#         "title": "Menu Create Form"
#     }

#     if request.method == "POST":
#         id = request.POST.get('category_id')
#         category_id = Category.objects.get(id=id)

#         # method one: non-argumented constructor
#         # data = Menu()
#         # data.menu_title = request.POST.get('menu_title')
#         # data.menu_desc = request.POST.get('menu_desc')
#         # data.menu_ingredient = request.POST.get('menu_ingredient')
#         # data.menu_price = request.POST.get('menu_price')
#         # data.category_id = category_id
#         # data.save()
        
#         # method two: argumented constructor
#         # menu_title = request.POST.get('menu_title')
#         # menu_desc = request.POST.get('menu_desc')
#         # menu_ingredient = request.POST.get('menu_ingredient')
#         # menu_price = request.POST.get('menu_price')

#         # data = Menu(menu_title=menu_title, menu_desc=menu_desc,menu_ingredient=menu_ingredient,
#         #             menu_price=menu_price)
#         # data.save()

#         # method three: form object
#         data = MenuCreateForm(request.POST)
#         if data.is_valid():
#             data.save()

#     return render(request, 'menus/create.html', context)

def menu_add(request):
    if request.method == "POST":
        data = MenuCreateForm(request.POST)
        if data.is_valid():
            # Retrieve the category_id from the POST data
            category_id = request.POST.get('category_id')
            try:
                # Attempt to retrieve the corresponding Category instance
                category = Category.objects.get(id=int(category_id))
            except (ValueError, Category.DoesNotExist):
                # Handle invalid category_id values or nonexistent Category instances
                context = {
                    "form": data,
                    "title": "Menu Create Form",
                    "desc": "Invalid category selected."
                }
                return render(request, 'menus/create.html', context)

            # Create a new Menu instance with the validated form data
            menu = data.save(commit=False)
            menu.category = category
            menu.save()

            # Redirect the user to the list of menus
            return redirect('menu-list')

    # If the request method is GET or the form data is invalid, render the form page
    menu_form = MenuCreateForm()
    context = {
        "form": menu_form,
        "title": "Menu Create Form"
    }
    return render(request, 'menus/create.html', context)


def menu_update(request):
    if request.method == "POST":
        id = request.POST.get('category_id')
        print(id)
        category_id = Category.objects.get(id=id)

        data = Menu.objects.get(id=request.POST.get('id'))
        data.menu_title = request.POST.get('menu_title')
        data.menu_desc = request.POST.get('menu_desc')
        data.menu_ingredient = request.POST.get('menu_ingredient')
        data.menu_price = request.POST.get('menu_price')
        data.category_id = category_id
        data.save()

        return redirect("menu-list")

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
# def category_create(request):
#     form = CategoryCreateForm()
#     context = {
#         "form": form,
#         "title": "Category Create Form"
#     }
#     return render(request, "menus/add_category.html", context)

def category_create(request):
    if request.method == "POST":
        form = CategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("menu-list")
    else:
        form = CategoryCreateForm()

    context = {
        "form": form,
        "title": "Category Create Form"
    }
    return render(request, "menus/add_category.html", context)