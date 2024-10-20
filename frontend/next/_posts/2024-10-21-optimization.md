---
layout: post
title: Optmization
description: >
  NextJS 앱 최적화
categories: next
accent_color: "#FFF"
accent_image:
  background: "#000"
theme_color: "#000"
sitemap: false
permalink: /frontend/next/optimization
---

## Images

- size optimization
- visual stability (로딩 중 layout shift 방지)
- faster page loads: native browser lazy loading, blur placeholder 기능 등
- assest flexibility: 온디멘드 이미지 resizing (서버 이미지도 가능)

### sizes

```js
// sizes prop, width, height prop
<Image
  src="/images/profile.jpg"
  alt="Picture of the author"
  // width={500}
  // height={500}
  sizes={"(max-width: 640px) 100vw, (max-width: 768px) 50vw, 33vw"}
  priority
/>
```

- priority: 미리 로딩, lazy-loading 제거됨
  - 무조건 로딩될 이미지에 사용 (ex. 로고)

### external resources

next.config.js

```js
/** @type {import('next').NextConfig} */
const nextConfig = {
  images: {
    remotePatterns: [{ hostname: "resources.example.com", path: "/" }],
  },
};
```

- 외부 이미지 불러올 때 사용

### fill

```js
<Image src={post.image} fill alt={"temp"} />
```

이러면 이미지가 꽉 차게 나옴.
container 필요!

```js
<div className={/*여기에 스타일링 추가*/}>
  <Image src={post.image} fill alt={"temp"} />
</div>
```

- sizes랑 같이 사용 권장됨 (로더 사용 시 그냥 fill 보다는 width, height 사용)

### Image loader

- `loader` prop: 이미지 소스를 determine 할 때 실행되는 함수

```js
const imageLoader = (config) => {
  console.log(config);
  return config.src;
};
```

- src, quality, width 돌려줌

- `quality` prop: 이미지 품질 조절 (0~100)

  - config object의 quality 속성으로 전달됨

- 예를 들어, cloudinary는 이미지 변환을 지원함

```js
const imageLoader = ({ src, width, quality }) => {
  const [urlStart, urlEnd] = config.src.split("upload/");
  const transformations = `w_200,h_150,q_${quality || 75}`;
  return `${urlStart}upload/${transformations}/${urlEnd}`;
};
```

## Metadata

- search engine crawler에게 페이지 정보 전달

### static metadata

- metadata: Metadata 객체에 title, description, openGraph같은거 추가하면 됨

```js
export const metadata = {
  title: "Home",
  description: "Home page",
};
```

### dynamic metadata

```js
export const generateMetadata = async (data) => {
  const posts = await fetchPosts();
  const numberOfPosts = posts.length;
  return {
    title: `Home (${numberOfPosts})`,
    description: "Home page",
  };
};
```

- `layout.tsx`에서 metadata 가 default
- override 필요 시 `page.tsx`에서 가능