from browsers.chrome import CHROME_VERSION
from browsers.firefox import FIREFOX_VERSION
from packaging.version import Version

CHROME_VERSION.sort(key=lambda v: Version(v))
CHROME_VERSION.reverse()
CHROME_VERSION = tuple(CHROME_VERSION)

FIREFOX_VERSION.sort(key=lambda v: Version(v))
FIREFOX_VERSION.reverse()
FIREFOX_VERSION = tuple(FIREFOX_VERSION)