---
layout: post
title: Router
description: >
  Modern React = Class형 컴포넌트 -> Hooks+함수형 컴포넌트
# image: /assets/img/blog/example-content-ii.jpg
sitemap: false
last_modified_at : 2022-08-31
permalink: /notes/React/Router
---


## 2022-08-30

<br>

- **SPA (Single Page Application)** 
  -  **라우팅** (어떤 주소에 어떤 UI를 보여줄지 결정하는 작업) 을 client가 담당함
  - Non-SPA (옛날식) : 클라이언트 gives 주소 > 서버 returns html
    - 문제: 사용자와 interaction이 많은 경우: 불필요한 트래픽 낭비
  - 클라이언트가 주소에 따라 페이지를 렌더링함
  - 필요한 데이터만 API로 서버에 연결> 서버 returns required json data
  <br>
  - 단점1: 앱의 크기가 커지면 JS 파일도 너무 커짐
    - 해결책: Code Splitting
    ![Code Splitting](./img/1code_splitting.png)
  - 단점2: 브라우저에서 JS가 구도오디지 않으면 UI 보기 불가능 (ex: )
    - 해결책: Server Side Rendering
  
  <br>

  - react-router : component 기반 라우팅 
    - 주요 컴포넌트
    1. BrowserRouter : HTML5 History API 사용 (주소만 바꾸고 페이지는 다시 불러오진 않음)
    2. HashRouter : uses '#' 
    3. MemoryRouter : 브라우저 주소와 무관 (test환경, react-native 등에서 사용)
    4. StaticRouter : 서버 사이드 렌더링
    5. Route : Route 정이할 떄 사용
    6. Link : Router 의 주소를 바꿈 (a 태그, but 새로고침 X)

  - next.js : SPA rendering very easy, code-splitting done easily
    -  page 경로 rendering