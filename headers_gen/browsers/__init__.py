from browsers.chrome import CHROME_VERSIONS
from browsers.firefox import FIREFOX_VERSIONS
from packaging.version import Version

CHROME_VERSIONS.sort(key=lambda v: Version(v))
CHROME_VERSIONS.reverse()
CHROME_VERSIONS = tuple(CHROME_VERSIONS)

FIREFOX_VERSIONS.sort(key=lambda v: Version(v))
FIREFOX_VERSIONS.reverse()
FIREFOX_VERSIONS = tuple(FIREFOX_VERSIONS)