#!/bin/bash

# Run this in home directory

# Set up the repository
git clone https://github.com/ProgMod-X/Oppgaver.git
cd Oppgaver/

# Set up the environment
python3 -m venv venv
source venv/bin/activate
pip install openai nbformat

# Set up the script directory
cd /home/ctf/Oppgaver/Scripts/

pwd
# Add execution permissions
chmod +x /home/ctf/Oppgaver/Scripts/AutomateWorkflow.sh

# Set up the cron job
echo "Kjør AutomateWorkflow.sh i home :)"
#(crontab -l ; echo "0 * * * * ~/Oppgaver/Scripts/AutomateWorkflow.sh >> /path/to/logfile.log 2>&1") | crontab -
