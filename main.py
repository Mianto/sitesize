import sitesize

list_url = [
    'https://www.yahoo.com/',
    'http://www.cnn.com',
    'http://www.python.org',
    'http://www.jython.org',
    'http://www.pypy.org',
    'http://www.perl.org',
    'http://www.cisco.com',
    'http://www.facebook.com',
    'http://www.twitter.com',
    'http://www.macrumors.com/',
    'http://arstechnica.com/',
    'http://www.reuters.com/',
    'http://abcnews.go.com/',
    'http://www.cnbc.com/',
    'http://www.cnbc.com/'
]

def main():
    url = input('Enter the url of the site: ').strip()
    valid_url = sitesize.url_checker(url)
    print('Getting size of the web page ...')
    size_byte = sitesize.get_webpage_size(valid_url)
    print('The size of the web page is {}'.format(size_byte))
    print(sitesize.get_webpages_size(list_url))

if __name__ == '__main__':
    main()