---
layout: post
title: 09 Logistic Regression
description: >

image: ../DataAnalytics/DataScience/assets/9-title.jpg
hide_image: true
sitemap: false
permalink: /notes/DataScience/LogisticRegression
---

- this list will be replaced by the toc
{:toc .large-only}

# Logistic Regression I

## Machine Learning Taxonomy

1. <cb>Supervised Learning</cb> (Labeled Data)
  - **_Regression_** : Quantitative Response <fade>still mostly used for classification...</fade>
  - **_Classification_** : Categorical Response

2. Unsupervised Learning (Unlabeled Data)
  - **_Dimensionality Reduction_**
  - **_Clustering_**

3. Reinforcement Learning (Reward) <fade>Alpha Go</fade>
  - Learning Paradigm: use of **??data** to uncover an underlying process

### Supervised Learning

- most studied and utilized
- training data contains explicit examples of what the **??output** should be for given inputs $$\rightarrow Supervised$$
  - correct label exists
- Typical Supervised Learning Procedure

<img src="../DataAnalytics/DataScience/assets/9-supervised.png" alt="supervised" style="height: 300px; width: auto;"/>

### Unsupervised Learning

- no output information for training data
  - instead, we get **??truth values** $$\Rightarrow$$ just given input examples
- Approaches:
  - Clustering (K-Means, mixutre models, heirarchical)
  - Hidden Markove Models (HMMs)
  - Feature Extraction (PCA, iCA, SVD)
- spontaneously finding **??patterns** in input data <fade> like categorization</fade>
- precursor to supervised learning
- way to create higher-level represtation of data <fade> like automated feature extraction </fade>

### Reinforcement Learning

- when training data contain no correct output for each input (no longer supervised)
- example: toddler learning not to touch a hot cup of tea
  - training examples do not say what to do, still uses examples to reinforce better actions
  - $$\Rightarrow$$ learns what one should do in similar situations
- training example의 target ouput X, but contains <cb>some possible output + measure of how good</cb>

<details>
  <summary>Supervised vs Unsupervised Example</summary>
  <div markdown="1">

- supervised
  <img src="../DataAnalytics/DataScience/assets/9-supervisedexample.png" alt="supervised" style="height: 300px; width: auto;"/>
- unsupervised
<img src="../DataAnalytics/DataScience/assets/9-unsupervisedexample.png" alt="supervised" style="height: 300px; width: auto;"/>
</div></details>

## Introduction

- Core of Linear Models
  - signal $$s = w^Tx$$ : combines input variables linearly
- Linear Regression
  - $$signal = output$$ for predicting real (unbounded) response
- Linear Classification
  - $$signal = threshold$$ at zero to preduce $$\pm 1$$ output, for binary decision
- **_Logistic Regression_** aka _Soft_ binary classification
  - example: Heart attack precision <fade>based on cholesterol lvl, blood pressure, age, weight...</fade>
    - 확실하게 예측은 불가능, but can predict **_how likely it is_**
  - binary decision (0 or 1) 보다 더 정교 $$\rightarrow$$ 0 ~ 1 <fade>closer to 1 -> more likely to get 심장마비</fade>
  - $$\Rightarrow$$ output: <cb>real</cb> (like regression) <cb>but bounded</cb> (like classification)
  - uncertain 가능
  - more appropriate than linear regression (no negative values)
  - <img src="../DataAnalytics/DataScience/assets/9-logistic.jpg" alt="logistic" style="height: 300px; width: auto;"/>

## Predicting Probability

### Logistic Regression Model

- Linear Classification: hard threshold on signal $$s=w^Tx$$
- $$h(x) = sign(w^Tx)$$
- Linear Regression: no threshold
- $$h(x) = w^Tx$$
- <cb>Logistic Regression</cb> <fade> between linear classification & regression </fade>
- $$h(x) = \theta(w^Tx)$$

- $$\theta$$ : aka _logistic_ function, _Sigmoid_ function, _soft threshold_

### Logistic Function θ

- definition: for $$-\infty < s < \infty$$ :
- $$\theta(s) = \frac{e^s}{1+e^s} = \frac{1}{1+e^{-s}}$$

<details>
  <summary>Proof</summary>
  <div markdown="1">

- $$1-\theta(s) = 1- \frac{1}{1+e^{-s}} = \frac{e^{-s}}{1+e^{-s}} = \theta(-s)$$
- $$\theta(s) = P(+1 \mid x)$$
- $$P(-1\mid x) = 1-\theta(s) = \theta(-s)$$

 </div></details>

- output lies between 0 and 1 <fade>can be interpreted as probability for binary events</fade>

  - <img src="../DataAnalytics/DataScience/assets/9-sigmoid.png" alt="sigmoid" style="height: 300px; width: auto;"/>

- $$\theta(s)$$ : can define error measure, has computational advantage

### Summary of Linear Models

- based on "**_signal_**" $$s = \sum_{i=1}^dw_ix_i$$

<details>
  <summary>Hyperbolic Tangent (another popular sigmoid)</summary>
  <div markdown="1">

- $$tanh(s)=\frac{e^s-e^{-s}}{e^s+e^{-s}}$$
- <img src="../DataAnalytics/DataScience/assets/9-tanh.png" alt="tanh" style="height: 300px; width: auto;"/>
- properties- $$tanh(s)$$ convergence:
  - large $$\mid s $$ : hard threshold
  - small $$\mid s $$ : no threshold

 </div></details>

<img src="../DataAnalytics/DataScience/assets/9-linearsummary.png" alt="linearsummary" style="height: 300px; width: auto;"/>

- example for heart attack:
  - input x: cholesterol level, age, weight, etc..
  - signal s = $$w^Tx$$ : _risk score_
  - **_Linear Classification_**: h(x) returns $$\pm 1$$: heart attack (+1) or not (-1) **for sure**
  - **_Linear Regression_**: h(x) returns risk score $$s$$
  - **_Logistic Regression_**: h(x) returns $$\theta(x)$$: probability of heart attack

## Cross-entropy Error Measure

### Learning Target of Logistic Reg

$$ f(x) = \mathbb P [y= +1 \mid x] $$

- <fade>ex : probability of heart attack given patient characteristics</fade>
- training data doesn't give us value of $$f$$, rather, **gives us _samples_ generated by this probability** $$(+1 / -1)$$

### Fitting

- <cb>Fitting</cb> : finiding a good $$h$$
- $$ h$$ is good if $$\begin{cases} h(x_n) \approx 1 & y_n = +1 \\ h(x_n) \approx 0 & y_n = -1 \end{cases}$$

- MSE works for linear models only, since it can fall into a local minimum <img src="../DataAnalytics/DataScience/assets/9-mse.png" alt="mse" style="height: 200px; width: auto;"/>

  - if in the yellow area, it will get stuck and will not converge into local minimum

- $$\Rightarrow$$ use <cb>Cross-Entropy</cb> error measure

$$
E_{in}(w) = \frac{1}{N}\sum_{n=1}^{N}ln(1+e^{-y_nw^Tx_n})
$$

- easier to do gradient-based optimization
- $$y_n = +1 $$ encourages $$w^Tx_n >> 0 \longrightarrow \theta(w^Tx_n) \approx 1 $$ (and vice versa) <img src="../DataAnalytics/DataScience/assets/9-ln.png" alt="mse" style="height: 200px; width: auto;"/>

### Error Measure

- based on <cb>likelihood</cb>

  > how **_likely_** is it to get output $$y$$ from input **X**

- recall:

  - $$ h(x)$$ = $$\theta(w^x)$$
  - $$ \theta(s)$$ =$$ \frac{e^s}{1+e^s} $$
  - $$ 1-\theta(s) $$= $$\theta(-s)$$

  $$
  P(y \mid x) = \begin{cases} h(x) & ,y = +1 & = \theta(w^Tx) \\ 1- h(x_n) &,y= -1 & = \theta(-w^Tx)  \end{cases} \hspace{0.5cm} = \hspace{0.5cm} \theta(yw^Tx)
  $$

  <details>
  <summary> PROOF </summary>
  <div markdown="1">

  - $$P(+1 \mid x)$$ = $$h(x) = \theta(w^Tx)=\frac{1}{1+exp(-w^Tx)}$$
  - $$P(-1 \mid x)$$ = $$1-h(x) = 1-\theta(w^Tx)$$
    - 1- $$\frac{1}{1+exp(-w^Tx)}$$
    - $$ \frac{exp(-w^Tx)}{1+ exp(-w^Tx)}$$
    - $$\Rightarrow$$ $$\theta(-w^Tx)$$

  </div></details>

### Criterion for choosing h: maximum likelihood

- $$\Rightarrow$$ select hypothesis $$h$$ that **_maximizes_** this probability

  - $$P(y_1\mid x_1)P(y_1\mid x_2)\cdots P(y_N\mid x_N) \Longrightarrow \Pi_{n=1}^{N} P(y_n\mid x_n)$$
  - getting all $$y_n$$'s from corresponding $$x_n$$'s

- we can easily **_optimize/minimize_** if we change the maximum likelihood into log form

  - $$-\frac{1}{N}ln(\Pi_{n=1}^{N}  P(y_n \mid x_n)) = \frac{1}{N} \sum_{n=1}^N ln\frac{1}{P(y_n \mid x_n)}$$
  - $$\Rightarrow$$ negative log likelihood
  - $$-\frac{1}{N}ln(\cdot)$$ <fade> = monotonically decreasing function</fade>

- $$\frac{1}{N} \sum_{n=1}^N ln\frac{1}{\theta(yw^Tx)} $$

  - $$\frac{1}{N} \sum_{n=1}^N ln\begin{cases} h(x_n) & y_n = +1 \\ 1- h(x_n) & y_n = -1 \end{cases}$$

  - $$ \frac{1}{N} \sum_{n=1}^N {[\![ y_n = +1]\!] ln\frac{1}{h(x_n)} + [\![ y_n = -1]\!] ln\frac{1}{1-h(x_n)}}$$

- back to $$E_{in}(w) = \frac{1}{N}\sum_{n=1}^{N}ln(1+e^{y_nw^Tx_n})$$
  <details>
  <summary>Proof</summary>
  <div markdown="1">

  - substituting $$\theta(yw^Tx)$$, $$ \frac{1}{N} \sum_{n=1}^N ln\frac{1}{\frac{e^{yw^Tx}}{1+e^{yw^Tx}}} $$
  - = $$\frac{1}{N} \sum_{n=1}^N ln\frac{1+e^{yw^Tx}}{e^{yw^Tx}}$$
  - = $$\frac{1}{N} \sum_{n=1}^N ln (1+e^{yw^Tx}) \cdot (e^{-yw^Tx})$$
  - $$ \frac{1}{N} \sum_{n=1}^N ln (1+e^{-yw^Tx})$$
  - since $$e^0 = 1 $$
  - <img src="../DataAnalytics/DataScience/assets/9-equations.png" alt="equations" style="height: 200px; width: auto;"/>

  </div></details>

- Practice Questions

  1. Select the expression that describes the odds ration $$\frac{P(Y=1\mid X)}{P(Y=0\mid X)}$$ of a logistic regression model. Recall: $$ P(Y=0\mid X) + {P(Y=1\mid X)} = 1 $$ for any $$X$$ and $$\theta(s) = \frac{1}{1+exp(-s)}$$
  - (a) $$X^Tw$$
  - (b) $$-X^Tw$$
  - (c) $$exp(X^Tw)$$
  - (d) $$\theta(X^Tw)$$
  - (e) None of these

  2. Select the expression that describes $$P(Y=0\mid X)$$ for a logistic regression model.
  - (a) $$\theta(-X^Tw)$$
  - (b) $$1-log(1+exp(X^Tw))$$
  - (c) $$1+log(1+exp(X^Tw))$$
  - (d) None of these

  <details>
    <summary>Answer</summary>
    <div markdown="1">

      1. (c)
      2. (a)

    </div></details>

### Training via Gradient Descent

- update rule: $$w(t+1) = w(t) - \alpha \nabla E_{in}(w(t))$$
  - $$\alpha$$: learning rate (step size)
  - $$E_{in}$$: Training error
  - examine all examples at each iteration: $$O(N)$$
  - stochastic gradient descent : $$O(1)$$
- Least Mean Square (LMS) rule (Windrow-Hoff learning rule)
  - when the cost function is mean squared error
  - $$w$$: = $$w - \alpha \nabla E_{in}(w)$$
  - = $$w + \alpha (y-w^Tx)\cdot x$$
    - $$(y-w^Tx)$$ : error
    - $$x$$ : input

## Logistic Regression Algorithm

1. intialize weights at time step t=0 to w(0)
2. **for** t = 0,1,2...**do**
3. $$\hspace{1cm}$$compute the gradient
  - $$ \nabla E_{in}(w(t)) = \frac{1}{N}\sum_{n=1}^N \frac{y_nx_n}{1+e^{y_nw^T(t)x_n}} $$

4. $$\hspace{1cm}$$ set the direction to move: $$v_t = - \nabla E_{in}(w(t))$$
5. $$\hspace{1cm}$$ update weights: $$w(t+1) = w(t) + \alpha(v_t)$$
6. $$\hspace{1cm}$$ iterate to next step until it is time to stop
7. return final weights **w**

- we have to choose 2 things:
  1. initial weights **w(0)**
  2. criterion for **stopping** gradient descent

### Initialization Criterion

1. w(0) = <cb>0</cb>
  - works pretty well for logistic regressions

2. w(0) = <cb>random</cb>
  - more common, avoid getting stuck on perfectly symmetric hilltop
    <img src="../DataAnalytics/DataScience/assets/9-hilltop.jpg" alt="hilltop" style="height: 200px; width: auto;"/>

3. choose **_each weight independently from normal distribution_** with zero mean and small variance
  - used pratically

### Stopping

1. set <cb>upper bound</cb> on **_number of iterations_**
  - PROBLEM: final weight quality not guaranteed

2. check <cb>gradient</cb> ($$\nabla E_{in}(w(t))$$) <cb>under threshold</cb> <fade>whenver loss function became too small</fade>
  - PROBLEM: eventually must happen, but don't know when
  - PROBLEM 2: relying soley on size of gradient **might stop too soon**
    <img src="../DataAnalytics/DataScience/assets/9-toosoon.png" alt="toosoon" style="height: 200px; width: auto;"/>

3. require <cb>both</cb>:
  - (i): **change** in error is small
  - (ii): error **itself** is small
  - logistic regression: (1) + (2) works well
    - <fade>(1) large upper bound for number of iterations</fade>
    - <fade>(2) small lower bound for the size of gradient</fade>
  - ultimately, (1) + (2) + (3) is good

<details>
  <summary>SUMMARY</summary>
  <div markdown="1">

  <img src="../DataAnalytics/DataScience/assets/9-summary1.png" alt="summary1" style="height: 300px; width: auto;"/>
  <img src="../DataAnalytics/DataScience/assets/9-summary2.png" alt="summary2" style="height: 300px; width: auto;"/>
  <img src="../DataAnalytics/DataScience/assets/9-summary3.png" alt="summary3" style="height: 300px; width: auto;"/>
 </div></details>

# Logistic Regression II

## Thresholding

- outputs of Logistic Regression : <cb>continous</cb>
- **_Logistic Regression + Decision Rule = Classification_**
- **Decision Rule** outputs 1 or 0 (depending on <cb>threshold</cb>)

  - ex: $$ T = 0.5$$
  - $$ classify(x) = \begin{cases} 1, & P(Y=1\mid x)>= 0.5 \\ 0, & P(Y=1 \mid x) < 0.5 \end{cases} $$

  <img src="../DataAnalytics/DataScience/assets/9-thresholds.png" alt="thresholds" style="height: 300px; width: auto;"/>

- widely used in **object detection**

<details>
  <summary>Thresholds for higher dimensions: also works fine</summary>
  <div markdown="1">

  <img src="../DataAnalytics/DataScience/assets/9-higherdim.png" alt="summary1" style="height: 300px; width: auto;"/>
  </div></details>

## Evaluation Metrics

### Accuracy

$$accuracy = \frac{ points \hspace{0.1cm} classified  \hspace{0.1cm} correctly }{ total  \hspace{0.1cm} points}$$

- **Pitfalls** of Accuracy (Spam/Ham Classification)
  - 100 emails, `5 = spam`, `95 = ham`, model classifies every email as ham
  - accuracy : `95%` ($$\frac{95}{95+5}%$$) $$\Rightarrow$$ is it good enough?
    - `NO`: detecting spam email = `0%`

### Classification Errors

<div style="display: inline">
  <img src="../DataAnalytics/DataScience/assets/9-classerror.png" alt="classerror" style="height: 300px; width: auto;"/>
  <img src="../DataAnalytics/DataScience/assets/9-matrix.png" alt="matrix" style="height: 300px; width: auto;"/>
</div>

- **True Positives**: correctly classified as positive
- **True Negatives**: correctly classified as negative
- **False Positives**: Mistakenly detected as positive (**false alarm**)
- **False Negatives**: Failed to Detect

### Precision and Recall

$$accuracy = \frac{TP + TN}{n} $$

- What proportions of points did our classifier classify correctly?
  - doesn't tell full story, especially in cases with high class imbalance
  - 정확도

$$precision = \frac{TP}{TP+FP} $$

- Of all observations that were predicted to be 1, what proportion were actually 1?
  - how precise is our classifier? Penalizes false positives
  - 1으로 분류된 애들 중, 실제 1인 퍼센티지

$$recall = \frac{TP}{TP+FN} $$

- Of all observations that were actually 1, what proprtion did we predict to be one?

  - How good is our classifier at detecting positives? Penalizes false negatives
  - 실제로 1인 애들 중, 1으로 분류된 퍼센티지

- Filtering Spam Mails:
  - 100 emails, `5 = spam`, `95 = ham`, model classifies every email as ham
  - $$TP = 0$$ , $$FP = 0$$ , $$TN=95$$, $$FN=5$$
  - accuracy : `95%` ($$\frac{95}{95+5}%$$)
  - precision: `undefined` ($$\frac{0}{0+0}%$$)
  - recall: `0%` ($$\frac{0}{0+5}%$$)
  - $$\rightarrow$$ accuracy does not tell full story
  - $$\Rightarrow$$ **Class Imbalance**: distribution of true observation is **_skewed_** (`95%` of true observations are negative)

**_Trade-off between precision and recall_**

- **`100%` recall** : making ALL classifier output "1"
  - no False Negatives, but many False Postives $$\longrightarrow$$ precision low
- $$\Rightarrow$$ Precision and Recall inversly related
- adjusting classification threshold

  - <cb>higher</cb> **threshold** : $$\longrightarrow$$ fewer FP, Larger Precision
  - <cb>lower</cb> **threshold** : $$\longrightarrow$$ fewer FN, Larger Recall

***Questions***: 
- In each of the following cases, what would we want to maximize: precision, recall, or accuracy?

<details>
 <summary>1. Predicting whether or not a patient has some disease</summary>
 <div markdown="1">

  - Maximize **RECALL** : if they are told to have disease $$\rightarrow$$ further testing
  - better than leaving them untreated

  </div></details>
<details>
  <summary>2. Determining whether or not someone should be sentenced to life in prison.</summary>
  <div markdown="1">
  
  - Maximize **PRECISION** : don't want to sentence guilty people ??????????
  </div></details>
<details>
  <summary>3. Determining if an email is spam or ham</summary>
  <div markdown="1">
  
  - Maximize **Accuracy** : (subjective) having spam emails ending up at inbox, or hams being filter out 중 택1
  </div></details>

### Metrics

**Accuracy vs. threshold**
- threshold $$\uparrow$$ $$\longrightarrow$$ **Larger** FN
- threshold $$\downarrow$$ $$\longrightarrow$$ **Larger** FP
- also, accuracy is maximized doesn't always mean $$T$$ = `0.5` 

**Precision vs. threshold**
- threshold $$\uparrow$$ $$\longrightarrow$$ **Fewer** FP
- $$\Rightarrow$$ precision increase
- $$precision$$ = $$\frac{TP}{TP+FP} = \frac{TP}{predicted \hspace{0.1cm}true} $$

**Recall vs. threshold**
- threshold $$\uparrow$$ $$\longrightarrow$$ **Larger** FN
- $$\Rightarrow$$ recall decrease
- $$Recall$$ = $$\frac{TP}{TP+FN} = \frac{TP}{Actually \hspace{0.1cm}true} $$

**Accuracy, Precision, Recall**

<div style="display: inline">
  <img src="../DataAnalytics/DataScience/assets/9-accuracy.png" alt="classerror" style="height: 150px; width: auto;"/>
  <img src="../DataAnalytics/DataScience/assets/9-precision.png" alt="matrix" style="height: 150px; width: auto;"/>
  <img src="../DataAnalytics/DataScience/assets/9-recall.png" alt="matrix" style="height: 150px; width: auto;"/>
</div>

**Precision Recall Curves**

<div style="display: inline">

  <img src="../DataAnalytics/DataScience/assets/9-prcurve.png" alt="matrix" style="height: 150px; width: auto;"/>
  <img src="../DataAnalytics/DataScience/assets/9-perfect.png" alt="matrix" style="height: 150px; width: auto;"/>
</div>

- threshold decrease: top left $$\longrightarrow$$ bottom right
- **Perfect Classifier**: precision = 1, recall = 1
  - PR curve to be at top right of graph
- **Area Under Curve** (AUC): optimal = 1 <fade>ROC more common</fade>

**Other Metrics**
- **False Positive Rate** (FPR):
  - $$\frac{FP}{FP+TN} \longrightarrow$$ what proportion of innocent ppl did I convict? 
- **True Positive Rate** (TPR):
  - $$\frac{TP}{TP+FN} \longrightarrow$$ what proportion of guilty ppl did I convict? $$\Rightarrow$$ RECALL

**ROC Curves** <fade>Receiver Operating Characteristics</fade>

<div style="display: inline">

  <img src="../DataAnalytics/DataScience/assets/9-roc.png" alt="roc" style="height: 150px; width: auto;"/>
  <img src="../DataAnalytics/DataScience/assets/9-perfectroc.png" alt="roc" style="height: 150px; width: auto;"/>
</div>

- plots `TPR` vs `FPR` 
- threshold $$\uparrow$$ $$\longrightarrow$$ `TPR` & `FPR` **decrease**
  - decreased `TPR` = bad (detecting fewer positives)
  - decreased `FPR` = good (fewer false positives)
  - $$\Rightarrow$$ Tradeoff
- **Perfect classifier**: `TPR`=1, `FPR` = 0, top-left
  - best possible AUC = 1
  - terrible AUC = 0.5 (randomly guessing)
  - model's AUC [0.5~1]

## Feature Engineering

> the process of **transforming raw features** into more **informative features** 

<img src="../DataAnalytics/DataScience/assets/9-feature.jpg" alt="feature" style="height: 300px; width: auto;"/>
  
  - <fade> 10년 전에 자주 사용한 기법, 이제는 DL 로 대체 </fade>

- enables to: 
  - **caputure domain knowledge**
  - **express non-linear relationships** using simple linear models
  - **encode non-numeric features** to be used as inputs to models 

$$\hat y=f_{\theta}(x) = \sum^p_{j=0}\phi (x)_j\theta _j $$

<img src="../DataAnalytics/DataScience/assets/9-phi.png" alt="phi" style="height: 200px; width: auto;"/>

- use $$\phi$$ to transform features

### Feature Functions Examples

- **Constant Feature Function**: adding another vector as <cb>bias term</cb>
  - <img src="../DataAnalytics/DataScience/assets/9-constant.png" alt="constant" style="height: 200px; width: auto;"/>
  - aka constant feature, offset, intercept term, bias

- **Modeling Non-linear Relationships**
  - <cb>apply non-linear function</cb> (like $$sin()$$) $$\Rightarrow$$ may be easier to optimize 
  - $$f_{\theta}(x) = \theta _0 +  \theta _1 x_1 +  \theta _2 x_2 +  \theta _3sin(x_1+x_2) $$ 
  
  <img src="../DataAnalytics/DataScience/assets/9-nonlinear.png" alt="constant" style="height: 200px; width: auto;"/>

<img src="../DataAnalytics/DataScience/assets/9-data.png" alt="constant" style="height: 200px; width: auto;"/>

- cannot use $$X$$ and $$Y$$ in linear model because of text, categorical data, missing values ...etc

#### Basic Transformations

1. Uninformative Features: <fade>like `UID`</fade>
  - $$transformation$$: ***Remove*** 

2. Quantitative Features  <fade>like `Age`</fade>
  - $$transformation$$: may ***apply non-linear transformations***  <fade>like Log</fade>
  - $$transformation$$:  ***Normalize/Standardize***  <fade>like (x-mean)/stdev<fade>
3. Categorical Features  <fade>like `State`</fade>
  - simply assiging values <fade>(Alalbama=1, .., Utah=30)</fade> may indicate that those values have meaning (order / magnitude) NOT PREFERABLE
  - $$transformation$$:  ***One-hot-Encode***

4. Missing Values
  - Quantitative:
    1. estimate and fill in (tricky) <fade>like substituting mean </fade>
    2. add another feature (boolean) named `missing_col_name` 
      - sometimes missing data can be a signal
    
  - Categorical: (2) above (add additional category)

**One hot Encoding** (Dummy Encoding)
<img src="../DataAnalytics/DataScience/assets/9-encoding.png" alt="constant" style="height: 300px; width: auto;"/>

**Bag of Words Encoding**
<img src="../DataAnalytics/DataScience/assets/9-bag.png" alt="constant" style="height: 100px; width: auto;"/>

- **bag**: **multiset** (unordered collection which may contain multiple instance of each element)
- stopwords typically removed 
- problems: 
  - too long and **inefficient** (high dimension but sparse)
  - word order information lost (no context) $$\Longrightarrow$$ `N-gram`
  - new unseen words dropped $$\Longrightarrow$$ add `unkown_column` for counting unseen words

**N-Gram Encoding** 
- when word order matters 
- problem: further inefficiency problem 

### Wrap up
- feature transformations to ***capture domain knowledge***
  - introduces additional infromation 

- bag of words can be used in autocompletion 

<img src="../DataAnalytics/DataScience/assets/9-autofinish.png" alt="autocompletion" style="height: 400px; width: auto;"/>

- Feature Engineering Problems
  - redundant features
  - too many features
  - overfitting
