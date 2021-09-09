from django.shortcuts import render

links_menu = [
        {'href': 'main', 'name': 'домой'},
        {'href': 'products', 'name': 'продукты'},
        {'href': 'contacts', 'name': 'контакты'},
]
# Create your views here.
def main(request):
    return render(request, 'mainapp/index.html', {'title': 'магазин', 'links_menu': links_menu})

def products(request):
    return render(request, 'mainapp/products.html', {'title': 'каталог', 'links_menu': links_menu})

def contact(request):
    return render(request, 'mainapp/contact.html', {'title': 'контакты', 'links_menu': links_menu})
