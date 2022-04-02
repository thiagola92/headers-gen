# fmt: off
MAC_SYSTEM: tuple[str, str] = (
    ("0", "Macintosh; Intel Mac OS X {os_version}"),
)

MAC_VERSION = (
    ("0", lambda v: v.replace(".", "_")),
)
# fmt: on
