from la_headers.accept import generate_accept
from la_headers.user_agent import generate_user_agent
from la_headers.accept_encondig import generate_accept_encoding
from la_headers.upgrade_insecure_requests import generate_upgrade_insecure_requests


def generate_headers(
    browser: str,
    version: str,
    os: str,
    device: str = "desktop",
    context: str = "default",
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
        "Upgrade-Insecure-Requests": generate_upgrade_insecure_requests(browser, version),
        "User-Agent": generate_user_agent(browser, version, os, device),
    }
