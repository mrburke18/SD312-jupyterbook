#!/bin/bash

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
        fi
    done
}

# Start traversal from the current directory
traverse .

echo "Image resizing completed."
