---
layout: post
title: Resize Observer
description: >
  30 minutes per day
categories: dev
sitemap: false
accent_image: /assets/default.jpg
permalink: /dev/resize-observer
sitemap: false
---

### 배경 설명

- 개발 내용: 화면 회전에 따라 에디터 패널 크기 조절하기

요구사항:

1. 가로 -> 세로 회전: bottom, height 유지
2. 세로 -> 가로 회전:

- Bottom: 캔버스 넘어가면 그만큼 내려주기 (top:0 가 아니라, Bottom을 계산해주어야 해서 복잡함)
- Height: 캔버스 넘어가면 캔버스 최대높이로 맞추기

=> 캔버스 높이를 알아야 한다 => ResizeObserver 사용

- [MDN Docs](https://developer.mozilla.org/en-US/docs/Web/API/ResizeObserver)

> Element의 크기 변화를 감지하는 API

### 사용법

생성

```js
const resizeObserver = useMemo(
  () =>
    new ResizeObserver((entries: ResizeObserverEntry[]) => {
      entries.forEach((entry: ResizeObserverEntry) => {
        console.log("@@ entry", entry);
      });
    }),
  []
);
```

- 위 entry 찍어보면

  ```js
  borderBoxSize: [ResizeObserverSize] // { blockSize: 1124, inlineSize: 820 }
  contentBoxSize: [ResizeObserverSize] // { blockSize: 1124, inlineSize: 820 }
  contentRect: DOMRectReadOnly {x: 0, y: 0, width: 820, height: 1124, top: 0, bottom: 1124, left: 0, right: 820}
  devicePixelContentBoxSize: [ResizeObserverSize] // { blockSize: 1124, inlineSize: 820 }
  target: div#playground.EditorPlaygroundView__Playground-sc-2f1bc596-0.kwtSLG
  ```

메소드

- `ResizeObserver.disconnect()`: 특정 옵저버가 관찰중이던 요소들을 관찰하지 않도록 설정
- `ResizeObserver.observe()`: 관찰할 요소 추가
- `ResizeObserver.unobserve()`: 관찰할 요소 제거

```js
useEffect(() => {
  const editorElem = document.querySelector("#playground");
  if (editorElem) {
    resizeObserver.observe(editorElem);
  }
}, [resizeObserver]);
```

### Observation Errors


- paint 단계 전 (유저에게 보여지기 전) 변화를 감지한다
- 따라서 Resize 이벤트 -> style, layout 재계산 => resize event 재발생 => 무한루프 가능

- cyclic dependency 대응법: process eleements deeper in the DOM during each iteration (?????)

  - 이거 안되면 `ResizeObserver loop completed with undelivered notifications` 윈도우 에러 발생

- 에러 발생 코드 : infinte loop 발생함 (div 사이즈 무한 확장) 에러 "repeating every frame"

```js
const divElem = document.querySelector("body > div");

const resizeObserver = new ResizeObserver((entries) => {
  for (const entry of entries) {
    entry.target.style.width = entry.contentBoxSize[0].inlineSize + 10 + "px";
  }
});

resizeObserver.observe(divElem);

window.addEventListener("error", (e) => {
  console.error(e.message);
});
```

- 종국에는 resize observer은 적절히 그럴싸한 레이아웃으로 마무리 될 것임 (??????)
  - 단, 사용자는 잠시 broken layout을 보게 될 수 있음 (1 frame에 끝나야 하는게 여러 frame에 걸쳐서 끝날 수 있음)

### requestAnimationFrame

- 위 이슈 해결을 위해 사용

> [requestAnimationFrame()](https://developer.mozilla.org/en-US/docs/Web/API/Window/requestAnimationFrame) 메서드는 브라우저에게 수행하기를 원하는 애니메이션을 알리고 다음 리페인트 이전에 해당 애니메이션을 업데이트하는 함수를 호출하게 된다

1. resizeobserver callback을 requestAnimationFrame callback으로 넣어주면 해결됨

- browser repaint 후에 resizeobserver callback이 실행됨

2. resize 옵저버 콜백이 resize를 다시 발생시키지 않도록 함

- ex) `expected size` 같은 제한을 두어서 무한루프 방지

```js
const divElem = document.querySelector("body > div");
const expectedSizes = new WeakMap();

const resizeObserver = new ResizeObserver((entries) => {
  requestAnimationFrame(() => {
    for (const entry of entries) {
      const expectedSize = expectedSizes.get(entry.target);
      if (entry.contentBoxSize[0].inlineSize === expectedSize) {
        continue;
      }
      const newSize = entry.contentBoxSize[0].inlineSize + 10;
      entry.target.style.width = `${newSize}px`;
      expectedSizes.set(entry.target, newSize);
    }
  });
});

resizeObserver.observe(divElem);

window.addEventListener("error", (e) => {
  console.error(e.message);
});
```
