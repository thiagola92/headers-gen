from packaging.version import Version

# fmt: off
ANDROID_SYSTEM: tuple[str, str] = (
    ("0", "Linux; Android {os_version}"),
)

ANDROID_VERSION = (
    ("0", lambda v: str(Version(v).major)),
)
# fmt: on
