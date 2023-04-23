---
layout: post
title: 07 Learning Problem
description: >

image: ../DataAnalytics/DataScience/assets/7-title.png
hide_image: true
sitemap: false
permalink: /notes/DataScience/LearningProblem
---

- this list will be replaced by the toc
{:toc .large-only}

## Introduction

- The big picture of Machine Learning (Learning from Data)
  <img src="../DataAnalytics/DataScience/assets/7-bigpicture.png" alt="lifecycle" style="height: 500px; width: auto;"/>

### Problem Setup

- **_Formalization_**:

  - $$X = ℝ^d$$ : input space
    - $$ℝ^d$$: d-dimensional Euclidean space
    - input vector $$x ∈ X : x = (x_1, x_2, ..., x_d)$$
  - let $$y={+1, -1}$$ : output space ($$\rightarrow$$ binary decision)

- **_Example_**: credit approval (P/F) of applicants of bank loan

  | component       | symbol                           | credit approval metaphor      |
  | :-------------- | :------------------------------- | :---------------------------- |
  | input           | $$x$$                            | customer application          |
  | output          | $$y$$                            | approve / deny                |
  | target function | $$f : X \rightarrow Y $$         | ideal credit approval formula |
  | data            | $$(x_1, y_1), ..., (x_N, y_N) $$ | historical records            |
  | hypothesis      | $$g: X \rightarrow Y$$           | formula to be used            |

  - $$f$$: unkown target function
  - $$X$$: input space (set of all possible inputs $$x$$)
  - $$Y$$: output space (set of all possible outputs)
  - $$N$$: the number of input-output examples ( training examples )
  - $$D≜ {(x_1, y_1), ..., (x_N, y_N)}$$: data set where $$y_n = f(x_n)$$

  - find $$g(x) \approx y=f(x)$$
  - Example:
    - $$x = \begin{bmatrix} x_1\\x_2\end{bmatrix}$$ where $$x_1$$: age and $$x_2$$: annual salary (in USD)
    - $$N=$$ 11, $$d=$$ 2, $$X= ℝ^2$$, and $$Y=$$ { `approve`, `deny`}
    - data set $$D$$:
      <img src="../DataAnalytics/DataScience/assets/7-dataset.png" alt="lifecycle" style="height: 300px; width: auto;"/>
    - $$\Rightarrow$$ linear model (easy, but might not be accurate) $$\rightarrow$$ find $$g$$ close to $$f$$

- **_Learning Algorithms_** $$A$$:
  - use $$D$$ to pick a formula $$ g : X \rightarrow Y $$ that approximates $$f$$
  - choose **$$g$$** from set of candidate formula under consideration, which we call hyothesis set **$$H$$**
    - ex) $$H$$ = set of all linear formulas $$\rightarrow$$ choose best linear fit to $$D$$ from this
  - Scenario Example: new customer applies for credit $$\rightarrow$$ bank makes decision
    - based on learned $$g$$, not on $$f$$ (unknown)
    - `if` **_$$g$$ faithfully replicates $$f$$_** $$\rightarrow$$ decision is reasonable (good)
    <details>
      <summary>Visualized</summary>
      <div markdown="1">
      <img src="../DataAnalytics/DataScience/assets/7-example.png" alt="example" style="height: 400px; width: auto;"/>
     </div></details>

## A simple Learning Model

- **_Solution Components_**
  - give a specific learning problem
    - target function $$f$$ (unknown)
    - training examples
    - learning algorithm, hypothesis set
  - **Learning Model** = $$Learning$$ $$Algorithm$$ + $$Hypothesis$$ $$Set$$
- **_Hypothesis Set_** $$H$$:
  - $$H$$ specified through $$h(x)$$ ($$h ∈ H$$)
  - functional form **$$h(x)$$**:
    - gives different weights to different coordinates of $$x$$
    - reflects their relative importance in the credit decision
  - in this example: $$h(x)$$ =linear model
    - $$H$$: set of lines

### Perceptron

- **_Making a Decision_**:

  - weighted coordinates combined to form a 'credit score'
  - resulting score compared to **threshold**

- **_The 'perceptron'_** (using linear model)
  - $$h(x)$$ = $$sign((\sum_{i=1}^dw_ix_i)-threshold)$$
  - = $$sign((\sum_{i=1}^dw_ix_i)+b)$$ `// b = bias`
    - $$sign(s)= \begin{cases} +1, s>0\\-1, ㄴ<0\end{cases}$$ (`s=0 ignored for now`)
    - `must find decision boundary`
  - $$h(x)$$ = $$sign(w^Tx)$$ `simplified version of linear model`
    - different values for parameters $$w_1, w_2, b$$
    - correspond to different lines $$w_1x_1 + w_2x_2+b=0$$
    - for `simplification`: treat bias $$b$$ as weight $$w_0 \equiv b$$
    - introduce artificial coordinate $$x_0=1$$
    - $$w_1x_1 + w_2x_2+w_0x_0 \Rightarrow$$ $$w^Tx  \Rightarrow \sum_{i=0}^d w_ix_i$$
- **_Roles of Learning Algorithm_**
  - search $$H$$ by looking for weights and bias that perform well on dataset
  - produce final hypothesis $$g \in H$$

## PLA

> Perceptron Learning Algorithm

- iterative, guaranteed to converge for linearly seperable

- GOAL: determine optimal **_w_** based on the data to produce
- ASSUME: data set is linearly seperable

- Steps (continued from Perceptron)

  1. perceptron implements $$h(x) \equiv sign(w^Tx)$$, given training set `(x1, y1), ..., (xN, yN)`
  2. PLA picks <cb>misclassified</cb> point
    - $$sign(w^Tx_n)$$ $$\neq y_n$$
    - $$\rightarrow$$ **updates** weight vector $$w \leftarrow w^Tx_n$$
      <img src="../DataAnalytics/DataScience/assets/7-pla.png" alt="example" style="height: 400px; width: auto;"/>
    - $$\Rightarrow$$ rule moves `boundary` in the direction of classifying $$x_n$$ correctly

  3. iterate until no misclassified data
    - iteration `t = 1, 2, ...` pick a misclassified point from `(x1, y1), ..., (xN, yN)` and run PLA iteration on it
    - $$w(t+1)$$ $$\leftarrow w(t) + y_nx_n$$
      <img src="../DataAnalytics/DataScience/assets/7-plaiteration.png" alt="example" style="height: 200px; width: auto;"/>

### Example

```
  You want to predict if movies will be profitable based on their screenplays.
  You hire two critics A and B to read a script you have
  and rate it on a scale 1 to 4.
  The critics are not perfect. Here is the data:
  ---------------------------------------
   #  Movie Name    A     B     Profit?
  ---------------------------------------
   1  Pellet Power  1     1       -
   2  Ghosts!       3     2       +
   3  Pac is Bac    2     4       +
   4  Not a Pizza   3     4       +
   5  Endless Maze  2     3       -
  ---------------------------------------
```

1. First, you want to check the linear separability of data. Plot the data on the 2D plane above, label movies with $$+$$ and $$-$$ and determine.
    <details>
      <summary>Answer</summary>
      <div markdown="1">

        |    +  +
        |    -
        |       +
        |  - 
        ㅡㅡㅡㅡㅡㅡ

    - $$\Rightarrow$$ <cb>Linearly Seperable</cb>
    </div></details>

2. Now decide to use a perceptron to classify you data. Suppose you directly use scores given above as features, together with a bias feature. That is $$f_0 = 1, f_1 =$$ score given by A, $$f_2 = $$ score given by B

  - Run one pass through data with perceptron algorithm, filling out the table below. Go through the data points in order (using data point #1 at step `1`)

  | step |   Weights    |                       Score                       | Correct? |
  | :--: | :----------: | :-----------------------------------------------: | :------: |
  |  1   | [ -1, 0, 0 ] | $$(-1 \cdot 1) + (0 \cdot 1) + (0 \cdot 1) = -1$$ |   yes    |
  |  2   |              |                                                   |          |
  |  3   |              |                                                   |          |
  |  4   |              |                                                   |          |
  |  5   |              |                                                   |          |

  <details>
    <summary>Answer</summary>
    <div markdown="1">
    
    - first x ($$x_0$$) = always 1 (artifical coordinate introduced)

    | step |   Weights    |                       Score                       | Correct? |
    | :--: | :----------: | :-----------------------------------------------: | :------: |
    |  1   | [ -1, 0, 0 ] | $$(-1 \cdot 1) + (0 \cdot 1) + (0 \cdot 1) = -1$$ |   yes    |
    |  2   | [ -1, 0, 0 ] | $$(-1 \cdot 1) + (0 \cdot 3) + (0 \cdot 2) = -1$$ |  ***no***  |
    |  3   | <cb>[  0, 3, 2 ]</cb> | $$( 0 \cdot 1) + (3 \cdot 2) + (2 \cdot 4) = 14$$ |   yes    |
    |  4   | [  0, 3, 2 ] | $$( 0 \cdot 1) + (0 \cdot 3) + (0 \cdot 4) = 17$$ |   yes    |
    |  5   | [  0, 3, 2 ] | $$( 0 \cdot 1) + (0 \cdot 2) + (0 \cdot 3) = 12$$ |  ***no***  |

  - change weight when <cb>incorrect</cb>
    - after `step 2`: weight (`[ -1, 0, 0 ]` )  @ (dot product)  <cb>+</cb>(`[ 1, 3, 2 ]`) = <cb><code>[ 0, 3, 2 ]</code></cb>
    - after `step 5`: weight (`[ 1, 3, 2 ]` )  @ (dot product)  <cb>-</cb>(`[ 1, 2, 3 ]`) = <cb><code>[ 0, 1, -1 ]</code></cb>
  - $$\Rightarrow$$ final weights = `[-1, 1, -1]`

  </div></details>


3. Have weights been learned that separate the data?

  <details>
    <summary>Answer</summary>
    <div markdown="1">
    
    - $$No$$ 
    - with weights `[-1, 1, -1]`, data `point 3` (−1 · 1 + 1 · 2 + −1 · 4 = −3 < 0 ) and `point 4` (−1 · 1 + 1 · 3 + −1 · 4 = −2 < 0 ) will be incorrect
      - step 2's 0 will be counted as positive

  </div></details>

4. Choose scenarios for which a perceptron using the features above can indeed perfectly handle a range of scenarios.
  - (a) Your reviewers are awesome: if the total of their scores is more than 8, then the movie will definitely be profitable, and otherwise it won’t be.
  - (b) Your reviewers are art critics. Your movie will be profitable if and only if each reviewer gives either a score of 2 or a score of 3
  - (c) Your reviewers are art critics. Your movie will be profitable if and only if each reviewer gives either a score of 2 or a score of 3

  <details>
    <summary>Answer</summary>
    <div markdown="1">
    
    - (a) : can classify (considering weights `[-8, 1, 1]`)
    - (b), (c): can't classify

   </div></details>
