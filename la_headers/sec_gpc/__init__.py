# https://globalprivacycontrol.github.io/gpc-spec/


from la_headers.utility import find_best_option
from la_headers.sec_gpc.chrome import CHROME_SEC_GPCS


_sec_gpcs = {
    "chrome": CHROME_SEC_GPCS,
    "firefox": tuple(),
}


def generate_sec_gpc(browser: str, version: str) -> str:
    options = _sec_gpcs[browser]
    sec_gpc = find_best_option(version, options)

    return sec_gpc