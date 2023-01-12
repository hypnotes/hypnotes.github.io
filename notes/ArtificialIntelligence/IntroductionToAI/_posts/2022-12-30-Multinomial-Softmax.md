---
layout: post
title: Mutinomial Softmax Classification
description: >
  DAY 4
# image: /assets/img/blog/example-content-ii.jpg
sitemap: false
permalink: /notes/IntroductionToAI/MultinoialSoftmaxClassification
---

* this list will be replaced by the toc
{:toc .large-only}


## Introduction

|Regression | Classification |
|:----------|:---------------|
| **Linear Regression** :  Exam Score Prediction  |  **Binary Classification** :  Pass/Fail<br/>**Multi-Level (Softmax) Classification** : Letter Grades  |

## Softmax Classification

<br/><img src="../ArtificialIntelligence/IntroductionToAI/assets/4-new.png" alt="linearModel" style="height: 400px; width: auto;"/>
- Where should 🌟 be classified to ? (A, B, or C?)
- only can be answered through Binary (0, 1) BUT you can ask a lot of questions
  - Q1) A or not A;  sig = 0.9 (> 0.5)
  - Q2) B or not B;  sig = 0.4 (< 0.5)
  - Q3) C or not C;  sig = 0.1 (<> 0.5)
  - => classified to 'A' 

- but in case A: 0.9999, B: 0.50001, C: 0.0001, how should we classify? (both A and B passes the threshold)

- **Softmax Classification does not use Thresholds. Instead, only the MAX VALUE is recognized**
  - in case there are two or more same max values, one is picked randomly

<br/><img src="../ArtificialIntelligence/IntroductionToAI/assets/4-ornot.png" alt="A,B,C" style="height: 300px; width: auto;"/>

- instead of doing it three times, put it in matrix and just calculate once 
- find maximum value from (A, B, C)

<br/><img src="../ArtificialIntelligence/IntroductionToAI/assets/4-hotencoding.png" alt="과정" style="height: 300px; width: auto;"/>

- One-Hot Encoding (```argmax```) : change into vector form with one '1.0' 

## Cost Function: CROSS-ENTROPY

| $$S(Y) = \bar Y$$ (model)| **LOG FUNCTION** | $$L=Y$$ (real) |
|:-----:|:-----:|:------:|
|0.7 <br/> 0.2 <br/> 0.1 | $$C(S, L) = - \sum L_i log(S_i)$$ | 1.0 <br/> 0.0 <br/> 0.0 |

### understanding cost function

|L |S|Cost | explained |
|:----|:----|:----|:----|
|          | [1, 0, 0] (=>A) | $$-1 \cdot log1 - 0 \cdot log0 - 0 \cdot log0 = 0 $$| since A is the correct answer, Cost = 0 |
|[1, 0, 0] | [0, 1, 0] (=>B) | $$-1 \cdot log0 - 0 \cdot log1 - 0 \cdot log0 = \infty $$| mismatch between 0, 1 => infinity |
|          | [0, 0, 1] (=>C) | $$-1 \cdot log0 - 0 \cdot log0 - 0 \cdot log1 = \infty $$| same as above|


## PyTorch implementation🔥

<br/><img src="../ArtificialIntelligence/IntroductionToAI/assets/4-vectorrep.png" alt="과정" style="height: 300px; width: auto;"/>


```py
import torch
import torch.nn.functional as F

# Training Data
x_train = torch.FloatTensor([[1,2, 1, 1], [2,1, 3, 2], [3,1,3,4], [4,1, 5, 5], [1,7,5,5], [1,2,5,6], [1,6,6,6], [1,7,7,7]])
y_train = torch.FloatTensor([[0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 1, 0], [0, 1, 0], [0, 1, 0], [1, 0, 0], [1, 0, 0]] )

index_y = torch.argmax(y_train, 1) # takes index position of max value (ex: [0,0,1] => index_y = 2)

W = torch.randn([4,3], requires_grad=True) 
b = torch.randn([3], requires_grad = True)  # 3 biases required
optimizer = torch.optim.SGD([W, b], lr = 0.01) 

def model_SoftmaxClassification(x):
  return F.softmax(torch.matmul(x, W) + b)

for step in range(50000):
  prediction = model_SoftmaxClassification(x_train)
  cost = F.cross_entropy(prediction, index_y)

  optimizer.zero_grad() # 0까지 optimize
  cost.backward()       
  optimizer.step()

x_test = torch.FloatTensor([[1,8,8,8]]) 
model_test = model_SoftmaxClassification(x_test) # returns in form [_, _, _] 
index = torch.argmax(model_test.detach(), 1).item() # max value index 
labels = ['A', 'B', 'C']
print('Model with [1,8,8,8] is', labels[index])
```

> 'Model with [1,8,8,8] is A'