---
title: JavaScript Interview Questions 9-12
category: JavaScript
date: 2020-07-27 23:00:00
author: dev-owen
---

# JavaScript Interview Questions 9-12

## 학습 목표

- 디자인 패턴 중 하나인 모듈 패턴(Module Pattern)에 대해 알아보고, 기존의 전통적 상속 방법과 비교해서 어떤 장단점이 있는지 알아본다.
- 호스트 객체(Host Objects)와 네이티브 객체(Native Objects)의 차이점에 대해서 알아본다.
- 함수 선언식(function statement)과 함수 표현식(function literal)의 차이점에 대해 알아본다.

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
원치 않은 다른 값을 변경하거나 변수나 메서드명의 충돌이 일어날 가능성도 있다. 이러한 부작용을 막기 위해 나타난 개념이 모듈 패턴이다.

모듈 패턴은 객체지향 프로그래밍에서 클래스의 컨셉을 반영하여 객체 내에서 변수를 선언하고 메서드로 조작할 수 있게 만드는 자바스크립트 디자인 패턴 중 하나이다. 
객체 내로 범위를 제한하기 때문에 private/public 캡슐화가 가능하고, 전역 범위에서 변수가 오염될 걱정을 하지 않아도 된다는 장점이 있다. 
모듈 패턴을 사용한 대표적인 라이브러리가 jQuery이다. 모듈 패턴은 클로저를 사용하여 다음과 같이 private 캡슐화를 수행한다.

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

## 호스트 객체(Host Objects)와 네이티브 객체(Native Objects)의 차이점은 무엇인가요?



## 다음 코드의 차이점은 무엇인가요?
```javascript
function Person() {}

const person = Person();

const _person = new Person();
```



## 참고자료
https://webclub.tistory.com/5
https://yubylab.tistory.com/entry/%EB%94%94%EC%9E%90%EC%9D%B8-%ED%8C%A8%ED%84%B4-for-javascript-Module-Pattern
https://addyosmani.com/resources/essentialjsdesignpatterns/book/#modulepatternjavascript
