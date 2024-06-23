from datetime import datetime


def filter_by_state(slovar, state='EXECUTED'):
    my_list = []
    for i in slovar:
        if i.get('state') == state:
            my_list.append(i)
    return my_list


def sort_by_date(slovar, ascending = True):
    def sort_key(record):
        return datetime.strptime(record["date"], "%Y-%m-%dT%H:%M:%S.%f")
    return sorted(slovar, key=sort_key, reverse=not ascending)
