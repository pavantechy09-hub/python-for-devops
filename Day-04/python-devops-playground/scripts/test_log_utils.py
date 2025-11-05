# scripts/test_log_utils.py
from log_utils import count_log_lines

error_count, info_count = count_log_lines("../logs/app1.log")
print(f"app1.log → {error_count} ERROR lines, {info_count} INFO lines")
