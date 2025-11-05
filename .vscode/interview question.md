# Python & DevOps Interview Preparation Notes

## Section 1: Python Basics & Data Structures

1. **What is a dictionary in Python?**
   - Key-value pair collection, fast lookup.
   - Example:
     server_config = {'server1': {'ip': '192.168.1.1', 'status': 'active'}}

2. **How to safely get a key from a dictionary?**
   - Use dict.get(key, default)
   - Example:
     status = server_config.get('server2', {}).get('status', 'Unknown')

3. **Difference between a list and a set**
   - List: Ordered, allows duplicates, index access.
   - Set: Unordered, unique elements, efficient membership check.

4. **Iterate through a dictionary**
   for server, config in server_config.items():
       print(server, config['ip'])

5. **What are Python sets and why are they useful in DevOps?**
   - Unordered collection of unique elements.
   - Use case: Track deployed services/packages uniquely.
     services = {'nginx', 'mysql', 'redis'}

6. **Check if element exists in a set or list**
   if 'nginx' in services:
       print("nginx is installed")

7. **Add/remove elements from a set**
   services.add('postgres')
   services.remove('mysql')

8. **How can lists be used in DevOps?**
   - For ordered logs, job queues, or pipeline stages.

9. **Difference between remove() and discard() in sets**
   - remove(): Raises KeyError if missing.
   - discard(): Does nothing if missing.

10. **Merge two dictionaries**
    dict1.update(dict2)

---

## Section 2: Python Functions & Exception Handling

11. **Define a Python function for DevOps**
    def get_server_status(server):
        return server_config.get(server, {}).get('status', 'Unknown')

12. **Handle exceptions**
    try:
        open("config.txt")
    except FileNotFoundError:
        print("File missing")

13. **Why exception handling is important in DevOps?**
    - Prevents scripts from crashing, ensures automation continuity.

14. **Difference between try-except and try-finally**
    - try-except: Catch errors.
    - try-finally: Cleanup code always executes.

15. **Pass variable arguments**
    def monitor_servers(*servers):
        for server in servers:
            print(server)

16. **Lambda functions**
    status_check = lambda x: x['status'] == 'active'

17. **Sort list of dictionaries by key**
    sorted_servers = sorted(servers, key=lambda x: x['uptime'])

18. **Remove duplicates from list**
    unique = list(set([1,2,2,3]))

19. **Python modules & importance in DevOps**
    - Reusable scripts for automation: os, requests, subprocess.

20. **Import modules**
    import os
    import requests as req

---

## Section 3: Python for DevOps Automation & Scripting

21. **Execute shell commands**
    import subprocess
    subprocess.run(["ls", "-l"])

22. **Read file line by line**
    with open("log.txt") as f:
        for line in f:
            print(line.strip())

23. **Write to file**
    with open("output.txt", "w") as f:
        f.write("Server status OK\n")

24. **Schedule script execution**
    import schedule, time
    def job(): print("Checking server health")
    schedule.every(5).minutes.do(job)
    while True: schedule.run_pending(); time.sleep(1)

25. **Parse JSON from API**
    import requests
    response = requests.get('https://api.github.com/repos/kubernetes/kubernetes/pulls')
    data = response.json()

26. **Extract PR creators**
    pr_creators = {}
    for pull in data:
        user = pull['user']['login']
        pr_creators[user] = pr_creators.get(user, 0) + 1

27. **Python with AWS**
    - Use boto3 library.

28. **Get EC2 instances**
    import boto3
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances()

29. **Log monitoring**
    import re
    with open("app.log") as f:
        errors = [line for line in f if re.search("ERROR", line)]

30. **Make Python scripts production-ready**
    - Logging, exception handling, config files, no hardcoding.

---

## Section 4: Python for CI/CD & Automation

31. **Check build status from Jenkins**
    url = "http://jenkins/job/myjob/lastBuild/api/json"
    res = requests.get(url).json()
    print(res['result'])

32. **Retry failed API call**
    import time
    for i in range(3):
        try:
            res = requests.get(url)
            if res.status_code == 200: break
        except: time.sleep(2)

33. **Python & Docker automation**
    import docker
    client = docker.from_env()
    client.containers.run("nginx", detach=True)

34. **Python & Kubernetes automation**
    - Use kubernetes Python client.

35. **Parse YAML**
    import yaml
    with open("config.yaml") as f:
        data = yaml.safe_load(f)

36. **Environment variables**
    import os
    db_host = os.getenv("DB_HOST", "localhost")

37. **Monitor disk usage**
    import shutil
    total, used, free = shutil.disk_usage("/")
    print(f"Free: {free // (2**30)} GB")

38. **Send email alerts**
    import smtplib
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('user','pass')
    server.sendmail('from','to','Alert: Server down!')
    server.quit()

39. **Monitor server uptime**
    - Ping server or check TCP port using socket.

40. **Filter logs by time range**
    - Use datetime to parse timestamps and filter.

---

## Section 5: Advanced Python + DevOps Questions

41. **Handle multiple servers concurrently**
    - threading or asyncio.

42. **Integrate Python scripts with GitHub Actions**
    - Use workflow steps to run scripts.

43. **Check process status**
    import psutil
    for proc in psutil.process_iter(['pid', 'name']):
        print(proc.info)

44. **Parse CSV logs**
    import csv
    with open("servers.csv") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row['hostname'], row['status'])

45. **REST API with headers**
    headers = {'Authorization': 'token XYZ'}
    res = requests.get(url, headers=headers)

46. **Backup files**
    import shutil
    shutil.copy('source.txt','backup/source.txt')

47. **Measure script execution time**
    import time
    start = time.time()
    # code
    print("Time:", time.time() - start)

48. **Compare two directories**
    import filecmp
    filecmp.cmpfiles("dir1","dir2", ["file1.txt"])

49. **Make Python script executable**
    chmod +x script.py
    ./script.py

50. **Log output to a file**
    import logging
    logging.basicConfig(filename='app.log', level=logging.INFO)
    logging.info("Server checked")

51. **Monitor memory usage**
    import psutil
    print(psutil.virtual_memory())

---

## Section 6: Practical Examples & Exercises

- **Server dictionary example**
  server_config = {
      'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active'},
      'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive'}
  }

- **Retrieve server status function**
  def get_server_status(server_name):
      return server_config.get(server_name, {}).get('status', 'Server not found')

- **GitHub PR extraction example**
  (Already covered in Q25-26)

- **List vs Set differences** (refer Q3-9)

---

# End of Notes
