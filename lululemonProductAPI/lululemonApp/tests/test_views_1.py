# from django.test import TestCase, RequestFactory
# from ..views import get_product_details
# from ..utils import fetch_product_details
# import mock
# from django.http import JsonResponse

# class ProductDetailsViewTestCase(TestCase):
#     def setUp(self):
#         self.factory = RequestFactory()

#     # Mock the fetch_product_details function to return sample data
#     @patch('lululemonApp.utils.get_product_details')

#     def test_get_product_details(self, mock_get_product_details):
#         # Mock the fetch_product_details function to return sample data
#         sample_product_details = [
#             {"product_display_name": "Leggings 1", "product_price": 50.0},
#             {"product_display_name": "Leggings 2", "product_price": 60.0}
#         ]

#         mock_get_product_details.return_value = sample_product_details

#         # Create a request
#         request = self.factory.get('/api/products/')
#         print('~~~~~~~~', request)
#         # Call the view function
#         response = get_product_details(request)
#         print('~~~~~~~~~~~', response)

#         # Extract the actual data from the response
#         actual_data = response.json()


#          # Assert that the view returns a JsonResponse
#         self.assertEqual(response.status_code, 200)
#         self.assertIsInstance(response, JsonResponse)
#         self.assertEqual(response.content_type, 'application/json')

#          # Check if the returned data matches the mock cached data
#         expected_data = [
#             {"product_display_name": "Leggings 1", "product_price": 50.0},
#             {"product_display_name": "Leggings 2", "product_price": 60.0}
#         ]
#         self.assertListEqual(actual_data, expected_data)

        