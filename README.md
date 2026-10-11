# 💻 LeetCode Solutions Tracker

A secure, automated repository containing my accepted solutions for **LeetCode** problems. This repository is automatically updated every night using **GitHub Actions**, bypassing the need for third-party browser extensions.

<!-- 
## 📊 Progress Statistics

 Use a service like LeetCode Stats Card (replace 'YOUR_LEETCODE_USERNAME' with your actual username) 
![LeetCode Stats](https://leetcode.com/u/Akhilreddy09/) -->
---

## 🛠️ How It Works

This repository stays updated entirely through automated cloud infrastructure:
* **Automation Hub:** A [GitHub Action](https://github.com) runs automatically every single night at **11:40 PM IST**.
* **Sync Engine:** The workflow utilizes the open-source `joshcai/leetcode-sync` engine to safely pull newly accepted submissions directly from LeetCode.
* **Security First:** Session identifiers are handled exclusively via encrypted GitHub Repository Secrets, ensuring complete privacy and credential safety.

---

## 📂 Repository Structure

All synced code is organized cleanly within the `/solutions` directory. Problems are cataloged automatically by their official LeetCode slug names:

```text
├── .github/
│   └── workflows/
│       └── sync_leetcode.yml    # The automated sync script
├── solutions/
│   ├── 0001-two-sum/
│   │   ├── two-sum.py           # Solution file (depends on language used)
│   │   └── README.md            # Problem statement markdown
│   └── 0002-add-two-numbers/
└── README.md                    # This profile dashboard
```

---

## 🚀 Manual Execution

If I want to sync my solutions immediately rather than waiting for the nightly cron schedule:
1. Navigate to the **Actions** tab of this repository.
2. Select the **Sync LeetCode Submissions** workflow on the left sidebar.
3. Click the **Run workflow** dropdown menu on the right.
4. Click the green **Run workflow** button.

---

## 📜 Disclaimer
The automation script fetches and syncs code files directly from my personal LeetCode account. All problem descriptions and original constraints belong entirely to [LeetCode](https://leetcode.com).
