# fmt: off
SAFARI_DESKTOP_USER_AGENTS = (
    ("0", "Mozilla/5.0 ({os}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{version} Safari/605.1.15")
)


SAFARI_MOBILE_USER_AGENTS = (
    ("0", "Mozilla/5.0 ({os}) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/{version} Mobile/15E148 Safari/604.1")
)


SAFARI_USER_AGENTS = {
    "desktop": SAFARI_DESKTOP_USER_AGENTS,
    "mobile": SAFARI_MOBILE_USER_AGENTS,
}
# fmt: on