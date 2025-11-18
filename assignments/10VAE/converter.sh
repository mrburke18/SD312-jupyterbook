#!/bin/bash

# Function to convert PGM images to PNG format in-place
convert_pgm_to_png_inplace() {
    local file="$1"
    echo "$1"
    convert "$file" "${file%.*}.png"
    rm "$file"  # Remove the original PGM file after conversion
}

# Function to traverse directories recursively
traverse() {
    local directory="$1"
    echo "$directory"
    for file in "$directory"/*; do
        if [ -d "$file" ]; then
            traverse "$file"
        elif [ -f "$file" ]; then
            # Check if the file is a PGM image
            convert_pgm_to_png_inplace "$file"
            #if file --mime-type "$file" | grep -q "image/x-portable-graymap"; then
            #fi
        fi
    done
}

# Start traversal from the current directory
traverse data

echo "PGM to PNG conversion in-place completed."
