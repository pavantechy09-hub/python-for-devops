"""
DevOps Real-Time Example: Managing Web Server Configuration with Variables

This script demonstrates:
1. Variables (global and local)
2. Variable scope and lifetime
3. Functions
4. CLI arguments
5. Environment variables

Use case: Updating and managing server configuration in a DevOps workflow.
"""

import os
import sys

# ===========================
# 1. Global Variables
# ===========================
# These variables can be accessed anywhere in this file
server_name = "my_server"
port = 80
is_https_enabled = True
max_connections = 1000

# ===========================
# 2. Functions and Local Scope
# ===========================
def print_config():
    """
    Print the current server configuration.
    Demonstrates accessing global variables.
    """
    print(f"Server Name: {server_name}")
    print(f"Port: {port}")
    print(f"HTTPS Enabled: {is_https_enabled}")
    print(f"Max Connections: {max_connections}")
    print("-" * 40)

def update_config(new_port=None, enable_https=None, max_conn=None):
    """
    Update the server configuration.
    Demonstrates local and global variables, and variable lifetime.
    """
    global port, is_https_enabled, max_connections  # Modify global variables

    # Local dictionary to track temporary updates
    temp_changes = {}

    if new_port:
        port = new_port
        temp_changes['port'] = port
    if enable_https is not None:
        is_https_enabled = enable_https
        temp_changes['https'] = is_https_enabled
    if max_conn:
        max_connections = max_conn
        temp_changes['max_connections'] = max_connections

    print(f"Temporary Updates (local variable): {temp_changes}")

# ===========================
# 3. Environment Variables
# ===========================
# Example: store sensitive info like passwords outside the code
# Set in terminal:
# Windows PowerShell: $env:SERVER_PASSWORD="joy123"
# Linux/macOS: export SERVER_PASSWORD="joy123"

server_password = os.getenv("SERVER_PASSWORD", "default_password")
print(f"Server Password (from environment variable): {server_password}")
print("-" * 40)

# ===========================
# 4. CLI Arguments
# ===========================
# Run this script with optional arguments:
# python devops_variables.py 443 True 2000
# Arguments: <port:int> <https:True/False> <max_connections:int>

if len(sys.argv) > 1:
    try:
        cli_port = int(sys.argv[1])
        cli_https = sys.argv[2].lower() == "true"
        cli_max_conn = int(sys.argv[3])
        print("Updating configuration from CLI arguments...")
        update_config(new_port=cli_port, enable_https=cli_https, max_conn=cli_max_conn)
    except IndexError:
        print("Not all CLI arguments provided. Skipping CLI updates.")
    except ValueError:
        print("Invalid CLI arguments. Please provide: <port:int> <https:True/False> <max_connections:int>")

# ===========================
# 5. Print Final Configuration
# ===========================
print("Final Server Configuration:")
print_config()

# ===========================
# 6. DevOps Function: Simulate Deployment
# ===========================
def deploy_service(service_name, instances=1):
    """
    Simulate deploying a service.
    Demonstrates using variables and functions in DevOps workflows.
    """
    deployment_status = f"Deploying {instances} instance(s) of {service_name}..."
    print(deployment_status)

    # Local variable to track success
    success = True
    if success:
        print(f"{service_name} deployed successfully!")
    else:
        print(f"{service_name} deployment failed.")

# Deploy a sample service
deploy_service("nginx", 3)
