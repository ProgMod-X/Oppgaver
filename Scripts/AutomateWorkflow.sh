#!/bin/bash

# Set your OpenAI API key
OPENAI_API_KEY="YOUR_OPENAI_API_KEY"

# Path to your repository and scripts
REPO_PATH="~/Oppgaver"
SCRIPTS_PATH="~/Oppgaver/Scripts"

# Pull new changes from the repository
cd "$REPO_PATH"
git pull

# Run the setup script to create/update the task index
python3 "$SCRIPTS_PATH/setup.py"

# Run the process tasks script
python3 "$SCRIPTS_PATH/process_tasks.py"

# Commit and push changes with task names
for notebook in "$REPO_PATH"/*/solution.ipynb; do
    task_name=$(basename "$(dirname "$notebook")")
    cd "$(dirname "$notebook")"
    git add solution.ipynb
    git commit -m "$task_name"
    git push
done
