# 🚀 Auto ML Training Logger with GitHub Actions

This repository demonstrates an automated Machine Learning activity logger using Python and GitHub Actions.  
It simulates ML training runs, logs model metrics, and automatically commits updates on a scheduled basis — helping maintain consistent GitHub activity.

---

## 📌 What This Project Does

- Simulates ML training metrics (accuracy, precision, recall, loss)
- Introduces a random delay to mimic real training time
- Appends results to a training log file
- Uses GitHub Actions to auto-commit changes daily
- Keeps GitHub contribution graph active 📊

---

## 🧠 Why This Project Exists

- Practice GitHub Actions automation
- Demonstrate ML experiment logging
- Learn CI/CD basics for ML workflows
- Maintain consistent GitHub contributions in a meaningful way

> ⚠️ Note: This project focuses on automation & logging, not actual model training.

---

## 🛠️ Tech Stack

- Python 3.11
- GitHub Actions
- Linux (Ubuntu runner)
- Cron scheduling

---

## 📂 Project Structure

```
auto-commit-ml/
│
├── ml_log.py                 # Simulates ML training & logs metrics
├── training_log.txt          # Auto-generated training logs
├── requirements.txt          # Python dependencies
└── .github/
    └── workflows/
        └── auto-commit-ml.yml # GitHub Actions workflow
```

---

## ⚙️ How It Works

1. GitHub Actions triggers the workflow (scheduled or manual)
2. Python script runs:
   - Waits for a random delay
   - Generates random ML metrics
   - Appends results to training_log.txt
3. GitHub Action commits the updated log file to main
4. Contribution graph updates automatically 🟩

---

## ⏰ Automation Schedule

The workflow runs twice daily:

| Time (UTC) | Time (IST) |
|-----------|-----------|
| 02:30     | 08:00     |
| 14:30     | 20:00     |

Manual execution is also supported via workflow_dispatch.

---

## 📊 Sample Log Entry

```
2025-01-31 14:30:12 | accuracy=0.9473 | precision=0.9124 | recall=0.9018 | loss=0.0342
```

---

## 🚦 How to Run Locally (Optional)

```bash
pip install -r requirements.txt
python ml_log.py
```

This will append a new entry to training_log.txt.

---

## 🧩 Key Learning Outcomes

- GitHub Actions & cron jobs
- Automating commits safely
- Logging ML experiment metrics
- CI/CD fundamentals for ML projects
- Clean GitHub activity practices

---

## 🔮 Future Enhancements

- CSV / JSON experiment logging
- README auto-update with latest metrics
- Real ML model integration
- Visualization of training metrics
- Cloud storage integration (S3 / GCS)

---

## 👤 Author

Aviral Goyal  
GitHub: https://github.com/avviiiral

---

## ⭐ If you find this useful
Give the repo a ⭐ — it helps and motivates further improvements!
