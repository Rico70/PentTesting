import requests
from requests import status_codes

response = requests.get("https://rafaelrrodriguez.com")

if(response.status_code == 200):
    response = requests.get("https://rafaelrrodriguez.com/wp-login.php")
    print('request sucess!')

    if(response.status_code == 200):
        print("vulnerable site")
    else:
        print(response.status_code)
        print(("Not a vulnerable site"))
else:
    print("request failure")