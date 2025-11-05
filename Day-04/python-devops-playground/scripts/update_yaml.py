import yaml

yaml_file = "../k8s_configs/deployment.yaml"

with open(yaml_file) as f:
    data = yaml.safe_load(f)

# Update container image version
data['spec']['template']['spec']['containers'][0]['image'] = "myapp:v2"

with open("../k8s_configs/deployment_updated.yaml", "w") as f:
    yaml.safe_dump(data, f)

print("Deployment image updated to myapp:v2")
