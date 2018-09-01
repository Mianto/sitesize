#!usr/bin/python3

from .core import *

def main():
    url = input('Enter the url of the site: ').strip()
    valid_url = url_checker(url)
    print('Getting size of the web page ...')
    size_byte = get_webpage_size(valid_url)
    print('The size of the web page is {}'.format(size_byte))

if __name__ == '__main__':
    main()
