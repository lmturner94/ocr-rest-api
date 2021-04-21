import requests
url = "https://safe-caverns-80544.herokuapp.com/todo/1"
with requests.session() as s:
     r = s.get(url)

     print(r)