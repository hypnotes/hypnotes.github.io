---
layout: post
title: Data Frame
description: >
  Another widely used data structure for data analyzing
# image: /assets/img/blog/example-content-ii.jpg
sitemap: false
permalink: /notes/R/DataFrame
categories: r
---

* this list will be replaced by the toc
{:toc .large-only}

## 데이터프레임 I - 기본 속성


### 벡터를 이용한 데이터프레임 만들기

<code>a = ['홍길동', '홍길순', '홍길자']; b = [80, 100, 70]; c = [60, 50, 70 ] </code>

```R
> DATA <- data.frame(row.names = a, 국어 = b, 영어 = c)
```
- DATA : 

    |            | 국어     |  영어     | 
    |:-----------|:---------|:---------|
    | 홍길동     | 80       | 60       |
    | 홍길순     | 100      | 50       |
    | 홍길자     | 70       | 70       |

- 새로운 열 추가


  ```R
  > DATA <- data.frame(DATA, 평균 = (b+c)/2, 합계 = b+c )
  ```
- DATA : 

    |            | 국어 | 영어  |  평균 | 합계  | 
    |:-----------|:-----|:-----|:-----|:-----|
    | 홍길동     | 80  | 60 | 70 | 140|
    | 홍길순     | 100 | 50 | 75 | 150 |
    | 홍길자     | 70 | 70 | 70 | 140 |

- 함수 str과 데이터프레임


  ```R
  > str( a )    
  chr [1:3] "홍길동" "홍길순" "홍길자"

  > str( DATA )
  'data.frame':   3 obs. of  4 variables:
  $ 국어: num  80 100 70
  $ 영어: num  60 50 70
  $ 평균: num  70 75 70
  $ 합계: num  140 150 140

  > class( DATA )
  [1] "data.frame"
  ```

- 구성요소와 벡터
  ```R
  > DATA$국어   
   [1]  80 100  70

  > str(DATA$국어)
    num [1:3] 60 50 70
  ```

- **rownames, colnames**
  ```R
  > rownames(DATA)
  [1] "홍길동" "홍길순" "홍길자"

  > colnames(DATA)
  [1] "국어" "영어" "평균" "합계
  ```

### INDEXING
- indexing: VECTORS
  ```R
  > DATA$국어[2]
   [1] 100
  > DATA$국어[c(1,3)]
   [1] 80 70
  ```
- indexing: DATAFRAMES
  ```R
  > DATA[1, 3]
   [1] 70
  > DATA[1:2, 4]
   [1] 140 150

  > DATA[ c(1,3) , c(3,4) ]
          평균 합계
  홍길동   70  140
  홍길자   70  14

  > DATA[ c(1,3) , ]
          국어 영어 평균 합계
  홍길동   80   60   70  140
  홍길자   70   70   70  140
  ```
  - row * col 중 하나 미표기 시 ALL 출력

### 값 편집 
  - VALUES
  ```R
  > DATA$영어[2] <- 70
  > DATA$영어[2:3] <- c( 70, 80 )
  > DATA[ 2:3, 1 ] <- c( 70, 80 )
  ```
  - ROW, COLNAMES
  ```R
  > rownames(DATA)[1] <- "깁갑동"
  > rownames(DATA)[2:3] <- c( "김철수", "김영희" )
  ```
  - DATA : 

    |            | 국어 | 영어  |  평균 | 합계  | 
    |:-----------|:-----|:-----|:-----|:-----|
    | 깁갑동     | 80  | 60 | 70 | 140|
    | 김철수     | 70 | 70 | 75 | 150 |
    | 김영희     | 80 | 80 | 70 | 140 |
  
### 조건 검색
```R
> DATA$영어[ DATA$영어 > 60]
 [1] 70 80
> DATA[ DATA$영어 > 60, 1:3 ]
          국어 영어 평균
  김철수   70   70   75
  김영희   80   80   70
```
- 연습문제 #1: 다음의 df를 만드시오.
  - df : 

    |            | 국어 | 영어  |  평균 |  
    |:-----------|:-----|:-----|:-----|
    | 깁갑동     | 80  | 61 | 70.5 |
    | 김철수     | 95 | 50 | 72.5 | 
    | 김영희     | 80 | 73 | 76.5 | 
  
  <details>                   <!--문제#1 -->
  <summary>답:</summary>
  <div markdown="1">
    ```R
    rowN <- c( "김갑동", "김철수", "김영희")
    kor <- c( 80, 95, 80)
    eng <- c( 61, 50, 73)
    df <- data.frame(rownames=rowN, 국어 = kor, 영어 = eng, 평균 = (kor+eng)/2)
    ``` 
  </div></details>


### 데이터프레임 정렬
```R
> sort(df$국어)
 [1] 80 95 80
> sort(-df$국어)
 [1] -95 -80 -80
```
- order
  ```R
  > order(df$국어)
   [1] 1 3 2
  > order(-df$국어)
   [1] 2 1 3
  > order(df$국어, decreasing = T)
   [1] 2 1 3
  > df$국어[order(df$국어)]
   [1] 80 80 95   #sort와 똑같다

  > df[ order( df$국어), ]
      rownames 국어 영어 평균
    1   김갑동   80   61 70.5
    3   김영희   80   73 76.5
    2   김철수   95   50 72.5
  > df[ order( -df$국어), ]
      rownames 국어 영어 평균
    2   김철수   95   50 72.5
    1   김갑동   80   61 70.5
    3   김영희   80   73 76.5
  > df[ order( df$국어) ,-df$영어 ]
      rownames 국어 영어 평균
    1   김갑동   80   61 70.5
    3   김영희   80   73 76.5
    2   김철수   95   50 72.5
  ```

## 데이터프레임 II - 파일 다루기

### Scan 함수들

- **수치 데이터** scan:

  ```R
  > scan( file = "filename.ext", what = numeric() )
  > scan( file = "filename.ext", what = numeric(), sep= ' ' )
  ```
  - 두 개 같음

- **문자열 데이터** scan:

  ```R
  > scan( file = "05_data02.txt", what = character())
  [1] "a"   "b"   "c"   "d"   "e"   "f g h i j"

  > scan( file = "05_data02.txt", what = "character" , quote = NULL)
  [1] "a"   "b"   "c"   "d"   "e"   "\"f"  "g" "h" "i" "j\"

  ```
  - **charater()** : space로 구분하며 인용보어 안에 있을 경우 하나로 묶는듯 하다
  - **"character", quote=NULL** : 각 space마다 구분하며 인용보어가 있을 시 문자열로 변환한다
  - 

### 함수 cat, 함수 write로 출력

 ```R
  > scan( file = "05_data02.txt", what = "char", quote =NULL)
  [1] "a"   "b"   "c"   "d"   "e"   "\"f"  "g" "h" "i" "j\""

  > cat(data, sep= "\n")
  a
  b
  c
  d
  e
  "f
  g
  h
  i
  j"

  > cat( data, file = "out.txt", sep = "\n" )
  > write( data, file = "out.txt", sep = "\n" )
  ```
  - 두 출력 방식 모두 같다.

### 함수 readLines, 함수 writeLines

```R
> readLines( "05_data02.txt")
[1] "a b c d e"   "\"f g h i j\""
> writeLines( readLines( "05_data02.txt") )
```
- scan vs. readLines
```R
> a <- readLines("03_WhatIsR.txt")
Warning..
> b <- scan( file = "03_WhatIsR.txt", what = "char", qutoe = NULL, sep = '\n')

> length(a) ; length(b)
[1] 26
[1] 17
```
- Length 차이 있는 이유는 readLines는 빈 줄도 한줄로 출력한다
  - scan, sep = "\n" 는 비어있는 줄은 무시한다

- 연습문제 #1: What Is R의 an -> a로 변환하고 내림차순 정렬
  <details>                   <!--문제#1 -->
  <summary>답:</summary>
  <div markdown="1">
    ```R
    > b <- scan(file = "03_WhatIsR.txt", what = "char", quote = NULL)
    Read 486 items
    > b [ b=="an"] <- "a"
    > b[b=="an"]
    character(0)
    > TEXT <- sort(b, decreasing = T)
    > head(TEXT)
    [1] "written" "written" "write"   "within"  "with"    "with"   
    ``` 
  </div></details>

### 벡터의 빈도표 만들기
```R
> Freq.TEXT <- table(TEXT)
> head( Freq.TEXT )
 TEXT
 "environment"      (easily)     (formerly    (including       (linear            …) 
            1             1             1             1             1             1 
> class( Freq.TEXT )  # [1] "table"
> length( Freq.TEXT ) # unique 수, 281
```
- table: 위에 table 명 무조건 출력, 밑에 빈도 수는 무조건 integer, table의 length를 찾는 것 : unique한 값의 개수를 찾는것과 같다

```R
#빈도 내림차순 정렬
> Freq.TEXT <- sort( table(TEXT), decreasing = T )  
> head(names(Freq.TEXT))
[1] "and" "a" "of" "is" "R" "the"
head(unname(Freq.TEXT))
[1] 27 18 18 14 14 
```

- 연습문제 #2: Freq2 (Freq의 알파벳 내림차순) 생성
  <details>                   <!--문제#1 -->
  <summary>답:</summary>
  <div markdown="1">
    ```R
    > Freq2 <- Freq.TEXT[order(-rank(names(Freq.TEXT)))]
    > head(Freq2)
    TEXT
    written   write  within    with Windows    wide 
          2       1       1       3       1       3 
    ``` 
  </div></details>

### 빈도표를 데이터프레임으로 전환
```R
> Freq.Data <- data.frame( Freq.TEXT )
> head(Freq.Data)
  TEXT Freq
1  and   27
2   of   18
3   is   14
4    R   14
5  the   14
6    a   13

> Freq.Data <- data.frame( row.names= rownames(Freq.TEXT), Freq = as.vector(Freq.TEXT))
> head(Freq.Data)
    Freq
and   27
of    18
is    14
R     14
the   14
a     13
```
- table 데이터구조는 벡터가 아님 -> unname(tablename) 보다 as.vector(tablename)이 훨씬 나음
- unname하면 안좋다...
- unname, table, 둘 다 사용해서 dataframe으로 변형해보기

### 데이터프레임에 상대빈도 열 추가
```R
> Freq.Data['Rel.Freq'] = round( Freq.Data$Freq / sum(Freq.Data$Freq), 3)
> head(Freq.Data)
      Freq Rel.Freq
  and   27    0.056
  of    18    0.037
  is    14    0.029
  R     14    0.029
  the   14    0.029
  a     13    0.027

```

### 함수 write.table
- DataFrame을 파일로 출력하기 
```R
> write.table( Freq.Data, file= "Freq.txt", quote = F, sep = "\t", col.names = NA )
```
- **quote = F** : rowname에 인용보어 제거
- **col.names = NA** : column명 앞으로 안치우치게

### 함수 read.delim
- DataFrame을 파일에서 가져오기
```R
> read.delim( file= "Freq.txt", sep = "\t", header = T, row.names = 1, quote = NULL)
```
- **row.names = 1** : 첫번쨰줄을 행명으로 사용한다.....?????

```R
> length(df)
[1] 2
> nrow(df)
[1] 281
> ncol(df)
[1] 2
> dim(df)
[1] 281   2
```