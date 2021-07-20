
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from . import views
from .models import Product
from .forms import ProductForm

def admin_console(request):
    products = Product.objects.all()
    return render(request, 'products/products_page.html', {'products': products})

def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(Product, pk=pk) # pk = pk is dictionary values|go check for the item if its not there don't crash just give a 404 error
    form = ProductForm(data=request.POST or None, instance=item) #
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('admin_console')
        else:
            print(form.errors)
    else:
        return render(request, 'products/present_product.html', {'form':form})

def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('admin_console')
    context = {"item": item, }
    return render(request, "products/confirmDelete.html", context)


def confirmed(request):
    if request.method == 'POST':
        form = ProductForm(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('admin_console')
    else:
        return redirect('admin_console')