---
title: JavaScript Interview Questions 9-12
category: interview
date: 2020-07-27 23:00:00
author: dev-owen
---

<br>

# JavaScript Interview Questions 9-12

<br>

## 학습 목표

- 디자인 패턴 중 하나인 모듈 패턴(Module Pattern)에 대해 알아보고, 기존의 전통적 상속 방법과 비교해서 어떤 장단점이 있는지 알아본다.
- 호스트 객체(Host Objects)와 네이티브 객체(Native Objects)의 차이점에 대해서 알아본다.
- 함수 선언식(function statement)과 함수 표현식(function literal)의 차이점에 대해 알아본다.

<br>

## 당신은 코드를 어떻게 구현하나요? (모듈 패턴, 전통적 상속)

모듈(module)은 전체 어플리케이션의 일부분을 독립적인 코드로 분리해서 만들어 놓은 것을 의미한다. 모듈을 구현하는 방법에는 여러가지 방법이 있다. 
그 중에 대표적인 방법들은 다음과 같다.

- 모듈 패턴 (The Module Pattern)
- 객체 리터럴 (Object Literal notation)
- AMD 모듈 (AMD Modules)
- CommonJS 모듈 (CommonJS Modules)
- ECMAScript 하모니 모듈 (ECMAScript Harmony Modules)

아마 이 글을 읽는 분들이 모듈을 구현하는 가장 익숙한 구현 방법은 객체 리터럴 방식이 아닐까 싶다.

```javascript
var myModule = {
  myProperty: "someValue",
  saySomething: function() {
    // ...
  }  	
}
myModule.myProperty; // someValue
myModule.saySomething();
```

이와 같은 객체 리터럴 방식을 통해서 코드를 캡슐화 하고 구조화 할 수가 있다. 하지만 이와 같이 수많은 모듈을 전역 스코프에서 사용하게 될 경우 
원치 않은 다른 값을 변경하거나 변수나 메서드명의 충돌이 일어날 가능성도 있다. 이러한 부작용을 막기 위해 나타난 개념이 `모듈 패턴`이다.

모듈 패턴은 객체지향 프로그래밍에서 클래스의 컨셉을 반영하여 객체 내에서 변수를 선언하고 메서드로 조작할 수 있게 만드는 자바스크립트 디자인 패턴 중 하나이다. 
객체 내로 범위를 제한하기 때문에 private/public 캡슐화가 가능하고, 전역 범위에서 변수가 오염될 걱정을 하지 않아도 된다는 장점이 있다. 
모듈 패턴을 사용한 대표적인 라이브러리가 jQuery이다. 모듈 패턴은 `클로저`를 사용하여 다음과 같이 private 캡슐화를 수행한다.

```javascript
var testModule = (function () {
  var counter = 0;
  function doSomethingPrivate() {
    // ...
  }
  return {
    incrementCounter: function() {
      return counter++;
    }
  };   
})();

testModule.incrementCounter();
```

이와 같이 코드를 작성하게 되면, 외부에서 incrementCounter() 메서드를 직접 접근하는 것이 불가능하고, counter 변수와 doSomethingPrivate 함수는 전역 범위에서 보호를 받을 수 있다. 
내부의 모든 리소스는 반드시 testModule 모듈을 통해서 접근해야 한다. 

그렇다면 모듈 패턴의 장점과 단점은 무엇일까?

### 장점

- 객체지향적으로 자바스크립트 코드를 구현할 수 있다.(은닉화, 다형성, 상속 등)
- 전역 범위에서 변수가 오염될 걱정을 하지 않아도 된다.

### 단점

- private/public 멤버를 다른 방식으로 접근해야 한다.
- private 멤버를 직접 접근할 수가 없기에, 테스트가 불가능하고 버그 수정하는 과정에서 조금 더 원인을 찾기가 어려울 수 있다.

<br>

## 호스트 객체(Host Objects)와 네이티브 객체(Native Objects)의 차이점은 무엇인가요?

`호스트 객체`는 브라우저 환경에서 제공하는 window, XMLHttpRequest, HTMLElement 등의 DOM 노드 객체와 같이 호스트 환경에 정의된 객체를 말한다. 
예를 들어 브라우저에서 동작하는 환경과 브라우저 외부에서 동작하는 환경의 자바스크립트(Node.js)는 다른 호스트 객체를 사용할 수 있다. 
브라우저에서 동작하는 환경의 호스트 객체는 전역 객체인 window, BOM(Browser Object Model)과 DOM(Document Object Model) 및 XMLHttpRequest 객체 등을 제공한다.

BOM(Browser Object Model) : 브라우저 객체 모델은 브라우저 탭 또는 브라우저 창의 모델을 생성한다. 최상위 객체는 `window` 객체로 현재 브라우저 창 또는 탭을 표현하는 객체이다.

![BOM](https://poiemaweb.com/img/BOM.png)

DOM(Document Object Model) : 문서 객체 모델은 현재 웹 페이지의 모델을 생성한다. 최상위 객체는 `document` 객체로 전체 문서를 포함한다.

![DOM](https://poiemaweb.com/img/DOM.png)

`네이티브 객체`는 ECMAScript 명세에 정의된 객체를 말하며, 어플리케이션 전역의 공통 기능을 제공한다. 네이티브 객체는 어플리케이션 환경과 관계없이 언제나 사용할 수 있다. 
Object, String, Number, Boolean, Function, Array, RegExp, Date, Math, Symbol 등과 같은 객체 생성에 관계가 있는 함수 객체와 메소드로 구분된다. 
원시 타입 값(string, number, boolean)에서 표준 빌트인 객체의 메서드로 호출할 때 Wrapper 객체로 일시 변환이 되는데, 이러한 Wrapper 객체에는 String, Number, Boolean 객체가 포함이 된다.

네이티브 객체를 Global Objects 라고 부르기도 하는데, 이는 전역 객체(Global Object)와는 다른 의미이므로 혼동하지 말아야 한다. 
전역 객체는 모든 객체의 최상위 객체를 의미하며 Client-side에서는 window, Server-side(Node.js)에서는 global을 가리킨다.

<br>

## 다음 코드의 차이점은 무엇인가요?
```javascript
function Person() {}

var person = Person();

var _person = new Person();
```

첫 번째 식은 함수 선언식(Function Declaration)이다. ES5까지는 이 방식으로 클래스를 생성하였다. (ES6부터는 class 키워드로 클래스를 정의한다.)
이 식만 가지고 실행은 되지 않는다. 하지만 전역 범위 네임스페이스에 해당 함수가 등록이 된다. 

두 번째 식은 함수 표현식(Function Expression)이다. 새로 정의된 person 변수는 Person 함수의 값을 참조한. 모든 함수 표현식은 return 값을 가진다.
만약 함수에 이름이 없을 경우 익명 함수로 할당이 되며, {} 로 감싸지는 식이 된다.

세 번째 식은 Person 클래스의 객체 인스턴스를 생성하며 동시에 해당 클래스의 생성자가 호출되는 식이다.
자바스크립트에서는 함수 자체가 그 객체의 생성자 역할을 하기 때문에 특별히 생성자 메서드를 정의할 필요가 없다. 클래스 안에 선언된 모든 내역은 인스턴스화되는 그 시간에 실행된다.

<br>

## 셀프 체크

1. 모듈 패턴은 ______ 를 사용하여 클래스의 private 캡슐화를 수행할 수 있다.
2. 브라우저 객체 모델(BOM)의 최상위 객체는 ______ 이고, 문서 객체 모델(DOM)의 최상위 객체는 ________ 이다.
3. 원시 타입 값에서 표준 빌트인 객체의 메서드를 호출하면 __________ 로 일시 변환된다.
4. var _person = new Person() 의 방식으로 객체 인스턴스를 생성하면 해당 클래스의 ______ 을 자동으로 호출한다.

<br>

## 참고자료

- https://webclub.tistory.com/5
- https://yubylab.tistory.com/entry/%EB%94%94%EC%9E%90%EC%9D%B8-%ED%8C%A8%ED%84%B4-for-javascript-Module-Pattern
- https://addyosmani.com/resources/essentialjsdesignpatterns/book/#modulepatternjavascript
- https://poiemaweb.com/js-built-in-object
- https://joshua1988.github.io/web-development/javascript/function-expressions-vs-declarations/
- https://developer.mozilla.org/ko/docs/Web/JavaScript/Introduction_to_Object-Oriented_JavaScript
- https://poiemaweb.com/es6-class
- https://medium.com/@rlynjb/js-interview-question-difference-between-function-person-var-person-person-and-var-ab6eb8c9ae88
