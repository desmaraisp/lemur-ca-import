try:
    VERSION = __import__('pkg_resources').get_distribution(__name__).version
    AUTHOR = __import__('pkg_resources').get_distribution(__name__).get_metadata('PKG-INFO').split('Author: ')[1].splitlines()[0]
    URL = __import__('pkg_resources').get_distribution(__name__).get_metadata('PKG-INFO').split('Home-page: ')[1].splitlines()[0]
except Exception as e:
    VERSION = 'unknown'
    AUTHOR = ''
    URL = ''