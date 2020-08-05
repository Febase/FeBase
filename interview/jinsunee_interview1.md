---
title: FE Interview - prototype위주로 조져보자
date: 2020-08-05 00:00:00
author: jinsunee
category: Interview
---

1. 다음 코드가 즉시 호출 함수 표현식(IIFE)로 동작하지 않는 이유에 관해서 설명해보세요: `function foo(){ }();`.
2. null과 undefined 그리고 undeclared의 차이점은 무엇인가요?
3. 클로져(Closure)는 무엇이며, 어떻게/왜 사용하는지 설명해주세요.
4. 익명함수(anonymous functions)는 주로 어떤 상황에서 사용하나요?

## 다음 코드가 즉시 호출 함수 표현식(IIFE)로 동작하지 않는 이유에 관해서 설명해보세요: `function foo(){ }();`.

즉시 호출 함수 표현식의 방식으로 선언된 함수는 선언과 동시에 바로 사용되는 함수 입니다.
즉, 함수 자체로는 스코프에 저장되지 않습니다.
그런데 위처럼
함수를 나타내는 키워드인 `function` 뒤에 함수 이름이 붙는다면 즉시 실행되는 함수가 아닌 선언후 사용이 되기 때문에 스코프에 함수의 흔적을 남기게 됩니다.
따라서, 함수가 선언된 후 뒤의 `()` 로 인해 함수가 실행되어지는 형태로 호출이 되는 차이점이 있습니다. - IIFE로 만들기 위해서는 어떻게 해야 하나요? 1. 함수의 이름이 들어간 순간 함수 선언식이 되기 때문에 foo를 빼야합니다.
`function () {} ()`

2.  익명함수는 () 괄호 안에 넣어주거나, 객체에 할당되어 표현되는 식이 아니면 에러가 발생하기 때문에 괄호로 감싸줍니다.
    `(function() {})()`

var hello = function () {}

(function() {
  
 })

## null과 undefined 그리고 undeclared의 차이점은 무엇인가요?

- undefined: `아직` 값이 할당되지 않은 상태
- undeclared: 변수의 이름 목록이 적혀있는 스코프에 조차 없는 상태.
- null: 선언된 적 있지만 빈 값으로 처리된 상태. 빈 값.

```
var tmp = 'hello world:)';
```

위 처럼 변수 선언을 위한 코드를 자바스크립트 엔진이 해석할 때 아래와 같이 세가지 과정을 거칩니다.

1. 선언 : 변수로 선언할 대상을 목록화 시킵니다. 그냥 이름만 적어놓는 느낌!
2. 초기화 : 변수 객체가 가질 값을 위해서 물리적인 메모리 공간을 할당하는데, `undefined`라는 값을 넣어놓으므로써, 아직 실제 값이 할당되기 전이지만 자리는 있다는 것을 표시해놓습니다.
3. 할당 : 실제 변수의 값을 할당합니다.

   - 두개를 구분하기 위해서는 어떻게 하면 될까요?
     undefined는 자리는 있지만 아직 값이 할당되지 않은 상태라는 것만 기억해둬도 구분하기 쉬울 것 같습니다.

## 클로져(Closure)는 무엇이며, 어떻게/왜 사용하는지 설명해주세요.

### 클로저란?

- 함수와 그 함수가 선언됐을 때의 렉시컬 환경(Lexical environment)과의 조합이다.
- 함수를 만들고 그 함수 내부의 코드가 탐색하는 스코프를 함수 생성 당시의 렉시컬 스코프로 고정하는 것.

```
function makeGreeting(name) {
    var greeting = "안녕! ";

    return function() {
        console.log(greeting + name);
    };
  }

  var g1 = makeGreeting("홍길동");
  var g2 = makeGreeting("김철수");

  g1();
  g2();
```

### 어떻게 사용할까요?

대표적으로, oop에서의 private를 쓰고 싶을 때 아래 처럼 사용할 수 있습니다.

```
  a = (function () {
    var privatefunction = function () {
        alert('hello');
    }

    return {
        publicfunction : function () {
            privatefunction();
        }
    }
})();
```

### 왜 사용?

- 클로져를 만들 때 선호하는 패턴은 무엇인가요? argyle (IIFEs에만 적용할 수 있다)
  클로저 안써봤어요..

## 익명함수(anonymous functions)는 주로 어떤 상황에서 사용하나요?

- 전역 스코프에 불필요한 변수를 추가해서 오염시키는 것을 방지
- IIFE 내부안으로 다른 변수들이 접근하는 것을 막기 위함.

# Self Check

- undefined와 null의 차이는?
- 익명함수는 어떤경우에 사용 가능한가요?
