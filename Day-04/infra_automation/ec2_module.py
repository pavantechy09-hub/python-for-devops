def launch_instance(name, instance_type):
    print(f"🚀 Launching EC2 instance: {name}")
    print(f"🖥️ Instance Type: {instance_type}")
    print("✅ EC2 instance launched successfully!\n")
    return {"instance_name": name, "instance_type": instance_type}
