# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent


from la_headers.utility import find_best_option
from la_headers.user_agent.chrome import CHROME_USER_AGENTS
from la_headers.user_agent.safari import SAFARI_USER_AGENTS
from la_headers.user_agent.firefox import FIREFOX_USER_AGENTS


_user_agents = {
    "chrome": CHROME_USER_AGENTS,
    "firefox": FIREFOX_USER_AGENTS,
    "safari": SAFARI_USER_AGENTS,
}


def generate_user_agent(browser: str, version: str, os: str, device: str) -> str:
    options = _user_agents[browser][device]
    best_option = find_best_option(version, options).format(version=version, os=os)

    return best_option
