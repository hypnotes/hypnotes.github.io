---
layout: post
title: 12 Decision Trees
description: >

#image: ../DataAnalytics/DataScience/assets/10-title.jpg
hide_image: true
sitemap: false
permalink: /notes/DataScience/DecisionTrees
---

- this list will be replaced by the toc
{:toc .large-only}

## Introduction

- **non-linear Classifiers**
  - non-linear decision boundary: add 'non-linear' features to linear model <fade>ex: logistic reg</fade>
  - use non-linear learners <fade>ex: nearest neighbors, decision trees, neural nets</fade>
  - K-Nearest Neighbor Classifier: 
    - simple, often a good baseline
    - Can approximate arbitrary boundary: non-parametric
    - Disadvantage: stores all data

- **Decision Tree**: ***a tree of questions*** that must be answered in sequence to yield predicted classification

  - <img src="../DataAnalytics/DataScience/assets/12-dectree.png" alt="nestrov" style="height: 300px; width: auto;"/>
  - $$ Y = (A\land B) \lor (\lnot A \land C)$$ ((A and B) or (not A and C)) 
  - one of the most **intuitive** classifer, easy to understand & construct
  - 놀랍게도 굉장히 잘 된다

- **Structure of Decision Tree**
  - **internal nodes**: attributes (features)
  - **Leafs**: classification outcome
  - **Edges**: assignment

- Example: Logistic Regression using petal data
<div style="display: inline">
  <img src="../DataAnalytics/DataScience/assets/12-petal.png" alt="nestrov" style="height: 200px; width: auto;"/>
  <img src="../DataAnalytics/DataScience/assets/12-logpetal.png" alt="nestrov" style="height: 200px; width: auto;"/>
</div>
  
  - logistic regression = linear $$\Rightarrow$$ linear decision boundaries 

## Decision Tree Basics

<img src="../DataAnalytics/DataScience/assets/12-treeiter.gif" alt="nestrov" style="height: 400px; width: auto;"/>

- seems good, gets every point correctly
- might result in overfitting

## Decision Tree Generation

### Traditional Algorithm
- all data starts in root node
- ***repeat*** until every node is either **pure**(one type) or **unsplittable** (duplicate but not splittable)
  1. pick **best feature** $$x$$, **best split value** β <fade>( x = petal_length, β = 2 )</fade>
  2. **Split Data into 2 nodes** ( x < β, x >= β )
- Learning Smallest (simplest) decision Tree : `NP-complete` (existing algorithms exponential)
- Use <cb>Greedy</cb> Hueristics
  - start with empty tree $$\rightarrow$$ choose next best attribute $$\rightarrow$$ recurse $$\circlearrowleft$$

- **Defining Best Feature**
<img src="../DataAnalytics/DataScience/assets/12-bestfeature.gif" alt="nestrov" style="height: 200px; width: auto;"/>

### Node Entropy 

$$
node \hspace{0.1cm} entropy\hspace{0.1cm}  S = -\sum _c p_c log_2p_c
$$

<img src="../DataAnalytics/DataScience/assets/12-entropy.png" alt="entropy" style="height: 200px; width: auto;"/>

- Entropy of Root Node
  - $$p_0= $$ $$\frac{34}{110} = 0.31$$
  - $$p_1= $$ $$\frac{36}{110} = 0.33$$
  - $$p_2= $$ $$\frac{40}{110} = 0.36$$
  - $$S =$$ $$ -(0.31 log_2(0.31)) -(0.33 log_2(0.33))-(0.36 log_2(0.36))$$
  - <span style="color: #b08adf">$$S = 1.58$$</span>

- Entropy = ***혼란도***: how unpredictable a node is
  - **LOW** Entropy: more predictable $$\Rightarrow$$ Good!
  - **HIGH** Entropy: more unpredictble

- Entropy: [0, 1]
  - **0 Entropy**: data all in one class ($$-1log_2(1)=0$$)
    - ex: `[ 34, 0, 0 ]` $$\rightarrow p_0 = \frac{34}{34} = 1$$
    - $$-1 log_2 (1) = $$ <span style="color: #b08adf">$$0$$</span>
    
  - **1 Entropy**: data evenly split between ***2*** classes
    - ex: `[ 4, 4 ]` $$\rightarrow  p_0 = \frac{4}{8} = 0.5$$, $$ p_1 = \frac{4}{8} = 0.5 $$
    - $$-0.5 log_2 (0.5) -0.5 log_2 (0.5) = $$ <span style="color: #b08adf">$$1$$</span>
  - **1.58 Entropy**: split evenly into 3 classes
    - ex: `[ 4, 4, 4 ]` $$\rightarrow  p_0 = p_1 = p_2 = \frac{4}{12} = 0.33 $$
      - $$3 \times -0.33 log_2 (0.33) = $$ <span style="color: #b08adf">$$1.58$$</span>
  - $$\Rightarrow$$ data evenly split between <span style="color: #b08adf">$$C$$</span> classes
    - $$C \cdot (\frac{1}{C}log_2(\frac{1}{C})) = -log_2(\frac{1}{C}) =$$ <span style="color: #b08adf">$$log_2(C)$$ </span>

- **Weighted Entropy as a Loss Function**
  - use it to decide hich split to take
  - given 2 nodes ($$X, Y$$) with each $$N_1, N_2$$ samples: 
    - $$L=\frac{N_1S(X)+N_2S(Y)}{N_1+N_2}$$
    - $$\Longrightarrow$$ MIDTERM
- **Defining Best Feature**
  - Choice #1: `width > 1.5`, child node entropies: $$entropy([50,46,2])=1.16$$, $$entropy([4,47])=0.4$$
    - **Weighted Average**: $$\frac{99}{150}*1.16 + \frac{51}{150}*0.4$$ <span style="color: #b08adf">$$log_2(C)0.9$$ </span>
    - <img src="../DataAnalytics/DataScience/assets/12-step1.png" alt="step1" style="height: 200px; width: auto;"/>
  - Choice #2: `length > 4`, child node entropies: $$entropy([50,9])=0.62$$, $$entropy([41,50])=0.99$$
    - **Weighted Average**:<span style="color: #b08adf">$$0.84$$ </span> $$\Rightarrow$$ **Better than choice (1)**
    - <img src="../DataAnalytics/DataScience/assets/12-step2.png" alt="step1" style="height: 200px; width: auto;"/>
  - Choice #3: `width > 0.5`, child node entropies: $$entropy([2,50,50])=1.12$$, $$entropy([48])=0$$
    - **Weighted Average**:<span style="color: #b08adf">$$0.76$$ </span> $$\Rightarrow$$ **Better than choice (2)**
    - <img src="../DataAnalytics/DataScience/assets/12-step3.png" alt="step1" style="height: 200px; width: auto;"/>
  - Choice #4: `width > 0.9`, child node entropies: $$entropy([50,50])=0.1$$, $$entropy([50])=0$$
    - **Weighted Average**:<span style="color: #b08adf">$$0.66$$ </span> $$\Rightarrow$$ **Better than choice (3)**
    - <img src="../DataAnalytics/DataScience/assets/12-step4.png" alt="step1" style="height: 200px; width: auto;"/>

- $$\Rightarrow$$ Traditional Decision Tree Generation Algorithm has overfitting issues

## Restricting Decision Tree Complexity

- Approaches Explained

1. Preventing Growth: set one or more special ***rules*** to prevent growth
  - ex: don't split nodes if <span style="color: #b08adf">`<1%` </span>of sample
  - ex: don't allow depth more than <span style="color: #b08adf">`7 levels` </span>
  - Choosing <span style="color: #b08adf">`hyperparameters` </span>?

2. Pruning: Let trees grow fully, then cut off less usefuly branches 
  - set **validation set** before creating tree
  - if replacing node by its most common prediction has no impact on validation error, **don't split node**

  - <img src="../DataAnalytics/DataScience/assets/12-pruning.png" alt="step1" style="height: 200px; width: auto;"/>
  - if (1) and (2) does not have significan difference, prune

## Random Forests

- fully grown trees: almost always overfit data
  - low model bias, high model variance
  - $$\Rightarrow$$ small changes in dataset $$\rightarrow$$ very different decision tree

  <details>
    <summary>Example</summary>
    <div markdown="1">
    <img src="../DataAnalytics/DataScience/assets/12-randomforest.png" alt="step1" style="height: 300px; width: auto;"/>

  </div></details>

- Random Forest Idea: **Build many decision tress and vote**

<img src="../DataAnalytics/DataScience/assets/12-vote.png" alt="step1" style="height: 300px; width: auto;"/>

- 6 votes orange : 3 votes green $$\Rightarrow$$ **ORANGE**

### Bagging
- Bootstrap AGGregatING

<img src="../DataAnalytics/DataScience/assets/12-bagging.png" alt="bagging" style="height: 300px; width: auto;"/>

- but bagging not enough to reduce model variance 
  - decision trees look very similar to each other
  - <fade>one strong feature always used for first split</fade>
  - <img src="../DataAnalytics/DataScience/assets/12-dectree2.png" alt="bagging" style="height: 300px; width: auto;"/>
  - $$\Rightarrow$$ ***only use a sample of $$m$$ features at each split***
    - usually $$m=\sqrt{p}$$ for decision trees in classification ($$p$$: # of features)
    - algorithm creates individual trees, each overfit in different way $$\Longrightarrow$$ 기대효과: overall forest has low variance

### Random Forest Algorithm

- 2 hyperparameters: **T** and $$m$$ 

1. Bootstrap training data **T** times. Fit decision tree each resample by:
  - start with data in one node (until all nodes are pure)
  - pick impure node
  - pick random subset of $$m$$ features $$\rightarrow$$ pick best feature $$x$$ and split value β  so that split loss is minimized <fade>(ex: x = petal_width, β = 0.8 => L=0.66)</fade>
  - split data into 2 nodes (x < β, x ≥ β)
2. [predict] ask **T** decision trees for prediction and take majority vote

- preventing growth, pruning, random forest $$\Rightarrow heuristics$$
  - not provably best/mathematically optimal 
  - 그저 sounded good, implemented, worked well

- Why we use Random Forests
  1. Versatile (regression & classification 가능)
  2. Invariant to feature scaling and translation
  3. Automatic feature selection
  4. Nonlienar decision boundaries without complicated feature engineering
  5. 다른 nonlinear model보다 overfit 심하진 않음
  6. Example of **ensemble method**: combine knowledge of many simple models to create sophisticated model
  7. Example of **bootstrap**: reduce model variance
- Provide alternate non-linear framework for classification & regression
  1. overfitting probability high
  2. boundaries can be more complex
  3. underlying principle fundamentally different 