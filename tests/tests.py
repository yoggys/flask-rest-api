### ignore this file in production, only for routing/models testing puposes ###

import requests as req

ENDPOINT = "http://127.0.0.1:5000/api/v1/users"

for ii in range(1, 100):
    try:
        data = req.post(ENDPOINT, {
            "email": f"test{ii}",
            "username": f"test{ii}",
            "password": f"test{ii}",
        }),
    except Exception as E:
        print(f"Something went wrong: {E}")
        exit(1)

    data = data[0]
    print(data.text)

    if  data.status_code == 200:
        id = data.json()['data']['id']
        url = ENDPOINT + f"/{id}"
        tests = [
            req.get(url),
            req.put(url, {
                "email": f"new{ii}",
                "username": f"new{ii}",
                "password": f"new{ii}",
            }),
            req.get(url),
            req.patch(url, {
                "email": f"test{ii}",
                "password": f"test{ii}"
            }),
            req.get(url),
        ]

data = req.get(ENDPOINT)
data = data.json()['data']
print(data)
for row in data:
    url = ENDPOINT + f"/{row['id']}"
    req.delete(url)

data = req.get(ENDPOINT)
data = data.json()['data']
print(data)