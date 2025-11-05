import os

log_dir = "../logs"
logs = os.listdir(log_dir)

for log_file in logs:
    if log_file.endswith(".log"):
        with open(os.path.join(log_dir, log_file)) as f:
            lines = f.readlines()
            error_lines = [line for line in lines if "ERROR" in line]
            info_lines = [line for line in lines if "INFO" in line]
            print(f"{log_file}: {len(error_lines)} ERROR lines, {len(info_lines)} INFO lines")
