---
collection:
  - "[[Maps]]"
  - "[[Collections]]"
created: "{{date}}"
rank: 1
---
~ [[Collections]] 

This note collects all notes where the `collection` property says `{{title}}`.

```dataview
TABLE WITHOUT ID
	file.link as Note,
	dateformat(created, "EEE, MMM dd, yyyy") as "Date Created"
WHERE
	contains(collection,this.file.link) and
	!contains(file.name, "Template")
SORT created desc
LIMIT 333
```
