from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .utils import fetch_product_details

from django.core.cache import cache
from django.views.decorators.cache import cache_page

# @cache_page(60 * 15) # Cache for 15 minutes

def get_product_details(request):
    urls = [
        "https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json",
        "https://shop.lululemon.com/c/accessories/_/N-1z0xcmkZ1z0xl44Z8ok?format=json"
    ]
    product_details_list = []
    for url in urls:
        product_details = fetch_product_details(url)
        if product_details:
            product_details_list.append(product_details)
    return JsonResponse(product_details_list, safe=False)

