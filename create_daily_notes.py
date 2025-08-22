#!/usr/bin/env python3
import os

base_dir = "/Users/hyunjimoon/MIT Dropbox/Angie.H Moon/tolzul/trickster makes the world/daily"
days_in_month = {
    '01': 31, '02': 29, '03': 31, '04': 30,
    '05': 31, '06': 30, '07': 31, '08': 31,
    '09': 30, '10': 31, '11': 30, '12': 31
}

template = """# {month}-{day}

## Time Portal
- [[Previous Year: {month}-{day}]]

## Animal of the Day
- [ ] 👾 A minor
- [ ] 🐢 D minor  
- [ ] 🐅 G major
- [ ] 🐙 C major

## Notes

## Resonances
"""

count = 0
for month, days in days_in_month.items():
    for day in range(1, days + 1):
        padded_day = str(day).zfill(2)
        filename = f"{month}-{padded_day}.md"
        filepath = os.path.join(base_dir, filename)
        
        with open(filepath, 'w') as f:
            f.write(template.format(month=month, day=padded_day))
        
        count += 1
        print(f"Created: {filename}")

print(f"\nTotal: {count} files created!")
