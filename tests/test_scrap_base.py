import unittest

from ggscrap.scrap_base import download_response, extract_subURLs


class Test_scrap_base(unittest.TestCase):

    def test_download_response(self):

        resp = download_response(url='none')
        print(resp)
        self.assertTrue(resp is None)

    def test_extract_subURLs(self):

        resp = download_response(url='none')
        urls = extract_subURLs(response=resp)
        print(urls)
        self.assertTrue(urls == [])