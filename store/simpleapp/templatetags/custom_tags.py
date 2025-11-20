from datetime import datetime
from django import template

register = template.Library()
MONTHS_RU = {
    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря",
}


@register.simple_tag()
def current_time():
    now = datetime.now()
    day = now.day
    month = MONTHS_RU[now.month]  # ← родительный падеж
    year = now.year
    return f"{day} {month} {year}"
