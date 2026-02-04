import os
import random
import subprocess
import time

TOKEN = os.environ["GH_PAT"]

with open("repos.txt") as f:
    repos = [r.strip() for r in f if r.strip()]

repo = random.choice(repos)
repo_name = repo.split("/")[-1]
commit_count = random.randint(3, 5)

print(f"Chosen repo: {repo}")
print(f"Commits today: {commit_count}")

clone_url = f"https://{TOKEN}@github.com/{repo}.git"
subprocess.run(["git", "clone", clone_url], check=True)

os.chdir(repo_name)

subprocess.run(["git", "config", "user.name", "Aviral Goyal"])
subprocess.run(["git", "config", "user.email", "YOUR_GITHUB_EMAIL"])

for i in range(commit_count):
    filename = f"auto_{int(time.time())}_{i}.txt"
    with open(filename, "w") as f:
        f.write(f"Auto commit {i+1}\n")

    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", f"auto commit {i+1}"], check=True)

    time.sleep(random.randint(60, 300))  # spacing commits

subprocess.run(["git", "push"], check=True)
