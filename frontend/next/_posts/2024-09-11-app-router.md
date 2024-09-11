---
layout: post
title: udemy approuter
description: >

categories: javascript
accent_color: "#D0C8B6"
accent_image:
  background: "#E2DAD5"
theme_color: "#D0C8B6"
sitemap: false
permalink: /frontend/next/approuter
---

- add table of contents
  {:toc}

- 기본적으로 server component이기에 console찍어도 terminal에 뜨지 F12에 안뜸
- `<Link>`

  - `<a>` 태그 문제점 : content 다시 다운받음 (이동 중 위에 Refersh 버튼 중간에 'x'로 바뀜)
  - `Link`사용 시: 서버에서 실행된 페이지 코드 보내주기에 페이지 이동 원활

**Layout**

- `layout.tsx` : 하나는 꼭 필요함 (각 폴더에 있으면 해당 폴더만 스코프)
- 가장 RootLayout:

  ```js
  export const metadata = {
    title: "NextJS Course App",
    description: "Your first NextJS app!",
  };

  export default function RootLayout({ children }) {
    return (
      <html lang="en">
        // META DATA (head) 요기에 없음!
        <body>{children}</body>
      </html>
    );
  }
  ```

  - **Children**: the CONTENT of `page.tsx`

  <!-- ![image](https://nextjs.org/_next/image?url=%2Fdocs%2Fdark%2Fon-demand-revalidation.png&w=3840&q=75){:.lead width="200" height="100" loading="lazy"} -->
