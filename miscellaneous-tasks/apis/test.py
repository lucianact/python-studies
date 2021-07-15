import requests 
from datetime import datetime


def get_applicant_and_location(userInput):

    url = userInput[0]
    # print(url)

    # Include an HTTP authorization header:
    api_token = userInput[2]
    # print(api_token)

    header = { "Authorization" : "Basic " + api_token}
    # test = header["Authorization"]
    # print(test)

    # Convert the UNIX timestamp given to extract the day of the week, hour, minutes (UTC format).
    time = float(userInput[1])
    # print(time)

    utc = datetime.utcfromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
    # print(utc)
    hour = datetime.utcfromtimestamp(time).strftime('%H')
    # print(hour)
    minute = datetime.utcfromtimestamp(time).strftime('%M')
    # print(minute)
    week_day = datetime.utcfromtimestamp(time).strftime('%w')
    # print(week_day)

    # Use the time extracted above as parameters to fetch the data 
    # Your request should have the following parameters: hour, minutes, dayOrder

    # MY COMMENT:
    # This piece of information was not very clear;
    # I had to spend significant amout of time testing
    # how these strings should look like
    payload = { 
                "hour" : hour,
                "minutes" : minute,
                "dayOrder": week_day
                }

    my_req = requests.get(url, headers=header,params=payload)
    
    response_status = my_req.status_code
    print(response_status)
    
    if response_status == 200: 
        # access response data:
        response = my_req.json()
        # print(response)
        data = response['data']
        # print(data)

        # filtering and printing the output:
        food_trucks = []

        for element in data:
            applicant = element["Applicant"]
            locationid = str(element["locationid"])
            pair = applicant + ", " + locationid
            food_trucks.append(pair)
        
        for line in sorted(food_trucks):
            print(line)
    
    else: 
        return "Something went wrong"

print(get_applicant_and_location(["https://api.filtered.ai/q/foodtruck", "1602172800", "ZmlsdGVyZWQ6YWRtaW4"]))