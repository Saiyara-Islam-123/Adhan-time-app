import requests

from datetime import datetime

def get_salah_time_na(date, country, city):

    url = "http://api.aladhan.com/v1/timingsByCity?city=" + city + " &country=" + country +"&method=2/:" + date
    
    response = requests.get(url)
    
    data = response.json()
    
    timings = data["data"]["timings"]
    
    fajr = timings["Fajr"]
    #sunrise = timings["Sunrise"]
    dhuhr = timings["Dhuhr"]
    asr = timings["Asr"]
    #sunset = timings["Sunset"]
    maghrib = timings["Maghrib"]
    isha = timings["Isha"]
    
    date_string_split = date.split("-")
    
    date = date_string_split[0]
    month = date_string_split[1]
    year = date_string_split[2]
    
    date_string = year + "-" + month + "-" + date
    
    fajr_date_time_string = date_string + " " + fajr
    
    dhuhr_date_time_string = date_string + " " + dhuhr
    
    asr_date_time_string = date_string + " " + asr
    
    maghrib_date_time_string = date_string + " " + maghrib
    
    isha_date_time_string = date_string + " " + isha    
    
    
    current_datetime = datetime.now()
    datetime_str = current_datetime.strftime('%Y-%m-%d %H:%M')

    
    print(datetime_str)
    print(fajr_date_time_string)
    
    if datetime_str == fajr_date_time_string:
        print("wake up! Fajr!")
    elif datetime_str == dhuhr_date_time_string:
        print("dhuhr time!")
        
    elif datetime_str == asr_date_time_string:
        print("asr time!")
        
    elif datetime_str == maghrib_date_time_string:
        print("maghrib time!")
    elif datetime_str == isha_date_time_string:
        print("isha time!")
    