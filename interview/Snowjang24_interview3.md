---
title: FE Interview
date: 2020-08-12 00:00:00
author: snowjang24
category: interview
---

## 오늘의 FE 질문

1. 전역 scope를 사용했을 때 장단점에 관해 설명해주세요.
2. 때때로 load event를 사용하는 이유에 관해 설명해주세요. 또 단점이 있다면 대안에 대해서도 설명해주세요.

## 전역 scope를 사용했을 때 장단점에 관해 설명해주세요.

### a. 장점

- 제작한 어플리케이션의 모든 모듈과 함수에서 글로벌 변수에 접근할 수 있다.
- 변수를 여러번 선언할 필요 없이, 모듈 밖에서 한 번만 선언해도 된다.
- 일관성 유지에 유용하기 때문에, 상수에 해당하는 값을 저장할 때 사용할 수 있다.
- 다양한 함수에서 공통으로 써야하는 변수가 있다면 유용하다.

### b. 단점

- 글로벌로 여러 변수가 선언되면 프로그램 실행이 끝날때 까지 해당 변수의 메모리를 유지하기 때문에 메모리 문제를 유발한다.
- 코드 리팩토링의 이유로 변수명을 변경해야할 때, 다른 모든 모듈 혹은 함수에서 해당 변수명을 직접 바꿔줘야하는 번거로움이 발생할 수 있다.
- 모듈 단위로 코드를 작성 시, 변수명을 모두 기억하지 못하면, 모듈 혹은 함수 내에 선언된 지역 변수와 충돌할 수 있다.
- 글로벌 변수는 모든 함수에서 수정이 가능하다. 따라서 다른 함수에서 수정이 이뤄지는 경우에 예상하지 못한 문제를 야기할 수 있다.

장점보다는 단점이 더 명확하기 때문에 상수 선언 이외에는 전역에 선언하는 것을 지양하는 것이 좋다.

## 때때로 load event를 사용하는 이유에 관해 설명해주세요. 또 단점이 있다면 대안에 대해서도 설명해주세요.

### `load` 이벤트를 사용하는 이유

`load` 이벤트가 발생되는 시점은 객체가 모두 로드 되었을 때 발생한다. 보통 웹 페이지의 모든 콘텐츠(이미지, 스크립트 파일, CSS 파일 등)가 로드된 이후 스크립트를 실행하기 위해, `document` 혹은 `<body>`에 Event Listener를 추가한다. 

```javascript
EventTarget.addEventListener('load', EventHandler);
```

`document`, `<body>` 외에도 `load` 이벤트는 아래의 태그들에서 사용이 가능하다.

```html
<body> <frame> <iframe> 
<img> <input type="image"> <link> 
<script> <style>
```

`document`, `<body>`에서 사용하는 것과 이유는 동일하지만 개개의 요소들이 로드된 이후 어떠한 작업을 하고싶을 때 쓸 수 있다.

추가적인 활용으로, `load` 이벤트는 방문자의 브라우저 유형 및 브라우저 버젼을 확인하고 해당 정보를 기반으로 적절한 버전의 웹 페이지를 로드하는데 이용할 수 있다.

또한 쿠키를 처리하는데 활용 가능하다.

```html
<body onload="checkCookies()">
<script>
function checkCookies() {
    var text = "";
    if (navigator.cookieEnabled == true) {
        text = "Cookies are enabled.";
    } else {
        text = "Cookies are not enabled.";
    }
    document.getElementById("demo").innerHTML = text;
}
</script>
```

### `load` 이벤트 사용의 단점과 그 대안

`load` 이벤트는 문서내의 모든 콘텐츠(이미지, 스크립트 파일, CSS 파일 등)의 로드가 끝난 후에 실행된다. 네트워크의 상황 혹은 로드해야하는 콘텐츠의 크기에 따라, 에플리케이션의 구동이 지연될 가능성이 생길 수 있다. 

이에 대한 대안으로 `DOMContentLoaded` 이벤트를 사용할 수 있다. `DOMContentLoaded`는 `load` 이벤트와는 달리, 모든 콘텐츠가 로드되기를 기다리지 않는다. 브라우저가 HTML을 읽고 DOM 트리를 완성하는 즉시 해당 이벤트가 발생한다. 따라서, `load` 에서 발생할 수 있는 지연 문제가 발생하지 않는다. 

DOM에 대한 접근만을 필요로 하는 경우, `DOMContentLoaded`는 `load`의 대안이기도 하지만 콘텐츠가 로드된 이후 어떠한 스크립트를 동작시켜야하는 상황에서는 `load` 이벤트를 사용하는 것이 옳다(이미지의 크기와 관련된 스크립트 처리 등의 경우).

각각의 특징을 잘 파악하고 적절하게 잘 사용하는 것이 중요하다.

## Self Check

- `load` 이벤트는 `document`에서만 발생한다. (O / X)
- 전역 스코프를 사용했을 때 장점 두 가지
- `DOMContentLoaded`는 콘텐츠가 로드되는 것을 모두 기다린 이후 이벤트가 발생한다. (O / X)

## Reference

- [Difference between Local and Global Variable](https://www.guru99.com/local-vs-global-variable.html)
- [onload Event - W3Schools](https://www.w3schools.com/jsref/event_onload.asp)