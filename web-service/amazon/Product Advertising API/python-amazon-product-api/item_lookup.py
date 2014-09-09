# -*- coding: utf-8 -*-

from amazonproduct.api import API
from amazonproduct.errors import AWSError
from amazonproduct.processors import BaseProcessor

import BeautifulSoup


class SoupProcessor(BaseProcessor):
    def parse(self, fp):
        soup = BeautifulSoup.BeautifulSoup(fp.read())

        for error in soup.findAll('error'):
            code = error.find('code').text
            msg = error.find('message').text
            raise AWSError(code, msg)

        return soup

if __name__ == '__main__':

    api = API(locale='jp', processor=SoupProcessor())
    result = api.item_lookup('B00LCL7A3G')

    print result
