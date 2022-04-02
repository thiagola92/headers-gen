from packaging.version import Version
from la_headers.utility import find_best_option
from la_headers.system.mac import MAC_SYSTEM
from la_headers.system.linux import LINUX_SYSTEM
from la_headers.system.android import ANDROID_SYSTEM
from la_headers.system.windows import WINDOWS_SYSTEM

_system = {
    "linux": LINUX_SYSTEM,
    "android": ANDROID_SYSTEM,
    "windows": WINDOWS_SYSTEM,
    "mac": MAC_SYSTEM,
}

_version = {
    "linux": lambda _: "",
    "android": lambda v: str(Version(v).major),
    "windows": lambda v: str(Version(v).major) + ".0",
    "mac": lambda v: v.replace(".", "_"),
}


def generate_system(os: str, os_version: str) -> str:
    """
    os:
        windows
        linux
        android
        mac
    """
    options = _system[os]
    version = _version[os](os_version)
    best_option = find_best_option(os_version, options).format(os_version=version)

    return best_option.strip
