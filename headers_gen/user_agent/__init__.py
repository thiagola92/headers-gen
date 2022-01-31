# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent


from headers_gen.utility import find_best_option
from headers_gen.exceptions import InvalidBrowserError
from headers_gen.user_agent.chrome import CHROME_USER_AGENTS
from headers_gen.user_agent.safari import SAFARI_USER_AGENTS
from headers_gen.user_agent.firefox import FIREFOX_USER_AGENTS


def get_safari_user_agent(version: str, device: str) -> str:
    return find_best_option(version, SAFARI_USER_AGENTS[device])


def get_chrome_user_agent(version: str, device: str) -> str:
    return find_best_option(version, CHROME_USER_AGENTS[device])


def get_firefox_user_agent(version: str, device: str) -> str:
    return find_best_option(version, FIREFOX_USER_AGENTS[device])


def generate_user_agent(browser: str, version: str, os: str, device: str) -> str:
    match browser:
        case "chrome":
            user_agent = get_chrome_user_agent(version, device)
            return user_agent.format(version=version, os=os)
        case "firefox":
            user_agent = get_firefox_user_agent(version, device)
            return user_agent.format(version=version, os=os)

    raise InvalidBrowserError("Invalid browser")
