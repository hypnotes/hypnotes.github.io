---
layout: post
title: Data Mutation
description: >
  데이터 변이 - 심층분석
categories: next
accent_color: "#FFF"
accent_image:
  background: "#000"
theme_color: "#000"
sitemap: false
permalink: /frontend/next/datamutation
---

### Server Actions

- react 에서 제공함 (넥스트 한정 X)
- form 의 action 속성은 server action을 지정함

```js
const NewPostPage = () => {
  const submitPostHandler = async (postData) => {
    "use server" // <---------- 이게 핵심
    ...
    console.log(data); // <---------- 터미널에 출력
  };

  return (
    ...
  )
};
```

#### [useFormStatus](https://ko.react.dev/reference/react-dom/hooks/useFormStatus)

- react 제공
- `<form>` tag 중간에 사용
- client 컴포넌트에서 사용

```jsx
"use client"
import { useFormStatus } from 'react';

export default function NewPostPage() {
  const { pending, data, method, action } = useFormStatus();

  return (
    ...
  )
}
```

#### [useActionState](https://ko.react.dev/reference/react/useActionState)

- react 제공
- 원래 useFormState 였으나, useActionState로 변경됨
- client 컴포넌트에서 사용

```jsx
"use client"
import { useActionState } from 'react';

export default function NewPostPage() {

  // 에러 발생 (server action in client component)
  const createPost = async (postData) => {
    "use server"
    ...
  };

  const [state, formAction] = useActionState(createPost, initialState, permalink?);

  return (
    <>
      <form action={formAction}>
        ...
      </form>
    </>
  )
}
```

- 해결방법: client 컴포넌트를 분리하기
- 해결방법2: server action을 분리하기

### "use server"

- 지시만 할 뿐,
  > ⚠️ 서버에서만 실행된다는 것을 의미하거나 보장하지 않음
  - 클라에서 숨기기 위해 사용 부적합
- server action이든 아니든 클라쪽에서 절대 실행하면 안되는 코드 있다면 [server-only](https://nextjs.org/docs/app/building-your-application/rendering/composition-patterns#keeping-server-only-code-out-of-the-client-environment) 패키지를 사용해야 함
