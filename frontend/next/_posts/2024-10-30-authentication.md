---
layout: post
title: Authentication
description: >
  Loggin Users In & Out
categories: next
accent_color: "#FFF"
accent_image:
  background: "#000"
theme_color: "#000"
sitemap: false
permalink: /frontend/next/authentication
---

### next cookies

```jsx
import { cookies } from "next/headers";

const cookieStore = cookies();

cookieStore.set(...);
cookieStore.get(...);
```
