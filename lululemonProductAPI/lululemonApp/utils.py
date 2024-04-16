import requests
from django.core.cache import cache
from django.views.decorators.cache import cache_page

@cache_page(60 * 15) # Cache for 15 minutes

def fetch_product_details(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        data = response.json()
        product = data.get("contents", [])[0].get("mainContent", [])[0].get("contents", [])[0].get("records", [])[0]
        product_details = {
            "product_display_name": product.get("attributes", {}).get("product.displayName"),
            "url": url
            # Add any extra fields here
        }
        return product_details
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None
