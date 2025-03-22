import requests

def fectch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    
    response = requests.get(url)
    data = response.json()
    
    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        gender = user_data["gender"]
        
        return username, country, gender
    
    else:
        raise Exception("User data not found.")    
    

def main():
    try:
        username, country, gender = fectch_random_user()
        print(f"Username: {username}")
        print(f"Country: {country}")
        print(f"Gender: {gender}")
    except Exception as e:
        print(f"Error: {e}")
    
if __name__ == "__main__":
    main()