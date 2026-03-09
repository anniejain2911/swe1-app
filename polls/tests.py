from django.test import TestCase


class SmokeTest(TestCase):
    def test_sanity(self):
        self.assertTrue(True)

    def test_dummy(self):
        self.assertTrue(False)
        
