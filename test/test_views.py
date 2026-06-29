import unittest
import json
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = rv.data.decode('utf-8').replace(" ", "")
        assert ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
        expected_data = {"imie": "Jakub", "msg": "Hello World!"}
        self.assertEqual(json.loads(rv.data), expected_data)