import re
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

LOG_PATTERN = re.compile(
    r'(?P<timestamp>\w{3} \d{2} \d{2}:\d{2}:\d{2}) .* sshd\[\d+\]: (?P<message>.+)')

IP_PATTERN = re.compile(r'(\d+\.\d+\.\d+\.\d+)')  # Extracts IP Addresses
USER_PATTERN = re.compile(r'Invalid user (\S+)')  # Extracts Usernames

LOG_FILE = "SSH.log"  

with open(LOG_FILE, "r") as file:
    logs = file.readlines()

# Processed Data
data = []

for log in logs:
    match = LOG_PATTERN.search(log)
    if match:
        timestamp = match.group("timestamp")
        message = match.group("message")
        ip_match = IP_PATTERN.search(message)
        user_match = USER_PATTERN.search(message)

        ip = ip_match.group(0) if ip_match else None
        user = user_match.group(1) if user_match else None

        if "Failed password" in message:
            attack_type = "Failed Password"
        elif "Invalid user" in message:
            attack_type = "Invalid Username"
        elif "reverse mapping checking" in message:
            attack_type = "Reverse DNS Failure"
        elif "Too many authentication failures" in message:
            attack_type = "Brute Force Blocked"
        else:
            attack_type = "Other"

        data.append([timestamp, ip, user, attack_type])

df = pd.DataFrame(data, columns=["Timestamp", "IP", "Username", "Attack Type"])

# Save Processed Logs to CSV
df.to_csv("processed_ssh_logs.csv", index=False)
print("[+] Processed logs saved as 'processed_ssh_logs.csv'")

# Basic Analysis
print("\n🔹 Top Attacking IPs:")
print(df["IP"].value_counts().head(10))

print("\n🔹 Most Common Attack Types:")
print(df["Attack Type"].value_counts())

# Visualisation

top_ips = df["IP"].value_counts().head(10)
plt.figure(figsize=(10, 5))
top_ips.plot(kind="bar", color="red")
plt.title("Top 10 Attacking IPs")
plt.xlabel("IP Address")
plt.ylabel("Attempt Count")
plt.xticks(rotation=45)
plt.show()

