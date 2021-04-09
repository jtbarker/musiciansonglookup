import unittest


class MyTestCase(unittest.TestCase):
    def test_token(self):
        self.assertNotEqual("bringyourowntoken", clientaccesstoken)


if __name__ == '__main__':
    unittest.main()
