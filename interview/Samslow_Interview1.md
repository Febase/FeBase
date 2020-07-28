---
title: FE Interview - prototype위주로 조져보자
date: 2020-07-28 00:00:00
author: samslow
category: Interview
---

- Javascript 상속과 Prototype에 관한 FE Interview 질문을 알아봅니다.

# 어떻게 할 것이냐

이번주부터는 FE Interview에 있는 질문들에서 Keyword를 뽑아 JS 기초를 다져보려고 한다.

질문들은 [여기](https://github.com/h5bp/Front-end-Developer-Interview-Questions/tree/master/src/translations/korean#JS-관련-질문)에서 볼 수 있고, 필자가 진행중인 스터디에서 동시에 진행중인 다른 질문은 [여기](https://github.com/Febase/FeBase)에서 볼 수 있다.

이번에는 JS Prototype과 상속에 관한 질문 위주로 4가지를 뽑아서 정리하려고 한다.

# `.call`과 `.apply`의 차이점은 무엇인가요?

기본적으로 함수 호출과 연관이 있는 메서드들이다.

예시로 이해하는게 빠르니 아래 코드를 보자

```javascript
let person1 = {
  name: "Jo",
};

let person2 = {
  name: "Kim",
  study: function (lastPoint1 = ".", lastPoint2 = "!") {
    console.log(
      this.name + "이/가 공부를 하고 있습니다" + lastPoint1 + lastPoint2,
    );
  },
};

person2.study(); // Kim이/가 공부를 하고 있습니다.!

// call()
person2.study.call(person1, "?", "~"); // Jo이/가 공부를 하고 있습니다?~

// apply()
person2.study.apply(person1, ["?", "~"]); // Jo이/가 공부를 하고 있습니다?~
```

**여기서 call()과 apply()의 사용을 보면 `person2` 에만 있는 `study` 메서드를 `person1` 이 사용할 수 있도록 하고있다.**

즉, 첫번째 매개변수를 통해 실행 문맥의 this를 정할 수 있도록 하는 것이다.

그리고 2번째 인자부터는 해당 메서드의 매개변수를 넣는 것이다.

**여기서 call()과 apply()의 차이점은 call은 인수를 순서대로 받지만 apply는 인수를 유사 배열로 받는다.**

그럼 유사배열이란 무엇일까?

![유사배열](https://www.dropbox.com/s/lzw34u94ltvx3yj/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202020-07-28%2004.44.47.png?dl=1)

크롬 개발 도구로 찍으면 나오는 위 사진처럼, 배열은 배열인데 Array.prototype을 상속받는 배열은 아닌 배열을 유사배열이라고 한다.

이것을 더 확실히 알고 싶다면 `instanceof`를 사용 해 볼 수 있다.

```js
const arr = [1, 2, 3, 4, 5];
const tags = document.getElementsByTagName("div");

arr instanceof Array; // true
tags instanceof Array; // false
```

유사배열과 배열의 차이점은 단지 Array.prototype의 메서드를 사용 할 수 없다.

유사배열이 가능한 이유는 Array도 Object이기 때문임을 알고 넘어가자.

call()과 apply()는 this 실행 문맥을 가져와서 실행 할 수 있다는 공통점이 있지만, 매개변수를 받는 방법에 있어서

call은 순서대로 받고 apply는 유사배열로 받는다는 차이점이 있다.

# Funtion.prototype.bind 를 설명하세요

위에서 설명한 apply, call과 세트인 3종 세트인 메서드다.

간단하게 말하면, apply·call은 메서드의 결과를 리턴하고 bind는 메서드 자체를 리턴한다.

bind는 원본 함수 객체를 감싸서 새롭게 바인딩하는 함수를 만드는데 이때 this를 바꾸는 것은 apply·call과 같지만 새롭게 감싸진 함수를 리턴한다.

이때 추가 매개변수는 call의 그것처럼 인자를 순서대로 받는 방식을 사용한다.

```javascript
let person1 = {
  name: "Jo",
};

let person2 = {
  name: "Kim",
  study: function (lastPoint1 = ".", lastPoint2 = "!") {
    console.log(
      this.name + "이/가 공부를 하고 있습니다" + lastPoint1 + lastPoint2,
    );
  },
};

person2.study(); // Kim이/가 공부를 하고 있습니다.!

// bind()
let student = person2.study.bind(person1, "!", "?");

student(); // Jo이/가 공부를 하고 있습니다!?
```

bind는 주로 React에서 Class Component를 작성할때 자주 마주치게 되는데 Component 상속을 할 때

**부모 Component의 this 실행 문맥을 가져오기 때문에** bind로 현재 Component의 this 실행 문맥으로 교체 해 주는 것이다.

# `document.write()`는 언제 사용하나요 ?

위 메서드를 Google에 검색 해 보면 알겠지만 2010년 글이 최신으로 올라 올 만큼 지금은 자주 사용되지 않는 메서드로 알려져있다.

왜냐하면, 크롬 개발 도구에서 그대로 쳐보면 알 수 있듯이 모든 document를 날려버리고(document.open) 새로 인자로 들어온 요소를 사용하기 때문이다.

단, IE에 대한 호환성 문제나 스크립트 병렬 로딩이 특수한 상황에서 필요할 때, 그리고 성능적인 문제로 새로 모든것을 시작하고 싶을 때(?) 사용 할 수 있다.

예를 들면, 계속 사용하던 브라우저 탭에서 A라는 링크를 클릭하는 시간보다 해당 링크를 새창에서 입력하면 더 빠르게 로딩 될 수 있다.

이게 가능한 이유는 현재까지 사용하던 브라우저는 과거의 내용에 대한 네비게이션과 JS 그리고 요새 브라우저들에 따라다니는 트래커들 때문에 리소스가 더 사용되지만

새창은 document.write()를 사용하므로 기존 리소스를 로드 할 필요가 없기 때문이다.

# UA 문자열을 이용하여 기능 검출(feature detection)과 기능 추론(featrue inference)의 차이점을 설명하세요

이 질문에서는 새로운 Keyword가 3가지나 등장하므로 이를 먼저 알고가자

- UA 문자열: User Agent String의 약어로 브라우저에서 어떤 사이트에 접속하면 서버는 요청한 브라우저가 어떤 브라우저인지에 따라 그에 맞게 결과를 보여준다. 예를들어 내가 Chrome으로 Naver를 들어가면 Naver 서버에는 User Agent로 아래 값을 받게 될 것이다.

  ```js
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36";
  ```

  이러한 정보는 광고 솔루션에서 유저를 트래킹할 때도 유용하고, 특정 브라우저에서 사이트 이용을 제한할 때도 사용 할 수 이싿.

- 기능 검출(feature detection) : 브라우저가 환경이 특정 기능을 제공하거나 제공하지 않을 수있는 단서를 프로그래밍 방식으로 테스트하여 런타임 환경 간의 차이를 처리하기 위해 웹 개발에 사용되는 기술

  ```js
  if ("geolocation" in navigator) {
    // navigator.geolocation를 사용할 수 있습니다
  } else {
    // 부족한 기능 핸들링
  }
  ```

- 기능 추론(feature inference): feature detection 처럼 기능을 확인하는 것은 똑같지만, A 라는 기능이 있을 때 B 도 있을거라고 추론하기 때문에 특정 상황이 아니면 사용 하지 않는 기법

  ```js
  if (document.getElementsByTagName) {
    element = document.getElementById(id);
  }
  ```

이렇게 3가지를 알고 문제를 다시 보면 조금 이해가 되는가?

UA 문자열을 가지고 해당 유저의 환경에 대한 정보를 모두 가져 올 수 있는것을 활용해 두 패턴에 대해 예시를 들어 설명 해 보자면

호환성 문제로 인해 Internet Explorer 지원을 하지 않기로 한 웹 서비스가 있다고 해보자.

그럼 이때 FE 개발자는 UA를 가지고 Internet Explorer 를 감지 할 수 있을 것이다.

```js
if (navigator.userAgent == "Chrome") {
  // navigator.userAgent는 UA 를 얻을 수 있는 메서드
  // do original things
} else {
  alert("IE에서는 동작하지 않습니다. chrome을 이용하세요"); // Feature Detection의 예시

  history.push("http://chrome-download-link"); // Featrue inference의 예시
}
```

두 방식을 pseudo code 로 구현한 내용이다.

alert()으로 알려주는 방식은 IE에서 잘 동작해서 경고를 띄워주겠지만(IE에서 페이지를 이동 해 주는 메서드가 없다는 전제)

Feature inference 방식으로 작성한 history.push()는 IE에서 지원하지 않기 때문에 작동하지 않을 가능성이 크다.

둘의 차이는 얼마나 추론과 탐지를 하느냐인데, 후자인 Feature inference는 특정 상황이 아니라면 사용하지 말아야 한다.

# Self check

1. (본문에 없음) js에서 예약어로 사용되고있으며, 함수의 매개변수를 모두 가져 올 수 있는 것은?
2. 유사 배열이란 무엇인가요?
3. 링크를 클릭해 웹 사이트를 여는 것과 새창에서 여는것의 시간 차이가 서로 다른 이유는 무엇인가요?
4. User Agent를 크롬 개발 도구에서 알 수 있는 방법은?

# Reference

- [https://velog.io/@josworks27/%ED%95%A8%EC%88%98%ED%98%B8%EC%B6%9C-call-apply-bind-%EC%B0%A8%EC%9D%B4](https://velog.io/@josworks27/함수호출-call-apply-bind-차이)
- [ZeroCho](https://www.zerocho.com/category/JavaScript/post/5af6f9e707d77a001bb579d2)
