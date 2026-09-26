import csv
from datetime import datetime, timedelta
from pathlib import Path

events = []


def add_event(
    timestamp,
    event_type,
    outcome,
    user,
    src_ip,
    device,
    location,
    details,
):
    events.append(
        {
            "timestamp": timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            "event_type": event_type,
            "outcome": outcome,
            "user": user,
            "src_ip": src_ip,
            "device": device,
            "location": location,
            "details": details,
        }
    )


base = datetime(2026, 9, 20, 8, 0, 0)

# Normal authentication activity
normal_users = [
    ("mohana", "192.0.2.10", "LAPTOP-001", "Melbourne"),
    ("helpdesk", "192.0.2.20", "LAPTOP-002", "Melbourne"),
    ("analyst1", "192.0.2.30", "LAPTOP-003", "Sydney"),
    ("user01", "192.0.2.40", "LAPTOP-004", "Brisbane"),
]

for index, user_data in enumerate(normal_users):
    user, src_ip, device, location = user_data

    add_event(
        base + timedelta(minutes=index * 15),
        "login",
        "success",
        user,
        src_ip,
        device,
        location,
        "Normal user authentication",
    )

# Detection scenario 1:
# Six failed logins followed by a successful login
for minute in range(6):
    add_event(
        base + timedelta(hours=1, minutes=minute),
        "login",
        "failure",
        "admin",
        "203.0.113.10",
        "UNKNOWN-DEVICE",
        "Melbourne",
        "Incorrect password",
    )

add_event(
    base + timedelta(hours=1, minutes=7),
    "login",
    "success",
    "admin",
    "203.0.113.10",
    "UNKNOWN-DEVICE",
    "Melbourne",
    "Authentication succeeded after repeated failures",
)

# Detection scenario 2:
# One source IP targeting multiple accounts
target_users = ["mohana", "helpdesk", "analyst1", "finance01"]

for index, user in enumerate(target_users):
    add_event(
        base + timedelta(hours=2, minutes=index),
        "login",
        "failure",
        user,
        "198.51.100.25",
        "UNKNOWN-DEVICE",
        "Unknown",
        "Authentication failure from shared source",
    )

# Additional failed attempts from the same source
for index in range(3):
    add_event(
        base + timedelta(hours=2, minutes=5 + index),
        "login",
        "failure",
        "finance01",
        "198.51.100.25",
        "UNKNOWN-DEVICE",
        "Unknown",
        "Repeated authentication failure",
    )

# Normal VPN activity
for index in range(5):
    add_event(
        base + timedelta(hours=3, minutes=index * 10),
        "vpn",
        "success",
        "mohana",
        "192.0.2.50",
        "LAPTOP-001",
        "Melbourne",
        "Expected remote-access connection",
    )

# Detection scenario 3:
# VPN connection from an unknown device and source
add_event(
    base + timedelta(hours=4),
    "vpn",
    "success",
    "admin",
    "203.0.113.75",
    "UNKNOWN-DEVICE",
    "Unknown",
    "Remote-access connection from an unfamiliar source",
)

# Software installation activity
software_events = [
    ("mohana", "Microsoft Teams", "approved"),
    ("helpdesk", "Security Update", "approved"),
    ("user01", "Unknown Toolbar", "review_required"),
]

for index, software_data in enumerate(software_events):
    user, software, outcome = software_data

    add_event(
        base + timedelta(hours=5, minutes=index * 5),
        "software_install",
        outcome,
        user,
        f"192.0.2.{60 + index}",
        f"LAPTOP-00{index + 1}",
        "Melbourne",
        f"Software installation: {software}",
    )

# Account-management activity
add_event(
    base + timedelta(hours=6),
    "account_change",
    "success",
    "helpdesk",
    "192.0.2.20",
    "ADMIN-WS01",
    "Melbourne",
    "Password reset completed for user01",
)

# Detection scenario 4:
# Privileged-group change linked to the admin account
add_event(
    base + timedelta(hours=6, minutes=10),
    "account_change",
    "success",
    "admin",
    "203.0.113.10",
    "UNKNOWN-DEVICE",
    "Melbourne",
    "User added to privileged group",
)

# Additional normal events to make the dataset more realistic
for index in range(20):
    user, src_ip, device, location = normal_users[index % len(normal_users)]

    add_event(
        base + timedelta(hours=7, minutes=index * 3),
        "login",
        "success",
        user,
        src_ip,
        device,
        location,
        "Normal user authentication",
    )

# Ensure that the dataset folder exists
output_folder = Path("dataset")
output_folder.mkdir(exist_ok=True)

output_path = output_folder / "sample_security_detection_events.csv"

fieldnames = [
    "timestamp",
    "event_type",
    "outcome",
    "user",
    "src_ip",
    "device",
    "location",
    "details",
]

with output_path.open(
    "w",
    newline="",
    encoding="utf-8",
) as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(events)

print(f"Created {len(events)} fictional security events.")
print(f"Saved to: {output_path}")
