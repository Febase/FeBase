---
title: ES Module에 대해서
date: 2020-06-25 00:00:00
author: nailerHeum
category: Javascript
---

# ES Module 에 대해서

---

## 학습 목표

- Module의 역사
- ES Module과 CommonJS Module의 차이를 알기
- ES Module의 작동 원리에 대해 알기

## ES Module은 자바스크립트의 공식적이며 표준화된 모듈 시스템이다.

---

### 문제 상황

 자바스크립트로 코딩할 때 변수들을 잘 관리하는 것이 중요하다.  변수를 관리하는 데 있어서 스코프를 잘 관리해야 한다. 스코프를 외부에서 공유하고 싶을 때는 상위의 스코프에 그 변수를 배치하는 방법이 있다. `jQuery` 의 경우 jQuery 플러그인들이 로드되기 전에 jQuery가 전역 스코프에 존재해야 하는 것도 그러한 이유이다.

 여러 스크립트 태그들이 난립하는 상황에서 코드들 사이의 의존성은 암시적이다. 전역 스코프에서 변수들을 관리하는 것은 암시적인 의존성 문제와 더불어 해당 변수에 대한 접근을 너무 쉽게 할 수 있어 고의적으로 또는 실수로 변수를 변조할 수 있는 가능성을 만든다.

### 해결책으로 등장한 모듈

 모듈을 통해 변수와 함수를 관리할 수 있다. 모듈은 함수와 변수들을 모듈 스코프에 넣는다. 모듈 내의 변수를 다른 모듈에서 사용할 수 있는 방법을 명시적으로 제공한다. 다른 모듈에서 사용하려면 `export` 와 `import`를 사용하면 된다. 다른 모듈에서 명시적으로 리소스를 사용할 수 있게 해준다.

 이를 통해 코드들을 독립적인 공간에서 작성하고, 조합할 수 있다. 이런 모듈들중 흔히들 알고 있는 모듈은 `CommonJS module`, `ES module`(ECMAscript modules)가 있다. 



## 자바스크립트와 모듈의 역사

---

 ES6 이전에는 ES Module이란 개념이 존재하지 않았다. 표준은 아니지만, 모듈 간 의존성 관리를 위해 AMD, CommonJS와 같은 모듈 개념들이 만들어졌고, 각 모듈 방식을 토대로 수 많은 파일을 한개 또는 몇 개의 파일로 합쳐주는 requireJS, Browserfy, Webpack 등의 번들러도 개발되었다. 사람들은 이를 통해 모듈 개발을 계속해왔고, **2015년에 ES6가 모듈 개념과 함께 등장한다.** ES6를 지원하는 환경이 많이 없었기 때문에 Babel을 통해 ES6 -> ES5, ES module을 CommonJS로 트랜스파일해주며 기존 모듈 방식을 대체해나갔다. ES6 등장 당시 webpack1은 ES6문법을 처리하지 못했기 때문에 Bable loader와 Webpack을 함께 사용하는 패턴을 많이 이용했다.  



## ES module vs CommonJS module

---

코드를 먼저 살펴보면

### commonJS module

**exporting**

```javascript
module.exports.hello = function () {console.log('hello')};
module.exports.numberOne = 1;

// or

module.exports = {
  hello: function() {console.log('hello')},
  numberOne: 1,
}
```

`module.exports` 객체를 조작한다. 이 객체에게 프로퍼티를 추가하거나, 다른 객체로 치환하는 방법을 사용한다.

**importing**

```javascript
const trashBin = require('./trashBin.js');
trashBin.hello();
trashBin.numberOne;
```

`require` 함수의 반환 값을 사용하는 형태이다.



### ES module

**exporting**

```javascript
export function hello() {console.log('hello')};
export const numberOne = 1;
```

다른 방법도 있다.

```javascript
function hello() {console.log('hello')};
const numberOne = 1;

export default { hello, numberOne };
```

`default` 를 이용한 내보내기는 한 번만 사용할 수 있다.

**importing**

```javascript
import { hello, numberOne } from './trashBin.js';

hello();
numberOne;
```





## ES module의 동작 방식 요약

---

 entry point인 파일에서 import 문들을 따라서 어떤 파일에 의존하는지를 알아낸다. 실행하게 되면, **Module Record** 라는 데이터 구조로 변환하기 위해 파일들을 모두 구문 분석한다. 

![](https://www.dropbox.com/s/112atwoy5or92hw/module_record.png?raw=1)

그리고 module record를 module instance로 변환시킨다. module instance는 코드와 상태를 결합한다. 코드는 명령어의 집합이고, 상태는 해당 시점에서의 변수값들을 의미한다. 

![](https://www.dropbox.com/s/hzmzkshzxc6onb1/code_state.png?raw=1)

 ES Module은 세가지 단계로 진행된다.

1. 구성 - 모든 파일을 찾아 다운로드하고 Module record로 구문 분석한다.
2. 인스턴스화 - export된 값을 모두 배치하기 위해 메모리에 있는 빈 공간들을 찾고 export와 import들이 메모리 공간들을 가리키게 한다. (**Linking**)
3. 평가 - 코드를 실행하여 메모리 안의 값을 변수의 실제 값으로 채운다.



**ES module 명세**는 위 3가지를 수행하는 방법을 알려주지만 파일을 처음에 어떻게 얻어 오는지에 대해 명시하지 않았다.

 파일을 불러오는 것은 **Loader** 인데 브라우저의 경우 HTML 명세를 따르고, 다른 경우에는 다른 로더를 가질 수 있다. 모듈을 불러오는 정확한 방식은 로더가 제어하는데 ES module의 경우 ES module method(`ParseModule`, `Module.Instantiate`, `Module.Evaluate`)라고 불린다.



### 평가 질문

---

1. 모듈이 왜 필요한가요?
2. ES Module은 언제 등장했나요?
3. ES Module이 모듈을 불러오는 과정을 설명해주세요.



 CommonJS 모듈 방식을 주로 사용해왔기 때문에 ES module에 대해 생소하기도 했고, 애초에 모듈의 동작 방식에 대해 깊게 생각해볼 일이 별로 없었기에 이번 공부가 새롭게 느껴졌다. 모듈 동작 방식에 대해서 깊게 알고 싶다면 module deep dive링크를 따라가 읽어볼 수 있다.



### Reference

---

[You don't know JS module](https://ui.toast.com/weekly-pick/ko_20190418/)

[ES module 심층 탐구](https://ui.toast.com/weekly-pick/ko_20180402/)

[module deep dive](http://www.webdesignagencymiami.org/sera-modules-a-cartoon-deep-dive/)

