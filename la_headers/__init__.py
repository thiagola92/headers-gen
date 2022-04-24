from la_headers.accept import generate_accept
from la_headers.system import generate_system
from la_headers.config import generate_random_config
from la_headers.sec_ch_ua import generate_sec_ch_ua
from la_headers.user_agent import generate_user_agent
from la_headers.accept_encondig import generate_accept_encoding
from la_headers.sec_ch_ua_mobile import generate_sec_ch_ua_mobile
from la_headers.sec_ch_ua_platform import generate_sec_ch_ua_platform
from la_headers.upgrade_insecure_requests import generate_upgrade_insecure_requests


def generate_headers(
    os: str,
    os_version: str,
    browser: str,
    version: str,
    device: str = "desktop",
    context: str = "default",
) -> dict:
    """
    os:
        windows
        linux
        android
        mac

    os_version:
        major.minor.patch
    
    browser options:
        chrome
        firefox

    version:
        major.minor.patch

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

    system = generate_system(os, os_version)

    return {
        "Accept": generate_accept(browser, version, context),
        "Accept-Encoding": generate_accept_encoding(browser, version),
        "Accept-Language": None,
        "Connection": None,
        "Sec-Ch-Ua": generate_sec_ch_ua(browser, version),
        "Sec-Ch-Ua-Mobile": generate_sec_ch_ua_mobile(browser, version, device),
        "Sec-Ch-Ua-Platform": generate_sec_ch_ua_platform(browser, version, os),
        "Upgrade-Insecure-Requests": generate_upgrade_insecure_requests(
            browser, version
        ),
        "User-Agent": generate_user_agent(browser, version, system, device),
    }


def generate_random_headers(
    os: str | None = None,
    os_version: str | None = None,
    browser: str | None = None,
    version: str | None = None,
    device: str | None = None,
    context: str | None = None,
) -> dict:
    config = generate_random_config()

    config["os"] = os or config["os"]
    config["os_version"] = os_version or config["os_version"]
    config["browser"] = browser or config["browser"]
    config["version"] = version or config["version"]
    config["device"] = device or config["device"]
    config["context"] = context or config["context"]

    return generate_headers(**config)