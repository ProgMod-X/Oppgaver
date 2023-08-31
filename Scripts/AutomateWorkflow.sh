#!/bin/bash

# Set your OpenAI API key
OPENAI_API_KEY="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"

git config --global user.email "auto@generated.documentation"
git config --global user.name "Documentation Bot"

# Pull new changes from the repository
cd "/home/ctf/Oppgaver"
git pull

# Run the process tasks script
python3 "/home/ctf/Oppgaver/Scripts/process_tasks.py"

# Commit and push changes with task names
for notebook in "$REPO_PATH"/*/solution.ipynb; do
    task_name=$(basename "$(dirname "$notebook")")
    cd "$(dirname "$notebook")"
    git add solution.ipynb
    git commit -m "$task_name"
    git push
done
