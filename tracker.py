import requests
import json
from datetime import datetime

USERNAME = "sam_coolshrestha"

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

response = requests.post(url, json=query)
data = response.json()

submissions = data["data"]["recentSubmissionList"]

# Load previous submissions
try:
    with open("submissions.json", "r") as f:
        saved = json.load(f)
except:
    saved = []

saved_titles = set([s["title"] for s in saved])

new_entries = []

for sub in submissions:
    if sub["statusDisplay"] == "Accepted" and sub["title"] not in saved_titles:
        dt = datetime.fromtimestamp(int(sub["timestamp"]))
        entry = {
            "title": sub["title"],
            "time": dt.strftime("%Y-%m-%d %H:%M"),
            "link": f"https://leetcode.com/problems/{sub['titleSlug']}"
        }
        saved.append(entry)
        new_entries.append(entry)

# Save updated submissions
with open("submissions.json", "w") as f:
    json.dump(saved, f, indent=2)

# Update README
if new_entries:
    with open("README.md", "a") as f:
        for entry in new_entries:
            f.write(f"{entry['time']} - [{entry['title']}]({entry['link']})\n")
