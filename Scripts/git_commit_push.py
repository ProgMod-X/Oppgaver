import subprocess

def commit_and_push_changes(task_name):
    subprocess.run(["git", "add", "-A"])
    subprocess.run(["git", "commit", "-m", f"Add solution for task: {task_name}"])
    subprocess.run(["git", "push"])

if __name__ == "__main__":
    task_name = sys.argv[1]
    commit_and_push_changes(task_name)
