from django.test import TestCase, RequestFactory
from django.core.paginator import Paginator
from unittest.mock import patch, MagicMock
from ..views import get_product_details
from ..utils import fetch_product_details
from django.core.paginator import Page
import json

class ProductListViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    @patch('lululemonApp.utils.Paginator')
    @patch('lululemonApp.utils.requests.get')
    @patch('lululemonApp.utils.cache.get', side_effect=[None, None])
    @patch('lululemonApp.utils.cache.set', side_effect=MagicMock())
    def test_fetch_products(self, mock_cache_set, mock_cache_get, mock_requests_get, mock_paginator):
        expected_response = return_expected_data()
        response1_data, response2_data = mock_input_data()

        mock_response1 = MagicMock()
        mock_response1.status_code = 200
        mock_response1.json.return_value = response1_data
        
        mock_response2 = MagicMock()
        mock_response2.status_code = 200
        mock_response2.json.return_value = response2_data

        # Mock the requests.get calls
        mock_requests_get.side_effect = [mock_response1, mock_response2]

        mock_request = self.factory.get('/products/')

        mock_page_1 = MagicMock(spec=Page)

        # Set the object_list attribute of the mocked page
        mock_page_1.object_list = expected_response

        mock_paginator.return_value.page.return_value = mock_page_1

        # The first call should trigger API requests
        combined_products_first_call = get_product_details(mock_request)

        json_combined_products_first_call = json.loads(combined_products_first_call.content)

        self.assertEqual(json_combined_products_first_call, expected_response)

def mock_input_data():
        mock_records1 = [
            {
                "attributes" : {
                "product.displayName": "Leggings 1",
                "product.price": 50.0,
                "product.allAvailableSizes": ["S", "M", "L"],
                "product.sku.skuImages": ["image1.jpg", "image2.jpg"],
                "product.defaultParentCategory": "Athletic Wear",
                "currencyCode": "USD",
                "url": "https://example.com/product/leggings-1"
                }
            },
            {
                "attributes" : {
                "product.displayName": "Leggings 2",
                "product.price": 60.0,
                "product.allAvailableSizes": ["XS", "S", "M", "L"],
                "product.sku.skuImages": ["image3.jpg", "image4.jpg"],
                "product.defaultParentCategory": "Athletic Wear",
                "currencyCode": "USD",
                "url": "https://example.com/product/leggings-2"
                }
            }
        ]

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
                "attributes":{
                "product.displayName": "Leggings 1",
                "product.price": 50.0,
                "product.allAvailableSizes": ["S", "M", "L"],
                "product.sku.skuImages": ["image1.jpg", "image2.jpg"],
                "product.defaultParentCategory": "Athletic Wear",
                "currencyCode": "USD",
                "url": "https://example.com/product/leggings-1"
                }
            },
            {
                "attributes":{
                "product.displayName": "Leggings 2",
                "product.price": 60.0,
                "product.allAvailableSizes": ["XS", "S", "M", "L"],
                "product.sku.skuImages": ["image3.jpg", "image4.jpg"],
                "product.defaultParentCategory": "Athletic Wear",
                "currencyCode": "USD",
                "url": "https://example.com/product/leggings-2"
                }
            }
        ]

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
        return response1_data, response2_data

def return_expected_data():
        expected_response = [
            {
                "product_display_name": "Leggings 1",
                "product_price": 50.0,
                "product_avialable_size": [
                "S",
                "M",
                "L"
                ],
                "product_sku_images": [
                "image1.jpg",
                "image2.jpg"
                ],
                "product_parent_category": "Athletic Wear",
                "product_currency_code": "USD",
                "url": "https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json"
            },
            {
                "product_display_name": "Leggings 2",
                "product_price": 60.0,
                "product_avialable_size": [
                "XS",
                "S",
                "M",
                "L"
                ],
                "product_sku_images": [
                "image3.jpg",
                "image4.jpg"
                ],
                "product_parent_category": "Athletic Wear",
                "product_currency_code": "USD",
                "url": "https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json"
            },
            {
                "product_display_name": "Leggings 1",
                "product_price": 50.0,
                "product_avialable_size": [
                "S",
                "M",
                "L"
                ],
                "product_sku_images": [
                "image1.jpg",
                "image2.jpg"
                ],
                "product_parent_category": "Athletic Wear",
                "product_currency_code": "USD",
                "url": "https://shop.lululemon.com/c/accessories/_/N-1z0xcmkZ1z0xl44Z8ok?format=json"
            },
            {
                "product_display_name": "Leggings 2",
                "product_price": 60.0,
                "product_avialable_size": [
                "XS",
                "S",
                "M",
                "L"
                ],
                "product_sku_images": [
                "image3.jpg",
                "image4.jpg"
                ],
                "product_parent_category": "Athletic Wear",
                "product_currency_code": "USD",
                "url": "https://shop.lululemon.com/c/accessories/_/N-1z0xcmkZ1z0xl44Z8ok?format=json"
            }
        ]
        return expected_response

if __name__ == '_main_':
    unittest.main()