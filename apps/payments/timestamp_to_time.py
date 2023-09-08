import datetime


def convert_timestamp_to_datetime(timestamp):
    timestamp = str(timestamp)
    if len(timestamp) < 10:
        return datetime.date(int(timestamp[0:4]), int(timestamp[4:6]), int(timestamp[6:8]))
    elif len(timestamp) > 10:
        return datetime.datetime(int(timestamp[0:4]), int(timestamp[4:6]), int(timestamp[6:8]),
                                 int(timestamp[8:10]), int(timestamp[10:12]), int(timestamp[12:14]))
    else:
        return None