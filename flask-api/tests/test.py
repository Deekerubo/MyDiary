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
        self.app = create_app("testing")
        self.client = self.app.test_client()
        self.route_get_entries = '/api/v1/entries'
        self.route_index = '/api/v1'
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()

    def test_main_page(self):
        response = self.app.get('/api/v1/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_adding(self):
        """Test API POST entry"""
        response = self.app.post('/api/v1/entries', data={"title":"Deployment", "content":"Crazy deployment"})
        self.assertEqual(response.status_code, 201)
    def test_mofiy(self):
        """Test API MODIFY entry"""
        self.app.post('/api/v1/entries', data={"title":"Deployment", "content":"Crazy deployment"})
        response = self.app.put('/api/v1/entries/1',)
        self.assertEqual(response.status_code, 201)
    def get_one_entry(self):
        """Test API GET an entry"""
        self.app.post('/api/v1/entries', data={"title":"Deployment", "content":"Crazy deployment"})
        response = self.app.get('/api/v1/entries/1')
        self.assertEqual(response.status_code, 200)
