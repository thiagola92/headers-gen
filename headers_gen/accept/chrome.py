# fmt: off
CHROME_DEFAULT_ACCEPTS = (
    ("97.0", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"),
    ("0.0", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"),
)

CHROME_IMAGE_ACCEPTS = (
    ("97.0", "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8"),
    ("0.0", "image/avif,image/webp,image/apng,image/*,*/*;q=0.8"),
)

CHROME_VIDEO_ACCEPTS = (
    ("0.0", "*/*"),
)

CHROME_AUDIO_ACCEPTS = (
    ("0.0", "*/*"),
)

CHROME_SCRIPT_ACCEPTS = (
    ("0.0", "*/*"),
)

CHROME_CSS_ACCEPTS = (
    ("0.0", "text/css,*/*;q=0.1"),
)

CHROME_ACCEPTS = {
    "default": CHROME_DEFAULT_ACCEPTS,
    "image": CHROME_IMAGE_ACCEPTS,
    "video": CHROME_VIDEO_ACCEPTS,
    "audio": CHROME_AUDIO_ACCEPTS,
    "script": CHROME_SCRIPT_ACCEPTS,
    "css": CHROME_CSS_ACCEPTS,
}
# fmt: on