import os
import sys

def detect_repo_language():
    cwd = os.getcwd().lower()
    if "java" in cwd:
        return "java"
    elif "python" in cwd:
        return "python"
    return None

def get_next_day_folder(problems_dir):
    folders = [f for f in os.listdir(problems_dir) if f.startswith("day")]
    if not folders:
        return "day0001"
    folders.sort()
    latest = folders[-1]
    latest_num = int(latest[3:])
    return f"day{latest_num + 1:04d}"

def create_scaffold(folder_name, language):
    problems_dir = "problems"
    folder_path = os.path.join(problems_dir, folder_name)

    if not os.path.exists(problems_dir):
        os.makedirs(problems_dir)

    if os.path.exists(folder_path):
        print(f"⚠️ {folder_name} already exists at {folder_path}")
        return False

    os.makedirs(folder_path)

    if language == "java":
        with open(os.path.join(folder_path, "Solution.java"), "w") as f:
            f.write("public class Solution {\n    public static void main(String[] args) {\n        // TODO: Implement solution\n    }\n}\n")
    elif language == "python":
        with open(os.path.join(folder_path, "solution.py"), "w") as f:
            f.write("def solution():\n    # TODO: Implement solution\n    pass\n\nif __name__ == \"__main__\":\n    solution()\n")

    with open(os.path.join(folder_path, "README.md"), "w") as f:
        f.write(f"# {folder_name}\n\n## Problem\n\n(TODO: Add problem description)\n\n## Approach\n\n(TODO: Explain your solution)\n")

    print(f"✅ Created scaffold for {folder_name} in {problems_dir}/")
    return True

def main():
    language = detect_repo_language()
    if not language:
        print("❌ Could not detect repo type (expected 'java' or 'python' in path).")
        return

    problems_dir = "problems"
    if not os.path.exists(problems_dir):
        os.makedirs(problems_dir)

    if len(sys.argv) > 1:
        # Manual mode: user gave a folder name
        folder_name = sys.argv[1]
        folder_path = os.path.join(problems_dir, folder_name)

        if os.path.exists(folder_path):
            print(f"⚠️ {folder_name} already exists.")
            choice = input(f"Do you want to create {get_next_day_folder(problems_dir)} instead? (y/n): ").strip().lower()
            if choice == "y":
                folder_name = get_next_day_folder(problems_dir)
                create_scaffold(folder_name, language)
            else:
                print("❌ Aborted. No folder created.")
        else:
            create_scaffold(folder_name, language)

    else:
        # Auto mode: create next day folder
        folder_name = get_next_day_folder(problems_dir)
        create_scaffold(folder_name, language)

if __name__ == "__main__":
    main()
