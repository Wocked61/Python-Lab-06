'''
# Name: Dylan Phan
# Date: 10/11/2024
# File Purpose: weather program main
'''
import weather


filename = 'weather_data.json'
data = {}

while True :
    inp1 = input('''
    *** TUFFY TITAN WEATHER LOGGER MAIN MENU

1. Set data filename
2. Add weather data
3. Print daily report
4. Print historical report
9. Exit the program

Enter menu choice: ''')
    if (inp1 == '1'):
        input2 = input('\nEnter data filename: ')
        data = weather.read_data(input2)


    if (inp1 == '2'):
        in_date = input('Enter date (YYYYMMDD): ')
        in_time = input('Enter time (hhmmss): ')
        in_temp = input('Enter temperature: ')
        in_humid = input('Enter humidity: ')
        in_rain = input('Enter rainfall: ')
        data[f'{in_date}{in_time}'] = {
            'weather': {
                't': int(in_temp),'h': int(in_humid),'r': float(in_rain)
            }
        }
        weather.write_data(data,filename)

    if (inp1 == '3'):
        in_date = input('Enter date (YYYYMMDD): ')
        print(weather.report_daily(data,in_date))

    if (inp1 == '4'):
        print(weather.report_historical(data))

    if (inp1 == '9'):
        break