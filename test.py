import unittest
import index
from urllib import parse

class TddTest(unittest.TestCase):
    def test_url_parse(self):
        url = index.url_parse("https://ameblo.jp/blackship-staff/page-%d.html", 3)
        self.assertEqual(url, parse.urlparse("https://ameblo.jp/blackship-staff/page-3.html"))


if __name__ == '__main__':
    unittest.main()