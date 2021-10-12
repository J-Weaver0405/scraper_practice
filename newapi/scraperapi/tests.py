from django.test import TestCase

# Create your tests here.

def test_url_request(page_request):
    assert page_request.status_code == 200