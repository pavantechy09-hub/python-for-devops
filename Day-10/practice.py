# Real-Time DevOps Example: Monitoring and Auditing Log Directories

# Scenario:
# In a DevOps environment, you often need to monitor multiple log directories across different servers or services. For example, you want to:

# Check which log files exist in /var/log/nginx and /var/log/mysql.

# Ensure there are no missing or stale log files.

# Handle situations where a folder may not exist or permissions are restricted.

# This is essential for automated log auditing and monitoring server health.

# Python Script with Real-Time DevOps Use Case
import os

def list_files_in_folder(folder_path):
    """
    List all files in a given folder path.
    
    Returns:
    - files: list of file names if accessible
    - error_message: string describing error if folder cannot be accessed
    """
    try:
        files = os.listdir(folder_path)
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"  # Folder does not exist
    except PermissionError:
        return None, "Permission denied"  # Folder exists but we don't have permission

def main():
    """
    Main function simulating a DevOps log audit.
    It iterates over multiple folders and lists files in each.
    """
    # Example: typical log folders in a Linux server
    folder_paths = input(
        "Enter a list of log folder paths separated by spaces (e.g., /var/log/nginx /var/log/mysql): "
    ).split()

    if not folder_paths:
        print("No folder paths provided. Exiting...")
        return

    # Iterate over each folder path
    for folder_path in folder_paths:
        files, error_message = list_files_in_folder(folder_path)

        if files is not None:
            print(f"\n[INFO] Files in '{folder_path}':")
            for file in files:
                print(f" - {file}")
        else:
            print(f"\n[ERROR] Cannot access '{folder_path}': {error_message}")

if __name__ == "__main__":
    main()

# Step-by-Step Notes for DevOps Understanding
# 1. Why multiple folder paths?

# In DevOps, logs are spread across multiple services (e.g., web server, database, application).

# A single folder listing isn’t enough. We need a loop to iterate over all relevant folders.

# for folder_path in folder_paths:


# This for loop is key for automating tasks for multiple servers or services.

# No manual checking of each folder.

# 2. Error Handling
# except FileNotFoundError:
#     return None, "Folder not found"
# except PermissionError:
#     return None, "Permission denied"


# DevOps servers may not have the same configuration. Some log folders may not exist or require sudo access.

# Handling errors prevents the script from crashing and allows logging/reporting.

# 3. Real-Time Use in DevOps

# You can integrate this script into a cron job or CI/CD pipeline:

# Audit server logs every hour.

# Ensure all expected log files exist.

# Trigger alerts if folders are missing or inaccessible.

# Example cron job:

# 0 * * * * /usr/bin/python3 /home/devops/list_logs.py >> /home/devops/log_audit_report.txt


# Runs every hour.

# Appends the audit results to a report file.

# Allows proactive monitoring and incident prevention.

# 4. Extending the Script for DevOps

# Recursive listing: Check subfolders for rotated logs.

# Logging output: Save output to a central audit file for compliance tracking.

# Remote servers: Use SSH + Python script to audit multiple servers from a central location.

# Example snippet to save output:

# with open("log_audit_report.txt", "a") as report:
#     report.write(f"Files in '{folder_path}':\n")
#     for file in files:
#         report.write(f" - {file}\n")

# 5. Why this is DevOps relevant

# Automation reduces manual checks.

# Ensures consistency across servers.

# Helps in compliance, troubleshooting, and alerting.

# Prepares infrastructure for scaling: more folders can be added dynamically to the script.

# 💡 Key Takeaways for DevOps Engineers

# for loops are ideal for iterating over multiple resources (servers, folders, containers).

# Error handling is crucial in distributed systems where permissions and paths may vary.

# Automating audits/log checks using scripts improves reliability and reduces manual effort.

# This can be a building block for more advanced monitoring, like integrating with Prometheus or ELK stack.