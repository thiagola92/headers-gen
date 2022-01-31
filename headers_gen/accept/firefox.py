# fmt: off
FIREFOX_DEFAULT_ACCEPTS = (
    ("92.0", "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"),
    ("72.0", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"),
    ("66.0", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
    ("65.0", "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"),
    ("0.0", "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"),
)

FIREFOX_IMAGE_ACCEPTS = (
    ("92.0", "image/avif,image/webp,*/*"),
    ("65.0", "image/webp,*/*"),
    ("47.0", "*/*"),
    ("0.0", "image/png,image/*;q=0.8,*/*;q=0.5"),
)

FIREFOX_VIDEO_ACCEPTS = (
    ("3.6", "video/webm,video/ogg,video/*;q=0.9,application/ogg;q=0.7,audio/*;q=0.6,*/*;q=0.5"),
)

FIREFOX_AUDIO_ACCEPTS = (
    ("3.6", "audio/webm,audio/ogg,audio/wav,audio/*;q=0.9,application/ogg;q=0.7,video/*;q=0.6,*/*;q=0.5"),
)

FIREFOX_SCRIPT_ACCEPTS = (
    ("0.0", "*/*"),
)

FIREFOX_CSS_ACCEPTS = (
    ("4.0", "text/css,*/*;q=0.1"),
)

FIREFOX_ACCEPTS = {
    "default": FIREFOX_DEFAULT_ACCEPTS,
    "image": FIREFOX_IMAGE_ACCEPTS,
    "video": FIREFOX_VIDEO_ACCEPTS,
    "script": FIREFOX_SCRIPT_ACCEPTS,
    "css": FIREFOX_CSS_ACCEPTS,
}
# fmt: on
