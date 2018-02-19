import requests
from base64 import b64encode

user_name = "raj_admin"#input("Enter login user name:")
f_username = "'{}'".format (user_name)
user_pwd = "Commvault@123"#input("Enter login password:")
b64_pwd = b64encode(user_pwd.encode()).decode()
f_pwd = "'{}'".format (b64_pwd)
xml_data = "<DM2ContentIndexing_CheckCredentialReq mode='Webconsole' username={} password={} />".format(f_username,f_pwd)
headers = {'Content-Type': 'application/xml', 'Accept': 'application/json'}  # set what your server accepts

post_login = requests.post('http://comm-server:81/SearchSvc/CVWebService.svc/Login', data=xml_data, headers=headers)
response_login = post_login.json()

print(response_login)
