def resource(name):  # function definition
    return f"this will be active, {name}!"  # returns a message

message = resource("Vpc,ec2")  # calling the function with input "Alice"

def addition(num1,num2):
    add = num1 + num2
    return add

def sub(num1,num2):
    sub =num1 - num2
    return(sub)

def mul(num1,num2):
    mul = num1 * num2
    return(mul)

print(addition(5,10))
print(sub(2,5))
print(mul(4,5))

#Packages = collection of modules (5 python file can be bundled)
# also called as library
# boto3 , github, jira == pypi( python package index; its a package for common)
# pip is docker CLI, can download and install from PYPI which has packages, modules
# numpy, panda, anaconda

#Virtual environment:
venv

#python -m venv test_env
#test_env\Scripts\activate
#deactivate
# Project A → boto3==1.28.0
# Project B → boto3==1.33.0
# 🧰 2. Replicate Environments Consistently

# In real-time DevOps work:

# You automate deployments (Terraform, Ansible, Python scripts).

# Your team and CI/CD pipeline (GitHub Actions, Jenkins, GitLab) must use the same library versions.