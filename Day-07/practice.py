"""
========================================================
Conditional Statements in Python – DevOps Examples
========================================================

This script demonstrates how to use if, elif, and else statements
in Python with practical DevOps scenarios.
"""

# Example 1: Basic if statement – checking server load
server_load = 85  # percent

if server_load > 80:
    print(f"WARNING: Server load is high at {server_load}%!")
# Here, the code block executes only if the condition is True

# Example 2: Using if-elif-else – server status check
server_status = "maintenance"

if server_status == "running":
    print("Server is operational.")
elif server_status == "maintenance":
    print("Server is under maintenance. Schedule tasks accordingly.")
elif server_status == "down":
    print("Server is down! Alert the sysadmin immediately!")
else:
    print("Unknown server status!")

# Example 3: Nested conditions – deployment eligibility
cpu_usage = 60
memory_usage = 75

if cpu_usage < 70:
    if memory_usage < 80:
        print("Server is healthy. Deployment can proceed.")
    else:
        print("Memory usage high. Deployment postponed.")
else:
    print("CPU usage high. Deployment postponed.")

# Example 4: Real-time log alert – multiple conditions
log_entry = "ERROR: Disk usage at 95% on server node3"

if "ERROR" in log_entry:
    if "Disk usage" in log_entry:
        print("CRITICAL ALERT: Disk usage exceeded threshold!")
    elif "CPU" in log_entry:
        print("CRITICAL ALERT: CPU usage exceeded threshold!")
    else:
        print("ERROR detected in log, please investigate.")
else:
    print("No critical issues found in log entry.")

# Example 5: Using else for fallback – backup task decision
backup_completed = False

if backup_completed:
    print("Backup completed successfully.")
else:
    print("Backup failed. Initiate recovery procedure!")

"""
Summary:
- `if` checks the first condition.
- `elif` allows multiple alternative conditions.
- `else` handles the default fallback when all conditions fail.
- Nested conditions allow more complex decision-making.
- Real-time DevOps examples: monitoring CPU, memory, disk usage, logs, and backups.
"""
# ✅ Key Notes for DevOps:
# Server Monitoring: if statements can trigger alerts when CPU, memory, or disk exceeds thresholds.

# Deployment Checks: Use nested conditions to ensure servers meet requirements before deployment.

# Log Parsing: if-elif statements help classify logs into critical, warning, or info.

# Fallbacks: else provides a safety net if none of the conditions match, like failed backups.