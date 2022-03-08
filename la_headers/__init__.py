from la_headers.accept import generate_accept
from la_headers.user_agent import generate_user_agent
from la_headers.accept_encondig import generate_accept_encoding


def generate_headers(
    browser: str,
    version: str,
    os: str,
    device: str,
    context: str,
) -> dict:
    """
    browser options:
        chrome
        firefox

    version:
        major.minor.patch
    
    os:
        ...

    device:
        desktop
        mobile
    
    context:
        default
        image
        video
        audio
        script
        css
    """

    return {
        "Accept": generate_accept(browser, version, context),
        "Accept-Encoding": generate_accept_encoding(browser, version),
        "Accept-Language": None,
        "Connection": None,
        "Sec-Ch-Ua": None,
        "Sec-Ch-Ua-Mobile": None,
        "Sec-Ch-Ua-Platform": None,
        "Sec-Gpc": None,
        "Upgrade-Insecure-Requests": None,
        "User-Agent": generate_user_agent(browser, version, os, device),
    }
