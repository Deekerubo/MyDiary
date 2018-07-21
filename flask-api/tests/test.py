import unittest
import os
import json

from app import create_app
from app import app
from flask import jsonify

class Tests(unittest.TestCase):
    """Test for entries"""

    def setUp(self):
        """Initialise Tests"""
        self.client = app.test_client
        self.route_get_entries = '/api/v1/entries'
        self.route_index = '/api/v1l'
        # self.route_get_entry = '/api/v1'
        # self.client = self.app.test_client
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_main_page(self):
        response = self.app.get('/api/v1/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_adding(self):
        """Test API POST entry"""
        response = self.app.post('/api/v1/entries', data={"title":"Sports day", "content":"The sports day"})
        self.assertEqual(response.status_code, 201)
    def test_mofiy(self):
        self.app.post('/api/v1/entries', data={"title":"Sports day", "content":"The sports day"})
        response = self.app.put('/api/v1/entries/0', data={"title":"Sports day", "content":"The sports day"})
        self.assertEqual(response.status_code, 201)
    def get_one_entry(self):
        self.app.post('/api/v1/entries', data={"title":"Sports day", "content":"The sports day"})
        response = self.app.get('/api/v1/entries/0')
        self.assertEqual(response.status_code, 200)
