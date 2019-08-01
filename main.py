import json

with open('config/db_connection.json') as db_config_file:
  data = json.load(db_config_file)

print(db_config_file) 

server_tnsname = data['server_tnsname']
db_username = data['db_username']
db_password = data['db_password']

print(server_tnsname)
print(db_username)
print(db_password)