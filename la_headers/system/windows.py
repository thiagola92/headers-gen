from packaging.version import Version

# fmt: off
WINDOWS_SYSTEM: tuple[str, str] = (
    ("0", "Windows NT {os_version}; Win64; x64"),
)

WINDOWS_VERSION = (
    ("0", lambda v: str(Version(v).major) + ".0"),
)
# fmt: on
