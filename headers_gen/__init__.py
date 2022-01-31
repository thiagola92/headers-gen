from headers_gen.accept import generate_accept
from headers_gen.user_agent import generate_user_agent
from headers_gen.accept_encondig import generate_accept_encoding


def generate_headers(browser: str, version: str, os: str, device: str, context: str) -> dict:
    return {
        "Accept": generate_accept(browser, version, context),
        "Accept-Encoding": generate_accept_encoding(browser, version),
        "User-Agent": generate_user_agent(browser, version, os, device),
    }