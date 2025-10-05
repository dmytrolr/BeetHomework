import unittest
import os
import json
from Phonebook import load_phonebook, save_phonebook


class TestPhonebookIO(unittest.TestCase):

    def setUp(self):
        self.test_file = 'test_contacts.json'
        self.test_data = {
            "123": {
                "first_name": "Іван",
                "last_name": "Петренко",
                "city": "Київ",
                "state": "Київська"
            }
        }
        save_phonebook(self.test_data, self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_phonebook(self):
        loaded = load_phonebook(self.test_file)
        self.assertEqual(loaded, self.test_data)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            load_phonebook('nonexistent.json')

    def test_save_phonebook(self):
        with open(self.test_file, 'r', encoding='utf-8') as f:
            content = json.load(f)
        self.assertEqual(content, self.test_data)
