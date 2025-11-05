"""
========================================================
Python Lists and Tuples – DevOps Examples
========================================================
"""

# ------------------------------
# 1. Working with Lists
# ------------------------------

# Creating a list of servers in a DevOps environment
servers = ['web-server-01', 'db-server-01', 'app-server-01']
print("Servers List:", servers)

# Accessing elements by index
first_server = servers[0]
print("First server:", first_server)

# Length of the list
num_servers = len(servers)
print("Number of servers:", num_servers)

# Adding a new server to the list
servers.append('cache-server-01')
print("After appending a server:", servers)

# Removing a server
servers.remove('db-server-01')
print("After removing db-server-01:", servers)

# Slicing the list to get first 2 servers
subset_servers = servers[0:2]
print("Subset of servers:", subset_servers)

# Concatenating lists (adding more servers)
more_servers = ['analytics-server-01', 'backup-server-01']
all_servers = servers + more_servers
print("All servers combined:", all_servers)

# Sorting servers alphabetically
all_servers.sort()
print("Sorted servers:", all_servers)

# Checking if a server exists in the list
is_web_server_present = 'web-server-01' in all_servers
print("Is web-server-01 present?", is_web_server_present)


# ------------------------------
# 2. Working with Tuples
# ------------------------------

# Creating a tuple for immutable server configurations
server_config = ('web-server-01', 'Ubuntu 22.04', '16GB RAM', '4 CPU')
print("\nServer Configuration Tuple:", server_config)

# Accessing elements by index
os_type = server_config[1]
print("OS Type:", os_type)

# Length of tuple
config_length = len(server_config)
print("Number of config items:", config_length)

# Concatenating tuples (creating a new tuple)
additional_config = ('100GB SSD', 'DataCenter-1')
full_config = server_config + additional_config
print("Full Server Configuration:", full_config)

# Tuple packing and unpacking (useful in DevOps for returning multiple values)
coordinates = (12.34, 56.78)
x, y = coordinates
print("Server coordinates:", x, y)

# Checking for element in tuple
is_ubuntu = 'Ubuntu 22.04' in server_config
print("Is Ubuntu installed?", is_ubuntu)


# ------------------------------
# 3. List vs Tuple – Key DevOps Use Cases
# ------------------------------

# Lists are used for dynamic data that changes frequently
dynamic_servers = ['web-01', 'db-01']
dynamic_servers.append('cache-01')  # easy to update
print("\nDynamic Servers (List):", dynamic_servers)

# Tuples are used for fixed, immutable configurations
immutable_config = ('web-01', 'Ubuntu', '16GB RAM')  # cannot be changed
print("Immutable Config (Tuple):", immutable_config)


# ------------------------------
# 4. Real DevOps Example: Managing Deployment Targets
# ------------------------------

deployment_targets = ['prod-server-01', 'prod-server-02', 'staging-server-01']

# Deploy only to production servers
for server in deployment_targets:
    if 'prod' in server:
        print(f"Deploying to {server}...")
    else:
        print(f"Skipping deployment for {server}.")

# Output:
# Deploying to prod-server-01...
# Deploying to prod-server-02...
# Skipping deployment for staging-server-01
# ✅ Key DevOps Notes:
# Lists for dynamic resources:
# Use lists when you expect servers, containers, or configuration items to change frequently.

# Tuples for fixed resources:
# Use tuples for server configurations, coordinates, or constants that should not change.

# Indexing and slicing:
# Access specific servers or configuration subsets efficiently.

# Concatenation and sorting:
# Merge multiple lists of servers and sort them for reporting or deployment order.

# Iteration in DevOps:
# Looping through lists/tuples is crucial for tasks like automated deployment, monitoring, and log processing.

# Real-time application:
# Lists + conditions are commonly used to filter servers for deployment, patching, or backups.