def how_many_days_in (month, year):
    if (month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        return 31
    elif (month == 2 and year%4 == 0):
        return 29
    elif (month == 2):
        return 28
    else:
        return 30

def since_or_until (day, month, year, curr_day, curr_month, curr_year):
        if (year == curr_year):
            if (month == curr_month):
                if (day == curr_day):
                    s = "that's now!"
            elif (month > curr_month):
                s = "until that day"
            else:
                s = "since that day passed"
        elif (year > curr_year):
            s = "until that day"
        else:
            s = "since that day passed"
        return (s)
        
def days_same_month (past, future):
    return future - past

def days_same_year (past_day, past_month, future_day, future_month, year):
    days = 0
    days = days + days_same_month (past_day, how_many_days_in (past_month, year))
    days = days + future_day
    for i in range (past_month + 1, future_month):
        days = days + how_many_days_in (i, year)
    return days


def dif_year (past_day, past_month, past_year, future_day, future_month, future_year):
    days = 0
    if (past_year == future_year):
        if (past_month == future_month):
            days = days_same_month (past_day, future_day)
        else:
            days = days_same_year (past_day, past_month, future_day, future_month, past_year)
    else:
        days = days + days_same_year (past_day, past_month, 31, 12, past_year)
        days += 1
        days = days + days_same_year (1, 1, future_day, future_month, future_year)
        for i in range (past_year+1, future_year):
            if (i%4 == 0):
                days += 366
            else:
                days += 365
    return (days)

        
if __name__ == '__main__':
    day = 14
    month = 2
    year = 2018
    hours = 0
    minutes = 0
    seconds = 0
    
    curr_day = 10
    curr_month = 10
    curr_year = 2017
    curr_hours = 0
    curr_minutes = 0
    curr_seconds = 0
        
    s = "days " + since_or_until (day, month, year, curr_day, curr_month, curr_year)
    if (s.startswith("days since")):
        print (dif_year (day, month, year, curr_day, curr_month, curr_year), s)
    else:
        print (dif_year (curr_day, curr_month, curr_year, day, month, year), s)
    
    
    
    
    