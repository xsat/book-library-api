from datetime import datetime


_DATETIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"


def from_mysql_datetime(datetime_string: str) -> datetime:
    return datetime.strptime(datetime_string, _DATETIME_FORMAT)


def to_mysql_datetime(datetime_object: datetime) -> str:
    return datetime_object.strftime(_DATETIME_FORMAT)


def today_datetime() -> datetime:
    return datetime.now()


def next_month_datetime() -> datetime:
    now: datetime = datetime.now()

    if now.month == 12:
        return now.replace(year=now.year + 1, month=1)

    return now.replace(month=now.month + 1)
