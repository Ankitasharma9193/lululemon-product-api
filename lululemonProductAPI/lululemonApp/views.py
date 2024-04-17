from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .utils import fetch_product_details, paginate

def get_product_details(request):
    urls = [
        "https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json",
        "https://shop.lululemon.com/c/accessories/_/N-1z0xcmkZ1z0xl44Z8ok?format=json"
    ]

    product_details_list = []

    for url in urls:
        product_details = fetch_product_details(url)
        if product_details:
            product_details_list.extend(product_details)

    page = paginate(request, product_details_list)
    
    return JsonResponse(list(page.object_list), safe=False)

    

