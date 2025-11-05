import subprocess

# List Docker containers
print("Listing all Docker containers...")
subprocess.run(["docker", "ps", "-a"])

# Build Docker image
print("Building Docker image 'myapp:v2'...")
subprocess.run(["docker", "build", "-t", "myapp:v2", "."])

# Run container
print("Running container 'myapp_container'...")
subprocess.run(["docker", "run", "-d", "--name", "myapp_container", "myapp:v2"])
