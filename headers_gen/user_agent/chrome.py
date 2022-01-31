# fmt: off
CHROME_DESKTOP_USER_AGENTS = (
    ("0", "Mozilla/5.0 ({os}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Safari/537.36"),
)


CHROME_MOBILE_USER_AGENTS = (
    ("0", "Mozilla/5.0 ({os}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{version} Mobile Safari/537.36"),
)


CHROME_USER_AGENTS = {
    "desktop": CHROME_DESKTOP_USER_AGENTS,
    "mobile": CHROME_MOBILE_USER_AGENTS,
}
# fmt: on