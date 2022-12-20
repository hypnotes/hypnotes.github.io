---
layout: post
title: 탐색적 분석
description: >
  Another widely used data structure for data analyzing
# image: /assets/img/blog/example-content-ii.jpg
sitemap: false
permalink: /notes/R/SearchAnalysis
---

* this list will be replaced by the toc
{:toc .large-only}


- 아직 못 끝냄 ..

## TDM

예제 데이터

```R
TDM <- data.frame( words=vector() )
   
for (i in list.files(path="./13_data")) {
  file <- scan(file = paste('./13_data', i, sep="/"), what="char", quote=NULL)
    file <- gsub('[(].+?[)]', '', tolower(file))
    file <- gsub('^[[:punct:]]+|[[:punct:]]+$', '', file)
    file <- file[ nchar(file) > 0 ]
    TDM <- merge( TDM, data.frame( table(file)),
                   by.x = "words", by.y = "file", all = T)
    colnames(TDM)[length(TDM)] <- substring(i, 1, 4) }
    # colname은 취임연도별

TDM <- data.frame(row.names=TDM$words, TDM[2:length(TDM)])
TDM[ is.na(TDM)] <- 0

colnames(TDM) <- gsub('X', '', colnames(TDM))
TDM['RowSums'] <- rowSums(TDM)
TDM <- TDM[order(TDM$RowSums, decreasing = T), ]

#Stop Words 제거하기

stop <- readLines('13_EnglishStopwords.txt')
NEW <- TDM[!(rownames(TDM) %in% stop), ]

```

## 1. 계층적 군집분석

- 유사도/비유사도에 따라 군집으로 분류
- **hierarchical clustering**
- bottom up (유사도 높은 항목부터 결함)
- 덴드로그램 

```R
plot( hclust( dist( scale ..., method = 'minkowski'), method= 'ward.D2'))
```

<br/><img src="../DataAnalytics/R/assets/dendrogram.png" alt="WordCloud" style="height: 400px; width: 400px;"/>

- 단점:
  - height 가 높은 곳에서는 무의미함 
  - 개별적인 유사도는 고려되기 어려움 

  - 행 따로, 열 따로 분석하므로 행범주와 열범주 사이의 관련성을 파악하기 어려움
  - 유사도 거리 계산 방법, 연결 방법 선택의 문제 (파일수가 많아야 다루기 용이)

## 2. 주성분 분석

- 계층적 군집분석의 단점을 대부분 보완함 
- **PCA** (Principal Component Analysis)
- 변수 간의 상관관계가 있는 다차원의 데이터를 효율적으로 저차원의 데이터로 요약
- bi plot
  - 90도 이내: 양의 상관성
  - 180도 음의 상관성
- 관계설정이 자유로우나 해석이 어렵다

```R
install.packages('AMR')
library(AMR)
PCA <- prcomp( scale ....)>
```

## 3. 대응분석 correspondence analysis 
- 지각도 (perception map)에서 공간적 좌표를 통해 공간적 방향과 근접성에 따라 상관성, 군집분석 

- 3 x 3 이상의 빈도 교차표, 즉, 행과 열로 구성되는 각 범주 간 절대빈도자료에서만 적용

- 시각적 분석 원리...

```R
install.packages('ca')
library(ca)
plot(ca (NEW[]), arrows=c(1,0))
```




