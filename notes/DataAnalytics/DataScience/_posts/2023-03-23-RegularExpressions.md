---
layout: post
title: 04 Regular Expressions
description: >

image: ../DataAnalytics/DataScience/assets/4-re.png
hide_image: true
sitemap: false
permalink: /notes/DataScience/RegularExpressions
---

- this list will be replaced by the toc
{:toc .large-only}

## String Canonicalization

> **_Canonicalize_**: Convert data that has more than one possible presentation into a standard form

<details>
    <summary>A Joining Problem </summary>
    <div markdown="1">
  <img src="../DataAnalytics/DataScience/assets/4-canonicalization.png" alt="lifecycle" style="height: 200px; width: auto;"/>
   </div></details>

- useful codes:
  - Replacement: `str.replace('&', 'and')`
  - Deletion: `str.replace(' ', '')`
  - Transformation: `str.lower()`

## Extracting data from text

### Date Information

```
169.237.46.168 - - [26/Jan/2014:10:47:58 -0800] "GET /stat141/Winter04/
HTTP/1.1" 200 2585 "http://anson.ucdavis.edu/courses/"
```

- how to get _Date Information_ from the above log file
- Better to use $$Regular$$ $$Expression$$ rather than scratch

  ```py
  import re
  pattern = r'\[(\d+)/(\w+)/(\d+):(\d+):(\d+):(\d+) (.+)\]'
  day, month, year, hour, minute, second, time_zone = re.search(pattern, text).groups()
  ```

- _Formal Language_ : set of strings, typically described implicitly

  - <fade>"The set of all strings of length less than 10 & that contains a 'horse'"</fade>

- _Regular Language_ : a formal language that can be described by a regular expression
  - <fade>`[0-9]{3}-[0-9]{2}-[0-9]{4}`</fade>
  - 3 of any digit, then a dash, then 2 of any digit, then a dash, then 4 of any digit.
  ```py
  text = "My social security number is 123-45-6789.";
  pattern = r"[0-9]{3}-[0-9]{2}-[0-9]{4}"
  re.findall(pattern, text)
  ```
- Useful Site for testing Regex: [Regex101](https://regex101.com/)

- Basic Operators

|       operation        | order | example  |     matches      |   does not match   |
| :--------------------: | :---: | :------: | :--------------: | :----------------: | ------------------ |
|     concatenation      |   3   | `AABAAB` |     `AABAAB`     | every other string |
|           or           |   4   |   `AA|BAAB`       |    `AA`, `BAAB`    | every other string |
| closure (zero or more) |   2   |  `AB*A`  | `AA`, `ABBBBBBA` |   `AB`, `ABABA`    |
|      parenthesis       |   1   |   `A(A|B)AAB`      |  `AAAAB`, `ABAAB`  | every other string |
|                        |       | `(AB)*A` | `A`, `ABABABABA` |    `AA` `ABBA`     |

<details>
    <summary>Regex that matches `moon`, `moooon` (even `o`s except 0)</summary>
    <div markdown="1">
    moo(oo)*n
   </div></details>
  
<details>
    <summary>Regex that matches `muun`, `muuuun`, `moon`, `moooon (even `o`s or `u`s except 0)</summary>
    <div markdown="1">
    mo(u(uu)*|o(oo)*)n
   </div></details>

- Expanded Regex Syntax

|                     operation                    |        example        |         matches          | does not match |
| :-----------------------------------------------: | :-------------: | :-------------------: | :----------------------: | :------------: |
|          any character (except newline)           |    `.U.U.U.`    | `CUMULUS`, `JUGULUM`  | `SUCCUBUS`, `TUMULTUOUS` |
|                  character class                  | `[A-Za-z][az]*` | `word`, `Capitalized` | `camelCase`, `4illegal`  |
|                   at least one                    |     `jo+hn`     |  `john`, `joooooohn`  |      `jhn`, `jjohn`      |
| zero or one | `joh?n` | `jon` `john` | any other string |
|           repeated exactly `{a}` times            | `j[aeiou]{3}hn` |   `jaoehn`,`jooohn`   |    `jhn`, `jaeiouhn`     |
|      repeated from `a` to `b` times: `{a,b}`      | `j[ou]{1,2}hn`  |    `john`, `juohn`    |     `jhn`, `jooohn`      |

- More Regular Expression Examples

  |            regex             |           matches            |              does not match               |
  | :--------------------------: | :--------------------------: | :---------------------------------------: | ------------------------------ |
  |          `.*SPB.*`           |  `RASPBERRY`, `CRISPBREAD`   |         `SUBSPACE`, `SUBSPECIES`          |
  | `[0-9]{3}-[0-9]{2}-[0-9]{4}` | `231-41-5121`, `573-57-1821` |         `231415121`, `57-3571821`         |
  |   `[a-z]+@([a-z]+\.)+(edu    |            com)`             | `horse@pizza.com`, `horse@pizza.food.com` | `frank_99@yahoo.com`, `hug@cs` |

<details>
    <summary>Regex n for any lowercase string that has a repeated vowel </summary>
    <div markdown="1">
    [a-z]*(aa|ee|ii|oo|uu)+[a-z]*
   </div></details>

<details>
    <summary>Regex n for any string that contains both a lowercase letter & number </summary>
    <div markdown="1">
    (.*[a-z].*[0-9].*)|(.*[0-9].*[a-z].*)
   </div></details>

## Advanced Regular Expressions Syntax

- since RE is difficult to read, it is (sarcastically) called "write only language"

|            operation             |          example          |           matches           | does not match |
| :------------------------------: | :----------: | :-----------------------: | :-------------------------: | :------------: |
|    built-in character classes    | `\w+`, `\d+` |     `fawef`, `231231`     | `this person`, `423 people` |
|     character class negation     |  `[^a-z]+`   | `PEPPERS3982`, `17211!@#` |      `porch`, `CLAmS`       |
|         escape character         |  `cow\.com`  |         `cow.com`         |          `cowscom`          |
|        beginning of line         |    `^ark`    |  `ark two`, `ark o ark`   |           `dark`            |
|           end of line            |    `ark$`    |    `dark`, `ark o ark`    |          `ark two`          |
| lazy version of zero or more \*? |   `5.*?5`    |       `5005`, `55`        |          `5005005`          |

- escape character: can be thought of it as "take this next character literally"

<details>
    <summary>Regex that matches anything inside of the angle brackets <> </summary>
    <div markdown="1">

    `<.*?>`
   </div></details>

## Regular Expressions in Python

- `re.findall(pattern, text)` : return list of all matches

  ```py
  text = """My social security number is 456-76-4295 bro,
          or actually maybe it’s 456-67-4295."""
  pattern = r"[0-9]{3}-[0-9]{2}-[0-9]{4}"
  m = re.findall(pattern, text)
  print(m)
  ```

  `>>> ['456-76-4295', '456-67-4295']`

- `re.sub(pattern, repl, text)` : return text with all instances of pattern replaced by repl.

  ```py
  text = '<div><td valign="top">Moo</td></div>'
  pattern = r"<[^>]+>"
  cleaned = re.sub(pattern, '', text)
  print(cleaned)
  ```

  `>>> 'Moo'`

- Raw strings in Python : **strongly suggest using RAW STRINGS**

  - using `r" "` instead of `""` or `''`
  - Rough idea: Regular expressions and Python strings both use \ as an escape character
  - Using non-raw strings leads to uglier regular expressions.

- RE Groups

  - Parentheses specifies a so-called 'group'
  - regular expression matchers <fade> ex: `re.findall` </fade> will return matches organized by groups (tuples, in Python)

  ```py
  s = """Observations: 03:04:53 - Horse awakens.
  03:05:14 - Horse goes back to sleep."""
  pattern = "(\d\d):(\d\d):(\d\d) - (.*)"
  matches = re.findall(pattern, s)
  ```

  `>>> [('03', '04', '53', 'Horse awakens.'), ('03', '05', '14', 'Horse goes back to sleep.')]`

- Practice Problem:

  ```py
  pattern = "YOUR REGEX HERE"
  matches = re.findall(pattern, log[0])
  day, month, year = matches[0]
  ```

  <details>
      <summary> Answer</summary>
      <div markdown="1">
    "\[(\d{2})/(\w{3})/(\d{4})"
     </div></details>

- Summary and other (alternative) tools

| basic python  |      re      |      pandas      |
| :-----------: | :----------: | :--------------: |
|               | `re.findall` | `df.str.findall` |
| `str.replace` |   `re.sub`   | `df.str.replace` |
|  `str.split`  |  `re.split`  |  `df.str.split`  |
| `'ab' in str` | `re.search`  | `df.str.contain` |
|  `len(str)`   |              |   `df.str.len`   |
|  `str[1:4]`   |              |  `df.str[1:4]`   |
