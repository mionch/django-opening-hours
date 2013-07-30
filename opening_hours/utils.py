import json

def is_open(date, opening_hours):
    if type(opening_hours) == str:
        opening_hours = json.loads(opening_hours)
    try:
        day = opening_hours[date.strftime("%a")[:2].lower()]
    except KeyError:
        return False
    for opening in day:
        start = opening[0].split(":")
        end = opening[1].split(":")
        start = int(start[0])*60 + int(start[1])
        end = int(end[0])*60 + int(end[1])
        now = date.hour*60 + date.minute
        if start < now < end:
            return True
    return False

