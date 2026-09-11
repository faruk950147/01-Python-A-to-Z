from datetime import datetime, timedelta
'''
# total_seconds = now.timestamp()
total_seconds = (now.hour * 3600 + now.minute * 60 + now.second)
minutes = total_seconds // 60
hours = minutes // 60
days = hours // 24
print(f"Total seconds: {int(total_seconds)}")
print(f"Total minutes: {int(minutes)}")
print(f"Total hours: {int(hours)}")
print(f"Total days: {int(days)}")


ONLINE_TIMEOUT_SECONDS = 60  # 60 seconds

last_seen = datetime(2025, 10, 14, 12, 0, 0)

is_online = (datetime.now() - last_seen).total_seconds() < ONLINE_TIMEOUT_SECONDS

print(f"Is online: {is_online}")
'''
ONLINE_TIMEOUT_SECONDS = 60

# 30 seconds ago
last_seen = datetime.now() - timedelta(seconds=30)
print(f"Last seen: {last_seen}")
is_online = (datetime.now() - last_seen).total_seconds() < ONLINE_TIMEOUT_SECONDS
print(f"Is online: {is_online}")

diff = (datetime.now() - last_seen).total_seconds()
print(f"Diff: {diff}")
print(f"Is online: {diff < ONLINE_TIMEOUT_SECONDS}")


