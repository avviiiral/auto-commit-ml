# 🤖 Daily ML Auto Commit using GitHub Actions

This repository demonstrates how to automate **daily GitHub commits** using **Python, Machine Learning–style logging, and GitHub Actions** — without using a local laptop.

The workflow runs on GitHub’s cloud infrastructure and updates a training log every day, simulating a real ML experimentation process.

---

## 🚀 What This Project Does

- Runs a **Python script daily**
- Simulates **Machine Learning training metrics**
- Automatically **commits changes to GitHub**
- Uses **GitHub Actions** (CI/CD)
- Requires **no local machine or manual work**

---

## 🧠 Why This Project?

This project showcases:
- Python automation
- ML-style experiment logging
- GitHub Actions (DevOps basics)
- CI/CD pipelines
- Cloud-based workflows

Perfect for **Data Science / ML / Analyst / DevOps portfolios**.

---

## 📁 Project Structure

```

auto-commit-ml/
│
├── ml_log.py # Python script that simulates ML training
├── requirements.txt # Python dependencies
├── training_log.txt # Auto-generated ML logs
└── .github/
└── workflows/
└── daily_commit.yml # GitHub Actions workflow
```

---

## ⚙️ How It Works

1. **GitHub Actions** triggers the workflow daily (cron job)
2. Python script runs:
   - Generates random ML metrics (accuracy, loss)
   - Appends results to `training_log.txt`
3. Workflow commits and pushes changes automatically

---

## ⏰ Workflow Schedule

The workflow runs **once every day automatically**  
(Also supports manual trigger via GitHub Actions UI)

---

## 📊 Sample Output

```
2026-01-29 02:30:01 | accuracy=0.9452 | loss=0.0314
2026-01-30 02:30:01 | accuracy=0.9123 | loss=0.0541
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

- No fake commits — every commit modifies real data
- Fully cloud-based automation
- Recruiter-friendly and transparent
- Easily extendable to real ML models

---

## 🔮 Future Enhancements

- Train a real ML model (scikit-learn)
- Log metrics to CSV / database
- Auto-update Jupyter notebooks
- Integrate Power BI / dashboards

---

## 👤 Author

**Aviral Goyal**  
Aspiring Data Scientist | Python | SQL | Power BI | Machine Learning

---

⭐ If you like this project, feel free to star the repository!
