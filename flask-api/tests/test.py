import unittest
import os
import json
from app import create_app

class Tests(unittest.TestCase):
    """Test for entries"""

    def setUp(self):
        self.app = create_app(config_name="testing")
        self.route_get_entries = '/api/v1/entries'
        self.route_index = '/api/v1'
        self.client = self.app.test_client

    def test_index(self):
        result = self.client.get(self.route_index)
        self.assertEqual(result.status_code, 200)



#make tests executable
if __name__ == "__main__":
    unittest.main()