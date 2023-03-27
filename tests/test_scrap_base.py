import unittest

from ggscrap.scrap_base import download_response, extract_subURLs, get_head_words, build_google_url


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


    def test_get_head_words(self):

        words = get_head_words('https://www.google.com/search?q=best+short')
        print(words)
        self.assertTrue(words == ['google'])
        words = get_head_words('http://edition.cnn.com/2023/01/24/uk/ghislaine-maxwell-jail-interview-gbr-intl/index.html?dicbo=v2-lQ1zjgr&iid=ob_lockedrail_topeditorial')
        print(words)
        self.assertTrue(words == ['edition', 'cnn'])
        words = get_head_words('https://www.airbnb.pl/menlo-park-ca/stays')
        print(words)
        self.assertTrue(words == ['airbnb'])


    def test_build_google_url(self):

        self.assertRaises(Exception, build_google_url)

        url = build_google_url('best short')
        print(url)
        self.assertTrue(url == 'https://www.google.com/search?q=best+short')