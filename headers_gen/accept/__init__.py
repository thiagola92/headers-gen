# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation/List_of_default_Accept_values


from headers_gen.utility import find_best_option
from headers_gen.exceptions import InvalidBrowserError
from headers_gen.accept.chrome import CHROME_ACCEPTS, CHROME_DEFAULT_ACCEPTS
from headers_gen.accept.firefox import FIREFOX_ACCEPTS, FIREFOX_DEFAULT_ACCEPTS


def get_chrome_accept(version: str, context: str) -> str:
    return (
        find_best_option(version, CHROME_ACCEPTS[context])
        or find_best_option(version, CHROME_DEFAULT_ACCEPTS)
        or "*/*"
    )


def get_firefox_accept(version: str, context: str) -> str:
    return (
        find_best_option(version, FIREFOX_ACCEPTS[context])
        or find_best_option(version, FIREFOX_DEFAULT_ACCEPTS)
        or "*/*"
    )


def generate_accept(browser: str, version: str, context: str) -> str:
    match browser:
        case "chrome":
            return get_chrome_accept(version, context)
        case "firefox":
            return get_firefox_accept(version, context)

    raise InvalidBrowserError("Invalid browser")
