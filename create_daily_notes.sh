#!/bin/bash
# Create 366 daily note files for the year

BASE_DIR="/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/trickster makes the world/daily"

# Function to create a file with the template
create_file() {
    local month=$1
    local day=$2
    local filename="${month}-${day}.md"
    local filepath="${BASE_DIR}/${filename}"
    
    cat > "$filepath" << EOF
# ${month}-${day}

## Time Portal
- [[Previous Year: ${month}-${day}]]

## Animal of the Day
- [ ] 👾 A minor
- [ ] 🐢 D minor  
- [ ] 🐅 G major
- [ ] 🐙 C major

## Notes

## Resonances
EOF
}

# Days in each month (including leap year)
declare -A days_in_month=(
    ["01"]=31 ["02"]=29 ["03"]=31 ["04"]=30
    ["05"]=31 ["06"]=30 ["07"]=31 ["08"]=31
    ["09"]=30 ["10"]=31 ["11"]=30 ["12"]=31
)

# Create files for each month
for month in 01 02 03 04 05 06 07 08 09 10 11 12; do
    days=${days_in_month[$month]}
    for ((day=1; day<=days; day++)); do
        # Pad day with zero if needed
        padded_day=$(printf "%02d" $day)
        create_file "$month" "$padded_day"
        echo "Created: ${month}-${padded_day}.md"
    done
done

echo "All 366 files created!"
