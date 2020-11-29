---
title: storybook
date: 2020-11-26 00:00:00
author: chjjh0
category: S2_Round1
---

## 특징

- bootstrap, materialUI 같은 CSS 프레임워크에서 제공하는 요소 팔레트와 유사하게 컴포넌트를 관리
- 컴포넌트 문서화를 통해 테스트, 유지보수에 유용
- 다양한 환경에서 활용 가능 (HTML, React, Vue, Svelte 등)
<br>
<br>
<br>

> 기본 사용법

```javascript
// CRA로 React Project 생성
npx create-react-app taskbox

// 생성된 프로젝트에 스토리북 추가 & 초기화
npx -p @storybook/cli sb init

// 스토리북 실행
npm run storybook
```

### sb init, 스토리북 초기화 [(링크)](https://storybook.js.org/docs/react/get-started/install)

- 사용자가 직접 작성해야할 것들이 자동으로 추가됨
1. package.json에 dependencies, scripts 추가

  ```javascript
  "devDependencies": {
    "@storybook/addon-actions": "^6.1.3",
    "@storybook/addon-essentials": "^6.1.3",
    "@storybook/addon-links": "^6.1.3",
    "@storybook/node-logger": "^6.1.3",
    "@storybook/preset-create-react-app": "^3.1.5",
    "@storybook/react": "^6.1.3"
  }
  "scripts": {
      "start": "react-scripts start",
      "build": "react-scripts build",
      "test": "react-scripts test",
      "eject": "react-scripts eject",
      "storybook": "start-storybook -p 6006 -s public",
      "build-storybook": "build-storybook -s public"
    },
  ...
  ```

2. storybook 폴더에 storybook 설정 파일 추가 <br>
 ![stories config files](https://user-images.githubusercontent.com/39721166/100541483-9cf1d400-3287-11eb-9094-cbaedf249f9e.png)


3. stories 폴더에 보일러플레이트 파일들 추가 <br>
  ![stories folder capture](https://user-images.githubusercontent.com/39721166/100540900-a5e0a680-3283-11eb-9ed6-085566474e9b.png)

<br>
<br>

> 예제

<b>Button.js<b>

```javascript
export const Button = ({ primary, backgroundColor, size, label, ...props }) => {
    // primary or secondary 모드
  const mode = primary ? 'storybook-button--primary' : 'storybook-button--secondary';

  return (
    <button
      type="button"
      className={['storybook-button', `storybook-button--${size}`, mode].join(' ')}
      style={backgroundColor && { backgroundColor }}
      {...props}
    >
      {label}
    </button>
  );
};
```

<b>Button.css<b>

```css
.storybook-button {
  font-family: 'Nunito Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif;
  font-weight: 700;
  border: 0;
  border-radius: 3em;
  cursor: pointer;
  display: inline-block;
  line-height: 1;
}
.storybook-button--primary {
  color: white;
  background-color: #1ea7fd;
}
.storybook-button--secondary {
  color: #333;
  background-color: transparent;
  box-shadow: rgba(0, 0, 0, 0.15) 0px 0px 0px 1px inset;
}
.storybook-button--small {
  font-size: 12px;
  padding: 10px 16px;
}
.storybook-button--medium {
  font-size: 14px;
  padding: 11px 20px;
}
.storybook-button--large {
  font-size: 16px;
  padding: 12px 24px;
}
```

<b>Button.stories.js<b>

```javascript
import React from 'react';

import { Button } from './Button';

export default {
  title: 'Example/Button',
  component: Button,
  argTypes: {
    backgroundColor: { control: 'color' },
  },
};

const Template = (args) => <Button {...args} />;

export const Primary = Template.bind({});
Primary.args = {
  primary: true,
  label: 'Button',
};

export const Secondary = Template.bind({});
Secondary.args = {
  label: 'Button',
};

export const Large = Template.bind({});
Large.args = {
  size: 'large',
  label: 'Button',
};

export const Small = Template.bind({});
Small.args = {
  size: 'small',
  label: 'Button',
};
```

<details>
<summary>관련 링크</summary>

- [args 설명](https://storybook.js.org/docs/react/writing-stories/args)
- [control 설명](https://storybook.js.org/docs/react/essentials/controls#gatsby-focus-wrapper)
- [storybook 5.2버전 이상부터 달라진 stories 작성 방법, CSF(Component Story Format)](https://storybook.js.org/docs/react/api/csf)

</details>

<br>
<br>

> 실행 결과

### 화면 영역별 특징
<details>
<summary>실행결과 Sample</summary>

- [react-dates](http://airbnb.io/react-dates/?path=/story/daterangepicker-drp--default)
- [storybook](https://storybook.js.org/docs/react/get-started/examples#gatsby-focus-wrapper)
</details>

<br>


- Preview 영역: Manager영역에서 선택한 story를 보여줌, iframe으로 되어있음
- Manager 영역: story들을 폴더구조로 볼 수 있음
- Preview, Manager 영역은 Storybook Communication Channel을 통해 데이터 전달

![storibookArea](https://user-images.githubusercontent.com/39721166/100540962-28696600-3284-11eb-8745-0750a7f64562.png)

- manager 영역에 폴더 구조로 관리<br>
( stories 파일에서 선언한 title: Example/Button )

<div>
  <img src='https://user-images.githubusercontent.com/39721166/100541008-65355d00-3284-11eb-9222-1fb3587e7818.png'>
  <img src='https://user-images.githubusercontent.com/39721166/100541010-66668a00-3284-11eb-8089-bf55385a303d.png'>
</div>
<br>

- stories파일과 컴포넌트의 props prototype을 참고하여 자동으로 아래와 같은 UI가 만들어짐

![controlPannel](https://user-images.githubusercontent.com/39721166/100541028-7f6f3b00-3284-11eb-955f-02c3dc6e3c22.png)


<details>
<summary>관련 링크</summary>

- [컴포넌트 공유 서비스](https://bit.dev/)
- [공식문서의 예제](https://storybook.js.org/docs/examples/)

</details>