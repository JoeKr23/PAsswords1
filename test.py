from msilib.schema import Class

from app import app
import unittest
from db import db

class FlaskTestCase(unittest.TestCase):

    ## Check for response code 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/username")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    ## Check content type (application/json)
    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/username")
        self.assertEqual(response.content_type, "application/json")

    ## Check that data is returned
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/username")
        self.assertTrue(b'username' in response.data and b'password' in response.data)

if __name__ == "__main__":
    db.init_app(app)
    unittest.main()