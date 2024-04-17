API Documentation:

Project Title: Lululemon Product API

Introduction:

The Lululemon Product API is a single GET API built with Python that interacts with the Lululemon website to extract product details from a list of URLs. This API retrieves the "product.displayName" value and additional useful fields from the specified URLs. The API is designed following RESTful principles and incorporates caching mechanisms to optimize performance and minimize excessive requests to the Lululemon API.

Installation:

Clone the repository from GitHub or GitLab:

  git clone https://github.com/yourusername/lululemon-product-api.git

Install dependencies:

    pip install -r requirements.txt

Path:

    ..\lululemon-product-api\lululemonProductAPI>

Usage:

  Start the server:
  
    python manage.py runserver

  Make a GET request to the API endpoint:
  
    http://127.0.0.1:8000/api/products

Pagination:

  For endpoints with pagination, you can specify the page and limit parameter in the URL. For example:
  
  GET /products?url=<url>&page=<page_number>&limit=<no_of_products>

Endpoints:

  /api/products: Retrieves product details from the specified URL.

Request Format:

  Method: GET
  
    URL: /api/products
    
  Query Parameters:
  
    url: The URL of the Lululemon product category to extract data from.
    
    page (optional): Page number for paginated requests.
    
    limit (optional): Limit the no of products to show on a page
    
  Response Format:
    The API response will be in JSON format and include the following fields:
    
      product_display_name: The display name of the product.
      
      product_price: The display price of the product 
      
      product_avialable_size: The display available sizes of the product
      
      product_sku_images: The display images url of the product
      
      product_parent_category: The display parent category of the product
      
      product_currency_code: currency code
      
      url: url of the product
      

Usage Examples:

  Get product details from a Lululemon product category:
  
    GET localserver/api/products

    Response example:
      {
        "product_display_name": "Example Leggings",
        "color": "Black",
        "price": "$98",
        ...
      }
  Get product details from a paginated Lululemon product category:
    GET localserver/api/products?page=1&limit=100

    Response example:
      {
        "product_display_name": "Example Leggings",
        "color": "Black",
        "price": "$98",
        ...
      }
  
Caching Mechanisms:

The API implements caching mechanisms using Django's caching framework to avoid excessive requests to the Lululemon API for repeated requests within a short time frame. Caching helps improve performance and reduce load on the Lululemon servers.

Unit Tests:

Unit tests have been implemented to ensure the correctness of the API implementation. Tests cover various scenarios including API endpoints, request handling, pagination and caching mechanisms.

Future Scope:

  Sorting
  
  Implementing sorting functionality would allow users to arrange the retrieved products by name (could be any other property), enabling easier navigation and search within the API response. This enhancement would enhance user experience and provide greater flexibility in accessing product information.
  
  Filtering by Category
  
  Introducing the capability to filter products by parent category would enable users to narrow down their search and retrieve products specific to their interests. This feature would enhance the API's usability by offering more targeted results based on user preferences.

Author


Ankita Sharma
