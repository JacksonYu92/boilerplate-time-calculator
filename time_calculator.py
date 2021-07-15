def add_time(start, duration, day=None):

    # days = {
    #     0: "Sunday",
    #     1: "Monday",
    #     2: "Tuesday",
    #     3: "Wednesday",
    #     4: "Thursday",
    #     5: "Friday",
    #     6: "Saturday",
    # }
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    # format start time
    start_time = start.split()[0]
    start_period = start.split()[1]
    # split time to hour and minute
    start_hour = int(start_time.split(":")[0])
    start_min = int(start_time.split(":")[1])

    # format start hour to 24 hr format
    if start_period == "PM":
        start_hour += 12

    # format duration
    duration_hours = int(duration.split(":")[0])
    duration_mins = int(duration.split(":")[1])

    # calculate new total hour & minute
    total_mins = start_min + duration_mins
    minutes = total_mins % 60
    extra_hour = total_mins // 60
    total_hours = start_hour + duration_hours + extra_hour

    # calculate days
    total_days = total_hours // 24
    hours_in_24 = total_hours % 24
    hours_in_12 = (total_hours % 24) % 12

    # fix 0:00 format to 12:00
    if hours_in_12 == 0:
        hours_in_12 = 12
    hours_in_12 = str(hours_in_12)

    # decide AM & PM
    period = None
    if hours_in_24 <= 11:
        period = "AM"
    else:
        period = "PM"

    # format minutes in "00"
    if minutes < 10:
        minutes = f"0{str(minutes)}"
    else:
        minutes = str(minutes)

    new_time = f"{hours_in_12}:{minutes} {period}"

    if day == None:
        if total_days == 0:
            return new_time
        if total_days == 1:
            return f"{new_time} (next day)"
        return f"{new_time} ({str(total_days)} days later)"
    else:
        day_index = days.index(day.title())
        new_day_index = int(day_index + total_days) % 7
        new_day = days[new_day_index]
        if total_days == 0:
            return f"{new_time}, {new_day}"
        if total_days == 1:
            return f"{new_time}, {new_day} (next day)"
        return f"{new_time}, {new_day} ({str(total_days)} days later)"