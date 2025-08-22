#!/bin/bash
# Move migrated files to archive

mkdir -p "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/trickster makes the world/daily/archive-2025"

cd "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/trickster makes the world/daily"

mv 2025-08-07-*.md archive-2025/
mv 2025-08-08-*.md archive-2025/
mv 2025-08-09-*.md archive-2025/

echo "Moved 2025 files to archive-2025/"
