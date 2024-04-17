from django.test import TestCase, RequestFactory
from ..views import get_product_details
from ..utils import fetch_product_details  # Mock this function
from unittest.mock import patch


@patch('lululemonApp.views.fetch_product_details')
@patch('lululemonApp.views.cache')

class ProductDetailsViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_product_details_cached(self, mock_cache, mock_fetch_product_details):
        # Mock the fetch_product_details function to return sample data
        sample_product_details = [{'name': 'Leggings', 'price': '$50'}, {'name': 'Accessories', 'price': '$20'}]
        mock_fetch_product_details.side_effect = [sample_product_details, sample_product_details]

        # Create a request
        request = self.factory.get('/products/')

        # Call the view function
        response = get_product_details(request)

        # Assert that the view returns a JsonResponse
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')

        # Assert that fetch_product_details was called twice with the correct URLs
        mock_fetch_product_details.assert_called_with('https://shop.lululemon.com/c/womens-leggings/_/N-8r6?format=json')
        mock_fetch_product_details.assert_called_with('https://shop.lululemon.com/c/accessories/_/N-1z0xcmkZ1z0xl44Z8ok?format=json')

        # Assert that cache.set was called once with the correct cache key and data
        mock_cache.set.assert_called_once_with('product_details_1', sample_product_details, timeout=3600)