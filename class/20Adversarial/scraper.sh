#!/bin/bash

# Source, destination, and remaining directories
source_dir="bing"
destination_dir="train/$1"
remaining_dir="test/$1"

# Function to resize images
resize_image_in_place() {
    local file="$1"
    convert "$file" -resize 500x500\> "$file"
}

# Function to traverse directories recursively
traverse() {
    local directory="$1"
    for file in "$directory"/*; do
        if [ -d "$file" ]; then
            traverse "$file"
        elif [ -f "$file" ]; then
            # Check if the file is an image
            if file --mime-type "$file" | grep -q "image"; then
                echo "$file"
                resize_image_in_place "$file"
            fi
            if [[ "$file" == *.tiff ]]; then
              rm $file
            fi
        fi
    done
}

# Ensure the source directory exists
if [ ! -d "$source_dir" ]; then
  mkdir -p "$source_dir"
fi

python bbid.py $1

traverse "$source_dir"

# Ensure the destination directory exists; create if not
if [ ! -d "$destination_dir" ]; then
  mkdir -p "$destination_dir"
fi

# Ensure the remaining directory exists; create if not
if [ ! -d "$remaining_dir" ]; then
  mkdir -p "$remaining_dir"
fi

# Get the total number of files in the source directory
total_files=$(find "$source_dir" -maxdepth 1 -type f | wc -l)

# Calculate the number of files to move (three-quarters of total_files)
files_to_move=$((total_files * 3 / 4))

# Move random files to the destination directory
find "$source_dir" -maxdepth 1 -type f -print0 | shuf -z -n "$files_to_move" | xargs -0 mv -t "$destination_dir"

# Move the remaining one-quarter to the remaining directory
find "$source_dir" -maxdepth 1 -type f -exec mv -t "$remaining_dir" {} +

echo "Random three-quarters moved to $destination_dir, remaining one-quarter moved to $remaining_dir."

