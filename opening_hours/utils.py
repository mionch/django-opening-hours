# -*- coding: utf-8 -*-
from collections import OrderedDict
import json

def is_open(date, opening_hours):
    if type(opening_hours) == str or type(opening_hours) == unicode:
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
        if end < start:
            end += 1440  # 24*60 plus 1 day
        now = date.hour*60 + date.minute
        if start < now < end:
            return True
    return False


days = OrderedDict([
    (u"mo", u"Pn. "),
    (u"tu", u"Wt. "),
    (u"we", u"Sr."),
    (u"th", u"Czw."),
    (u"fr", u"Pt. "),
    (u"sa", u"Sb. "),
    (u"su", u"Ndz."),
])

def opening_hours_set(opening_hours):
    for day, label in days.iteritems():
        values = opening_hours.get(day)
        if len(values) == 1 and len(values[0]) == 2:
            open_from = values[0][0]
            open_to = values[0][1]
            if open_from and open_to:
                return True
    return False

def readable_opening_hours_value(opening_hours):
    output = u""
    for day, label in days.iteritems():
        values = opening_hours.get(day)
        if len(values) == 1 and len(values[0]) == 2:
            open_from = values[0][0]
            open_to = values[0][1]
            if open_from and open_to:
                output += u"{}: {} - {}\n".format(label, open_from, open_to)
                continue
    return output