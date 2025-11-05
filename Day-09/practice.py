"""
DevOps Automation Simulation in Python
This script demonstrates:
- Lists and tuples for managing servers and configurations
- For loops for provisioning and deployment
- While loops for monitoring and real-time checks
- break and continue for controlling loops
- Logging and alerting simulation
"""

import time
import random

# ==============================================
# 1. Define Servers and Configurations
# ==============================================

# List of servers (mutable because we might add/remove servers)
servers = ['web-server-01', 'db-server-01', 'app-server-01']

# Tuple for server types (immutable because types don't change)
server_types = ('web', 'database', 'application')

# Configuration dictionary (key: server name, value: config status)
server_config_status = {server: 'pending' for server in servers}

print("=== Initial Server List and Types ===")
print("Servers:", servers)
print("Server Types:", server_types)
print("Configuration Status:", server_config_status)
print("\n")

# ==============================================
# 2. Provision Servers (For Loop Example)
# ==============================================

print("=== Provisioning Servers ===")
for server in servers:
    # Simulate provisioning
    print(f"Provisioning {server}...")
    time.sleep(0.5)  # Simulate time delay
    server_config_status[server] = 'provisioned'

print("Provisioning Complete!")
print("Configuration Status:", server_config_status)
print("\n")

# ==============================================
# 3. Deploy Applications (For Loop with Continue/Break)
# ==============================================

print("=== Deploying Applications ===")
for server, status in server_config_status.items():
    if status != 'provisioned':
        print(f"Skipping deployment on {server}, not provisioned yet.")
        continue  # Skip servers that are not provisioned

    # Simulate a failure on the database server
    if 'db-server' in server:
        print(f"Deployment failed on {server}! Exiting loop...")
        break  # Stop deployment if critical failure occurs

    print(f"Deploying application on {server}...")
    server_config_status[server] = 'deployed'
    time.sleep(0.5)

print("Deployment Status:", server_config_status)
print("\n")

# ==============================================
# 4. Continuous Monitoring (While Loop Example)
# ==============================================

print("=== Monitoring Server Health ===")
monitoring_attempts = 0
max_attempts = 5

while monitoring_attempts < max_attempts:
    monitoring_attempts += 1
    print(f"Monitoring attempt {monitoring_attempts}...")
    
    # Randomly simulate server health check (True = healthy, False = unhealthy)
    server_health = {server: random.choice([True, False]) for server in servers}

    for server, is_healthy in server_health.items():
        if not is_healthy:
            print(f"ALERT: {server} is DOWN! Taking action...")
        else:
            print(f"{server} is healthy.")

    # Exit loop early if all servers are healthy
    if all(server_health.values()):
        print("All servers healthy. Ending monitoring early.")
        break

    time.sleep(1)  # Wait before next monitoring check

print("\nMonitoring Complete!\n")

# ==============================================
# 5. Backup and Cleanup Example (For Loop)
# ==============================================

print("=== Backing up Servers ===")
for server in servers:
    print(f"Creating backup for {server}...")
    time.sleep(0.5)  # Simulate backup time
print("Backups complete!\n")

# ==============================================
# 6. Log Analysis Example (For Loop)
# ==============================================

print("=== Log File Analysis ===")
log_file = [
    "INFO: Web server started",
    "ERROR: Database connection failed",
    "DEBUG: App server loaded modules",
    "ERROR: Disk space low on web-server-01"
]

for line in log_file:
    if "ERROR" in line:
        print(f"Detected ERROR: {line}")

print("\n=== DevOps Automation Simulation Completed ===")
# ✅ Features Demonstrated
# Lists and Tuples

# Lists: dynamic server list (servers)

# Tuples: immutable server types (server_types)

# For Loops

# Provisioning, deployment, backup, log analysis

# While Loops

# Continuous monitoring with early exit using break

# Loop Control

# continue: Skip servers not ready for deployment

# break: Stop deployment on critical failure

# DevOps Concepts

# Server provisioning

# Application deployment

# Continuous monitoring and alerts

# Backup automation

# Log analysis

