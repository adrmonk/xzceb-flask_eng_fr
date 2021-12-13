import unittest

from translator import english_to_french, french_to_english


class Test_english_to_french (unittest.TestCase):
    def test1 (self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french('This is my house'),"C'est ma maison")
        self.assertEqual(english_to_french('Nice to meet you'),'Ravi de vous rencontrer')
        self.assertEqual(english_to_french(' '),' ')
        self.assertNotEqual(english_to_french('Hello'),' ')
        self.assertNotEqual(english_to_french('Hello'),'Hello')

class Test_french_to_english (unittest.TestCase):
    def test1 (self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english("C'est ma maison"),'This is my house')
        self.assertEqual(french_to_english('Ravi de vous rencontrer'),'Nice to meet you')
        self.assertEqual(french_to_english(' '),' ')
        self.assertNotEqual(french_to_english('Bonjour'),' ')
        self.assertNotEqual(french_to_english('Bonjour'),'Bonjour')
     

unittest.main()