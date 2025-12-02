#!/bin/bash

# Script to automatically generate [[bin]] entries for Cargo.toml
# Finds all .rs files in src/bin/*/ directories and generates entries

CARGO_TOML="Cargo.toml"
TEMP_FILE=$(mktemp)
DEPS_FILE=$(mktemp)

# Extract [package] section (everything before [[bin]] or [dependencies])
awk '/^\[\[bin\]\]/ || /^\[dependencies\]/ {exit} {print}' "$CARGO_TOML" > "$TEMP_FILE"

# Extract [dependencies] section if it exists (handles it being anywhere in the file)
awk '/^\[dependencies\]/{found=1} found{if(/^\[/ && !/^\[dependencies\]/){exit}; print}' "$CARGO_TOML" > "$DEPS_FILE"

# Remove trailing blank lines from package section
sed -i.bak -e :a -e '/^\n*$/{$d;N;ba' -e '}' "$TEMP_FILE" 2>/dev/null || \
{ awk '{if (NF || !blank_seen) {if (NF) blank_seen=0; else blank_seen=1; print}}' "$TEMP_FILE" > "${TEMP_FILE}.tmp" && mv "${TEMP_FILE}.tmp" "$TEMP_FILE"; }

# Add dependencies section if it exists
if [ -s "$DEPS_FILE" ]; then
    echo "" >> "$TEMP_FILE"
    cat "$DEPS_FILE" >> "$TEMP_FILE"
fi
rm -f "$DEPS_FILE"

# Add exactly one blank line before bin entries
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
