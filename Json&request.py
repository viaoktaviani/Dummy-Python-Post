import json 
import requests
import time
import datetime

ulang= 500
for i in range(ulang):
    time.sleep(1)
    Drone_data={
        "droneName" : "via",
        "droneID" : "608641d26c22e4003203546c",
        "userID" : "608641d26c22e4003203546c",
        "batteryState" :"40",
        "connectionState" :"on",
        "controllerState" : "on",
        "actuatorState" : "on",
        "missionState" : "done",
        "flightState": "TESTING",
        "updated" : datetime.datetime.now(),
    }

    class DateTimeJSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime.datetime):
                return obj.isoformat()
            else:
                return super(DateTimeJSONEncoder, self).default(obj)

    url='https://development-navier.azurewebsites.net/api/drone/add-status'
    headers ={ 'Content-type':'application/json'}
    Push=requests.post(url,data=json.dumps(Drone_data, indent=4, cls=DateTimeJSONEncoder),headers=headers)
    print("Status code: ", Push.status_code)
    print("Printing Entire Post Request")
    print(Push.json())

