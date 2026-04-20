import requests
import json
from datetime import datetime

import os

USERNAME = os.getenv("LEETCODE_USERNAME")

if not USERNAME:
    raise ValueError("❌ Please set LEETCODE_USERNAME")

url = "https://leetcode.com/graphql"

query = {
    "query": """
    query recentSubmissions($username: String!) {
      recentSubmissionList(username: $username) {
        title
        titleSlug
        statusDisplay
        timestamp
      }
    }
    """,
    "variables": {"username": USERNAME}
}

# ✅ Request with headers (IMPORTANT)
response = requests.post(
    url,
    json=query,
    headers={
        "Content-Type": "application/json",
        "Referer": "https://leetcode.com",
        "User-Agent": "Mozilla/5.0"
    }
)

data = response.json()

# ✅ Error handling (VERY IMPORTANT)
if "data" not in data or data["data"] is None:
    print("❌ API Error:", data)
    exit()

submissions = data["data"]["recentSubmissionList"]

# ✅ Load previous submissions safely
try:
    with open("submissions.json", "r") as f:
        saved = json.load(f)
except:
    saved = []

# ✅ Better duplicate handling (title + time)
saved_entries = set((s["title"], s["time"]) for s in saved)

new_entries = []

for sub in submissions:
    if sub["statusDisplay"] == "Accepted":
        dt = datetime.fromtimestamp(int(sub["timestamp"]))
        formatted_time = dt.strftime("%Y-%m-%d %H:%M")

        if (sub["title"], formatted_time) not in saved_entries:
            entry = {
                "title": sub["title"],
                "time": formatted_time,
                "link": f"https://leetcode.com/problems/{sub['titleSlug']}"
            }
            saved.append(entry)
            new_entries.append(entry)

# ✅ Save updated submissions
with open("submissions.json", "w") as f:
    json.dump(saved, f, indent=2)

# ✅ Update README
if new_entries:
    with open("README.md", "a") as f:
        for entry in new_entries:
            f.write(f"{entry['time']} - [{entry['title']}]({entry['link']})\n")

# ✅ Debug output (helps in GitHub Actions logs)
print("\n📊 Fetched submissions:")
for sub in submissions:
    print(sub["title"], "-", sub["statusDisplay"])

print(f"\n✅ New entries added: {len(new_entries)}")
