# PortSwiggerSolutions
I will more or less systematically post automatic solutions to challenges from the portswigger platform.
https://portswigger.net/web-security/all-labs

In each case the script works the same way

Correct
```
python3 solution.py https://<ID>.web-security-academy.net <collab ID>9.oastify.com
```

Wrong
```
python3 solution.py https://<ID>.web-security-academy.net/ <collab ID>9.oastify.com
python3 solution.py https://<ID>.web-security-academy.net http://<collab ID>9.oastify.com
python3 solution.py https://<ID>.web-security-academy.net/ http://<collab ID>9.oastify.com
python3 solution.py <ID>.web-security-academy.net http://<collab ID>9.oastify.com
python3 solution.py <ID>.web-security-academy.net/ http://<collab ID>9.oastify.com
```
