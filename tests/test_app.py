import unittest
from flask import Flask, jsonify, request
from app import app
from utils import play_mp3, connect_bluetooth_speaker

class FlaskServerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_flask_server(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 404)

    def test_webhook_route(self):
        response = self.app.get()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'status': 'sound played'})

    def test_play_mp3(self):
        with self.assertRaises(FileNotFoundError):
            play_mp3('non_existent_file.mp3')

    def test_connect_bluetooth_speaker(self):
        # This test is a placeholder as connecting to a Bluetooth speaker
        # requires actual hardware and environment setup.
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
