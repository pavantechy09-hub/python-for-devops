"""
==========================================
Python Operators in DevOps: Full Demonstration
==========================================
This script demonstrates all Python operators with DevOps-specific, real-time examples.

Topics Covered:
1. Arithmetic Operators
2. Assignment Operators
3. Relational Operators
4. Logical Operators
5. Bitwise Operators
6. Identity Operators
7. Membership Operators
8. Operator Precedence

Each section includes examples with detailed explanations and real-world DevOps usage.
"""

print("\n--- 1. ARITHMETIC OPERATORS ---")
# Example: Calculating server uptime in hours
uptime_days = 5
uptime_hours_per_day = 24
total_hours = uptime_days * uptime_hours_per_day  # Multiplication
print(f"Server uptime in hours: {total_hours}")

# Addition and subtraction
added_hours = total_hours + 2  # e.g., adding manual adjustment
reduced_hours = total_hours - 5  # e.g., subtract maintenance downtime
print(f"Adjusted uptime hours (+2): {added_hours}")
print(f"Adjusted uptime hours (-5): {reduced_hours}")

# Division and floor division
servers = 3
hours_per_server = total_hours / servers
hours_per_server_floor = total_hours // servers
print(f"Average hours per server: {hours_per_server}")
print(f"Floor division hours per server: {hours_per_server_floor}")

# Modulus and exponentiation
remainder = total_hours % servers
print(f"Remaining hours after equal distribution: {remainder}")
print(f"Example of exponentiation: 2**3 = {2**3}")


print("\n--- 2. ASSIGNMENT OPERATORS ---")
# Example: Tracking deployed containers
containers = 10
print(f"Initial containers: {containers}")
containers += 5  # deployed 5 more
print(f"After deployment += 5: {containers}")
containers -= 3  # removed 3 containers
print(f"After scaling down -= 3: {containers}")
containers *= 2  # duplicating across environments
print(f"Duplicated containers *=2: {containers}")
containers //= 4  # evenly distributing across 4 clusters
print(f"Distributed containers //=4: {containers}")
containers %= 3
print(f"Remaining containers %=3: {containers}")
containers **= 2
print(f"Exponential example containers **=2: {containers}")


print("\n--- 3. RELATIONAL OPERATORS ---")
# Example: Comparing CPU usage thresholds
cpu_usage = 85
warning_threshold = 80
critical_threshold = 90

print(f"CPU at {cpu_usage}% > warning? {cpu_usage > warning_threshold}")
print(f"CPU at {cpu_usage}% < critical? {cpu_usage < critical_threshold}")
print(f"CPU at {cpu_usage}% == 85? {cpu_usage == 85}")
print(f"CPU at {cpu_usage}% != 70? {cpu_usage != 70}")
print(f"CPU >= warning? {cpu_usage >= warning_threshold}")
print(f"CPU <= critical? {cpu_usage <= critical_threshold}")


print("\n--- 4. LOGICAL OPERATORS ---")
# Example: Check if alert needs to be triggered
disk_usage = 92
high_disk_alert = disk_usage > 90
high_cpu_alert = cpu_usage > 90

# Trigger alert if either CPU or Disk usage is high
trigger_alert = high_disk_alert or high_cpu_alert
print(f"Trigger alert (disk OR CPU high)? {trigger_alert}")

# Trigger alert only if both are critical
critical_alert = high_disk_alert and high_cpu_alert
print(f"Critical alert (disk AND CPU high)? {critical_alert}")

# Invert condition: no alert needed
no_alert_needed = not (high_disk_alert or high_cpu_alert)
print(f"No alert needed? {no_alert_needed}")


print("\n--- 5. BITWISE OPERATORS ---")
# Example: Using bitmask flags for server status
# 0b001 = Running, 0b010 = Maintenance, 0b100 = Backup
server_status = 0b101  # Running + Backup
maintenance_flag = 0b010
running_flag = 0b001

# Check if server is running
is_running = server_status & running_flag
print(f"Is server running? {'Yes' if is_running else 'No'}")

# Add maintenance flag
server_status |= maintenance_flag
print(f"Server status after maintenance |= : {bin(server_status)}")

# Toggle running status
server_status ^= running_flag
print(f"Server status after toggle ^= : {bin(server_status)}")

# Flip all bits (simulate status reset)
print(f"Flipped status ~: {bin(~server_status)}")


print("\n--- 6. IDENTITY OPERATORS ---")
# Example: Check if two config objects point to the same memory
config_a = {"env": "prod", "replicas": 3}
config_b = config_a  # same reference
config_c = {"env": "prod", "replicas": 3}  # different object

print(f"config_a is config_b? {config_a is config_b}")
print(f"config_a is config_c? {config_a is config_c}")
print(f"config_a is not config_c? {config_a is not config_c}")


print("\n--- 7. MEMBERSHIP OPERATORS ---")
# Example: Check if a node is in the cluster
cluster_nodes = ["node1", "node2", "node3"]
node_to_check = "node2"
print(f"{node_to_check} in cluster? {node_to_check in cluster_nodes}")

missing_node = "node5"
print(f"{missing_node} not in cluster? {missing_node not in cluster_nodes}")


print("\n--- 8. OPERATOR PRECEDENCE ---")
# Example: Auto-scaling decision calculation
cpu_avg = 75
memory_avg = 60
scale_factor = 2

# Precedence: multiplication before addition
decision_score = cpu_avg + memory_avg * scale_factor
print(f"Decision score without parentheses: {decision_score}")

# Parentheses to override precedence
decision_score_parentheses = (cpu_avg + memory_avg) * scale_factor
print(f"Decision score with parentheses: {decision_score_parentheses}")


print("\n--- Script execution complete ---")
# ✅ Features of This Script:
# Arithmetic Operators → Calculating uptime, average server hours.

# Assignment Operators → Managing container deployments.

# Relational Operators → Checking CPU thresholds.

# Logical Operators → Triggering alerts based on combined metrics.

# Bitwise Operators → Server status flags (common in infrastructure monitoring).

# Identity Operators → Comparing config objects for memory reference.

# Membership Operators → Checking nodes in clusters.

# Operator Precedence → Auto-scaling decision logic.

"""
==========================================
Python Operators & Text Handling in DevOps
==========================================
This script demonstrates all Python operators + Regex & String operations
with real-world DevOps examples: log parsing, alert messages, config handling.

Topics Covered:
1. Arithmetic Operators
2. Assignment Operators
3. Relational Operators
4. Logical Operators
5. Bitwise Operators
6. Identity Operators
7. Membership Operators
8. Operator Precedence
9. String Operations
10. Regex Operations
"""

import re

print("\n--- 9. STRING OPERATIONS ---")
# Example 1: Handling log messages
log_message = "ERROR: Disk usage at 92% on server node2"

# Accessing characters and slicing
print(f"First character: {log_message[0]}")
print(f"Log level: {log_message[:5]}")  # ERROR

# String methods
print(f"Lowercase: {log_message.lower()}")
print(f"Uppercase: {log_message.upper()}")
print(f"Check if starts with 'ERROR': {log_message.startswith('ERROR')}")
print(f"Check if ends with 'node2': {log_message.endswith('node2')}")

# Splitting & joining
words = log_message.split()
print(f"Words in log message: {words}")
rejoined = "-".join(words)
print(f"Rejoined with '-': {rejoined}")

# String formatting & f-strings
server_name = "node2"
disk_usage = 92
alert_msg = f"ALERT: Disk usage {disk_usage}% on server {server_name}"
print(alert_msg)

# Substring search and replacement
cleaned_log = log_message.replace("ERROR", "WARNING")
print(f"Cleaned log: {cleaned_log}")


print("\n--- 10. REGEX OPERATIONS ---")
# Regex is extremely useful for parsing logs, extracting IPs, timestamps, etc.

log_lines = [
    "2025-11-04 12:30:15 INFO Server node1 running smoothly",
    "2025-11-04 12:31:00 ERROR Disk usage 92% on node2",
    "2025-11-04 12:32:10 WARNING CPU at 85% on node3"
]

# Extract timestamps from logs
timestamp_pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
timestamps = [re.search(timestamp_pattern, line).group() for line in log_lines]
print(f"Timestamps extracted: {timestamps}")

# Find all nodes mentioned in logs
node_pattern = r"node\d"
nodes = [re.findall(node_pattern, line)[0] for line in log_lines if re.findall(node_pattern, line)]
print(f"Nodes mentioned in logs: {nodes}")

# Extract log levels (INFO, ERROR, WARNING)
level_pattern = r"\b(INFO|ERROR|WARNING)\b"
levels = [re.search(level_pattern, line).group() for line in log_lines]
print(f"Log levels: {levels}")

# Replace all ERROR with ALERT
alert_logs = [re.sub(r"ERROR", "ALERT", line) for line in log_lines]
print("Logs after ALERT replacement:")
for log in alert_logs:
    print(log)

# Check if a line contains a critical alert (disk > 90%)
critical_disk_pattern = r"Disk usage (\d+)%"
for line in log_lines:
    match = re.search(critical_disk_pattern, line)
    if match and int(match.group(1)) > 90:
        print(f"Critical disk usage detected in line: {line}")


print("\n--- Complete DevOps Python Examples Executed ---")
# ✅ What’s New in This Update:
# String Operations:

# Log parsing, substring checks, splitting/joining.

# Formatting alerts using f-strings.

# Search & replace log levels.

# Regex Operations:

# Extract timestamps, server nodes, log levels from logs.

# Replace "ERROR" with "ALERT" dynamically.

# Detect critical conditions (disk > 90%) automatically.