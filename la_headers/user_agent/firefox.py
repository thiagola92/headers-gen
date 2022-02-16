# fmt: off
FIREFOX_DESKTOP_USER_AGENTS = (
    ("0", "Mozilla/5.0 ({os}; rv:{version}) Gecko/20100101 Firefox/{version}"),
)


FIREFOX_MOBILE_USER_AGENTS = (
    ("0", "Mozilla/5.0 ({os}; rv:{version}) Gecko/{version} Firefox/{version}"),
)


FIREFOX_USER_AGENTS = {
    "desktop": FIREFOX_DESKTOP_USER_AGENTS,
    "mobile": FIREFOX_MOBILE_USER_AGENTS,
}
# fmt: on
