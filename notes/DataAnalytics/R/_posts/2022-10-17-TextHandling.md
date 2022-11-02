---
layout: post
title: 텍스트 처리 함수
description: >
  Another widely used data structure for data analyzing
# image: /assets/img/blog/example-content-ii.jpg
sitemap: false
permalink: /notes/R/TextHandling
---

* this list will be replaced by the toc
{:toc .large-only}

## 텍스트 처리 함수

- toupper()   #안에: vector
- tolower()

- nchar()   #문자열또는 문자열 vector만 들어감 
  - 문자열의 길이 알려준다
- mean함수에 적용 시 평균 어휘길이 찾을 수 있다
- Factor은 nchar함수 적용 불가능 하다

### 텍스트 가독성 (readability)
- 텍스트 수준 평가 기준 (몇학년정도) ex: Lexile

- 연습문제 2
```R
#make Freq with 03_WhatIsR.txt
> head(Freq)
      Freq Length
  and   27      3
  of    18      2
  the   17      3
  is    14      2
  r     14      1
  a     13      1
```
1. 소문자 변환
2. 빈도표 빈도 내림차순 
3. 빈도표 데이터프레임으로 변환
4. 행제목의 각 어휘에 대한 어휘길이 새로운 열로 추가
5. 열제목 : Freq, Length

  <details>                   <!--문제#1 -->
  <summary>답:</summary>
  <div markdown="1">
    ```R
    > TEXT <- tolower(TEXT) #1
    > Freq <- sort(table(TEXT), decreasing = T) #2
    > Freq <- data.frame(row.names= names(Freq), Freq = as.vector(Freq), Length = nchar(names(Freq))) #3, 4, 5
    ``` 
  </div></details>


### 문자열 연결 
 - **paste** 함수: 각자 다른 애들을 하나의 문자열로 연결
```R
> paste( 1,2,3,4,5 )
[1] "1 2 3 4 5"
> paste("a", "b", "c", "d", "e")
[1] "a b c d e"
> paste("a", 1, 2, "d", 3)
[1] "a  1 2 d 3"
```
- paste는 데이터 구조 가리지 않는다

```R
> paste( "a", 1:5 )
[1] "a 1" "a 2" "a 3" "a 4" "a 5"
> paste("a", "b", 1:5)
[1] "a b 1" "a b 2" "a b 3" "a b 4" "a b 5"
> paste( c("a", "b"), 1:5 )   #교차 pasting
[1] "a 1" "b 2" "a 3" "b 4" "a 5"

> paste(1:12, month.abb)
 [1] "1 Jan"  "2 Feb"  "3 Mar"  "4 Apr"  "5 May"  "6 Jun"  "7 Jul"  "8 Aug"  "9 Sep"  "10 Oct" "11 Nov" "12 Dec"

```
- 함수 paste: **sep** 이용

  ```R
  > paste( "I", "dont", "know", sep = "")
  [1] "Idontknow"
  > paste( "I", "dont", "know", sep = " ")
  [1] "I dont know"
  > paste( "I", "dont", "know", sep = "\t")
  [1] "I\tdont\tknow"
  > paste( "I", "dont", "know", sep = "\n")
  [1] "I\ndont\nknow"
  ```

- **COLLAPSE**
```R
> String <- paste(Sample, collapse = " ")
> String
[1] "What is R? Introduction to R R is a language and.."
> length(String)
[1]  1
```
- **sep**: 서로 다른 논항을 연결할 때 사용
  - sep 미존재 시 : " " <- default
- **collapse**: 
```R
> paste( "a", "b", "c", sep= ":" )
[1] "a:b:c"
> paste( "a", "b", "c", 1:3, sep= ":" )
[1] "a:b:c:1" "a:b:c:2" "a:b:c:3"
> paste( "a", "b", "c", collapse = ";" )  #효과X, "a b c"가 하나기 떄문에...????뭐래는거야 
[1] "a b c"
> paste( "a", "b", "c", collapse = ";" , sep=":" )  #효과X
[1] "a:b:c"
> paste( "a", "b", "c", 1:3, collapse = ";" , sep=":" )
[1] "a:b:c:1;a:b:c:2;a:b:c:3"
```

### N-Gram 만들기

```R
> bi.gram <- paste(Sample[1:(length(Sample)-1)], Sample[2:length(Sample)], sep = " " )
# [1] "What is"         "is R?"          
# [3] "R? Introduction" "Introduction to"
# [5] "to R"            "R a"   
```
- 1 ~ n-1 : 2 ~ n 이렇게 만들기
- <code>trigram</code> 도 같은 원리로 작성

### 문자열 분리: strsplit, unlist

- a = "I do not know" 

```R
> strsplit(a, " ")  #두번째 인자 기준
[[1]]
[1] "I" "do" "not" "know" 

> strsplit(a, "" )
[[1]]
 [1] "I" " " "d" "o" " " "n" "o" "t" " " "k"
[11] "n" "o" "w"

```
- list 로 출력한다

```R
> b <- c( "하나 둘 셋", "넷 다섯 여섯"); b;
[1] "하나 둘 셋" "넷 다섯 여섯"

> strsplit(b, " " )
[[1]]
[1] "하나" "둘" "셋"
[[2]]
[1] "넷" "다섯" "여섯"

> unlist( strsplit(b, " "))
[1] "하나" "둘" "셋" "넷" "다섯" "여섯"
```
### 함수 substr, substring 
- R에서 문자열 indexing 안됨 => substring 사용

```R
> a <- c( 'apple', 'banana', 'orange')

> substr(a, 2, 5)
[1] "pple" "anan" "rana"
> substring(a, 2, 5)
[1] "pple" "anan" "rana"

> substr(a, 2, 10)
[1] "pple"   "anana"  "range"
> substring(a, 2, 10)
[1] "pple"   "anana"  "range"

> substr(a, 2)
ERROR...
> substring(a, 2)
[1] "pple"   "anana"  "range"
```
- substring(a, 시작위치, 끝위치) 중 끝 위치보다 적으면 그냥 있는대까지 출력
- <code>substr()</code>은 반드시 3가지 인자 
- <code>substring()</code>은 마지막 인자 생략 시 끝까지인것으로 간주
- 응용문제
  ```R
  > substr(a, 1, 1) <- toupper(substr(a, 1, 1)); a;
  [1] "Apple" "Banana" "Orange"
  ```

- 연습문제

  <details>                   <!--문제#1 -->
  <summary>whatisR 소문자로 변환 뒤 어휘문자열의 마지막 알파벳 또는 문장부호만 추출, 빈도 내림차순의 빈도표 Final 산출</summary>
  <div markdown="1">
    ```R
    > Final <- substring( tolower(TEXT), nchar(TEXT))
    > Final <- sort(table(Final), decreasing = T)
    > Final
    Final
    e  s  d  n  r  ,  t  .  a  f  y  h  l  o  g  c  )  w  k  m  u  "  ?  +  x 
    79 69 46 45 41 33 29 22 19 19 18 15 15  9  7  4  3  3  2  2  2  1  1  1  1 
    ``` 
  </div></details>


## 정규표현 I


### 함수 grep : INDEX
- 정규표현 = 문자열 부분 일치
- 비교연산자 = 완전 일치

- a = "the first", "the second", "the third"
```R
> grep( 찾고자하는String, SampleString )
> grep( "i", a )  
[1] 1 3
```
- <fontcolor><bold>index를 반환</fontcolor></bold>한다
- **value = T** 속성을 넣으면 index가 아닌 값을 반환함
```R
> grep( "i", a, value = T )  
[1] "the first" "the third"
```

### 함수 grepl : T/F 값
```R
> grepl("i", c("the first", "the second", "the third"))
[1]  TRUE FALSE  TRUE
```

- <fontcolor><bold> TRUE, FALSE 반환 </bold> </fontcolor>
- 대괄호안에서 사용 가능(grep, grepl)
- value = T 속성 사용 **불가능**

### 함수 gsub : 문자열 치환 (바꾸기)
```R
> gsub( 바꿀문자열, 목표문자열, 전체문자열)
> gsub( "the", "a", a ) # a 벡터안 문자열들 중 "the" -> "a"
 [1] "a first"  "a second" "a third" 
```

### 문자열 시작과 끝
- <code>^x</code>: x로 시작하는 string
- <code>y$</code>: y로 끝나는 string
- <code><bold>ignore.case = T </bold><code>
```R
> grep("^T", a, value= T, ignore.case = T)
[1] "the first"  "the second" "the third" 
```

### 정규표현 or
a ← c ("gray", "grey", "grant" )

```R
> grep ("ra|re", a, value = T)
[1] "gray"  "grey"  "grant"
```
- SPACE Matters

```R
> unlist( strsplit( a, "th" ))
[1] ""    ""  "e first"   ""    "e second"  ""  "e "   "ird"

> unlist( strsplit( a, "t|h" ))
[1] ""    ""    "e firs"    ""    ""    "e second"  ""  ""    "e "  ""  "ird"
```

- 연습문제 #1 : WhatIsR의 단어 중 'w' 또는 'W"로 시작하거나 끝나는 문자열 추출
답안 (3가지 방법)

1. TEXT[ grep("^w|^W|w$|W$", TEXT)]
2. TEXT[ grepl("^w|w$", TEXT, ignore.case=T)]
3. grep("^w|w$", TEXT, ignore.case=T, value=T)


### 반복 문자 및 매칭 문자
| 정규표현 문자    | 의미     | 예 ]
|:--------------|:------------|:------------|
| **\*** |  0 or 1 more time  | ca*t = ct, cat, caat, caaaaaat, ... |
| **+** |  at least 1 time | ca+t = cat, caat, caaaaaat, ... |
| **?** |  0 or 1 time  | ca?t = ct, cat |
| **.** | _하나 들어감  | ca.t = caat, cabt; ca..t = caaat, caabt 등등 |

- 연습문제 #2: 
  - 문자열 끝이 "ed" 또는 "e"인 경우 출력 &&
  - 문자열 중간에 '-' 포함


답:
  - TEXT[ grep("^.+-.+(ed$|e$)", TEXT)] 또는
  - grep("^.+-.+(ed$|e$)", TEXT, value = T)

### 문자 목록 중 하나 일치
- [kbp] = k,b,p 중 하나 일치
- [A-Z] / [a-z] / [a-zA-Z]
- [가-힣] 
- [^가] : [] 안에 있는 '^'는 <code>not</code>임 
- NOT 개념 제대로 이해하기 

### 이스케이프 문자
- 정규표현 메타문자
  - . $ * ? | ^ [] ()

- 문제:

  ```R
  > a <- c( '3.45', '10+4=14', '$15')
  > grep('.', a, value = T)
  [1] "3.45", "10+4=14", "$15"
  > grep('.++', a, value = T)
  Error
  > grep( '^$', a, value = T)
  character(0)
  ```
- 해결: <code>\\</code> 또는 <code>[]</code> 사용
  
  ```R
  > grep( '\\.', a, value = T )
  [1] "3.45"
  > grep( '[.]', a, value = T)
  [1] "3.45"
  > grep( '.+\\+', a, value = T )
  [1] "10+4=14"
  > grep( '.+[.+]', a, value = T )
  [1] "3.45"  "10+4=14"
  > grep( '^\\$', a, value = T )
  [1] "$15"
  ```

  - 연습문제: 문장부호 (.?!) 기준으로 WhatIsR의 문장 추출 (총 23줄)
  <details>                   <!--문제#1 -->
    <summary>답</summary>
    <div markdown="1">

      ```R
      > sentences <- unlist(strsplit(paste(TEXT, collapse = " "), "[?.!]" ))
      ```
    </div></details>


## 정규표현 II


### 반복 문자 및 매칭 문자

| 문자유형   | 설명     | 예 |
|:--------------|:------------|:------------|
| **[:digit:]** |  0 1 2 3 4 5 6 7 8 9 | 
| **[:alpha:]** |  자연언어 문자 |  |
| **[:upper:]** |  대문자  |   |
| **[:lower:]** | 소문자  |  |
| **[:punct:]** | ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~  |   |
| **[:space:]** | 탭, 스페이스, 엔터  |   |
| **[:blank:]** | 탭, 스페이스  |   |
| **[:alnum:]** | 문자와 숫자  |   |
| **[:graph:]** | 문자, 숫자, 문장부호  |   |


- page 3

### 어휘 경계 \\b 여기 보기...

```R
a <- c( "motor car", "car", "cartoon", "bicarbonate", " car", "car\n", "123car", "~car.")

#부분매칭    
> grep( "car", a, value = T ) 
[1] "motor car"   "car"         "cartoon"     "bicarbonate" " car"       
[6] "car\n"       "123car"      "!car." 
##car 앞 공백............???
> grep( "\\bcar", a, value = T )
[1] "motor car" "car"       "cartoon"   " car"      "car\n"     "!car."    
##car 뒤 .....
> grep( "car\\b", a, value = T )
[1] "motor car" "car"       " car"      "car\n"     "123car"    "!car."    
##
> grep( "\\bcar\\b", a, value = T )
[1] "motor car" "car"       " car"      "car\n"     "!car."    
##
> grep( "^car$", a, value = T )
[1] "car"

```

### 최소 매칭

| 문자    | 설명     |
|:--------------|:------------|
| **\*?** |  * 와 같으나 문자열을 최소로 매치 | 
| **+?** |  + 와 같으나 문자열을 최소로 매치 | 
| **??** |  ? 와 같으나 문자열을 최소로 매치  |  

```R
> b
[1] "<a href=\"in.html\">HERE</a><a href=\"out.html\">"


> gsub('href=".*"', "문자열", b)
[1] "<a 문자열>"
> gsub('href=".*?"', "문자열", b)
[1] "<a 문자열>HERE</a><a 문자열>"

> gsub('href=".+"', "문자열", b)
[1] "<a 문자열>"
> gsub('href=".+?"', "문자열", b)
[1] "<a 문자열>HERE</a><a 문자열>"
```
- 연습문제 #1 <br>1. What Is R의 문장부호 제거 및 소문자 변환<br>2. 빈도표 내림차순 추출 및 데이터프레임 변환 (행명= 어휘) <br>3. 상대빈도 열 추가 뒤 파일 저장 
  <details>                   <!--문제#1 -->
  <summary>답:</summary>
  <div markdown="1">
    ```R
    > text <- gsub("[[:punct:]]", "", tolower(TEXT)) 
    > text <- sort(table(text), decreasing = T)
    > text.Freq <- data.frame(row.names=names(text), Freq = as.vector(text))
    > text.Freq<- data.frame(text.Freq, Rel.Freq = round(text.Freq$Freq/sum(text),3))
    > write.table(text.Freq, file = "freq.txt", quote=F, sep="\t", col.names=NA)
    ``` 
  </div></details>


### 기본적인 영문 텍스트 전처리 작업

1. 대문자의 소문자 변환
2. 모든 문장부호 및 숫자 제거
3. 소유격 <code>'s</code>, 부정 <code>n't</code>, <code>I'm</code>, <code>you're</code>, <code>you've</code> 등 분리/제거 
4. 불용어 stop word 목록 제거
  - 길이 2 또는 3 이하 어후 ㅣ제거 (약자, a, an, in, on..etc)
  - the, in, what 등 기능어/문법어 (say, people) 등 텍스트 주제어가 될 가능성 적은 고빈도 어휘 제거
5. <fontcolor>stemming</fontcolor>: <code>walked</code> => <code>walk</code> 와 같이 어미 제거
6. <fontcolor>lemmatizing</fontcolor>: <code>am, are, ...</code> => <code>be</code>와 같이 기본형 복원 

\* 기본일 뿐, 맹목적으로 따르지 않아야 한다 (절대적 기준은 존재하지 않으며, 관찰에 따라 가공 과정이 다르다)

- 연습문제 #2 <br>1. 07_data01.txt 소문자 변환<br>2. 어휘 앞뒤 문장부호연쇄 제거 <br>3. 빈도표 추출 후 빈도 내림차순 => dataframe 변환
  <details>                   <!--문제#1 -->
  <summary>답:</summary>
  <div markdown="1">
    ```R
    > text <- tolower(TEXT)
    > TEXT <- gsub("^[[:punct:]]+|[[:punct:]]+$", "", text)
    > TEXT.tab <- sort(table(TEXT), decreasing = T)
    > Freq.text <- data.frame(row.names=names(TEXT.tab), Freq = as.vector(TEXT.tab))
    ``` 
  </div></details>

## 워드클라우드 WordCloud

- 텍스트형 데이터 시각화 

### 패키지 packages

- library같은, 특정 기능 (함수 집합) 제공 (ex: wordcloud)

```R
#한번만 다운로드
install.packages('패키지명')
#사용 시 매번 불러오기
library(패키지명)

##wordcloud 사용 예시
wordcloud(rownames(Freq.text), Freq.text$Freq, #여기까지만 하면 흑백으로 출력
  scale=c(3, 0.8), min.freq=2, max.words=90, 
  random.order=F, rot.per=0.4, color = brewer.pal(8, "Dark2"))
```

- **WORDCLOUD** 설명
  ```R
  > wordcloud( 단어들(텍스트형벡터), 수치형벡터, 
               scale=(최대폰트사이즈, 가장작은 폰트사이즈),
               min.freq = 가장 작은 수치 
               max.words = 출력할 최대 단어들
               random.order = F (빈도순으로 중간에 몰림)
               rot.per = 0.4 (세로로 출력하는 단어; 40%, 가로: 60%),
               colors = brewer.pal(최대색상들, "Dark2") #팔레트 종류중 하나
              )
  ```