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


print(1+1)
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


#solve fibonacci problem
#f(n) = f(n-2)+f(n-1), given n>=2

def get_fibonacci_sequence():
  #O(1)
  fibonacci_list = [0,1]
  
  #O(1)
  i=2

  #O(n-2) ~ O(n)
  while(i<10):
    #O(1) O(1) O(1)
    fibonacci_list.append(fibonacci_list[i-2] + fibonacci_list[i-1])
    print(fibonacci_list)
    print("===========")
    #O(1)
    i = i+1

  return fibonacci_list

#Total Complexity = O(n)
#which is better than an exponential time complexity that results from the recursive fibonacci
# refer exponential cost in the video https://www.youtube.com/watch?v=pqivnzmSbq4&feature=youtu.be
list_fib = get_fibonacci_sequence()
#print(list_fib)

import bison
b = bison.Bison("ishan is bison")
c = bison.Bison("ishan is bison")
print(b.name)
print(c.name)
print(b.name == c.name)
print(b==c)

#get memory hashvalue of the new object
print(1)