#!/bin/bash
# Move all date-formatted files to Chain 1

# From Chain 4
mv "4_👾segment-replicate-capitalize/🧍‍♀️case/temporal_patterns/🎍year/💭theorizing/ent_bootcamp/2025-07-17.md" "1_🐢acculturate-evaluate/"
mv "4_👾segment-replicate-capitalize/🧍‍♀️case/temporal_patterns/🏛️quarter/2025-Q3.md" "1_🐢acculturate-evaluate/"

# From Chain 4 daily files
for file in 4_👾segment-replicate-capitalize/🧍‍♀️case/temporal_patterns/🤜day/20*.md; do
  if [ -f "$file" ]; then
    mv "$file" "1_🐢acculturate-evaluate/"
  fi
done

# From _ref folder
for file in _ref/*20*-*.md; do
  if [ -f "$file" ]; then
    filename=$(basename "$file")
    mv "$file" "1_🐢acculturate-evaluate/$filename"
  fi
done

echo "Date files moved to Chain 1"