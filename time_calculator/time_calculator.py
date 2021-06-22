def add_time(original_time, extra_time, input_day=None):
    hour, minutes, time_stamp = ' '.join(original_time.split(':')).split()
    if time_stamp == "PM":
        hour = int(hour) + 12
    hour, minutes = int(hour), int(minutes)
    extra_hours, extra_minutes = extra_time.split(':')
    extra_hours, extra_minutes = int(extra_hours), int(extra_minutes)

    ans_minutes = (minutes + extra_minutes) % 60
    if len(str(ans_minutes)) <= 1:
        ans_minutes = '0' + str(ans_minutes)
    else:
        ans_minutes = str(ans_minutes)
    converted_minutes = (minutes + extra_minutes) // 60

    total_hour = hour + extra_hours + converted_minutes
    total_day = (total_hour // 24)
    if (total_hour % 24) <= 11:
        ans_time_stamp = "AM"
    else:
        ans_time_stamp = "PM"

    ans_hour = (total_hour % 24) % 12
    if ans_hour == 0:
        ans_hour = 12
    ans_hour = str(ans_hour)

    day_dict = {"Saturday": 0, "Sunday": 1, "Monday": 2, "Tuesday": 3, "Wednesday": 4, "Thursday": 5, "Friday": 6}
    day_dict2 = {0: "Saturday", 1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday"}

    new_time = ans_hour + ":" + ans_minutes + ' ' + ans_time_stamp
    if input_day is None:
        if total_day == 0:
            return new_time
        elif total_day == 1:
            new_time = new_time + ' (next day)'
            return new_time
        else:
            new_time = new_time + ' (' + str(total_day) + ' days later)'
            return new_time
    else:
        ans_day = (day_dict[input_day.lower().capitalize()] + total_day) % 7
        ans_day = day_dict2[ans_day]
        if total_day == 0:
            new_time = new_time + ', ' + ans_day
            return new_time
        elif total_day == 1:
            new_time = new_time + ', ' + ans_day + ' (next day)'
            return new_time
        else:
            new_time = new_time + ', ' + ans_day + ' (' + str(total_day) + ' days later)'
            return new_time
