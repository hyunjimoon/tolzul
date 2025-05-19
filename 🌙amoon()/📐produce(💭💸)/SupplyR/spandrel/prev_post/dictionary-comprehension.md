---
title: "dictionary comprehension"
date: "2019-06-04"
categories: 
  - "blog"
---

```
budget = 10 
total_ratio = 0
company_list = ['c', 'l', 's']

budget_ratio = {'c': 1, 'l':1, 's':1}

for c in company_list:
    total_ratio += budget_ratio[c]
    dic = {c : budget * budget_ratio[c]/total_ratio for c in company_list}
```
