import requests

def fetch_product_details(url):
    print('~~~~~~ URL:',url)
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx and 5xx status codes
        data = response.json()
        product = data.get("contents", [])[0].get("mainContent", [])[0].get("contents", [])[0].get("records", [])[0]
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print(product)
        product_details = {
            "product_display_name": product.get("attributes", {}).get("product.displayName"),
            "product_price": product.get("attributes", {}).get("product.price"),
            "product_avialable_size": product.get("attributes", {}).get("product.allAvailableSizes"),
            "product_sku_images": product.get("attributes", {}).get("product.sku.skuImages"),
            "product_parent_category": product.get("attributes", {}).get("product.defaultParentCategory"),
            "product_currency_code": product.get("attributes", {}).get("currencyCode"),
            "url": url
        }
        return product_details
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None
