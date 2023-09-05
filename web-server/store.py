import requests


def get_categoriies():
    r =  requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code)
    print(r.text)
    print(type(r.text))
    categories = r.json()
    print(type(categories))

    for category in categories:
        print(type(category))
        print(category['name'])