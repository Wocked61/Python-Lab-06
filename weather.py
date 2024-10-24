'''
# Name: Dylan Phan
# Date: 10/11/2024
# File Purpose: weather functions
'''

import json
import calendar

def read_data(filename):
    try:
          with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
    	return {}


def write_data(data, filename):
    with open(filename,'w') as file:
        return json.dump(data, file)

def max_temperature(data, date):
	temps = [x['t']for key, x in data.items() if date in key]
	return max(temps)

def min_temperature(data,date):
	temps = [x['t']for key, x in data.items() if date in key]
	return min(temps)

def max_humidity(data, date):
	humidity = [x['h']for key , x in data.items() if date in key]
	return max(humidity)

def min_humidity(data, date):
	humidity = [x['h']for key , x in data.items() if date in key]
	return min(humidity)

def tot_rain(data, date):
	rain = [x['r']for key , x in data.items() if date in key]
	return sum(rain)

def report_daily(data, date):
    output ='''========================= DAILY REPORT ========================
Date                      Time  Temperature  Humidity  Rainfall
====================  ========  ===========  ========  ========
'''

    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:8])
    cal_month = calendar.month_name[month]
    act_date = f"{cal_month} {day}, {year}"

    for key,x in sorted(data.items()):
        if key.startswith(date):
            time = f"{key[8:10]}:{key[10:12]}:{key[12:]}"
            output += (f"{act_date:<21} {time:<10} {x['t']:>10} {x['h']:>9} {x['r']:>9.2f}\n")
    return output
 
def report_historical(data):
    output = '''============================== HISTORICAL REPORT ===========================
                          Minimum      Maximum   Minumum   Maximum     Total
Date                  Temperature  Temperature  Humidity  Humidity  Rainfall
====================  ===========  ===========  ========  ========  ========
'''

    dates = sorted(set(key[:8] for key in data.keys()))
    for date in dates:
        min_temp = min_temperature(data,date)
        max_temp = max_temperature(data,date)
        min_humid = min_humidity(data,date)
        max_humid = max_humidity(data,date)
        rain = tot_rain(data,date)
        act_date = f"{calendar.month_name[int(date[4:6])]} {int(date[6:8])}, {int(date[0:4])}"
        output += f"{act_date:<31}{min_temp:<13}{max_temp:<10}{min_humid:<10}{max_humid:<8}{rain:<3.2f}\n"
    return output
