import os
import sys

# -------------------------------
# FUNCTION 1: Simulate DB Connection using ENV variables
# -------------------------------
def connect_to_db():
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASS")

    if not db_user or not db_pass:
        print("❌ Missing DB_USER or DB_PASS environment variables.")
        return
    print(f"🔐 Connecting to database as {db_user} ...")
    print("✅ Database connection successful!")

# -------------------------------
# FUNCTION 2: Deploy a Microservice
# -------------------------------
def deploy_service(service_name, environment):
    token = os.getenv("DEPLOY_TOKEN")
    if not token:
        print("❌ DEPLOY_TOKEN not found. Cannot deploy.")
        return
    print(f"🚀 Deploying {service_name} to {environment} environment...")
    print(f"🔑 Using token: {token[:3]}****")
    print(f"✅ {service_name} deployed successfully to {environment}!")

# -------------------------------
# FUNCTION 3: Auto-scale resources
# -------------------------------
def scale_resources(current_instances, multiplier):
    new_count = current_instances * multiplier
    print(f"📈 Scaling resources from {current_instances} → {new_count} instances")

# -------------------------------
# MAIN ENTRY POINT
# -------------------------------
if len(sys.argv) < 2:
    print("""
Usage:
  python devops_automation.py <action> [arguments]

Actions:
  connect_db                            - Connect to DB using environment variables
  deploy <service> <env>                - Deploy a service to given environment
  scale <current_instances> <multiplier> - Scale up or down resources

Examples:
  $env:DB_USER = "admin"
  $env:DB_PASS = "mypassword"
  python devops_automation.py connect_db

  $env:DEPLOY_TOKEN = "abcdef123"
  python devops_automation.py deploy myapp staging

  python devops_automation.py scale 5 2
""")
    sys.exit(1)

action = sys.argv[1]

if action == "connect_db":
    connect_to_db()

elif action == "deploy":
    if len(sys.argv) != 4:
        print("Usage: python devops_automation.py deploy <service> <environment>")
    else:
        deploy_service(sys.argv[2], sys.argv[3])

elif action == "scale":
    if len(sys.argv) != 4:
        print("Usage: python devops_automation.py scale <current_instances> <multiplier>")
    else:
        current = int(sys.argv[2])
        multiplier = float(sys.argv[3])
        scale_resources(current, multiplier)

else:
    print(f"❌ Unknown action: {action}")
