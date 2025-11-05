# Python DevOps Examples Script
# ====================================
# This script demonstrates Python basics with a DevOps context:
# 1. Regular Expressions
# 2. Numeric Types
# 3. Strings
# 4. Lists, Tuples, Sets, Dicts
# 5. Boolean, None, and Custom Classes

# ====================================
# 1. REGULAR EXPRESSIONS (Regex)
# ====================================
import re

print("\n--- REGEX EXAMPLES ---")

# Example: Extract IP addresses from a server log
log_data = "Server connected from 192.168.1.10 and 10.0.0.5"
ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'  # Pattern for IPv4 addresses
ips = re.findall(ip_pattern, log_data)
print("Extracted IPs:", ips)

# Example: Validate email addresses in a config file
config_emails = ["admin@company.com", "user@@bademail.com", "dev@company.org"]
email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
valid_emails = [email for email in config_emails if re.match(email_pattern, email)]
print("Valid Emails:", valid_emails)

# ====================================
# 2. NUMERIC TYPES
# ====================================
print("\n--- NUMERIC TYPES ---")

# Integers for server counts
num_servers = 5
print("Number of servers:", num_servers, type(num_servers))

# Floating-point numbers for CPU usage
cpu_usage = 75.5
print("CPU Usage:", cpu_usage, type(cpu_usage))

# Complex number example (less common in DevOps)
z = 2 + 3j
print("Complex number:", z, type(z))

# Arithmetic operations
total_connections = 100 + 250
print("Total connections:", total_connections)

# Using built-in functions
rounded_cpu = round(cpu_usage)
print("Rounded CPU usage:", rounded_cpu)

# ====================================
# 3. STRINGS
# ====================================
print("\n--- STRING EXAMPLES ---")

# Server configuration strings
server_name = "web01"
port = 443
protocol = "HTTPS"

# String formatting using f-strings
config_line = f"Connecting to {server_name} on port {port} using {protocol}"
print(config_line)

# Accessing individual characters
print("First character of server_name:", server_name[0])

# Slicing
print("First 3 letters of server_name:", server_name[:3])

# String methods
raw_config = "   max_connections=1000   "
clean_config = raw_config.strip()  # Remove leading/trailing spaces
print("Clean config line:", clean_config)

# Splitting and joining strings
config_parts = clean_config.split("=")
key, value = config_parts[0], config_parts[1]
print("Key:", key, "| Value:", value)

# Replace text
new_config_line = clean_config.replace("1000", "2000")
print("Updated config line:", new_config_line)

# ====================================
# 4. DATA TYPES: LISTS, TUPLES, SETS, DICTS
# ====================================
print("\n--- DATA STRUCTURES ---")

# List: Mutable sequence of server names
server_list = ["web01", "web02", "db01"]
print("Server List:", server_list)
server_list.append("cache01")
print("Updated Server List:", server_list)

# Tuple: Immutable sequence of ports
ports_tuple = (80, 443, 22)
print("Ports Tuple:", ports_tuple)

# Set: Unique IP addresses
unique_ips = {"192.168.1.10", "10.0.0.5", "192.168.1.10"}
print("Unique IPs Set:", unique_ips)

# Frozenset: Immutable set of environment names
envs = frozenset(["dev", "staging", "prod"])
print("Immutable Environments:", envs)

# Dictionary: Server configuration mapping
server_config = {
    "name": "web01",
    "ip": "192.168.1.10",
    "port": 443,
    "https": True
}
print("Server Config:", server_config)

# ====================================
# 5. BOOLEAN, NONE, CUSTOM CLASS
# ====================================
print("\n--- BOOLEAN, NONE, CUSTOM CLASS ---")

# Boolean values
server_online = True
print("Server Online?", server_online)

# None type: Used for uninitialized values
pending_server = None
print("Pending server:", pending_server)

# Custom class example for DevOps server object
class Server:
    def __init__(self, name, ip, port=80):
        self.name = name
        self.ip = ip
        self.port = port
    
    def info(self):
        return f"{self.name} -> {self.ip}:{self.port}"

# Create server objects
web_server = Server("web01", "192.168.1.10", 443)
db_server = Server("db01", "192.168.1.20")

print("Web Server Info:", web_server.info())
print("DB Server Info:", db_server.info())

# ====================================
# SCRIPT COMPLETE
# ====================================
print("\n--- Script execution complete ---")
# ✅ Features:
# Regex: Parse IP addresses and validate emails.

# Numeric Types: Track servers, CPU usage, and arithmetic operations.

# Strings: Manage configuration data with formatting, slicing, and splitting.

# Lists, Tuples, Sets, Dicts: Organize server info, unique IPs, and immutable data.

# Boolean & None: Server status checks and uninitialized variables.

# Custom Class: Encapsulate server info like a real DevOps object.

