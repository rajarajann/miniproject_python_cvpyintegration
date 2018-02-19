import requests
from base64 import b64encode

user_name = "raj_admin"#input("Enter login user name:")
f_username = "'{}'".format (user_name)
user_pwd = "Commvault@123"#input("Enter login password:")
b64_pwd = b64encode(user_pwd.encode()).decode()
f_pwd = "'{}'".format (b64_pwd)
xml_data = "<DM2ContentIndexing_CheckCredentialReq mode='Webconsole' username={} password={} />".format(f_username,f_pwd)
headers = {'Content-Type': 'application/xml','Accept': 'application/json'} # set what your server accepts

post_login = requests.post('http://comm-server:81/SearchSvc/CVWebService.svc/Login', data=xml_data, headers=headers)
print(type(post_login))
response_login = post_login.json()
response_token = response_login ['token']
split_token = response_token.split(" ")
auth_token = split_token[1]
print(auth_token)

whoami_headers = {'Content-type': 'application/xml', 'Accept': 'application/json','Cookie2': response_token}
post_whoami = requests.post('http://comm-server:81/SearchSvc/CVWebService.svc/WhoAmI', headers=whoami_headers)
print(type(post_whoami))
response_whoami = post_whoami.text
whoami_list = response_whoami.split(" ")
print(whoami_list[1],whoami_list[2],whoami_list[3],whoami_list[4])