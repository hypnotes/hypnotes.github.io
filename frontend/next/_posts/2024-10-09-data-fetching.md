---
layout: post
title: Data Fetching
description: >
  데이터 가져오기 - 심층분석
categories: next
accent_color: "#FFF"
accent_image:
  background: "#000"
theme_color: "#000"
sitemap: false
permalink: /frontend/next/datafetching
---

### Basic Data Fetching with Server Components

```js
// SERVER COMPONENT (async 붙여도 됨)
export const PostDetailPage = async () => {
  // 로딩 중일떄는 `loading.tsx` 렌더링함
  const { post } = await getPostData();

  if (!post) {
    return notFound();
  }

  return (
    <div>
      <h1>{post.title}</h1>
      <p>{post.body}</p>
    </div>
  );
};
```

### Detailed Data Fetching with Suspense

- 일부분만 로딩하고 싶을 때 사용 (컴포넌트로 분리 후 Suspense로 감싸기)

```js
..

return (
  <>
    <Suspense fallback={<div>Loading Filter</div>}>
      <FilterHeader year={selectedYear} month={selectedMonth}/>
    </Suspense>
    <Suspense fallback={<div>Loading Posts</div>}>
      <FilteredPost year={selectedYear} month={selectedMonth}/>
    </Suspense>
  </>
)
```

- 또는 같은 suspense로 묶기 (어차피 selectedYear, selectedMonth가 같은데 두번 로딩할 필요 없음)
