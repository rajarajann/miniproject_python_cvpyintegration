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

response_login = post_login.json()
response_token = response_login ['token']
split_token = response_token.split(" ")
auth_token = split_token[1]


post_headers = {'Content-type': 'application/xml', 'Accept': 'application/json','Cookie2': response_token}
post_whoami = requests.post('http://comm-server:81/SearchSvc/CVWebService.svc/WhoAmI', headers=post_headers)

response_whoami = post_whoami.text
whoami_list = response_whoami.split(" ")
print(whoami_list[1],whoami_list[2],whoami_list[3],whoami_list[4])

get_headers = {'Accept': 'application/json','Cookie2': response_token}
get_clientinfo = requests.get('http://comm-server:81/SearchSvc/CVWebService.svc/Client', headers = get_headers)
response_clientinfo = get_clientinfo.json()

def all_clients(allclients_header):
    client_properties_dict = {}
    get_clientinfo = requests.get('http://comm-server:81/SearchSvc/CVWebService.svc/Client', headers=allclients_header)
    response_clientinfo = get_clientinfo.json()
    r1 = response_clientinfo['clientProperties']

    client1 = r1[0]
    client1_client = client1['client']
    client1_client_clientEntity = client1_client['clientEntity']
    client_properties_dict ['client-1'] = client1_client_clientEntity

    client2 = r1[1]
    client2_client = client2['client']
    client2_client_clientEntity = client2_client['clientEntity']
    client_properties_dict['client-2'] = client2_client_clientEntity
    #print(client_properties_dict)
    return client_properties_dict

client_dictionary = all_clients(get_headers) #type : Dict

print ("Client Name:    ",client_dictionary['client-1']['clientName'],"     ","Client ID:   ",client_dictionary['client-1']['clientId'])
client_ID = client_dictionary['client-1']['clientId']

def backupset(client_ID,backupset_header):
    get_backupsetinfo = requests.get('http://comm-server:81/SearchSvc/CVWebService.svc/Backupset?clientId=%d' % (client_ID), headers=backupset_header)
    response_backupinfo = get_backupsetinfo.json()
    r1=response_backupinfo['backupsetProperties']
    r2 = r1[0]
    backupset_entity_dict = r2['backupSetEntity']
    backupsetID = backupset_entity_dict['backupsetId']
    print(backupsetID)

backupset(client_ID,get_headers)

def

