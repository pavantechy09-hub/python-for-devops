"""
Real-Time DevOps Monitoring Script
----------------------------------
This script demonstrates:
1. Dictionaries for server configurations and PR contributors.
2. Sets for unique services and hosts.
3. Lists for ordered logs.
4. GitHub API integration to track active contributors.
"""

import requests

# -----------------------------
# SECTION 1: Server Configurations
# -----------------------------
# Dictionary storing server info
server_config = {
    'server1': {'ip': '192.168.1.1', 'port': 8080, 'status': 'active', 'services': ['nginx', 'mysql']},
    'server2': {'ip': '192.168.1.2', 'port': 8000, 'status': 'inactive', 'services': ['nginx', 'postgres']},
    'server3': {'ip': '192.168.1.3', 'port': 9000, 'status': 'active', 'services': ['redis', 'nginx']}
}

# Function to get server status
def get_server_status(server_name):
    return server_config.get(server_name, {}).get('status', 'Server not found')

# Function to get services running on a server
def get_server_services(server_name):
    return set(server_config.get(server_name, {}).get('services', []))

# -----------------------------
# SECTION 2: Logs (List Example)
# -----------------------------
# List storing logs in order
logs = [
    "server1 started",
    "server2 failed to start",
    "server3 started",
    "server1 nginx deployed"
]

# -----------------------------
# SECTION 3: Unique Services (Set Example)
# -----------------------------
# Collect all unique services across servers
all_services = set()
for server in server_config.values():
    all_services.update(server['services'])

# -----------------------------
# SECTION 4: GitHub PR Contributors
# -----------------------------
GITHUB_API_URL = 'https://api.github.com/repos/kubernetes/kubernetes/pulls'

def fetch_github_pr_creators():
    """
    Fetches active contributors (PR creators) from Kubernetes GitHub repository.
    Returns a dictionary: {username: number_of_prs}
    """
    try:
        response = requests.get(GITHUB_API_URL)
        response.raise_for_status()
        pull_requests = response.json()

        pr_creators = {}
        for pull in pull_requests:
            creator = pull['user']['login']
            pr_creators[creator] = pr_creators.get(creator, 0) + 1

        return pr_creators

    except requests.exceptions.RequestException as e:
        print(f"Error fetching GitHub data: {e}")
        return {}

# -----------------------------
# SECTION 5: Main Execution
# -----------------------------
def main():
    print("=== Server Status and Services ===")
    for server_name in server_config:
        status = get_server_status(server_name)
        services = get_server_services(server_name)
        print(f"{server_name}: Status={status}, Services={services}")

    print("\n=== Ordered Logs ===")
    for log in logs:
        print(log)

    print("\n=== All Unique Services Across Servers ===")
    print(all_services)

    print("\n=== GitHub PR Contributors ===")
    pr_creators = fetch_github_pr_creators()
    if pr_creators:
        for creator, count in pr_creators.items():
            print(f"{creator}: {count} PR(s)")
    else:
        print("No PR data available or failed to fetch.")

if __name__ == "__main__":
    main()
# <!-- ✅ Features of this script:
# Dictionaries: Manage server info (server_config) and GitHub contributors (pr_creators).

# Lists: Store ordered logs (logs) to simulate DevOps event tracking.

# Sets: Track unique services across servers (all_services).

# API Integration: Fetch real-time PR data from Kubernetes GitHub repo.

# Readable & Executable: Everything is in one script with clear sections and functions. -->