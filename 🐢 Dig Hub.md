# 🐢 Dig Hub - Deep Analysis

## Core Mission
Dissect complex systems, unearth hidden parameters

## Key Files
```dataview
LIST
FROM #🐢dig
SORT file.mtime DESC
LIMIT 10
```
- [[📜🐢]]
## Recent Dissections
```dataview
TABLE file.ctime as "Created", length(file.outlinks) as "Connections"
FROM #🐢dig
WHERE file.ctime > date(today) - dur(7 days)
```

## Connections
- Deep Mode Partner: [[🐙 Cal Hub]]
- Grounds the vision of: [[🐅 Gen Hub]]
