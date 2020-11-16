---
title: nextjs_tutorial_ch1
date: 2020-11-17 12:00:00
author: dev-owen
category: S2_Round1
---

# Next.js에 대해서 알아보자 #1. Intro

Next.js는 React에서 기존에 CSR(Client Side Rendering)의 특징에 더하여 SSR(Servers Side Rendering)을 혼합하여 운영환경에서 최적의 퍼포먼스를 낼 수 있게 도와주는 프레임워크이다. 2020년 11월 현재 버전 10.0.1이 나와있으며 다음과 같은 기능들을 지원한다.

- 페이지 기반 라우팅 (동적 라우팅)
- 데이터 패칭
- 빠른 성능을 위한 코드 스플리팅
- CSS in JS
- 이미지 최적화
- 빠른 컴포넌트 재활성화
- 정적 파일 처리
- 타입스크립트
- 환경 변수
- 브라우저 지원

각각에 대한 자세한 사항들은 이후에 하나씩 알아보고자 한다.

<br>
 
Next.js는 SPA에서 CSR이 가질 수 밖에 없는 한계들을 보완해 주는 도구이다. SSR과 CSR에 대한 포스팅 참고

CSR은 초기 로딩 속도가 전통적인 SSR 방식에 비해 길다. 그 이유는 브라우저에서 화면을 렌더링하는데 필요한 모든 파일(HTML, CSS, JS, 이미지와 같은 대용량 파일 등)을 전부 받아온 다음 렌더링을 하기 때문이다. 그리고 이처럼 초기 로딩속도가 느리면 SEO(검색 엔진 최적화) 측면에서도 불리할 수밖에 없게 된다. 이러한 단점들을 극복하기 위한 도구 중 하나가 React에서는 Next.js인 것이다.

Next.js를 통해서 Node 서버 기반의 페이지를 만들 수가 있는데 (SSR), 페이지를 이동할 때마다 필요한 JSON 데이터를 가져올 수도 있고 (CSR) 이 두 가지 렌더링 방식을 필요에 맞게 적절하게 섞어쓸 수 있다는 점이 장점이다. 예를 들어 블로그와 같이 정적인 컨텐츠가 많은 페이지는 SSR, 페이스북 뉴스피드 같이 실시간으로 사용자 인터랙션이 많은 페이지는 CSR을 사용할 수가 있다.

성능을 최적화 하는 과정에서도 Next.js가 많은 도움을 준다. 그 중 한 가지 방법은 pre-rendering이다. 서버사이드에서 빌드 중 실행되는 getStaticProps 함수를 통해 페이지 렌더링에 필요한 데이터를 받아오고 이와 같이 pre-rendering된 페이지는 초기 페이지 로딩이 CSR에 비해 빠르며, SEO 관점에서도 유리하다. 또 다른 방법은 code-splitting이다. 라우트 기반의 코드 스플리팅은 한 번에 파싱&컴파일 되어야 하는 코드의 양을 최소화 시켜주며 결과적으로 페이지 로드 시간의 단축을 이끌어낼 수 있다.

<br> 

간단한 Next.js app을 만들면서 연습해 보자

```shell script
mkdir nextjs-tutorial
cd nextjs-tutorial
npm init
npm install --save next react react-dom
```
package.json 파일에 간단한 스크립트를 추가한다.

```javascript
// package.json
{
  "scripts": {
    // ...
    "dev": "next",
    "build": "next build",
    "start": "next start"
  }
}
```

next.js는 pages 폴더에 route와 동일한 이름의 컴포넌트로 만들어야 한다는 규칙이 있다. 예를 들어 url이 /about 이면 해당 컴포넌트는 pages/about.jsx와 같이 만들어 져야 한다.
```javascript
// pages/about.jsx

import React from 'react';

const About = (props) => {
  const {message} = props;

  return (
    <div>
      <p>Hello World!</p>
      <p>{message}</p>
    </div>
  );
};

export async function getStaticProps(context) {
  return {
    props: {
      message: `Next.js`
    }
  };
};

export default About;
```


이와 같이 컴포넌트를 하나 만들어 준 후 
```shell script
npm run build && npm run dev
```

빌드 후 실행하면 .next 폴더가 하나 생성된다. 그리고 나서 localhost:3000에 방금 만든 app이 실행되고 있는 것을 볼 수 있다.

이렇게 정말 간단한 next.js app을 하나 시작해 보았다. 다음 포스팅에서는 페이지를 추가하고, 동적 데이터를 추가하는 작업을 하는 튜토리얼을 포스팅 해 보려고 한다.

 
## 참고자료
- [Next.js 공식문서](https://nextjs.org/)
- [Next.js로 Static Site 만들기](https://medium.com/@pks2974/nextjs-%EB%A1%9C-static-site-%EB%A7%8C%EB%93%A4%EA%B8%B0-f9ab83f29e7)
- [Next.js 튜토리얼](https://brunch.co.kr/@hee072794/81)
- [nextjs는 어떻게 동작하는가?](https://blueshw.github.io/2018/04/15/why-nextjs/)

