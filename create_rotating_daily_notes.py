#!/usr/bin/env python3
import os

base_dir = "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/trickster makes the world/daily"
days_in_month = {
    '01': 31, '02': 29, '03': 31, '04': 30,
    '05': 31, '06': 30, '07': 31, '08': 31,
    '09': 30, '10': 31, '11': 30, '12': 31
}

# Questions and tags for each animal/key
questions = {
    'A': ("## A minor: why same vision, different fate? -> promise architecture", "#👾"),
    'D': ("## D minor: what is promise's ambition and precision? ->", "#🐢"),
    'G': ("## G major: how to optimize promise's ambition and precision?", "#🐅"),
    'C': ("## C major: how to use optimized promise's ambition and precision?", "#🐙")
}

# Rotation order
order = ['A', 'D', 'G', 'C']

day_counter = 0
for month, days in days_in_month.items():
    for day in range(1, days + 1):
        padded_day = str(day).zfill(2)
        filename = f"{month}-{padded_day}.md"
        filepath = os.path.join(base_dir, filename)
        
        # Determine which question and tag to use
        current_key = order[day_counter % 4]
        current_question, current_tag = questions[current_key]
        
        template = f"""# {month}-{padded_day}

{current_question}

## Notes

{current_tag}
"""
        
        with open(filepath, 'w') as f:
            f.write(template)
        
        day_counter += 1
        print(f"Created: {filename} - {current_key} {current_tag}")

print(f"\nTotal: {day_counter} files created!")
