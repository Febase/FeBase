---
title: FE Interview - Samslow 3
date: 2020-08-10 00:00:00
author: samslow
category: Interview
---

- 아래 질문에 답할 수 있습니다.
  - mutable object와 immutable object에 관해 설명 해주세요.
  - 동기방식과 비동기 방식 함수의 차이에 관해서 설명 해주세요.

# mutable object와 immutable object에 관해 설명 해주세요

### JavaScript에서 immutable 객체에는 어떤것이 있을까

Javascript의 원시타입(primitive data type)은 변경 불가능한 값(immutable value) 이다.

- Boolean
- null
- undefined
- Number
- String
- Symbol (New in ECMAScript 6)

기본 자료형 이외의 모든 값은 객체(Object) 타입이며 객체 타입은 변경 가능한 값(mutable value)이다.

즉, 객체는 새로운 값을 다시 만들 필요없이 직접 변경이 하고 변경이 불가능하다는 뜻은 메모리 영역에서의 변경이 불가능하다는 의미이며 재할당은 가능하다.

단 `defineProperty` 처럼 `객체 상수 속성`을 이용하면 mutable한 객체도 immutable하게 바꿀 수 있다.

```js
let myObject = {};
Object.defineProperty(myObject, "number", {
  value: 42,
  writable: false, // 새 값을 선언 가능하게 할 것인가?
  configurable: false, // 값을 변경 할 수 있고 삭제 할수도 있는가?
});
console.log(myObject.number); // 42
myObject.number = 43;
console.log(myObject.number); // 42
```

`객체 확장 방지` 로 `preventExtensions` 를 사용하거나, `seal` 메소드로 객체를 확장 방지 할 뿐만 아니라 제거, 선언도 못하게 하는 방법, 즉 `preventExtensions` 에 `configurable` 를 `false`로 하는 것이라 보면 된다. 또 `freeze` 를 사용해서 `seal` 의 모든 immutable 속성에 프로토타입 변경 방지까지 할 수 있는데 이는 js에서 객체 불변성의 끝판왕이라고 볼 수 있다.

```js
var myObject = {
  a: 2,
};

Object.preventExtensions(myObject);

myObject.b = 3; // 에러가 남!
myObject.b; // undefined

var immutable = Object.freeze({});
var immutable = Object.seal({});
```



### Immutability의 장점과 단점

불변한 객체들은 기본적으로 위에 명시한 원시타입들이고 기본적으로 객체의 상태를 변경 할 수 없다.

클래스가 가지고 있는 값은 오직 생성자에 의해서만 설정 될 수 있으며, 변경을 원한다면 원하는 값을 가진 새로운 객체를 생성해야한다. 비교하기가 애매해서 아래 예시가 적절한 예시는 아니니 참고만 하길 바란다.

```js
let str = "string is immutable";
str[0] = "c";
console.log(str) // "string is immutable"
```

이들의 장점과 단점은 아래와 같다.

* 장점
  * 값이 보장되므로 안전하게 변수를 공유 할 수 있다.
  * 값이 보장되므로 객체비교시 더 쉽고 빠르게 가능하다.
  * 함수형 프로그래밍에서 특히, 불변객체를 이용하면 프로그램 파악이 쉽다.
  * 여러 스레드가 동시에 immutable 변수를 사용해도 값이 변경되지 않으므로 걱정이 없다.
* 단점
  * 매번 새로운 객체를 만들어버리면 퍼포먼스가 나빠지기 때문에, 이를 고려해여 하므로 Facebook의 immutablejs를 사용하는 등의 라이브러리를 사용하는 것도 좋다.
  * 그래프같은 순환 구조를 만들기가 어렵다.
    * 수정, 초기화도 될 수 없는 두 객체가 어떻게 서로 참조하게 할 것인가?





# 동기 방식과 비동기 방식의 차이에 관해서 설명 해주세요.

동기방식은 현재의 명령문이 컴파일되고 에러없이 실행되기 전까지 다음 명령문을 실행하지 않는다.

반면 비동기 방식은 현재 명령문의 완료와 상관 없이 다음 명령문을 실행한다.

![](https://blog.kakaocdn.net/dn/bztSy0/btqCz451jcO/1UjnGAajLPDoBmh3VqNRjK/img.jpg)

js에서 `setTimeout` 가 대표적인 예시가 될 수 있는데, 이 함수는 2번째 매개변수로 주어진 시간만큼 이후에 1번째 매개변수로 주어진 함수를 실행한다.

콜백함수는 모든 작업이 완료되고 호출 스택이 비어 있을 때만 호출된다. 

하지만 전체적인 프로그램 실행에는 방해되지 않게 진행되는데 이것이 가능한 이유는 이 함수가 비동기방식으로 동작하기 때문이다.

만약 비동기라는 개념이 없었다면, 싱글 스레드 프로그램에서는 이런 단순 대기 함수에서 모든 작업이 멈출 것이다.

```js
console.log("1");
setTimeout(console.log, 5000, "2"); 
console.log("3");
```

위 결과가 예측 가능한가? 처음 본 사람이라면 1 2 3 이라고 답 할 것이고, setTimeout이 호출 스택이 비면 콜백 큐에서 소환된다는 것을 아는 사람은 1 3 2 라고 답할 것이다.

JS가 싱글 스레드 방식이지만 이 함수가 비동기방식으로 동작 할 수 있는 이유는 Web API에 setTimeout의 처리를 위임하기 때문이다.

JS 엔진과 별도로 따로 비동기 처리를 따로 돌면서 콜백 함수를 가지고 이벤트 루프에 들어가 처리되는대로 다시 JS 엔진으로 이를 돌려보내준다.

JS에서 비동기를 다루는 아이들은 아래와 같은 객체들이 있다.

* Promise
* async/await
* 콜백 함수



# Self check

1. js에서 원시타입이 아닌 객체는 (immutability/ mutability)를 갖지만, `________` 는 객체를 Immutable하게 하게 할 뿐더러 prototype마저도 변경 할 수 없게 한다.
2. immutable 객체가 그래프같은 순환 구조를 만들기가 어려운 이유는?
3. 만약 `setTimeout` 이 동기 방식이었다면 어떤 문제가 발생할까?
4. JS는 (싱글/ 멀티) 스레드이고 브라우저에서는 `________` 같은 도구로 (싱글/ 멀티) 스레드를 구현할 수 있다.


# Reference

- https://blog.rhostem.com/posts/2020-04-13-fe-interview-handbook-js-2
