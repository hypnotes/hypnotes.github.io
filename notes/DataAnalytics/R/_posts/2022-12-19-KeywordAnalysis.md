---
layout: post
title: 키워드 분석
description: >
  Another widely used data structure for data analyzing
# image: /assets/img/blog/example-content-ii.jpg
sitemap: false
permalink: /notes/R/KeywordAnalysis
---

* this list will be replaced by the toc
{:toc .large-only}


## 키워드

- <fontcolor>키워드</fontcolor> : 텍스트에서 중요한 어휘
  - **aboutnes** 파악 가능 (무엇을 전달하려고 하는가)
  - aboutness != 고빈도 어휘

- 산출 방식
  - 키워드 산출 공식 : Chi-squared, log-likelihood, ...
    - 특정어휘를 지속적으로 반복, 특정 뜻을 여러 어휘로 반복 을 여태 육안으로 분석했다면 이제 **통계로 분석**하기
  - 비교대상 텍스트, 참조 코퍼스

- positive, negative keywords 유심히 분석할 것 (추후 더 보기)

### 함수 merge

```R
merge( 1번째 DF, 2번쨰 DF, by.x = '1번쨰DF의 colname', by.y= '2번째DF의 colname', all = F 또는 T)
```

```R
> A <- rep(letters[1:4], 1:4)
> A.Frame <- data.frame(table(A))
> A.Frame
  A Freq
1 a    1
2 b    2
3 c    3
4 d    4
> B <- rep(letters[2:5], 4:1)
> B.Frame <- data.frame(table(B))
> B.Frame
  B Freq
1 b    4
2 c    3
3 d    2
4 e    1
```
```R
#교집합 (all = F )
merge(A.Frame, B.Frame, 
      by.x = 'A', by.y='B', all = F)
  A Freq.x Freq.y
1 b      2      4
2 c      3      3
3 d      4      2

#합집합 (all = T )
  A Freq.x Freq.y
1 a      1     NA
2 b      2      4
3 c      3      3
4 d      4      2
5 e     NA      1

```
### 함수 Reduce

```R
Reduce ( 함수, 벡터/리스트) # lapply와 거꾸로
```
- 왼쪽부터 순차적으로 2개씩 연산한다 

## TDM : Term Document Matrix

- 예제 데이터: 12_data 폴더 속 [ 12_Crowley.txt, 12_Obama.txt, 12_Question.txt, 12_Romney.txt ] 4가지 파일 
  - 데이터 설명: 2012년 미국 대선 Obama vs Romney, 
  - Crowley(사회자), Question (질문자) 발화 추출

<br/><img src="../DataAnalytics/R/assets/tdm.png" alt="TDM" style="height: 400px; width: 400px;"/>

- 방법 I:

  ```R
  TDM <- data.frame( words=vector() )
   
  for (i in list.files(path="./12_data")) {
    file <- scan(file = paste('./12_data', i, sep="/"), what="char", quote=NULL)
     file <- gsub('[(].+?[)]', '', tolower(file))
     file <- gsub('^[[:punct:]]+|[[:punct:]]+$', '', file)
     file <- file[ nchar(file) > 0 ]
     TDM <- merge( TDM, data.frame( table(file)),
                   by.x = "words", by.y = "file", all = T)
     colnames(TDM)[length(TDM)] <- substring(gsub('[.].+$', '', i), 4) }
  ```

- 방법 II: <code>lapply</code> 사용
  
  ```R
  DF <- lapply(list.files(path="./12_data"), 
  +              function(x){scan(file=paste("./12_data", x, sep="/"), what="char", quote=NULL)})

  DF <- lapply(DF, function(x){gsub('[(].+?[)]', '', tolower(x))})
  DF <- lapply(DF, function(x){gsub('^[[:punct:]]+|[[:punct:]]+$', '', x )})
  DF <- lapply(DF, function(x){ data.frame(table(x[nchar(x) >0 ]))})
  # DF로 만들면 list가 된다

  TDM <- Reduce(function(x, y){merge(x, y, by='Var1', all=T)}, DF) #경고메시지 출력

  #colnames 적절하게 처리
  colnames(TDM) <- c('words', unlist(lapply(list.files(path="./12_data"),
                   function(x) {substring(gsub('[.].+$', '', x), 4)})))

  ```

### TDM 가공

```R
#Rownames 바꾸기 , 2번째 column부터
TDM <- data.frame(row.names=TDM$words, TDM[2:length(TDM)])
#NA 값 0으로 대체
TDM[ is.na(TDM) ] <- 0 

colSums(TDM)
Crowley    Obama Question   Romney 
   1756     7468      568     7982 
```
- <code>colSums</code>의 자료구조: named vector
- Romney가 가장 많은 말을 했음을 알 수 있다

### Comparison Cloud 

```R
library(wordcloud)
comparison.cloud(TDM[c(2,4)], 
  random.order=FALSE, scale=c(2,0.9), rot.per=.4, 
  max.words=200, colors=brewer.pal(8, "Dark2"), 
  title.size=1.1)

```
- comparison cloud의 단점:
  1. 베타적, 두개 이상 할때 (예: 1~4) 1에서 나온 키워드가 3에서 나오지 않는다 (??)
  2. column이 많아질 수록 효과 X

## Chi-Square 잔차: 키워드 분석

$$ 
  Chi = \frac {(관찰-기대)^2}{기대빈도}
$$

$$ 
  잔차 = \sqrt {Chi} = \frac {관찰-기대}{\sqrt {기대빈도}}
$$

```R
CHI <- chisq.test( TDM[c(2,4) ])$residuals  #오류 출력
CHI <- as.data.frame(CHI) #으로 바꾸고 정렬 필요
#Obama 기준 정렬
head( CHI[order(CHI$Obama, decreasing = T), ], 20)
#Romney 기준 정렬
head( CHI[order(CHI$Romney, decreasing = T), ], 20)
```





- 연습문제 #2 하기..:
   

    <details>                   
    <summary>답</summary>
    <div markdown="1">

    ```R
    
    ```

    </div></details>


