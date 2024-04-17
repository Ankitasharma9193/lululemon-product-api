from django.test import TestCase, RequestFactory
from django.core.paginator import Paginator
from unittest.mock import patch, MagicMock
from ..views import get_product_details
from ..utils import fetch_product_details

class ProductListViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch('lululemonApp.utils.requests.get')
    @patch('lululemonApp.utils.cache.get', side_effect=[None, None])
    @patch('lululemonApp.utils.cache.set', side_effect=MagicMock())
    def test_fetch_products(self, mock_cache_set, mock_cache_get, mock_requests_get):
        mock_records1 = [
            {
                "product.displayName": "Leggings 1",
                "product.price": 50.0,
                "product.allAvailableSizes": ["S", "M", "L"],
                "product.sku.skuImages": ["image1.jpg", "image2.jpg"],
                "product.defaultParentCategory": "Athletic Wear",
                "currencyCode": "USD",
                "url": "https://example.com/product/leggings-1"
            },
            {
                "product.displayName": "Leggings 2",
                "product.price": 60.0,
                "product.allAvailableSizes": ["XS", "S", "M", "L"],
                "product.sku.skuImages": ["image3.jpg", "image4.jpg"],
                "product.defaultParentCategory": "Athletic Wear",
                "currencyCode": "USD",
                "url": "https://example.com/product/leggings-2"
            }
            # Add more mock records as needed
        ]

        # Example usage:
        response1_data = {
            "contents": [
                {
                    "mainContent": [
                        {
                            "contents": [
                                {
                                    "records": mock_records1
                                }
                            ]
                        }
                    ]
                }
            ]
        }

        mock_records2 = [
            {
                "product.displayName": "Leggings 1",
                "product.price": 50.0,
                "product.allAvailableSizes": ["S", "M", "L"],
                "product.sku.skuImages": ["image1.jpg", "image2.jpg"],
                "product.defaultParentCategory": "Athletic Wear",
                "currencyCode": "USD",
                "url": "https://example.com/product/leggings-1"
            },
            {
                "product.displayName": "Leggings 2",
                "product.price": 60.0,
                "product.allAvailableSizes": ["XS", "S", "M", "L"],
                "product.sku.skuImages": ["image3.jpg", "image4.jpg"],
                "product.defaultParentCategory": "Athletic Wear",
                "currencyCode": "USD",
                "url": "https://example.com/product/leggings-2"
            }
            # Add more mock records as needed
        ]

        # Example usage:
        response2_data = {
            "contents": [
                {
                    "mainContent": [
                        {
                            "contents": [
                                {
                                    "records": mock_records2
                                }
                            ]
                        }
                    ]
                }
            ]
        }

        mock_response1 = MagicMock()
        mock_response1.status_code = 200
        mock_response1.json.return_value = response1_data
        
        mock_response2 = MagicMock()
        mock_response2.status_code = 200
        mock_response2.json.return_value = response2_data

        # Mock the requests.get calls
        mock_requests_get.side_effect = [mock_response1, mock_response2]

        mock_request = self.factory.get('/products/')

        # Call the fetch_products function twice
        # The first call should trigger API requests
        combined_products_first_call = get_product_details(mock_request)
        print('~~~~~~~~~~~~~~~~~~~~~~~~`', combined_products_first_call)

        # The second call should retrieve data from cache
        # combined_products_second_call = get_product_details(mock_request)

        # Check the combined products from the first call
        # expected_combined_products = response1_data + response2_data
        # self.assertEqual(combined_products_first_call, expected_combined_products)

        # Check that cache is set correctly
        mock_cache_set.assert_called_with('combined_products', expected_combined_products, timeout=300)

        # Check the combined products from the second call
        # self.assertEqual(combined_products_second_call, expected_combined_products)

        # Check that cache is accessed instead of making API requests
        mock_cache_get.assert_called_with('combined_products')

if __name__ == '_main_':
    unittest.main()