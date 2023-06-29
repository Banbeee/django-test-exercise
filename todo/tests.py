from django.test import TestCase

# Create your tests here.
class SampleTestCase(TestCase):
    def teest_sample(self):
        self.assertEqual(1 + 2, 3)