import requests
from django.core.cache import cache

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
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        data = response.json()
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
