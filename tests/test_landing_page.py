import unittest

import landing_page


class Landing_pageTestCase(unittest.TestCase):

    def setUp(self):
        self.app = landing_page.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to landing_page', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
