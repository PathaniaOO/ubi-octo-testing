import requests
database ={
    1:"Alice",
    2:"Bob",
    3:"Charlie"
}

def get_user_from_db(user_id):
    return database.get(user_id)

def get_users():
    respone = requests.get("https://jsonplaceholder.typicode.com/users")
    if respone.status_code == 200:
        return respone.json()
    else:
        raise requests.HTTPError