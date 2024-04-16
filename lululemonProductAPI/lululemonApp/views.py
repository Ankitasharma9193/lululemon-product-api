from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .utils import fetch_product_details

from django.core.cache import cache

def get_product_details(request):
    print('~~~~~~~~~~~~~~~~~~`', request);
    # Define a cache key based on the request parameters (if needed)
    cache_key = f"product_details_{request.user.id}"  # Customize this key as per your use case

    # Attempt to retrieve cached data
    cached_data = cache.get(cache_key)

    if cached_data:
        # If cached data exists, return it directly
        return JsonResponse(cached_data, safe=False)
    else:
        urls = [
            "https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json",
            "https://shop.lululemon.com/c/accessories/_/N-1z0xcmkZ1z0xl44Z8ok?format=json"
        ]
        product_details_list = []
        for url in urls:
            product_details = fetch_product_details(url)
            if product_details:
                product_details_list.append(product_details)

         # Cache the fetched data for future requests (adjust the timeout as needed)
        cache.set(cache_key, product_details_list, timeout=3600)  # Cache for 1 hour (3600 seconds)

        return JsonResponse(product_details_list, safe=False);

