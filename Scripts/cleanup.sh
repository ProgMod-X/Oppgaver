#!/bin/bash

# Function to recursively rename files
rename_files() {
    local current_dir="$1"
    for file in "$current_dir"/*; do
        if [ -d "$file" ]; then
            rename_files "$file"
        elif [ "${file##*/}" = "oppgave.md" ]; then
            mv "$file" "${file%/*}/README.md"
            echo "Renamed $file to ${file%/*}/README.md"
        fi
    done
}

# Define the root folder where you want to start renaming files
root_folder="/mnt/c/Users/danie/GitHub/Oppgaver/Oppgaver/Grunnleggende-Programmering"

# Call the function with the root folder
rename_files "$root_folder"

echo "Renaming process completed."
