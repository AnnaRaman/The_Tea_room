from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.db.models import Q

from products.models import Product
# Create your views
#  here.


def index(request):
    """ A view to return the index page """
    products = Product.objects.all()
    query = None

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't search anything!")
            return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'search_term': query,
        'products': products,
    }
    return render(request, 'home/index.html', context)


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None

    if request.GET:


        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't search anything!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,

    }

    return render(request, 'products/products.html', context)
