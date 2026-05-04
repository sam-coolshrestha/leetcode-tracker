# leetcode-tracker


MY DAILY LEETCODE PRACTICE:
2026-04-16 06:42 - [Delete Columns to Make Sorted](https://leetcode.com/problems/delete-columns-to-make-sorted)
2026-04-16 06:39 - [Shortest Distance to Target String in a Circular Array](https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array)
2026-04-16 06:18 - [Shortest Distance to Target String in a Circular Array](https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array)
2026-04-16 06:06 - [Minimum Distance to the Target Element](https://leetcode.com/problems/minimum-distance-to-the-target-element)
2026-04-05 12:28 - [Decode the Slanted Ciphertext](https://leetcode.com/problems/decode-the-slanted-ciphertext)
2026-04-05 05:52 - [Robot Return to Origin](https://leetcode.com/problems/robot-return-to-origin)
2026-04-02 18:26 - [Maximum Amount of Money Robot Can Earn](https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn)
2026-04-01 17:07 - [Robot Collisions](https://leetcode.com/problems/robot-collisions)
2026-03-28 14:56 - [Minimum Absolute Difference Between Two Values](https://leetcode.com/problems/minimum-absolute-difference-between-two-values)


# 🚀 LeetCode Tracker (GitHub Actions)

Automatically track your **LeetCode accepted submissions** and update your GitHub repository using **GitHub Actions**.

This project fetches your latest LeetCode submissions, stores them, and appends them to your `README.md` — all **automatically**.


---

## ✨ Features

* 📊 Fetches your recent **accepted submissions**
* 🔄 Runs automatically using **GitHub Actions**
* 🟢 Keeps your GitHub contribution graph active
* 📁 Stores history in `submissions.json`
* 📝 Updates `README.md` with solved problems
* ⚙️ Easily customizable for any user

---

## 🧠 How It Works

1. GitHub Actions runs on a schedule (daily)
2. It calls LeetCode’s GraphQL API
3. Fetches your recent submissions
4. Filters accepted problems
5. Saves new entries
6. Updates your README automatically

---

## 🛠️ Setup Guide (For New Users)

Follow these steps to use this project for your own LeetCode profile:

---

### 1️⃣ Fork the Repository

Click the **Fork** button (top-right) to create your own copy.

---

### 2️⃣ Add Your LeetCode Username (IMPORTANT)

Go to:

👉 `Your Repo → Settings → Secrets and variables → Actions`

Click **New repository secret** and add:

```
Name: LEETCODE_USERNAME
Value: your_leetcode_username
```

⚠️ Replace `your_leetcode_username` with your actual LeetCode username
(e.g., from `https://leetcode.com/u/your_name/`)

---

### 3️⃣ Enable GitHub Actions

If workflows are disabled:

👉 Go to **Actions tab → Enable workflows**

---

### 4️⃣ Run the Workflow

Option A (manual):

* Go to **Actions**
* Select **LeetCode Tracker**
* Click **Run workflow**

Option B (automatic):

* It will run daily based on schedule

---

## 📂 Project Structure

```
leetcode-tracker/
│
├── tracker.py              # Main script (fetches submissions)
├── submissions.json        # Stores submission history
├── README.md               # Updated automatically
├── last_run.txt            # Timestamp (ensures daily commits)
└── .github/
    └── workflows/
        └── update.yml      # GitHub Actions workflow
```

---

## ⚙️ Customization Options

You can modify this project easily:

---

### 🕒 Change Run Time

Edit this in `update.yml`:

```
cron: "0 18 * * *"
```

This runs at **11:30 PM IST**

Use [crontab.guru](https://crontab.guru/) to customize your schedule.

---

### 📄 Change Output Format

Edit inside `tracker.py`:

```
f.write(f"{entry['time']} - [{entry['title']}]({entry['link']})\n")
```

You can format it as:

* bullet list
* table
* grouped by date

---

### 📁 Change File Names (Advanced)

You can modify:

* `submissions.json`
* `README.md`

Or make them environment-based for more flexibility.

---

### 🔁 Disable Daily Commits

Remove this step in `update.yml` if you don’t want daily commits:

```
Update last run timestamp
```

---

## ⚠️ Important Notes

* 🔒 Secrets are NOT shared in forks → every user must add their own
* 📊 Only recent submissions (~20) are fetched each run
* 🔁 Over time, it builds your full history automatically
* 🌍 Timezone depends on your cron setting

---

## 🧪 Troubleshooting

### ❌ Workflow not running

* Enable Actions
* Check YAML syntax

### ❌ No submissions fetched

* Verify your LeetCode username
* Ensure profile is public

### ❌ No updates in README

* No new accepted submissions
* Or duplicate entries filtered

---

## 🌟 Future Improvements (Optional Ideas)

* 📊 Difficulty-wise stats (Easy / Medium / Hard)
* 🔥 Daily streak counter
* 📈 Graphical dashboard
* 💅 Styled README UI

---

## 🤝 Contributing

Feel free to fork, improve, and create pull requests!

---

## ⭐ Support

If you found this useful:
👉 Give it a ⭐ on GitHub

---

## 📌 Summary

✔ Fully automated
✔ Reusable for any user
✔ Minimal setup (just 1 secret)
✔ Clean and extensible

---

Happy Coding 🚀
2026-04-21 17:14 - [Fibonacci Number](https://leetcode.com/problems/fibonacci-number)
2026-05-03 14:19 - [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence)
2026-05-03 14:13 - [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence)
2026-05-03 14:09 - [Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence)
2026-05-03 04:58 - [Rotate String](https://leetcode.com/problems/rotate-string)
2026-05-03 03:54 - [Number of Provinces](https://leetcode.com/problems/number-of-provinces)
2026-05-04 18:51 - [Climbing Stairs](https://leetcode.com/problems/climbing-stairs)
2026-05-04 04:02 - [Rotate Image](https://leetcode.com/problems/rotate-image)
2026-05-04 03:57 - [Rotate Image](https://leetcode.com/problems/rotate-image)
