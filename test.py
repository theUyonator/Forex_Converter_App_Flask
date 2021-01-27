from unittest import TestCase
from app import app
from fxconverter import ForexConverter

class ForexConverterTest(TestCase):
    """This class holds methods testing the view functions in app.py"""
    def setup(self):
        """This method holds code that runs before every test method"""
        app.config["TESTING"] = True

    def test_start_converter(self):
        """This method test to if the view function for the home route "/" works """
        with app.test_client() as client:
            resp = client.get("/")
            html = resp.get_data(as_text = True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1 class="mt-3 ml-3">FOREX CONVERTER</h1>', html)

    def test_redirect(self):
        """This method test to see if a redirect takes place on form submission"""
        with app.test_client() as client:
            resp = client.get("/fx_converter?from=USD&to=AUD&amount=10")

            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "http://localhost/")
    
    def test_redirect_followed(self):
        """This method test to see if the expected content shows after the redirect takes place"""
        with app.test_client() as client:
            resp = client.get("/fx_converter?from=USD&to=AUD&amount=10", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<p><strong>The result is $12.94</strong></p>', html)
