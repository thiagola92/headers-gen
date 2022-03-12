# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation/List_of_default_Accept_values


from la_headers.utility import find_best_option
from la_headers.accept.chrome import CHROME_ACCEPTS
from la_headers.accept.firefox import FIREFOX_ACCEPTS


_accepts = {
    "chrome": CHROME_ACCEPTS,
    "firefox": FIREFOX_ACCEPTS,
}


def generate_accept(browser: str, version: str, context: str) -> str:
    context_options = _accepts[browser][context]
    default_options = _accepts[browser]["default"]
    best_option = (
        find_best_option(version, context_options)
        or find_best_option(version, default_options)
        or "*/*"
    )

    return best_option
