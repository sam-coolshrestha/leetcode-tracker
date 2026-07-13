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


#  LeetCode Tracker (GitHub Actions)

Automatically track your **LeetCode accepted submissions** and update your GitHub repository using **GitHub Actions**.

This project fetches your latest LeetCode submissions, stores them, and appends them to your `README.md` — all **automatically**.


---


##  Features

*  Fetches your recent **accepted submissions**
*  Runs automatically using **GitHub Actions**
*  Keeps your GitHub contribution graph active
*  Stores history in `submissions.json`
*  Updates `README.md` with solved problems
*  Easily customizable for any user

---

##  How It Works

1. GitHub Actions runs on a schedule (daily)
2. It calls LeetCode’s GraphQL API
3. Fetches your recent submissions
4. Filters accepted problems
5. Saves new entries
6. Updates your README automatically

---

##  Setup Guide (For New Users)

Follow these steps to use this project for your own LeetCode profile:

---

### 1️⃣ Fork the Repository

Click the **Fork** button (top-right) to create your own copy.

---

### 2️⃣ Add Your LeetCode Username (IMPORTANT)

Go to:

 `Your Repo → Settings → Secrets and variables → Actions`

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

 Go to **Actions tab → Enable workflows**

---

### 4️⃣ Run the Workflow

Option A (manual):

* Go to **Actions**
* Select **LeetCode Tracker**
* Click **Run workflow**

Option B (automatic):

* It will run daily based on schedule

---

##  Project Structure

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

##  Customization Options

You can modify this project easily:

---

###  Change Run Time

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

### Change File Names (Advanced)

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

##  Future Improvements (Optional Ideas)

*  Difficulty-wise stats (Easy / Medium / Hard)
*  Daily streak counter
*  Graphical dashboard
*  Styled README UI

---

##  Contributing

Feel free to fork, improve, and create pull requests!

---

## Support

If you found this useful:
 Give it a ⭐ on GitHub

---

##  Summary

✔ Fully automated
✔ Reusable for any user
✔ Minimal setup (just 1 secret)
✔ Clean and extensible
2026-05-29 09:22 - [Minimum Element After Replacement With Digit Sum](https://leetcode.com/problems/minimum-element-after-replacement-with-digit-sum)
2026-05-30 17:26 - [Reverse Bits](https://leetcode.com/problems/reverse-bits)
2026-05-30 17:04 - [Block Placement Queries](https://leetcode.com/problems/block-placement-queries)
2026-06-01 16:14 - [Rotate List](https://leetcode.com/problems/rotate-list)
2026-06-01 16:12 - [Rotate List](https://leetcode.com/problems/rotate-list)
2026-06-01 15:32 - [Minimum Cost of Buying Candies With Discount](https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount)
2026-06-02 17:35 - [Earliest Finish Time for Land and Water Rides I](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i)
2026-06-03 17:31 - [Two Sum](https://leetcode.com/problems/two-sum)
2026-06-03 17:08 - [Earliest Finish Time for Land and Water Rides I](https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i)
2026-06-04 09:25 - [Zigzag Conversion](https://leetcode.com/problems/zigzag-conversion)
2026-06-04 08:49 - [Unique Paths II](https://leetcode.com/problems/unique-paths-ii)
2026-06-08 16:38 - [Separate the Digits in an Array](https://leetcode.com/problems/separate-the-digits-in-an-array)
2026-06-08 16:19 - [Partition Array According to Given Pivot](https://leetcode.com/problems/partition-array-according-to-given-pivot)
2026-06-10 10:16 - [Maximum Total Subarray Value I](https://leetcode.com/problems/maximum-total-subarray-value-i)
2026-06-16 08:15 - [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal)
2026-06-16 07:06 - [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring)
2026-06-16 06:09 - [Container With Most Water](https://leetcode.com/problems/container-with-most-water)
2026-06-17 08:06 - [Customers Who Never Order](https://leetcode.com/problems/customers-who-never-order)
2026-06-17 07:55 - [Duplicate Emails](https://leetcode.com/problems/duplicate-emails)
2026-06-17 07:53 - [Duplicate Emails](https://leetcode.com/problems/duplicate-emails)
2026-06-17 07:44 - [Combine Two Tables](https://leetcode.com/problems/combine-two-tables)
2026-06-17 07:26 - [Island Perimeter](https://leetcode.com/problems/island-perimeter)
2026-06-17 06:05 - [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree)
2026-06-17 05:32 - [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree)
2026-06-17 05:12 - [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal)
2026-06-18 09:05 - [Rotting Oranges](https://leetcode.com/problems/rotting-oranges)
2026-06-19 08:14 - [Course Schedule II](https://leetcode.com/problems/course-schedule-ii)
2026-06-19 08:03 - [Course Schedule](https://leetcode.com/problems/course-schedule)
2026-06-22 08:34 - [Maximum Number of Balloons](https://leetcode.com/problems/maximum-number-of-balloons)
2026-06-22 05:51 - [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree)
2026-06-22 05:51 - [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree)
2026-06-22 05:44 - [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree)
2026-06-24 09:53 - [Find the Highest Altitude](https://leetcode.com/problems/find-the-highest-altitude)
2026-06-24 07:41 - [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)
2026-06-25 10:38 - [Valid Anagram](https://leetcode.com/problems/valid-anagram)
2026-06-25 10:16 - [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix)
2026-06-25 09:58 - [Largest Odd Number in String](https://leetcode.com/problems/largest-odd-number-in-string)
2026-06-26 10:18 - [Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list)
2026-06-26 10:05 - [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii)
2026-06-26 09:58 - [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list)
2026-06-26 09:53 - [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle)
2026-06-26 09:48 - [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list)
2026-06-26 07:10 - [Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list)
2026-06-27 18:22 - [Find the Difference](https://leetcode.com/problems/find-the-difference)
2026-06-27 18:05 - [Ransom Note](https://leetcode.com/problems/ransom-note)
2026-06-27 18:05 - [Ransom Note](https://leetcode.com/problems/ransom-note)
2026-06-29 19:02 - [Sum of Left Leaves](https://leetcode.com/problems/sum-of-left-leaves)
2026-06-29 18:57 - [Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title)
2026-06-29 18:01 - [Subsets II](https://leetcode.com/problems/subsets-ii)
2026-06-29 17:08 - [Combination Sum II](https://leetcode.com/problems/combination-sum-ii)
2026-06-29 17:02 - [Combination Sum II](https://leetcode.com/problems/combination-sum-ii)
2026-06-29 08:09 - [Count Good Numbers](https://leetcode.com/problems/count-good-numbers)
2026-07-02 09:50 - [Assign Cookies](https://leetcode.com/problems/assign-cookies)
2026-07-03 17:19 - [Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree)
2026-07-03 09:39 - [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)
2026-07-06 15:04 - [Tenth Line](https://leetcode.com/problems/tenth-line)
2026-07-06 14:57 - [Valid Phone Numbers](https://leetcode.com/problems/valid-phone-numbers)
2026-07-06 14:53 - [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits)
2026-07-06 14:50 - [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii)
2026-07-06 14:49 - [Pascal's Triangle II](https://leetcode.com/problems/pascals-triangle-ii)
2026-07-06 14:29 - [Relative Ranks](https://leetcode.com/problems/relative-ranks)
2026-07-06 13:53 - [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view)
2026-07-06 12:43 - [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths)
2026-07-06 11:58 - [Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths)
2026-07-06 10:25 - [Battleships in a Board](https://leetcode.com/problems/battleships-in-a-board)
2026-07-06 09:25 - [Word Break](https://leetcode.com/problems/word-break)
2026-07-13 10:51 - [Majority Element](https://leetcode.com/problems/majority-element)
2026-07-13 08:28 - [Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number)
2026-07-13 08:10 - [Merge Intervals](https://leetcode.com/problems/merge-intervals)
2026-07-13 08:10 - [Merge Intervals](https://leetcode.com/problems/merge-intervals)
2026-07-13 08:09 - [Merge Intervals](https://leetcode.com/problems/merge-intervals)
