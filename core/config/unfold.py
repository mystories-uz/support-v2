from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from . import unfold_navigation as navigation

UNFOLD = {
    "SITE_TITLE": "Django Default",
    "SITE_HEADER": "Django Default",
    "SITE_URL": "/",
    "SITE_ICON": {
        "light": lambda request: static("images/django-logo.png"),
        "dark": lambda request: static("images/django-logo.png"),
    },
    "SITE_FAVICONS": [
        {
            "rel": "icon",
            "sizes": "32x32",
            "type": "image/svg+xml",
            "href": lambda request: static("images/django-logo.png"),
        },
    ],
    "SITE_SYMBOL": "speed",
    "SHOW_HISTORY": True,
    "SHOW_VIEW_ON_SITE": True,
    "LOGIN": {
        "image": lambda request: static("images/login.jpg"),
    },
    "STYLES": [
        lambda request: static("css/tailwind.css"),
    ],
    "COLORS": {
        "font": {
            "subtle-light": "107 114 128",
            "subtle-dark": "156 163 175",
            "default-light": "75 85 99",
            "default-dark": "209 213 219",
            "important-light": "17 24 39",
            "important-dark": "243 244 246",
        },
        "primary": {
            "50": "65 144 176",
            "100": "65 144 176",
            "200": "65 144 176",
            "300": "65 144 176",
            "400": "65 144 176",
            "500": "65 144 176",
            "600": "65 144 176",
            "700": "65 144 176",
            "800": "65 144 176",
            "900": "65 144 176",
            "950": "65 144 176",
        },
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "uz": "🇺🇿",
                "ru": "🇷🇺",
            },
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": navigation.PAGES,
    },
    "TABS": [
        {
            "models": [
                "support.messages",
                "support.answer",
                "support.dailymessages",
            ],
            "items": [
                {
                    "title": _("Xabarlar"),
                    "link": reverse_lazy("admin:support_messages_changelist"),
                },
                {
                    "title": _("Javoblar"),
                    "link": reverse_lazy("admin:support_answer_changelist"),
                },
                {
                    "title": _("Kunlik Xabarlar"),
                    "link": reverse_lazy("admin:support_dailymessages_changelist"),
                },
            ],
        },
        {
            "models": [
                "support.info",
                "support.infolinks",
            ],
            "items": [
                {
                    "title": _("Ma'lumotlar"),
                    "link": reverse_lazy("admin:support_info_changelist"),
                },
                {
                    "title": _("Ma'lumot Linklari"),
                    "link": reverse_lazy("admin:support_infolinks_changelist"),
                },
            ],
        },
    ],
}
