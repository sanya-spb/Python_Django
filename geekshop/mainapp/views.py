from django.shortcuts import render
from mainapp.models import Product

links_menu = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products:index', 'name': 'продукты'},
        {'href': 'contacts', 'name': 'контакты'},
]
# Create your views here.
def main(request):
    # return render(request, 'mainapp/index.html', {'title': 'магазин', 'links_menu': links_menu})
    title = 'магазин'
    products = Product.objects.all()[:4]
    content = {'title': title, 'products': products, 'links_menu': links_menu}

    return render(request, 'mainapp/index.html', content)

def products(request):
    title = 'каталог'
    # products = Product.objects.all()[:4]
    content = {'title': title, 'links_menu': links_menu}

    return render(request, 'mainapp/products.html', content)

def contact(request):
    title = 'контакты'
    # products = Product.objects.all()[:4]
    content = {'title': title, 'links_menu': links_menu}

    return render(request, 'mainapp/contact.html', content)
