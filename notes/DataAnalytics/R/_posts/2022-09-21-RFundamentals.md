---
layout: post
title: Corpus
description: >
  Fundamentals of Corpus Knowledge
# image: /assets/img/blog/example-content-ii.jpg
sitemap: false
permalink: /notes/R/RFundamentals
---

* this list will be replaced by the toc
{:toc .large-only}

- MOST IMPORTANT: <fontcolor>자기주도 학습</fontcolor>, 관찰과 질문

## 환경설정
- [Download R](http://cran.r-project.org)
- [IDE](https://www.rstudio.com/products/rstudio/download/#download)

- PATH에 추가<br>
    1) R 우클릭 > 속성 > 고급<br>
    2) "관리자 권한으로 실행" 설정해 두기<br>


## R기초

- R은 통계분석을 위해 통계학자가 제작함
- R의 출력결과는 Vector 형식임 
    - ex) 입력: 2 + 2 출력: [1] 4
- R의 시작값은 1이다 (타 언어 = 0 )
- R은 enter을 쳐도 식이 제대로 완성될 때까지 값을 출력하지 않음 (input을 계속 받으려고 함)
    - <details> <!--enter 쳐도 계속 나옴 -->
        <summary>example) </summary>
        <div markdown="1">
        <img src="/img/Rmultiline.png" alt="cmdnotend"/>
        </div></details>
- 한줄에 여러 명령 가능 <code>;</code>로 분활
    - 답은 따로 나옴 (다른 줄로)

- <code># 주석, comment</code>
<details>   <!--산술 연산자 -->
<summary>산술 연산자</summary>
<div markdown="1">
```R
2 + 2      # [1] 4
2 - 1      # [1] 1
2 * 2      # [1] 4
4 / 2      # [1] 2
5 %/% 2    # [1] 2 (몫)
5 %% 2     # [1] 1 (나머지)
(3+2) ^ 2  # [1] 125 (거듭제곱)
```
</div></details>

<details> <!--변수명 -->
<summary>변수명</summary>
<div markdown="1">
영문자로 시작할 시 숫자, 마침표 가능. **case sensitive**
```R
    x <- 3
    x <- x + 2
```
</div></details>


<details> <!--자료형 -->
<summary> Data Types (자료형)</summary>
<div markdown="1">
```R
class(TRUE)     # [1] "logical" (all capitalized)
class(F)        # [1] "logical"
class(12.3)     # [1] "numeric"
class(12)       # [1] "numeric"
class(12L)      # [1] "integer" (12로 출력됨)
class(3+2i)     # [1] "complex"
class('a')      # [1] "character"
class("TRUE")   # [1] "character"
```
- 변환 방법: as.numeric(12L) => numeric으로 변함
</div></details>

## Data Structure (데이터, 자료 구조)
- 기본: <fontcolor>vector</fontcolor>
- 한 **데이터구조 당 한 종류의 자료형만** 가능
    - 다른 데이터 추가 시 기존 자료형으로 자동 변환됨

- 벡터 생성 : <code>a <- c( 'red', 'green', 'yellow' )</code>
    - c : combine
    - <code>> class(a)</code> : [1] "character"
    - <code>> str(a) </code>  : chr [1:3] "red", "green", "yellow"  (벡터X)

- **Factor** : (통계에서의 명목 척도)
    - 척도: 숫자로 변환되어 있음 
    - f <- factor(c ('....'))
- **Data Frame** : 
    - g <- data.frame( gender = c("..."),
                       name   = c("..."))
    - table처럼 나옴
    - 인용보어 없음 ("")
    - 각 column마다 datatype 같아야 함
    - column 명 = variable 
    - dim(g)로 ***dimension*** 확인 가능