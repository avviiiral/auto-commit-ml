# 🤖 Automated ML Activity with GitHub Actions (Daily Auto Commits)

This repository demonstrates a **fully automated Machine Learning–style workflow** using **Python and GitHub Actions** that generates **natural-looking daily GitHub commits without using a local machine**.

The automation runs entirely on GitHub’s cloud infrastructure and simulates real ML experimentation with **randomized metrics, delays, and commit messages**.

---

## 🚀 What This Project Does

- Runs a **Python ML-style script automatically**
- Generates **realistic ML metrics** (accuracy, precision, recall, loss)
- Introduces a **random execution delay** on each run
- Uses **different commit messages every time**
- Commits and pushes changes **twice per day automatically**
- Requires **no laptop or manual intervention**

---

## 🧠 Why This Project Exists

This project is designed to showcase:
- Python automation skills
- Machine Learning experiment logging
- GitHub Actions (CI/CD & DevOps fundamentals)
- Cloud-based workflows
- Clean, recruiter-safe GitHub activity

This is **not fake commit spam** — every commit updates real data.

---

## 📁 Project Structure

```
auto-commit-ml/
│
├── ml_log.py                     # Python script simulating ML training runs
├── requirements.txt              # Python dependencies
├── training_log.txt              # Auto-generated experiment logs
└── .github/
      └── workflows/
            └── daily_commit.yml  # GitHub Actions automation
```

---

## ⚙️ How It Works

1. **GitHub Actions** triggers the workflow on a fixed schedule (cron)
2. The Python script:
   - Waits for a random delay (to avoid robotic timing)
   - Generates random ML metrics
   - Appends results to `training_log.txt`
3. The workflow:
   - Selects a random commit message
   - Commits and pushes changes automatically

---

## ⏰ Automation Schedule

The workflow runs **twice daily**:

| UTC Time | IST (India) |
|--------|-------------|
| 02:30  | 08:00 AM |
| 14:30  | 08:00 PM |

Manual runs are also supported via the **Actions** tab.

---

## 📊 Sample Training Log Output

```
2026-01-29 02:31:12 | accuracy=0.9421 | precision=0.9314 | recall=0.9042 | loss=0.0371
2026-01-29 14:32:45 | accuracy=0.9173 | precision=0.9025 | recall=0.8896 | loss=0.0518
```

---

## 🛠 Technologies Used

- Python
- GitHub Actions
- GitHub CI/CD
- Machine Learning concepts
- Cloud automation

---

## ✅ Key Highlights

- Randomized execution delay for natural timing
- Different commit messages per run
- Realistic ML experiment metrics
- Fully automated & cloud-based
- Recruiter-friendly and transparent

---

## 🔮 Possible Extensions

- Train a real ML model using scikit-learn
- Log metrics to CSV or database
- Auto-update Jupyter notebooks
- Integrate dashboards (Power BI / Tableau)
- Weekly heavy training runs

---

## 👤 Author

**Aviral Goyal**  
Aspiring Data Scientist | Python | SQL | Power BI | Machine Learning

---

⭐ If you find this project useful, feel free to star the repository!
