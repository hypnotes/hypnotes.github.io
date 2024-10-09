---
layout: post
title: App Router
description: >
  udemy 강의
categories: next
accent_color: "#FFF"
accent_image:
  background: "#000"
theme_color: "#000"
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

- **Next Images** : lazy loading 가능
  - dynamic loading 할꺼면 fill 써도 됨 (instead of width, height 추가!)

**Components**

1. Server Components
2. React Server Components (RSC) <-- NEXT JS

- console에 안찍힘! (브라우저에서 실행 안된다는 뜻)
- eventhandlers, hooks 사용 불가

3. Client Components

- next는 fullstack (has backend executing the code) 이기 때문에 DEFAULT server component로 생성함

- **_usePathName()_** (provided by NEXT)

  ```js
  const path = usePathName();
  ```

  - client side only

- `use client` 는 최ㅣㅣㅣ대한 far down the tree에 넣기

> 📌 server component는 async function으로 변환이 가능하다!<br/>

- 안에 `await` 사용 가능

- 🥷 "aggressive caching under the hood"

  - data 를 포함해서 페이지를 캐싱함 (production mode는 특히나 더)

- `loading.ts` 추가! (page.ts 의 sibling)

  - 근데 이거보다는 그냥 로딩 필요한 부분 `<Suspense fallback={}>`처리가 더 좋음

- `not-found.tsx` 추가

  - `404` 페이지

  ```js
  const PostDetailPage = () => {
  const { id } = useParams();

  const item = tempData.find((data) => data.index === Number(id));

  // 가장 가까운 not-found.tsx로 이동
  if (!item) {
    notFound();
  }
  ...
  };

  ```

### Server Actions

- form submit과 같은 서버 액션은 `use server`로 명시
  - instead of `<form action={'/some-url'}>`
- `async` 함수로 만들어야 함

```js
export async function SharePost() {
  const sharePost = async (id) => {
    'use server';
    console.log('share post'); // terminal에 뜸
  };

  return {
    <form action={sharePost}>
      ...
    </form>
  };
}
```

**client component에서 server action:**

- error 뜸
- 다른 파일에 분리

actions.ts

```js
"use server";
export async function SharePost() {
  console.log("share post");
}
```

```js
// NO ERROR
"use client";
export async function SharePost() {
  return {
    <form action={sharePost}>
      ...
    </form>
  };
}
```

- form 사용 시 더 좋은 피드백을 위해
  - `import { useActionState } from 'react';`
  - `const [state, formAction] = useActionState(sharePost, {message: null});`
  - 해서 `state.message && ...`으로 버튼명 변경해주던지 하기
  - 대신, `sharePost` 의 첫번째 인자는 `prevState`여야 함. 두번쨰가 실제 값

### Production

`npm run build`, `npm run start`로 production mode로 확인

- 더 빠름
- [PRODUCTION ONLY] generates all static pages during build (pre-rendering)
- $$\rightarrow$$ 무언가 post (rest)하면 refetching 필요
- `revalidatePath('/posts')`로 해당 페이지만 revalidate 가능
  - `revalidatePath('/posts', 'page')` // 'layout' 등 특정 파일만도 가능

### assets

- `public` 폴더에 넣어두면 `/_next/`에 자동으로 들어감 (build time)
- 그 외 로컬에는 저장 X (S3, CloudFront 등에 저장)

### Meta Data
