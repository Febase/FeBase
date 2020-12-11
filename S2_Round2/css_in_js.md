---
title: CSS-in-JS
date: 2020-12-03 12:00:00
author: dev-owen
category: S2_Round2
---

# CSS in JS

기존에 CSS는 .css 파일에 작성해서 사용하였다. 프로젝트의 규모가 커지면서 항상 큰 스타일 시트를 유지하는 것이 번거로워졌고 그래서 새로운 아이디어가 나왔다. 스타일시트를 문서레벨이 아닌 컴포넌트 레벨로 추상화 하여 마치 모듈처럼 사용하는 것이다.

CSS-in-JS는 JS를 사용하여 스타일을 선언적이고 유지보수가 가능한 방식으로 설명한다. JS를 CSS로 전환하는 고성능 컴파일러로, 런타임 및 서버 사이드에서 작동한다.

참고로 인라인 스타일과 CSS-in-JS는 다르다. 차이점이 있다면 인라인 스타일은 DOM 노드에 속성으로 추가하였고, CSS-in-JS는 DOM 상단에 `<style>` 태그를 추가했다. 여기서 CSS-in-JS가 가진 이점은 실제 CSS가 생성이 되기 때문에 미디어 쿼리나 :disabled, :before 같은 선택자를 사용하는 것이 가능하다는 점이다.

### 인라인 스타일

```jsx
const textStyles = {
  color: white,
  backgroundColor: black
}

<p style={textStyles}>inline style!</p>

// 브라우저는 DOM 노드를 다음과 같이 연결한다.

<p style="color: white; backgrond-color: black;">inline style!</p>
```

### CSS-in-JS (styled-components)

```jsx
import styled from 'styled-components';

const Text = styled.div`
  color: white,
  background: black
`

<Text>Hello CSS-in-JS</Text>

// 브라우저는 DOM 노드를 다음과 같이 연결한다.

<style>
.hash136s21 {
  background-color: black;
  color: white;
}
</style>

<p class="hash136s21">Hello CSS-in-JS</p>
```

기존에 CSS는 컴포넌트 기반을 고려하여 만들어진 적이 없었다. CSS-in-JS는 이러한 한계를 정확하게 해결할 수 있는 도구로 볼 수가 있다. 이 외에도 CSS-in-JS가 가진 장점은 다음과 같다.

- 컴포넌트 단위의 추상화 (모듈화)
- 진정한 분리 법칙
    - 부모 요소의 속성을 상속하지 않음
- 스코프가 있는 선택자
    - 복잡한 어플리케이션에서 선택자 충돌을 피할 수 있다.
- 현재 화면중에 사용중인 스타일만 DOM에 있음
- 벤더 프리픽스(-webkit-, -moz, -webkit- 등)가 자동생성

현재 사용되고 있는 CSS-in-JS 라이브러리에는 다음과 같은 것들이 있다. (2020년 12월 기준)
![npm trend](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7da56ac4-d4be-449d-8d3c-646c7e8fc24b/screencapture-npmtrends-styled-components-vs-jss-vs-glamorous-vs-aphrodite-vs-styletron-vs-radium-vs-emotion-core-2020-12-03-02_03_42.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201206T061250Z&X-Amz-Expires=86400&X-Amz-Signature=bc396cbc14cd12caa215651baf037742136e8a6dcc6fe5b2b85bbb942a59f0c1&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22screencapture-npmtrends-styled-components-vs-jss-vs-glamorous-vs-aphrodite-vs-styletron-vs-radium-vs-emotion-core-2020-12-03-02_03_42.png%22 "이미지 출처: npm trend")

### styled-components (31.7K stars)

```jsx
import React, { Component } from 'react';
import styled from 'styled-components';

const Title = styled.h1`
  color: white;
`;

const Wrapper = styled.div`
  background: black
`

class App extends Component {
  render() {
    return (
        <Wrapper>
            <Title>Hello World!</Title>
        </Wrapper>
    );
  }
}

export default App;
```

### emotions(12K stars)

```jsx
// this comment tells babel to convert jsx to calls to a function called jsx instead of React.createElement
/** @jsx jsx */
import { css, jsx } from '@emotion/react'

const color = 'white'

const Box = css`
    padding: 32px;
    background-color: hotpink;
    font-size: 24px;
    border-radius: 4px;
    &:hover {
	      color: ${color};
    }
`

render(
	  <div css={Box}>
		    Hover to change color.
	  </div>
)
```

### 참고자료

- [Thinking about emotion js vs styled component](https://ideveloper2.dev/blog/2019-05-05--thinking-about-emotion-js-vs-styled-component/)
- [[번역] CSS-in-JS에 관해 알아야 할 모든 것](https://d0gf00t.tistory.com/22)
- [Styled components vs Emotion js: A performance perspective](https://dev.to/meetdave3/styled-components-vs-emotion-js-a-performance-perspective-4eia)
