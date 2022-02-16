# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Encoding
# https://www.iana.org/assignments/http-parameters/http-parameters.xml#http-parameters-1


from la_headers.utility import find_best_option
from la_headers.accept_encondig.chrome import CHROME_ACCEPT_ENCODINGS
from la_headers.accept_encondig.firefox import FIREFOX_ACCEPT_ENCODINGS


_accept_encodings = {
    "chrome": CHROME_ACCEPT_ENCODINGS,
    "firefox": FIREFOX_ACCEPT_ENCODINGS,
}


def generate_accept_encoding(browser: str, version: str) -> str:
    options = _accept_encodings[browser]
    accept_encoding = find_best_option(version, options) or "*/*"

    return accept_encoding
