import os
import sys

# ----------------------------
# 1️⃣ Functions (Reusable Code)
# ----------------------------
def check_server_status(server_name):
    return f"Server {server_name} is running"

servers = ["web01", "db01", "cache01"]
for s in servers:
    print(check_server_status(s))

def deploy_app(app_name):
    return f"Deploying {app_name}..."

apps = ["nginx", "redis", "myapp"]
for a in apps:
    print(deploy_app(a))

# ----------------------------
# 2️⃣ Simulated Module
# ----------------------------
class InfraUtils:
    """Simulating a module with a class"""

    @staticmethod
    def create_vm(name):
        return f"VM {name} created"

    @staticmethod
    def delete_vm(name):
        return f"VM {name} deleted"

# Using the simulated module
print(InfraUtils.create_vm("web01"))
print(InfraUtils.delete_vm("web01"))

# ----------------------------
# 3️⃣ Simulated Package
# ----------------------------
class InfraAutomation:
    """Simulating a package with nested classes as modules"""

    class VMModule:
        @staticmethod
        def create_vm(name):
            return f"VM {name} created"

    class NetworkModule:
        @staticmethod
        def create_vpc(name):
            return f"VPC {name} created"

# Using the simulated package
print(InfraAutomation.VMModule.create_vm("app01"))
print(InfraAutomation.NetworkModule.create_vpc("vpc01"))

# ----------------------------
# 4️⃣ Environment Variables (Workspace Simulation)
# ----------------------------
# Simulate setting an env variable for password (like DevOps secret)
os.environ["PASSWORD"] = "joy"

password = os.getenv("PASSWORD")
print(f"Using password from env: {password}")

# ----------------------------
# 5️⃣ Command-Line Arguments (Calculator Example)
# ----------------------------
# Example: python all_in_one.py 5 add 3
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

# Only run if arguments are provided
if len(sys.argv) == 4:
    num1 = float(sys.argv[1])
    operation = sys.argv[2]
    num2 = float(sys.argv[3])

    if operation == "add":
        print(f"Result: {add(num1, num2)}")
    elif operation == "sub":
        print(f"Result: {sub(num1, num2)}")
    elif operation == "mul":
        print(f"Result: {mul(num1, num2)}")
    else:
        print("Invalid operation! Use add, sub, or mul")
else:
    print("No calculator arguments provided")
