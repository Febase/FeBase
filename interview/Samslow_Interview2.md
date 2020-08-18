---
title: FE Interview 5
date: 2020-08-05 00:00:00
author: samslow
category: Interview
---

- 아래 질문에 답할 수 있습니다.
  - document load event와 DOMContentLoaded event의 차이점은 무엇인가요?
  - `==`와 `===`의 차이점은 무엇인가요?
  - JavaScript의 "동일출처정책(the same-origin policy)"에 대해서 설명하세요.

# `document load` 이벤트와 `document DOMContentLoaded` 이벤트의 차이점은 무엇인가요?

document는 HTML 문서의 핵심을 담고있는 객체로 window의 자식 객체이다.

문제의 2가지 이벤트는 모두 생명주기중 하나인데 DOM이 로드될때 갖는 흐름이다.

- `DOMContentLoaded`
  - 브라우저가 HTML을 전부 읽고 DOM 트리를 모두 완성하면 즉시 발생한다.
  - 이미지파일, CSS는 기다리지 않는다.
  - 이때 `<img />` 가 참조는 되지만 사이즈는 0x0으로 나온다.
  - `document.addEventListenr('DOMContentLoaded', ...)`로 사용
- `load`
  - HTML로 DOM 트리가 만들어지고 CSS, JS와 Assets들이 모두 load되면 발생한다.
  - Assets들의 실제 크기를 알려면 이때를 이용해야한다.
  - `window.onload`로 사용

# `==`와 `===`의 차이점은 무엇인가요?

JS에서 JS Magic을 쉽게 경험 할 수 있는 비교연산자이다.

다만, `==` 는 타입이 다르면 타입을 서로 같게 변환 해 주고, `===` 는 타입 변환도 하지 않고 값을 비교한다.

즉, `==` 는 타입이 달라도 값만 같으면 `true` 를 반환하고 `===` 는 타입과 값 모두 값아야 `true`를 반환한다.

다음 JS Magic을 통해서 `==` 이 어떻게 위험한지 확인 해 보자

```js
1 == "1"; // true
1 == [1]; // true
1 == true; // true
0 == ""; // true
0 == "0"; // true
0 == false; // true
```

<div align="center" style="color: gray">WONDERFUL</div>

편의를 위해 `null`과 `undefined` 를 비교할 때를 제외하고는 `==` 은 사용하지 않도록 하자.

# JavaScript의 "동일출처정책(the same-origin policy)"에 대해서 설명하세요.

> 동일 출처 정책(same-origin policy)은 어떤 출처에서 불러온 문서나 스크립트가 다른 출처에서 가져온 리소스와 상호작용하는 것을 제한하는 중요한 보안 방식입니다. 동일 출처 정책은 잠재적으로 해로울 수 있는 문서를 분리해, 공격받을 수 있는 경로를 줄입니다. _MDN_

즉, 웹 브라우저가 보안을 위해 프로토콜, 호스트, 포트가 동일한 서버로만 비동기 요청을 주고 받을 수 있도록 한 정책이다.

프로토콜, 호스트, 포트는 크롬 개발자 도구에서 `location`을 찍어보면 알 수 있다.

![location](https://www.dropbox.com/s/6t272nxvf1bh23v/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202020-08-05%2004.24.41.png?raw=1)

다시 말해 동일 출처 정책이란 같은 **Origin 출처의 서버로만 요청을 주고 받을 수 있다는 것이다.**

- `http://www.same-domain.com/` --> `http://www.same-domain.com` = `same-origin`
- `http://www.same-domain.com` -/-> `http://www.cross-domain.com` = `cross-origin`

뿐만 아니라 `https:` 의 기본 포트인 443에서 같은 origin의 8080포트로 요청을 보내도 `cross-origin`이 뜬다.

이를 해결하기 위해서 자주 접하는 단어인 CORS를 사용한다.

> Cross-Origin Resource Sharing(CORS) 은 추가 HTTP 헤더를 사용하여 브라우저가 한 출처에서 실행중인 웹 애플리케이션에 선택된 액세스 권한을 부여하도록하는 메커니즘입니다. 다른 출처의 자원. **웹 응용 프로그램은 자체와 다른 출처 (도메인, 프로토콜 또는 포트)를 가진 리소스를 요청할 때 cross-origin HTTP 요청을 실행**합니다._MDN_

즉, _Same-Origin Policy의 문제점을 해결하기 위한 정책인 만큼_ **CORS란 cross-Origin 즉, 출처가 다른 도메인에서의 AJAX요청이라도 서버 단에서 데이터 접근 권한을 허용하는 정책**이다.

이를 해결하려면 아래 방법 중 하나를 시도 할 수 있다.

- 서버
  - `Access-Control-Allow-Origin` 응답 헤더에 `*` 로 처리해서 모든 도메인 가능하도록 하기
  - 미들 웨어(보통 library 사용)
- 클라이언트
  - 프록시 설정
    - ![img](https://media.vlpt.us/post-images/yejinh/8650aaa0-3111-11ea-9a27-fbf26c473eb5/Proxy-Server.png)
    - 다양한 이유로 (주로 보안의 문제로) 직접 통신하지 못하는 두 개의 컴퓨터 사이에서 서로 통신할 수 있도록 돕는 역할을 가리켜 프록시라 일컫는다.
    - 클라이언트 - 서버 중간에서 요청을 받아 `Access-Control-Allow-Origin`헤더를 추가해주는 중간 다리 역할을 놔주는 방법으로 해결할 수 있다.

# Mini Coding Test

다음이 작동하도록 JS 를 작성 해 보세요.(EASY)

```js
duplicate([1, 2, 3, 4, 5]); // [1,2,3,4,5,1,2,3,4,5]
```

해결 방법에는 여러가지가 있지만 아래와 같이 함수를 만들어 해결 할 수 있을 것이다.

```js
const duplicate(arr) => {
  return arr.concat(arr)
}
```

# Self check

1. 만약 HTML 문서 끝에 `<script />` 가 있다면, `DOMContentLoaded` 는 `<script />` (이전/ 이후)에 발생한다.

   - 단, `______` 속성이 있는 `<script />`나 `<script />` 내에 동적으로 생성된 엘리먼트가 있을 경우에는 `DOMContentLoaded` 를 막지 않는다.

2. ```js
   <script>
     document.addEventListener('DOMContentLoaded', () => log('DOMContentLoaded')); ···  1

     window.onload = () => log('window onload'); ···  2
   </script>

   <iframe src="iframe.html" onload="log('iframe onload')"></iframe> ··· 3

   <img src="http://en.js.cx/clipart/train.gif" id="img" />
   <script>
     img.onload = () => log('img onload'); ··· 4
   </script>
   ```

   위 코드에서 log가 찍히는 결과는 ?

3. `null == undefined`의 결과와 이유는 ?
4. Array.prototype의 method중 concat()과 join()의 차이점은?

# Reference

- https://ko.javascript.info/onload-ondomcontentloaded
- https://velog.io/@yejinh/CORS-4tk536f0db
