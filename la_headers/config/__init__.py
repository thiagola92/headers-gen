from random import choice

from la_headers.config.chrome import CHROME_VERSION
from la_headers.config.firefox import FIREFOX_VERSION
from la_headers.config.android import ANDROID_VERSION

_options: list[dict] = [
    {
        "os": ["linux"],
        "os_version": ["22.04", "21.10", "21.04"],
        "browser": ["chrome"],
        "version": CHROME_VERSION[:10],
        "device": ["desktop"],
        "context": ["default"],
    },
    {
        "os": ["linux"],
        "os_version": ["22.04", "21.10", "21.04"],
        "browser": ["firefox"],
        "version": FIREFOX_VERSION[:10],
        "device": ["desktop"],
        "context": ["default"],
    },
    {
        "os": ["windows"],
        "os_version": ["10", "11"],
        "browser": ["chrome"],
        "version": CHROME_VERSION[:10],
        "device": ["desktop"],
        "context": ["default"],
    },
    {
        "os": ["windows"],
        "os_version": ["10", "11"],
        "browser": ["firefox"],
        "version": FIREFOX_VERSION[:10],
        "device": ["desktop"],
        "context": ["default"],
    },
    {
        "os": ["android"],
        "os_version": ANDROID_VERSION[:10],
        "browser": ["chrome"],
        "version": CHROME_VERSION[:10],
        "device": ["mobile"],
        "context": ["default"],
    },
    {
        "os": ["android"],
        "os_version": ANDROID_VERSION[:10],
        "browser": ["firefox"],
        "version": FIREFOX_VERSION[:10],
        "device": ["mobile"],
        "context": ["default"],
    },
]


def generate_random_config() -> dict:
    config = dict(choice(_options))

    for k in config:
        config[k] = choice(config[k])
    
    return config
