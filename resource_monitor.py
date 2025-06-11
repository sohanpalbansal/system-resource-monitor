import psutil
import time
import csv
from datetime import datetime

log_file = "log.csv"

# Header write here if file is new
with open(log_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Time", "CPU_Usage (%)", "RAM_Usage (%)", "Disk_Usage (%)"])

# push data for 1 min 
for _ in range(12):  # 12 times × 5 seconds = 1 minute
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    with open(log_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, cpu, ram, disk])

    print(f"{timestamp} - CPU: {cpu}%, RAM: {ram}%, Disk: {disk}%")
    time.sleep(4)  # Already waited 1 sec in cpu_percent
