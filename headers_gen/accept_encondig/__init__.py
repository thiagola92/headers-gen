# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Encoding
# https://www.iana.org/assignments/http-parameters/http-parameters.xml#http-parameters-1


from headers_gen.utility import find_best_option
from headers_gen.exceptions import InvalidBrowserError
from headers_gen.accept_encondig.chrome import CHROME_ACCEPT_ENCODINGS
from headers_gen.accept_encondig.firefox import FIREFOX_ACCEPT_ENCODINGS


def get_chrome_accept_encoding(version: str) -> str:
    return find_best_option(version, CHROME_ACCEPT_ENCODINGS) or "*/*"


def get_firefox_accept_encoding(version: str) -> str:
    return find_best_option(version, FIREFOX_ACCEPT_ENCODINGS) or "*/*"


def generate_accept_encoding(browser: str, version: str) -> str:
    match browser:
        case "chrome":
            return get_chrome_accept_encoding(version)
        case "firefox":
            return get_firefox_accept_encoding(version)
    
    raise InvalidBrowserError("Invalid browser")