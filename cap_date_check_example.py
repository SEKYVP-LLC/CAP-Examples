import datetime
import dateutil

sent = datetime.datetime.strptime("2024-09-15T13:19:00-05:00", "%Y-%m-%dT%H:%M:%S%z")
expire = datetime.datetime.strptime("2024-09-16T01:30:00-05:00", "%Y-%m-%dT%H:%M:%S%z")

def is_expired(sent, expire):
    current = datetime.datetime.now(dateutil.tz.tzlocal())
    if expire < current:
        return True
    return False

def is_active(sent, expire):
    current = datetime.datetime.now(dateutil.tz.tzlocal())
    if is_expired(sent, expire):
        if sent > current:
            return True
        return False

print("Active:", is_active(sent, expire))
print("Expired:", is_expired(sent, expire))