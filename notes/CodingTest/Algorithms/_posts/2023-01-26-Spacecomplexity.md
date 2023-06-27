---
layout: post
title: Space Complexity
description: false
# image: /assets/img/blog/example-content-ii.jpg
sitemap: false
permalink: /notes/CodingTest/Algorithm/spacecomplexity
---

* this list will be replaced by the toc
{:toc .large-only}


## Time vs Space

- nowadays, **time complexity is prioritized** over space since space has become quite abundant and cheap. 
- However, approxiamte calculation of space is required
- In Fields related to Big Data, some do consider space complexity

## Space Complexity
- space required to execute and finish a program
1. **<fontcolor>Fixed Space</fontcolor>** (고정 공간): (not related to algorithm) where code is saved, simple variable and constants
2. **<fontcolor>Dynamic (variable) Space</fontcolor>** (가변 공간): (ALGORITHM) dynamic space required during execution  

$$ S(P) = c + S_P(n) $$
  - $$ c $$ : fixed 
  - $$ S_P(n) $$ : dynamic 

- **SPACE COMPLEXITY = (depends on) Dyanmic Space**

## Example

```py
def factorial(n):
  fac = 1
  for index in range(2, n+1):
    fac = fac * index
  return fac
```

- $$ Space Complexity$$ : $$  O(1)$$
  - 3 variables (`n`, `fac`, `index`)

```py
def factorial(n):
  if n > 1:
    return n * factorial(n-1)
  else:
    return 1
```
- $$ Space Complexity$$ : $$O(n)$$
  - $$n$$ variables (`n` created every time it is recursed)