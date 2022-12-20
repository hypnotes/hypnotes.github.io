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



- 연습문제 #1 <br>1. 08_Sejong_UTF-8.txt 줄단위로 불러오고 형태소만 추출하기
  <details>                   <!--문제#1 -->
  <summary>답:</summary>
  <div markdown="1">
    ```R
    > TEXT <- scan( file ="08_Sejong_UTF-8.txt", what= "char", quote= NULL, sep="\n", encoding="UTF-8")
    > a <- grep("^9BTE", TEXT, value=T)
    > b <- unlist(strsplit(a, '\t'))
    > c <- unlist(strsplit(b, " [+] ")) 
    > Mors <- grep("/", c, value=T)  #이거 말고 by 3해서 3번쨰꺼만 추출도 가능
    > head(Mors)
    [1] "식물/NNG"   "들/XSN"     "의/JKG"     "사생활/NNG" "이승우/NNP"
    [6] "장편/NNG"  
    > length(Mors)
    [1] 114303
    ``` 
  </div></details>

<br/>

- 연습문제 #2 : 변수 Mors에 대해서 Mors.Freq 만들기 (내림차순 데이터프레임)
  <details>                   <!--문제#1 -->
  <summary>답:</summary>
  <div markdown="1">
    ```R
    > Mors <- grep("/", c, value=T)
    > Mors.Freq <- sort(table(Mors), decreasing = T)
    > Mors.Freq <- data.frame(row.names=rownames(Mors.Freq), Freq = as.vector(Mors.Freq))
    > head(Mors.Freq, 10)

    ``` 
  </div></details>
<br/>

- 연습문제 #3 : Wordcloud 만들기
  <details>                   <!--문제#1 -->
  <summary>답:</summary>
  <div markdown="1">
    ```R
    > library(wordcloud)
    > wordcloud(rownames(Mors.Freq), Mors.Freq$Freq, 
                scale=c(3, 0.8), min.freq=2, max.words=100,
                randm.order=F, rot.per=0.4, color=brewer.pal(8, "Dark2")) 
    ``` 
  </div></details>

<br/>

- 연습문제 #4 : NNG.Freq 만들기
  <details>                   <!--문제#1 -->
  <summary>답:</summary>
  <div markdown="1">
    ```R
    > NNG <- grep("/NNG", Mors, value=T)
    > NNG <- sort(table(NNG), decreasing = T)
    > NNG.Freq <- data.frame(row.names = rownames(NNG), Freq = as.vector(NNG))
    ``` 
  </div></details>

<br/>

- 연습문제 #5 : NNG.Freq 의 '/NNG' 제거
  <details>                   <!--문제#1 -->
  <summary>답:</summary>
  <div markdown="1">
    ```R
    > NNG.Freq <- data.frame(row.names = gsub("/NNG", "", rownames(NNG)), Freq = as.vector(NNG))
    ```
  </div></details>

<br/>

- 연습문제 #6 : NNG.Freq 저장
  <details>                   <!--문제#1 -->
  <summary>답:</summary>
  <div markdown="1">
    ```R
    > write.table(NNG.Freq, file="NNG.txt", quote=F, sep="\t", col.names=NA, fileEncoding="UTF-8")
    ```
  </div></details>