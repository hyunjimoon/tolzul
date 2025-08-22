#!/usr/bin/env python3
import os

base_dir = "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/trickster makes the world/daily"

# Files to migrate and their target MM-DD files
migrations = {
    "2025-08-07-charlie-feedback.md": "08-07.md",
    "2025-08-07-charlie-model-progression.md": "08-07.md",
    "2025-08-07-smartcity.md": "08-07.md",
    "2025-08-08-promise-precision-evolution.md": "08-08.md",
    "2025-08-09-curiosity-energy.md": "08-09.md",
    "2025-08-09-interesting-criteria.md": "08-09.md"
}

for source_file, target_file in migrations.items():
    source_path = os.path.join(base_dir, source_file)
    target_path = os.path.join(base_dir, target_file)
    
    # Read source content
    with open(source_path, 'r') as f:
        source_content = f.read()
    
    # Read current target content
    with open(target_path, 'r') as f:
        target_content = f.read()
    
    # Find where Notes section is and insert before the tag
    lines = target_content.split('\n')
    insert_index = -1
    
    for i, line in enumerate(lines):
        if line.strip().startswith('#🐅') or line.strip().startswith('#🐢') or line.strip().startswith('#👾') or line.strip().startswith('#🐙'):
            insert_index = i
            break
    
    # Combine content
    if insert_index != -1:
        # Insert source content before the tag
        lines.insert(insert_index, "\n" + source_content + "\n")
        updated_content = '\n'.join(lines)
    else:
        # If no tag found, append at end
        updated_content = target_content + "\n\n" + source_content
    
    # Write back
    with open(target_path, 'w') as f:
        f.write(updated_content)
    
    print(f"Migrated {source_file} → {target_file}")

print("\nMigration complete!")
