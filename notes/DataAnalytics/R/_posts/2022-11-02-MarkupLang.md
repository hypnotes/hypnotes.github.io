---
layout: post
title: Markup Language and Character Code
description: >
  Another widely used data structure for data analyzing
# image: /assets/img/blog/example-content-ii.jpg
sitemap: false
permalink: /notes/R/Markup
---

* this list will be replaced by the toc
{:toc .large-only}

## 마크업 언어

- 준비단계

  ```R
  > TEXT <- scan(file = "07_data01.txt", what = "char", quote = NULL)
  Read 938 items
  > TEXT <- tolower(TEXT)
  > TEXT <- gsub("^[[:punct:]]+[[:punct:]]+$", "", TEXT)
  > TEXT.table <- sort(table(TEXT), decreasing = T)
  > TEXT.Freq <- data.frame(row.names=names(TEXT.table), Freq = as.vector(TEXT.table))
  ```

- tip: WORDCLOUD 만들 때는 빈도 내림차순 할 필요 없음