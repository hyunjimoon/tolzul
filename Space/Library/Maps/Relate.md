---
up:
  - "[[Home Pro Basic]]"
collection:
  - "[[Views]]"
  - "[[Space/Library/Maps/Maps]]"
related:
  - "[[Space/Library/Maps/Add]]"
  - "[[Space/Library/Maps/Communicate]]"
created: 2022-02-22
rank: 3.5
mapState:
  - 🟩
obsidianUIMode: preview
cssclasses: []
tags:
  - map
---
~ [[ARC Framework]] 

> [!rainbow] ARC » [[Space/Library/Maps/Add]] | **[[Space/Library/Maps/Relate]]** | [[Space/Library/Maps/Communicate]] 

This note is a place of joy, without expectations or obligations, which will be a head-scratcher for a culture obsessed with tasks—but when you start giving your thoughts the honor they deserve, your thoughts become richer and more meaningful.

This is where the garden metaphor gives us a way to approach relating ideas:

> [!trees] **[[Garden]]** » [[Plant]] | [[Cultivate]] | [[Question]] | [[Repot]] | [[Revitalize]] | [[revisit]] — [[Architect]] ⤴️

---

To discover notes that haven't been modified in a long time, go to [[Dusty Ideas]].

---

# 🔗 Related Research Papers

Visual overview of papers that explore relationships between concepts.

```dataview
TABLE WITHOUT ID
	year as Year,
	choice(image, embed(link(image)), 
	       choice(diagrams, "🖼️", "📄")) as Poster,
	file.link as Title,
	join(list(by)) as Author,
	battlefield as Field,
	rank as Rank
WHERE
	contains(collection, [[Papers]]) and
	file.name != ".md"
SORT rank desc, year desc
LIMIT 10
```

--- 
