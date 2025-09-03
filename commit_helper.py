import os
import subprocess

def is_git_repo():
    """Check if the current folder is a Git repository."""
    try:
        subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            check=True,
            capture_output=True,
            text=True,
        )
        return True
    except subprocess.CalledProcessError:
        return False

def get_latest_day_folder():
    problems_dir = "problems"
    if not os.path.exists(problems_dir):
        print("❌ 'problems/' folder not found.")
        return None

    folders = [f for f in os.listdir(problems_dir) if f.startswith("day")]
    if not folders:
        print("❌ No day folders found in 'problems/'.")
        return None

    folders.sort()
    return folders[-1]

def has_changes():
    """Check if there are staged/unstaged changes."""
    result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    return bool(result.stdout.strip())

def main():
    if not is_git_repo():
        print("❌ This is not a Git repository. Run 'git init' first.")
        return

    latest_day = get_latest_day_folder()
    if not latest_day:
        return

    if not has_changes():
        print("⚠️ No changes detected. Nothing to commit.")
        return

    print(f"📂 Latest folder detected: {latest_day}")

    # Inputs with validation
    problem_title = input("🔹 Enter problem title: ").strip()
    while not problem_title:
        problem_title = input("❌ Title cannot be empty. Enter problem title: ").strip()

    source = input("🔹 Source (Personal, CodeWars, LeetCode): ").strip()
    while not source:
        source = input("❌ Source cannot be empty. Enter source: ").strip()

    languages = input("🔹 Languages (Java, Python, both): ").strip()
    while not languages:
        languages = input("❌ Languages cannot be empty. Enter languages: ").strip()

    # Build commit message
    commit_msg = f"{latest_day}: {problem_title} ({source}) ({languages})"

    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
    except subprocess.CalledProcessError:
        print("❌ Git commit failed. Check your repo setup.")
        return

    push_choice = input("🚀 Push to remote? (y/n): ").strip().lower()
    if push_choice == "y":
        try:
            subprocess.run(["git", "push"], check=True)
            print(f"✅ Commit pushed: {commit_msg}")
        except subprocess.CalledProcessError:
            print("❌ Git push failed. Check your remote setup.")
    else:
        print(f"✅ Commit created locally: {commit_msg}")

if __name__ == "__main__":
    main()
