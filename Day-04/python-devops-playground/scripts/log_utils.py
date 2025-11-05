# scripts/log_utils.py

def count_log_lines(log_file_path):
    with open(log_file_path) as f:
        lines = f.readlines()
        error_lines = [line for line in lines if "ERROR" in line]
        info_lines = [line for line in lines if "INFO" in line]
    return len(error_lines), len(info_lines)
