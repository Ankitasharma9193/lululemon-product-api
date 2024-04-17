import requests
from django.core.cache import cache

#Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def fetch_product_details(url):
    # Define a cache key based on the request parameters
    cache_key = url

    # Attempt to retrieve cached data
    cached_data = cache.get(cache_key)

    if cached_data:
        # If cached data exists, return it directly
        return cached_data

    # If cached data does not exist, fetch data from the API
    product_list = []
    # Make a GET request to the API
    try:
        response = requests.get(url)

        # Raise an exception for 4xx and 5xx status codes
        response.raise_for_status() 

        # Parse the response data
        data = response.json()

        # Extract the product details from the response data
        products = data.get("contents", [])[0].get("mainContent", [])[0].get("contents", [])[0].get("records", [])
        for product in products:
            product_details = {
                "product_display_name": product.get("attributes", {}).get("product.displayName"),
                "product_price": product.get("attributes", {}).get("product.price"),
                "product_avialable_size": product.get("attributes", {}).get("product.allAvailableSizes"),
                "product_sku_images": product.get("attributes", {}).get("product.sku.skuImages"),
                "product_parent_category": product.get("attributes", {}).get("product.defaultParentCategory"),
                "product_currency_code": product.get("attributes", {}).get("currencyCode"),
                "url": url
            }

            # Append the product details to the list
            product_list.append(product_details)

        # set the fetched data in the cache
        cache.set(cache_key, product_list, timeout=3600)  # Cache for 1 hour (3600 seconds)

        # Return the product list
        return product_list

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def paginate(request, product_details_list):
    PER_PAGE_ITEMS_LIMIT = 10

    # Get the page number from query parameters (default to 1)
    page_number = int(request.GET.get('page', 1))
    # Default page size is 10
    page_size = int(request.GET.get('limit', PER_PAGE_ITEMS_LIMIT))

    # Paginate the product details list, 10 items per page
    paginator = Paginator(product_details_list, per_page = page_size) 

    try:
        # Get the specified page of products
        page_obj = paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        page_obj = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        page_obj = paginator.page(paginator.num_pages)

    return page_obj
