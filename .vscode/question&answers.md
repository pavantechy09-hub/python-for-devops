Q1: What is a dictionary in Python and why is it used?
Answer:
A dictionary is a collection of key-value pairs. It allows fast retrieval of values using keys. In DevOps, dictionaries are used to store configurations, environment variables, or API responses.
Example:
server_config = {'server1': 'active', 'server2': 'inactive'}
print(server_config['server1'])  # Output: active

Q2: How do you add or modify elements in a dictionary?
Answer:
Use key assignment to modify or add.
Example:
my_dict = {'name': 'John'}
my_dict['name'] = 'Alice'  # Modify
my_dict['age'] = 30        # Add

Q3: How can you check if a key exists in a dictionary?
Answer:
Use the 'in' operator.
Example:
if 'age' in my_dict:
    print('Age exists')

Q4: Explain sets and their use cases.
Answer:
A set is an unordered collection of unique elements. Useful in DevOps to remove duplicates, manage unique hosts, or calculate intersections between environment groups.
Example:
hosts_set = {'host1', 'host2', 'host2'}  # Result: {'host1', 'host2'}

Q5: How do you perform union, intersection, and difference on sets?
Answer:
set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))        # {1,2,3,4,5}
print(set1.intersection(set2)) # {3}
print(set1.difference(set2))   # {1,2}

Q6: Compare lists vs sets in Python.
Answer:
- Lists: ordered, allow duplicates, indexed access.
- Sets: unordered, unique elements, no indexing.
Use lists when order matters; sets when uniqueness and set operations matter.

Q7: Write a Python function to get server status from a dictionary.
Answer:
def get_server_status(server_name, server_dict):
    return server_dict.get(server_name, {}).get('status', 'Server not found')
server_config = {'server1': {'status': 'active'}, 'server2': {'status': 'inactive'}}
print(get_server_status('server1', server_config))  # active

Q8: How can you list files in multiple directories?
Answer:
import os
def list_files(folders):
    for folder in folders:
        try:
            files = os.listdir(folder)
            print(f"Files in {folder}: {files}")
        except Exception as e:
            print(f"Error accessing {folder}: {e}")
list_files(['/etc', '/tmp'])

Q9: Explain integration of Python with GitHub API.
Answer:
Python's requests module can fetch data from GitHub API.
Example:
import requests
url = 'https://api.github.com/repos/kubernetes/kubernetes/pulls'
response = requests.get(url)
if response.status_code == 200:
    prs = response.json()
    for pr in prs[:5]:  # first 5 PRs
        print(pr['user']['login'])

Q10: How to count the number of PRs per user from GitHub API?
Answer:
pr_creators = {}
for pr in prs:
    user = pr['user']['login']
    pr_creators[user] = pr_creators.get(user,0)+1
print(pr_creators)

Q11: Explain Python lists and common operations.
Answer:
- Mutable, ordered collection.
- Add: append(), insert()
- Remove: remove(), pop(), del
- Iterate: for i in list
Example:
my_list = [1,2,3]
my_list.append(4)
my_list.remove(2)

Q12: How do you remove duplicates from a list using sets?
Answer:
my_list = [1,2,2,3]
unique_list = list(set(my_list))  # [1,2,3]

Q13: Explain dictionary iteration.
Answer:
for key, value in my_dict.items():
    print(key, value)

Q14: How to handle missing keys in a dictionary?
Answer:
Use get() with default.
Example:
print(my_dict.get('age','Not Found'))

Q15: Explain mutability in Python lists and sets.
Answer:
Both are mutable. Lists: change values at index. Sets: add/remove elements.

Q16: How to merge two dictionaries?
Answer:
dict1 = {'a':1}
dict2 = {'b':2}
dict1.update(dict2)  # dict1 = {'a':1,'b':2}

Q17: How to filter active servers from a dictionary?
Answer:
active_servers = {k:v for k,v in server_config.items() if v['status']=='active'}

Q18: Explain Python exception handling.
Answer:
Use try-except blocks for errors like FileNotFound, PermissionError.
Example:
try:
    open('file.txt')
except FileNotFoundError:
    print('File not found')

Q19: Explain Python functions with return values.
Answer:
def add(a,b):
    return a+b
print(add(2,3))  # 5

Q20: Explain Python modules and importing.
Answer:
Modules are reusable code files. Import with import module_name
Example:
import os
print(os.listdir('/'))

Q21: What is Python list comprehension?
Answer:
A concise way to create lists.
Example:
squares = [x*x for x in range(5)]
print(squares)  # [0,1,4,9,16]

Q22: How to filter even numbers from a list using list comprehension?
Answer:
nums = [1,2,3,4,5]
evens = [x for x in nums if x%2==0]
print(evens)  # [2,4]

Q23: How do you read environment variables in Python?
Answer:
import os
db_user = os.getenv('DB_USER','default_user')
print(db_user)

Q24: Explain logging in Python for DevOps scripts.
Answer:
Use the logging module to track script execution.
Example:
import logging
logging.basicConfig(level=logging.INFO)
logging.info('Script started')

Q25: How do you execute shell commands from Python?
Answer:
import subprocess
subprocess.run(['ls','-l'])

Q26: Explain Python decorators.
Answer:
Decorators modify function behavior without changing code.
Example:
def log(func):
    def wrapper():
        print('Before')
        func()
        print('After')
    return wrapper
@log
def say_hello():
    print('Hello')
say_hello()

Q27: How do you handle JSON data in Python?
Answer:
import json
data = '{"name":"John"}'
parsed = json.loads(data)
print(parsed['name'])

Q28: How to write data to JSON file in Python?
Answer:
import json
data = {'name':'John'}
with open('file.json','w') as f:
    json.dump(data,f)

Q29: Explain Python sets for removing duplicates from logs.
Answer:
logs = ['a','b','a']
unique_logs = set(logs)  # {'a','b'}

Q30: How to combine multiple dictionaries?
Answer:
dict1 = {'a':1}
dict2 = {'b':2}
dict3 = {'c':3}
combined = {**dict1, **dict2, **dict3}

Q31: How to sort a dictionary by values?
Answer:
my_dict = {'a':3,'b':1}
sorted_dict = dict(sorted(my_dict.items(), key=lambda item:item[1]))
print(sorted_dict)  # {'b':1,'a':3}

Q32: How do you implement retries in Python scripts for DevOps tasks?
Answer:
import time
for i in range(3):
    try:
        # perform action
        break
    except Exception:
        time.sleep(5)  # retry after 5 seconds

Q33: How to handle YAML files in Python for configuration?
Answer:
import yaml
with open('config.yaml') as f:
    cfg = yaml.safe_load(f)
print(cfg)

Q34: Explain Python virtual environments.
Answer:
Virtualenv isolates project dependencies.
python -m venv myenv
source myenv/bin/activate
pip install package

Q35: How to read command-line arguments in Python?
Answer:
import sys
print(sys.argv)  # list of arguments

Q36: How to monitor script performance in Python?
Answer:
Use time module.
import time
start = time.time()
# code
end = time.time()
print(f"Execution time: {end-start} sec")

Q37: How to send emails from Python script in DevOps?
Answer:
import smtplib
server = smtplib.SMTP('smtp.example.com',25)
server.sendmail('from@example.com','to@example.com','Body text')

Q38: How to fetch files from S3 bucket using Python?
Answer:
import boto3
s3 = boto3.client('s3')
s3.download_file('bucket','file.txt','local.txt')

Q39: How do you parse logs and extract error lines in Python?
Answer:
with open('log.txt') as f:
    errors = [line for line in f if 'ERROR' in line]

Q40: How to schedule Python scripts using cron in DevOps?
Answer:
0 2 * * * /usr/bin/python3 /path/to/script.py  # cron entry

Q41: Explain multithreading in Python.
Answer:
Threading allows parallel execution.
import threading
def task(): print('Running')
t = threading.Thread(target=task)
t.start()

Q42: How to create a Python class for server objects?
Answer:
class Server:
    def __init__(self,name,status):
        self.name=name
        self.status=status
s = Server('s1','active')
print(s.name,s.status)

Q43: How to serialize Python objects?
Answer:
import pickle
data = {'a':1}
with open('file.pkl','wb') as f:
    pickle.dump(data,f)

Q44: How to deserialize Python objects?
Answer:
import pickle
with open('file.pkl','rb') as f:
    data = pickle.load(f)
print(data)

Q45: How to handle large CSV files in Python efficiently?
Answer:
import pandas as pd
chunks = pd.read_csv('large.csv', chunksize=10000)
for chunk in chunks:
    # process chunk

Q46: How to check Python version and installed packages?
Answer:
import sys
import pkg_resources
print(sys.version)
installed = pkg_resources.working_set
print(installed)

Q47: How to run shell scripts from Python and capture output?
Answer:
import subprocess
result = subprocess.run(['ls','-l'], stdout=subprocess.PIPE)
print(result.stdout.decode())

Q48: How to monitor server health using Python scripts?
Answer:
import psutil
print(psutil.cpu_percent())
print(psutil.virtual_memory().percent)

Q49: How to handle API rate limits in Python scripts?
Answer:
import time
for i in range(10):
    try:
        # call API
        pass
    except Exception:
        time.sleep(60)  # wait on rate limit

Q50: What is the difference between Python 2 and 3 for DevOps scripts?
Answer:
- Python 3: print() function, Unicode by default, integer division.
- Python 2: print statement, ASCII by default.
Use Python 3 for modern DevOps automation.
