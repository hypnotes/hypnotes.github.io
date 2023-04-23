---
layout: post
title: 05 Visualization
description: >

image: ../DataAnalytics/DataScience/assets/5-title.png
hide_image: true
sitemap: false
permalink: /notes/DataScience/Visualization
---

- this list will be replaced by the toc
{:toc .large-only}

## Introduction

- <cb>Visualization</cb>

  > use of computer-generated, interactive, visual representations of data to **_amplify cognition_**
  > finding **_artificial memory_** that best supports our natural means of **_perception_**

- visualizations are for humans (take advantage of human visual perception system)

<details>
  <summary>Visualize, then quantify! </summary>
  <div markdown="1">
  
  <img src="../DataAnalytics/DataScience/assets/5-dataset.png" 
  alt="dataset" style="height: 200px; width: auto;"/>
  
  - all four dataset have the ***same mean***, standard deviations, and correlation $$\rightarrow$$ same regression line!

  <img src="../DataAnalytics/DataScience/assets/5-example.png" alt="example" style="height: 400px; width: auto;"/>

- yet their graph look very different
- $$\Rightarrow$$ **_Visualization complements statistics_**

 </div></details>

- Goal of Data Visualization

1. To help your own understanding of data/results
  - key part of EDA, useful throughout modeling

2. To communicate results/conclusions to others
  - minimize explanations

3. Inform human decisions 
  - every visualizations have tradeoffs

### Encoding

- **_encoding_**: $$variable \longrightarrow$$ `map` $$visual$$ $$element$$

<img src="../DataAnalytics/DataScience/assets/5-mark.png" alt="example" style="height: 300px; width: auto;"/>

- **_mark_**: represents a datum

- $$Q$$ : How many variables are we encoding here?

  <img src="../DataAnalytics/DataScience/assets/5-howmany.png" alt="example" style="height: 300px; width: auto;"/>

  <details>
    <summary>Answer</summary>
    <div markdown="1">

  - $$4$$ variables

  1. `x`
  2. `y`
  3. area
  4. color

  </div></details>

- $$Q$$ : What is wrong with this visualization?

  <img src="../DataAnalytics/DataScience/assets/5-wrong.png" alt="example" style="height: 300px; width: auto;"/>

  <details>
    <summary>Answer</summary>
    <div markdown="1">

  - incorrect use of bar chart
  - qualitative data used (`Nationality`) instead of quantitative
  - $$\Rightarrow$$ not all encoding channels are exchangeable

   </div></details>

### Distribution

- <cb>distribution</cb>: describes frequency at which values of variable occur

1. show percentages (distrubtion) of category
2. all values must be accounted for once and _only once_

- $$Q1$$ : Does this chart show a distribution?

  <img src="../DataAnalytics/DataScience/assets/5-distributionexample.png" alt="example" style="height: 300px; width: auto;"/>

  <details>
    <summary>Answer</summary>
    <div markdown="1">

  - <cb>NO</cb>
  - individuals can be in more than one category
  - numbers and bar length correspond to _time_, not proportion or number of individuals in category

   </div></details>

- $$Q2$$ : Does this chart show a distribution?

  <img src="../DataAnalytics/DataScience/assets/5-distributionexample2.png" alt="example" style="height: 300px; width: auto;"/>

  <details>
    <summary>Answer</summary>
    <div markdown="1">

  - <cb>NO</cb>
  - does show percentages of individuals in different categories
  - `BUT` individuals can be in more than one category

   </div></details>

- $$Q3$$ : Does this chart show a distribution?

  <img src="../DataAnalytics/DataScience/assets/5-distributionexample3.png" alt="example" style="height: 300px; width: auto;"/>

  <details>
    <summary>Answer</summary>
    <div markdown="1">

  - <cb>YES!</cb>
  - shows the distribution of the qualitative ordinal variable “income tier.”
  - Each individual is in exactly one category
  - The values we see are the proportions of individuals in that category
  - Everyone is represented, as the total percentage is 100%.

   </div></details>

## Type of Visualizations

### Bar plots

- most **_common way for qualitative_** (categorical) variable
- also works for numerical variables on different categories

- **_not a distribution_**, but still makes sense

- _length_ encode values

  - width = nothing
  - colors = may indicate sub-category

- Ways to plot:

  1. matplotlib `plt` : <fade>basis of all three</fade>
  2. pandas `.plot()` : <fade>can make default plots</fade>
  3. seaborn `sns` : <fade>allow sophisticated visualizations quickly</fade>

- `births['Maternal Smoker']` = series of boolean values
  <details>
    <summary><code>births['Maternal Smoker].value_counts().plot( kind = 'bar' )</code></summary>
    <div markdown="1">
    <img src="../DataAnalytics/DataScience/assets/5-normal.png" alt="example" style="height: 300px; width: auto;"/>
   </div></details>

  <details>
    <summary><code>sns.countplot( births['Maternal Smoker'] )</code></summary>
    <div markdown="1">
    <img src="../DataAnalytics/DataScience/assets/5-sns.png" alt="example" style="height: 300px; width: auto;"/>
   </div></details>

- list of majors and list of corresponding GPA
  - `plt.bar( majors, gpas )` (horizontal: change `bar` $$\rightarrow$$ `barh`)
  - `sns.barplot( majors, gpa )`
  <details>
    <summary>result</summary>
    <div markdown="1">
    <img src="../DataAnalytics/DataScience/assets/5-bar.png" alt="example" style="height: 300px; width: auto;"/>
    - here, the color is meaningless
   </div></details>

### Rug plots, Histograms, Density Curves

- **_Rug Plots_**

  - for **quantitative** (numerical) varibles
  - shows _each and every_ value
  - issues:
    - too much detail
    - hard to see bigger picture
    - **_Overplotting_** (ex: birthweights at 120: can't tell, **all on top of each other**)
  - `sns.rugplot(bweights)`

- **_Histograms_**

  - smoothed version of rug plot (lose granularity, gain interpretability)
  - horizontal axis $$\leftrightarrow$$ : divided into **bins**
    - `proportion in bin = width of bin * height of bin`
  - area: proportions (total area = 1 (100%))
  - units of height: proprtion per unit on the x-axis
    <details>
      <summary><code>plt.hist( bweights, bins=bw_bins, ec='w')</code></summary>
      <div markdown="1">
      
      - where `bw_bins = range(50, 200, 5)`

      <img src="../DataAnalytics/DataScience/assets/5-hist.png" alt="example" style="height: 300px; width: auto;"/>
      - $$\Rightarrow$$ by default, `matplotlib` show **counts** on y-axis, instead of proportions per unit
     </div></details>

    <details>
      <summary><code>plt.hist( bweights, <cb>density=True</cb>, bins=bw_bins, ec='w')</code></summary>
      <div markdown="1">  
      <img src="../DataAnalytics/DataScience/assets/5-histdenst.png" alt="example" style="height: 200px; width: auto;"/>
      - $$\Rightarrow$$ total area sums to 1 (y-axis fixed)
     </div></details>

  - $$Example$$  
    <img src="../DataAnalytics/DataScience/assets/5-calc.png" alt="example" style="height: 300px; width: auto;"/>

    - $$\approx$$ `120` babies born with weight between `110`~`115` (y-axis = count)
    - total `1174` observations (given)
    - looking at y-axis=proportion graph:
      - width of bin [110, 115) = $$5$$
      - Height of bar [110, 115) = $$0.02$$
      - proportion of bin = `5` \* `0.02` = $$0.1$$
      - Number in bin = `0.01` \* `1174` = **_$$117.4$$_** $$\approx$$ `120`!

  - beware of drawing strong conclusions from looks of histogram
    - **_Number of bins influences appearance!_**
    - Freedman-Diaconis rule:
      $$
      Bin width = 2\frac{IQR(x)}{\sqrt[\leftroot{10} \uproot{5} 3]{n}}
      $$
  - Bins don't need to to have the same width
    - $$\Rightarrow$$ especially crucial to think of proportions as areas
      <img src="../DataAnalytics/DataScience/assets/5-beware.png" alt="example" style="height: 400px; width: auto;"/>

- **_Density Curves_**

  - instead of discrete histogram, visualize by continuous distribution
  - <code>sns.histplot(bweights, <cb>kde=True</cb>)</code>
    <img src="../DataAnalytics/DataScience/assets/5-densitycurve.png" alt="example" style="height: 250px; width: auto;"/>
  - Desity Curve _only_
    <details>
      <summary><code>sns.displot(bweights, kind='kde')</code></summary>
      <div markdown="1">
      
      - or `sns.kdeplot(bweights)`
      <img src="../DataAnalytics/DataScience/assets/5-densitycurve2.png" alt="example" style="height: 300px; width: auto;"/>
     </div></details>

### Describing Quantitative Distributions

- **_Mode_** of distribution : local or global maximum
  <details>
    <summary>unimodal, bimodal, multimodal</summary>
    <div markdown="1">

    <img src="../DataAnalytics/DataScience/assets/5-modes.png" alt="example" style="height: 300px; width: auto;"/>

   </div></details>

- **_Skew_** and **_Tails_**:

  - ex) long right tail = "skewed right"
    <img src="../DataAnalytics/DataScience/assets/5-skew.png" alt="example" style="height: 300px; width: auto;"/>
  - mean : balancing point of density
  - skewed right = median < mean
  - **symmetric**: both tails are equal size

  <img src="../DataAnalytics/DataScience/assets/5-symmetric.png" alt="example" style="height: 300px; width: auto;"/>
  - **unimodal** and **symmetric**, roughly **normal**

- **_Outliers_**

### Box Plots and Violin Plots

- **_Quartiles_**

  - `25th percentile`: First/Lower quartile
  - `50th percentile`: Second quartile (median)
  - `75th percentile`: Third/Upper quartile

  - $$IQR$$ (Interquartile Range) = `third quartile` - `first quartile`
    - measures spread

  <img src="../DataAnalytics/DataScience/assets/5-quartiles.png" alt="example" style="height: 300px; width: auto;"/>

- **_Box Plots_**

  - `sns.boxplot( bweigths )`
    <img src="../DataAnalytics/DataScience/assets/5-box.png" alt="example" style="height: 400px; width: auto;"/>
  - 참고: box width means nothing
    <details>
      <summary>check by coding</summary>
      <div markdown="1">

    ```py
    q1 = np.percentile( bweights, 25 )
    q2 = np.percentile( bweights, 50 )
    q3 = np.percentile( bweights, 75 )
    iqr = q3 - q1
    whisk1 = q1 - ( 1.5 * iqr )
    whisk2 = q4 + ( 1.5 * iqr )

    whisk1, q1, q2, q3, whisk2
    >>> (73.5, 108.0, 120.0, 131.0, 165.5)
    ```

     </div></details>

- **_Violin Plots_** : box-whisker + density curve

  <img src="../DataAnalytics/DataScience/assets/5-violin.png" alt="example" style="height: 400px; width: auto;"/>
  - ***width have meaning***

### Comparing Quantitative Distributions

- **_Overlaid histograms and density curves_**:

  <img src="../DataAnalytics/DataScience/assets/5-overlaid.png" alt="example" style="height: 200px; width: auto;"/>

  - First graph: not bad but looks like 3 seperate histograms
  - Second graph: too much information and unclear
  - Third: although estimates are rough, it's the best

- **_Side by side box plots and violin plots_**:

  <img src="../DataAnalytics/DataScience/assets/5-sidebyside.png" alt="example" style="height: 300px; width: auto;"/>
  - concise, well suited side by side
  - violin plot shows us bimodal nature of `True` category

### Relationships between two quantitative variables

- **_Scatter plots_**: used to **reveal relationship between pairs of numerical variables**

  - help inform modeling choices
    <img src="../DataAnalytics/DataScience/assets/5-scatter.png" alt="example" style="height: 200px; width: auto;"/>

  - color usage also helpful
    <img src="../DataAnalytics/DataScience/assets/5-scatteroverplot.png" alt="example" style="height: 200px; width: auto;"/>
  - **overplotting** : points on top of each other
    - $$\Rightarrow$$ use <cb>random noise</cb> in both `x` `y` directions
      $$
      \begin{bmatrix}
      65 & 170 \\
      65 & 170 \\
      ...
      \end{bmatrix} \rightarrow
      \begin{bmatrix}
      65^{+0.2} & 170^{+0.2}\\
      65^{-0.2} & 170^{-0.2}\\
      ...
      \end{bmatrix}  \Rightarrow
      \begin{bmatrix}
      65.2 & 170.2\\
      64.8 & 169.8\\
      ...
      \end{bmatrix}
      $$
    - $$\Rightarrow$$ change in shape, but clearer

  <details>
      <summary><code>sns.lmplot(data=births, x=‘Maternal Height’, y=‘Birth Weight’, ci=False)</code></summary>
      <div markdown="1">
      - or `sns.jointplot(data=births, x=‘Maternal Height’, y=‘Birth Weight’)`

    <img src="../DataAnalytics/DataScience/assets/5-scattercode.png" alt="example" style="height: 300px; width: auto;"/>
     </div></details>

- **_Hex plots_**:

  - $$\approx$$ 2-D histogram
  - shows joint distribution
  - xy plane binned into hexagons
  - darker (more shaded) $$\rightarrow$$ greater density/frequency
  - Why hexagons ⬡ instead of squares □?
    - easier to see linear relationships
    - more efficient for covering region
    - visual bias of squares (tend to see ver, hori lines)
    <details>
        <summary><code>sns.jointplot(data=births, x=‘Maternal Height’, y=‘Birth Weight’, <cb>kind=’hex’</cb>)</code></summary>
        <div markdown="1">

      <img src="../DataAnalytics/DataScience/assets/5-hexplot.png" alt="example" style="height: 300px; width: auto;"/>
       </div></details>

- **_Contour plots_**:
  - $$\approx$$ 2-D versions of density curve
  - default: shows **_marginal distributions_** on the horizontal and vertical axes.
  - $$\Rightarrow$$ histograms/density curves of each variable independently
  <details>
      <summary><code>sns.jointplot(data=births, x=‘Maternal Height’, y=‘Birth Weight’, <cb> kind=’kde’, fill=True</cb>)</code></summary>
      <div markdown="1">
      
      <img src="../DataAnalytics/DataScience/assets/5-contourplot.png" alt="example" style="height: 300px; width: auto;"/>
     </div></details>

## Principles of Visualization

### Scale

- case study: Planned Parenthood accused of selling aborted fetal tissues for profit.
  - below graph presented by Congressman Chaffetz (from another report)
    <img src="../DataAnalytics/DataScience/assets/5-plannedparenthood.png" alt="example" style="height: 300px; width: auto;"/>
  - $$\Rightarrow$$ Misleading; **Do not use two different scales for the same axis**!
  <details>
      <summary>Visualization with correct scale</summary>
      <div markdown="1">
      
    <img src="../DataAnalytics/DataScience/assets/5-correctscale.png" alt="example" style="height: 300px; width: auto;"/>
    <img src="../DataAnalytics/DataScience/assets/5-correctscale.png" alt="example" style="height: 100px; width: auto;"/>
      - $$\Rightarrow$$ Abortions increased from 13% to 26% of total procedures.
     </div></details>
- Reveal the data
  - choose axis limits to fill the visualization
  - if necessary: zoom in on the bulk of data
  - create multiple plots to show different regions of interest
    <img src="../DataAnalytics/DataScience/assets/5-reveal.png" alt="example" style="height: 200px; width: auto;"/>

### Conditioning

- case study: median weekly earnings
  <img src="../DataAnalytics/DataScience/assets/5-conditioning.png" alt="example" style="height: 200px; width: auto;"/>

  - $$\Rightarrow$$ right is more clear

- Distributons and relationships in subgroups

  - **Juxtaposition**: placing multiple plots side by side with same scale ('small multiples')
    <img src="../DataAnalytics/DataScience/assets/5-smallmultiples.png" alt="example" style="height: 200px; width: auto;"/>

  - **Superposition**: placing multiple densitiy curves, scatter plots on top of each other
  - use color and shapes to reperesent additional variables

### Perception

- **_Colors_**
  <img src="../DataAnalytics/DataScience/assets/5-colormap.png" alt="example" style="height: 200px; width: auto;"/>

  - jet: `boundary` (old `matplotlib` default colormap)
  - viridis: `continuous change` (current `matplotlib` default)
  <details>
      <summary>Jet/rainbow colormap misleads</summary>
      <div markdown="1">
      
    <img src="../DataAnalytics/DataScience/assets/5-rainbow.png" alt="example" style="height: 300px; width: auto;"/>
    - sometimes colorless is better
     </div></details> 
  <details>
      <summary>Use perceptually uniform colormaps</summary>
      <div markdown="1">
      
    <img src="../DataAnalytics/DataScience/assets/5-perceptuallyuniform.png" alt="example" style="height: 300px; width: auto;"/>
    - except Google `Turbo` Colormap (Rainbow) is actually perceptually uniform
     </div></details>
  - use colors to highligh data type
    <img src="../DataAnalytics/DataScience/assets/5-goodcolor.png" alt="example" style="height: 300px; width: auto;"/>

    - **Qualitative**: choose qualitative scheme that helps distinguish categories
    - **Quantitative**: choose color scheme that **implies magnitude**

  - **Sequential** and **Diverging**

    <img src="../DataAnalytics/DataScience/assets/5-seqdiv.png" alt="example" style="height: 200px; width: auto;"/>
    - left (sequential scheme): light color = extreme values
    - right (diverging scheme): light color = middle (neutral) values

  - good to use color packages

- **_Markings_**
  <img src="../DataAnalytics/DataScience/assets/5-marking.png" alt="example" style="height: 300px; width: auto;"/>
  - $$\Rightarrow$$ accurate _preferred_
  - Lengths are easy to distinguish (bar graphs)
  - avoid:
    - angles & areas (pie charts)
    - wordclouds
    - jiggling baseline (stacked bar charts, area charts)
  - related: Overplotting

### Context

- instead of keys, better if labeled directly
  <img src="../DataAnalytics/DataScience/assets/5-context.png" alt="example" style="height: 300px; width: auto;"/>
- add context directly to plot
- captions: comprehensive, conclusions ...etc

### Smoothing

- Histograms : smoothed version of rug plots
- <cb>Smoothing</cb> allows to focus on general structure rather than individual observations

  - points : `[ 2.2, 2.8, 3.7, 5.3, 5.7 ]`
  - bins : `[0,2)`, `[2,4)`, `[4,6)`, `[6, 8]`
    <img src="../DataAnalytics/DataScience/assets/5-kde.png" alt="example" style="height: 300px; width: auto;"/>

  - area = proportion, `(2 * 0.1) * 5 = 1`

- **_KDE_** : Kernal Density Estimation

  - estimate **_probability density function_** (or density curve)

  1. **_Place kernal_** at each data point
     <img src="../DataAnalytics/DataScience/assets/5-kdestep1.png" alt="example" style="height: 200px; width: auto;"/>

    - **_1.1_**: choose $$kernal$$ and $$bandwidth (\alpha)$$
      - **kernal** : `Gaussian`, **alpha** = `1`

  2. **_Normalize Kernals_**
     <img src="../DataAnalytics/DataScience/assets/5-kdestep2.png" alt="example" style="height: 200px; width: auto;"/>

    - 5 different kernals with area `1` each
    - we want area = `1` _altogether_ $$\Rightarrow$$ **multiply each by $$1/5$$**

  3. **_Sum Kernals_**
     <img src="../DataAnalytics/DataScience/assets/5-kdestep3.png" alt="example" style="height: 200px; width: auto;"/>

    - <cb>kernel density estimate</cb> = sum of the normalized kernels at each point
    - $$\Rightarrow$$ same result as `sns.distplot` !

- **_Kernals_**: _valid density function_

  1. must be non-negative for all inputs
  2. must integrate to 1

  - $$Gaussian$$: most common kernal

    $$
    K_a(x, x_i) = \frac{1}{\sqrt{2\pi\alpha^2}}e^{-\frac{(x-x_i)^2}{2\alpha^2}}
    $$

    - $$x$$ : any input
    - $$x_i$$ : $$i^{th}$$ observed value
    - kernals cenetered on observed values $$\rightarrow$$ mean of distribution = $$x_i$$
    - $$bandwidth parameter = \alpha$$ : controls smoothness of KDE
      - also standard deviation of the Gaussian
        <img src="../DataAnalytics/DataScience/assets/5-gaussian.png" alt="example" style="height: 200px; width: auto;"/>

  - $$Boxcar$$: another common kernal
    - assign uniform density to points within 'window' of observation, 0 elsewehere
    - resembles histogram
      $$
      K_a(x, x_i) =
        \begin{cases}
        \frac{1}{\alpha}, |x-x_i| <= \frac{a}{2}\\
        0, else
        \end{cases}
      $$
        <details>
          <summary>Bocar kernel centered on xi=4 with α = 2 </summary>
          <div markdown="1">
        <img src="../DataAnalytics/DataScience/assets/5-boxcar.png" alt="example" style="height: 200px; width: auto;"/>
          </div></details> 
      <details>
          <summary>Gaussian vs Boxcar</summary>
          <div markdown="1">
        <img src="../DataAnalytics/DataScience/assets/5-gaubox.png" alt="example" style="height: 300px; width: auto;"/>
         </div></details>

- **_Effect of bandwidth on KDEs_**

  - bandwidth $$\approx$$ bin (in histogram)
  - KDE becomes smoother as $$\alpha$$ increases
    <img src="../DataAnalytics/DataScience/assets/5-alpha.png" alt="example" style="height: 300px; width: auto;"/>

  - simpler to understand, but gets rid of potentially important distributional information
  - $$\alpha$$ : **_hyperparameter_**

- **_Summary of KDE_**:
  $$
  f_\alpha(x) = \frac{1}{n}\sum_{i=1}^{n} K_\alpha(x, x_i)
  $$
  - $$x$$: any number on the number line (input to our function)
  - $$n$$: number of observed data points
  - $$x_i (x_1, x_2,...,x_n)$$ : observed data point (used to create KDE)
  - $$\alpha$$ : bandwidth or smoothing parameter
  - $$K_\alpha(x, x_i)$$ : kernal centered on observation $$i$$
    - each kernal individaully has `area` = `1`. We multiply by `1/n` so that `total area` = `1`

### Transformation

- transforming data can _reveal patterns_
  - ex: when distribution has large range, `log` useful
    <img src="../DataAnalytics/DataScience/assets/5-transform.png" alt="example" style="height: 200px; width: auto;"/>
- **_linearize_**

  - good because we can automatically known relationship between `x` and `y` $$\Rightarrow$$ simple to interpret

- log review

  - $$y = a^x$$ $$\rightarrow \log (y) = x\log (a)$$
  - $$y = ax^k$$ $$\rightarrow \log (y) = \log (a) + k \log (x)$$

- **_Log of y-values_**
  - $$\log y = ax+b $$
    $$
    \rightarrow
      \log y = ax+b \rightarrow
      y = e^{ax+b} \rightarrow
      y = e^{ax}e^b \rightarrow
      y = Ce^{ax}
    $$
  - $$\Rightarrow$$ **exponential** relationhip
    <img src="../DataAnalytics/DataScience/assets/5-log.png" alt="example" style="height: 300px; width: auto;"/>
- **_Log of x and y-values_**

  - $$\log y = a \cdot \log x+b $$

    $$
    \rightarrow
      \log y = ax+b \rightarrow
      y = e^{a\cdot \log x+b} \rightarrow
      y = Ce^{a\cdot \log x} \rightarrow
      y = Cx^a
    $$

    <img src="../DataAnalytics/DataScience/assets/5-logxy.png" alt="example" style="height: 300px; width: auto;"/>

  - $$\Rightarrow$$ **power** relationhip (one-term **polynomial**)

- **_Turkey-Mosteller Bulge Diagram_**

<img src="../DataAnalytics/DataScience/assets/5-turkey.png" alt="example" style="height: 400px; width: auto;"/>

- following will help linearize
- multiple solutions exist, some will fit better than the others
- $$sqrt$$ and $$log \rightarrow$$ `smaller`
- $$power \rightarrow$$ `bigger`
- these transformations will result in increasing / decreasing scale of axis

<details>
  <summary>Example</summary>
  <div markdown="1">
  <img src="../DataAnalytics/DataScience/assets/5-turkeyexample.png" alt="example" style="height: 300px; width: auto;"/>
  </div></details>