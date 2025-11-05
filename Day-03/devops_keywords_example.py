"""
Python Keywords in Real DevOps Context

This script demonstrates the use of Python keywords
in practical DevOps automation examples.
"""

# ==============================
# 1-3. Logical Operators: and, or, not
# ==============================
cpu_usage = 70
memory_usage = 80

# Check if server is overloaded
if cpu_usage > 75 and memory_usage > 75:
    print("Server overloaded: High CPU and Memory")
elif cpu_usage > 75 or memory_usage > 75:
    print("Server partially overloaded")
else:
    print("Server running normally")

# Using 'not' to invert a condition
maintenance_mode = False
if not maintenance_mode:
    print("Deployments are allowed")
print("-" * 40)

# ==============================
# 4-6. if, elif, else
# ==============================
status_code = 503
if status_code == 200:
    print("Server is healthy")
elif status_code == 503:
    print("Server unavailable, try later")
else:
    print("Server status unknown")
print("-" * 40)

# ==============================
# 7-9. while, for, in
# ==============================
# Example: Monitor servers until they all become healthy
servers = ["web1", "web2", "db1"]
healthy = [False, False, False]

# Simulate server checks
i = 0
while i < len(servers):
    print(f"Checking {servers[i]}...")
    healthy[i] = True
    i += 1

for server, status in zip(servers, healthy):
    if status in [True]:
        print(f"{server} is healthy")
print("-" * 40)

# ==============================
# 10-12. try, except, finally
# ==============================
try:
    # Simulate reading a config file
    with open("server_config.txt", "r") as f:
        config = f.read()
except FileNotFoundError:
    print("Config file not found, using default settings")
finally:
    print("Config check complete")
print("-" * 40)

# ==============================
# 13-14. def, return
# ==============================
def calculate_max_connections(server_load):
    """Return adjusted max connections based on server load"""
    if server_load > 80:
        return 500
    return 1000

current_load = 85
max_conn = calculate_max_connections(current_load)
print(f"Adjusted max connections: {max_conn}")
print("-" * 40)

# ==============================
# 15. class
# ==============================
class Server:
    """Represent a server in a DevOps workflow"""
    def __init__(self, name, ip):
        self.name = name
        self.ip = ip

    def deploy(self):
        print(f"Deploying {self.name} at {self.ip}")

web_server = Server("web1", "192.168.1.10")
web_server.deploy()
print("-" * 40)

# ==============================
# 16-18. import, from, as
# ==============================
import os  # access environment variables
from datetime import datetime as dt  # alias for convenience

print("Current time:", dt.now())
print("Home directory:", os.getenv("HOME"))
print("-" * 40)

# ==============================
# 19-21. True, False, None
# ==============================
deployment_success = True
rollback_needed = False
last_error = None

if deployment_success:
    print("Deployment successful")
if rollback_needed is False:
    print("No rollback required")
if last_error is None:
    print("No errors recorded")
print("-" * 40)

# ==============================
# 22. is
# ==============================
a = web_server
b = web_server
print("Are both references the same object?", a is b)
print("-" * 40)

# ==============================
# 23. lambda
# ==============================
# Quick check: filter servers with names starting with 'web'
filtered_servers = list(filter(lambda s: s.startswith("web"), servers))
print("Web servers:", filtered_servers)
print("-" * 40)

# ==============================
# 24. with
# ==============================
# Use context manager for file handling (safe resource handling)
with open("deploy_log.txt", "w") as log_file:
    log_file.write("Deployment started...\n")
print("Deployment log created")
print("-" * 40)

# ==============================
# 25-26. global, nonlocal
# ==============================
deployment_count = 0  # global variable

def deploy_service():
    global deployment_count  # modify global variable
    deployment_count += 1
    print(f"Deployment count: {deployment_count}")

def nested_example():
    count = 0
    def inner():
        nonlocal count  # modify enclosing function variable
        count += 1
        print(f"Inner count: {count}")
    inner()
    inner()

deploy_service()
nested_example()
