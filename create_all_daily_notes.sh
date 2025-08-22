#!/bin/bash
# Create 366 daily note files with custom questions

BASE_DIR="/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/trickster makes the world/daily"

# Function to create a file with the template
create_file() {
    local month=$1
    local day=$2
    local filename="${month}-${day}.md"
    local filepath="${BASE_DIR}/${filename}"
    
    cat > "$filepath" << EOF
# ${month}-${day}

## A minor: why same vision, different fate? -> promise architecture

## D minor: what is promise's ambition and precision? ->

## G major: how to optimize promise's ambition and precision?

## C major: how to use optimized promise's ambition and precision?

## Notes

EOF
}

# Create files for all 12 months
# January
for day in {01..31}; do
    create_file "01" "$day"
done

# February (29 days for leap year)
for day in {01..29}; do
    create_file "02" "$day"
done

# March
for day in {01..31}; do
    create_file "03" "$day"
done

# April
for day in {01..30}; do
    create_file "04" "$day"
done

# May
for day in {01..31}; do
    create_file "05" "$day"
done

# June
for day in {01..30}; do
    create_file "06" "$day"
done

# July
for day in {01..31}; do
    create_file "07" "$day"
done

# August
for day in {01..31}; do
    create_file "08" "$day"
done

# September
for day in {01..30}; do
    create_file "09" "$day"
done

# October
for day in {01..31}; do
    create_file "10" "$day"
done

# November
for day in {01..30}; do
    create_file "11" "$day"
done

# December
for day in {01..31}; do
    create_file "12" "$day"
done

echo "All 366 files created!"
