import random
from CUTEXMUSIC.utils.database import get_theme

themes = [
    "CUTE1",
    "CUTE2",
    "CUTE3",
    "CUTE4",
    "CUTE5",
    "CUTE6",
    "CUTE7",
    "CUTE8",
    "CUTE9",
    "CUTE10",
    "CUTE11",
    "CUTE12",
    "CUTE13",
    "CUTE14",
    "CUTE15",
    "CUTE16",
    "CUTE17",
    "CUTE18",
    "CUTE19",
    "CUTE20",
    "CUTE21",
    "CUTE22",
    "CUTE23",
    "CUTE24",
    "CUTE25",
    "CUTE26",
    "CUTE27",
    "CUTE28",
    "CUTE29",
    "CUTE30",
    "CUTE31",
    "CUTE32",
    "CUTE33",
    "CUTE34",
    "CUTE35",
    "CUTE36",
    "CUTE37",
    "CUTE38",
    "CUTE39",
]


async def check_theme(chat_id: int):
    _theme = await get_theme(chat_id, "theme")
    if not _theme:
        theme = random.choice(themes)
    else:
        theme = _theme["theme"]
        if theme == "Random":
            theme = random.choice(themes)
    return theme
