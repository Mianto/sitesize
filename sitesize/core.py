
from urllib.parse import urlparse
from urllib.error import URLError, HTTPError
from urllib.request import urlopen

def url_checker(url):
    """
    :param url: String containing url of the site
    :return: Validated url
    """
    try:
        parse_result = urlparse(url)
        if all([parse_result.scheme, parse_result.netloc]):
            return url
        elif parse_result.scheme == '':
            url = 'http://' + url
            return url
    except:
        return False


def get_webpage_size(url):
    """
    :param url: String containing validated url
    :return: Int length of the web page in bytes
    """
    try :
        site = urlopen(url)
    except URLError as e:
        print(e.reason)
    except HTTPError as e:
        print(e.code)

    meta_data = site.info()
    if 'Content-Length' in meta_data.keys():
        return meta_data['Content-Length']
    else:
        return len(site.read())

