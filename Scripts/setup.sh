#!/bin/bash

# Set up the repository
git clone https://github.com/ProgMod-X/Oppgaver.git /path/to/your/repository
cd /path/to/your/repository

# Set up the environment
python3 -m venv venv
source venv/bin/activate
pip install openai nbformat

# Set up the script directory
git clone https://github.com/ProgMod-X/Oppgaver.git /path/to/your/scripts
cd /path/to/your/scripts

# Add execution permissions
chmod +x AutomateWorkflow.sh

# Set up the cron job
(crontab -l ; echo "0 * * * * /path/to/your/scripts/AutomateWorkflow.sh >> /path/to/logfile.log 2>&1") | crontab -