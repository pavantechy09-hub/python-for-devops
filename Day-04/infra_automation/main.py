# main.py — Uses all modules (like real DevOps automation script)

from ec2_module import launch_instance
from monitor_module import setup_cloudwatch, check_health
from k8s_module import update_deployment

def main():
    print("🚧 Starting Infrastructure Automation 🚧\n")

    # Step 1 — Launch EC2
    instance_info = launch_instance("web-server", "t3.micro")

    # Step 2 — Set up monitoring
    setup_cloudwatch(instance_info["instance_name"])
    check_health(instance_info["instance_name"])

    # Step 3 — Update Kubernetes Deployment
    update_deployment("web-app", replicas=3)

    print("🎯 Infrastructure Automation Completed Successfully!")

if __name__ == "__main__":
    main()
