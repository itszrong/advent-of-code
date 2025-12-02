#!/bin/bash

# Script to automatically generate [[bin]] entries for Cargo.toml
# Finds all .rs files in src/bin/*/ directories and generates entries

CARGO_TOML="Cargo.toml"
TEMP_FILE=$(mktemp)

# Extract [package] section (lines before any other section)
awk '/^\[/ && !/^\[package\]/ {exit} {print}' "$CARGO_TOML" | sed '/^$/d' > "$TEMP_FILE"

# Extract [dependencies] section if it exists (only non-blank lines)
DEPS=$(awk '/^\[dependencies\]/{found=1} found{if(/^\[/ && !/^\[dependencies\]/){exit}; if(NF) print}' "$CARGO_TOML")

# Add dependencies section if it exists
if [ -n "$DEPS" ]; then
    echo "" >> "$TEMP_FILE"
    echo "$DEPS" >> "$TEMP_FILE"
fi

# Add blank line before bin entries
echo "" >> "$TEMP_FILE"

# Collect all bin entries first
BIN_ENTRIES=$(mktemp)
find src/bin -name "*.rs" -type f ! -name "*copy*" | sort | while read -r file; do
    bin_name=$(basename "$file" .rs)
    echo "$bin_name|$file" >> "$BIN_ENTRIES"
done

# Write bin entries with blank lines between them
first=true
while IFS='|' read -r bin_name file; do
    if [ "$first" = true ]; then
        first=false
    else
        echo "" >> "$TEMP_FILE"
    fi
    echo "[[bin]]" >> "$TEMP_FILE"
    echo "name = \"$bin_name\"" >> "$TEMP_FILE"
    echo "path = \"$file\"" >> "$TEMP_FILE"
done < "$BIN_ENTRIES"

rm -f "$BIN_ENTRIES"

# Replace original file
mv "$TEMP_FILE" "$CARGO_TOML"

echo "Updated $CARGO_TOML with binary entries"
