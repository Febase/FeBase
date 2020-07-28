---
title: This keyword, call & apply
date: 2020-07-08 00:00:00
author: nailerHeum
category: Javascript
---



# 'this' keyword, call & apply

### 학습 목표

- this가 뭔지?
- this가 어떻게 결정되는지
- call과 apply의 사용법과 차이점

## this는 execution context의 thisbinding이다.

---

execution context는 Lexical Environment, Variable Environment, ThisBinding에 대한 정보를 갖고 있다. 

여기서 ThisBinding이 `this` 이다. 

`this`는 해당 함수가 현재 어느 Execution Context에서 구동하고 있는지를 알려준다.

execution context는 함수 호출에 따라서 새로 생성되기 때문에 `this`또한 **함수 호출시점**에 정해진다. 호출 시점에서 함수에게 `argumentsList`와 `thisArg`라는 객체가 전달된다. 

**함수 호출 직전에서의 thisArg 결정 과정**

1. MemberExpression을 해석해서 함수가 저장된 레퍼런스 값인 `ref` 를 얻는다.
    - 이 `ref`는 base value, referenced name, strict reference flag를 갖는다.
    - base value: reference가 속한 context object를 가리킨다.
    - referenced name: string 값으로 지정된 function identifier다.
    - strict reference flag(boolean): strict mode에서 실행되는 코드인지 아닌지
2. `getValue(ref)`를 통해 함수 `func`를 불러온다.
3. 주어진 arguments들로 `argumentsList`를 생성한다.
4. `Type(func)`가 객체가 아닐 경우 또는 `IsCallable(func)` 가 `false`인 경우 `TypeError` 를 던진다.
5. `Type(ref)`가 `Reference`일 경우 
    - `ref`의 base value가 Object나 primitive wrapper object(원시 래퍼 객체)이면 `thisArg`는 `ref`의 base value가 된다.
    - 이외에 `ref` 의 base value가 Environment Record라면 그 base value에서 `ImplicitThisValue()` 를 호출해 나온 값이 `thisArg`가 된다.
6. `Type(ref)`의 값이 `Reference`가 아닌 경우 `thisArg`는 `undefined`가 된다.
7. `Call` 오퍼레이션을 통해 `thisArg`와 `argumentList`를 전달해 함수를 호출한다.

(Primitive Wrapper Object(원시 래퍼 객체): null과 undefined를 제외한 모든 원시 값은 원시 값을 wrapping한 객체를 갖는다.)

ECMA spec에 따르면 ThisBinding 값이 결정되는 과정은 아래와 같다.

**ThisBinding(this) 결정 과정**

1. 만약 함수가 strict mode라면 ThisBinding을 `thisArg`로 지정한다.
2. 이외에(strict mode가 아니고), `thisArg` 값이 `null`이나 `undefined`일 경우, ThisBinding 값을 전역 객체로 지정한다.
3. 이외에 `Type(thisArg)`가 Object가 아니라면 ThisBinding을 `ToObject(thisArg)` 으로 지정한다.
4. 이외의 경우 ThisBinding을 `thisArg`로 지정한다.

(`.call` 과 `.apply`와 같이 `this`를 수정하는 기능들은 `thisArg` 값을 전달할 수 있게 해주는 기능인 것이다.)

(함수 코드에 진입할 때 실행컨텍스트 관련 동작을 더 알고 싶다면 [http://www.ecma-international.org/ecma-262/5.1/#sec-10.4.3](http://www.ecma-international.org/ecma-262/5.1/#sec-10.4.3))

**정리**

- 대부분의 경우 `this`의 값은 함수를 호출한 방법에 의해 결정된다. 실행중에는 할당할 수 없고 함수를 호출할 때마다 다를 수 있다.
- 엄격 모드(`'use strict'`)와 비엄격모드에 따라 `this`가 다르게 동작할 수 있다.

    예시)

    ```jsx
    function f() {
        return this;
    }
    f();
    // Window {parent: Window, opener: null, top: Window, length: 0, frames: Window, …}

    "use strict";
    function f(){
      return this;
    }
    f();
    // undefined
    ```

### global execution context(전역 실행 문맥)

`this` 실행 환경에 따라 다르게 나타난다.

```jsx
// browser
console.log(this === window);
-> true
this
-> Window {parent: Window, opener: null, top: Window, length: 0, frames: Window, …}

// node REPL
console.log(this === global);
-> true
this
->
Object [global] {
  global: [Circular],
  clearInterval: [Function: clearInterval],
  clearTimeout: [Function: clearTimeout],
  setInterval: [Function: setInterval],
  setTimeout: [Function: setTimeout] {
    [Symbol(nodejs.util.promisify.custom)]: [Function]
  },
  queueMicrotask: [Function: queueMicrotask],
  clearImmediate: [Function: clearImmediate],
  setImmediate: [Function: setImmediate] {
    [Symbol(nodejs.util.promisify.custom)]: [Function]
  }
}

// js file running on node runtime
console.log(this === module.exports); // true
console.log(this === global); // false
console.log(this === globalThis); // false
console.log(global === globalThis); // true
function f() {
	return this;
}
console.log(f() === global);
```

node의 경우 repl의 this는 전역객체를, js 파일의 this는 module.exports 객체를 가리킨다. 전역객체에 접근하려면 `global` 이나 `globalThis`로 접근한다.

이외 this 관련 특징들

- new 키워드를 이용해 객체로 인스턴스화 되었을 때 this는 항상 인스턴스화 된 객체를 참조한다.
- 객체의 method로 함수가 호출될 때, this값은 언제나 인스턴스화 된 객체를 참조한다.

## call & apply

---

`call()`은 인수 목록을, `apply()`는 인수 배열 하나를 받는다는 차이점 빼고 동일한 동작을 한다.

**구문**

`func.call(thisArg[, arg1[, arg2[, ...]]]);`

- thisArg: this 값
- arg1, arg2, ... : 인수들

`func.apply(thisArg, [argsArray]);`

- thisArg: this 값
- argsArray: 인수 배열

call 과 apply 모두 thisArg에 null이나 undefined가 들어갈 수 있고, strict mode에 따라 전역객체로 대체되거나, undefined, null이 들어갈 수 있다.

```jsx
'use strict';
function a() {
  console.log(this);
  console.log(this.num);
}
const obj = {num: 5};
a.call(obj);
// { num: 5 }
// 5
```

```jsx
'use strict'
function a() {
  console.log(this);
  console.log(this.num);
}
const obj = {num: 5};
a.call(undefined);
// undefined
// TypeError: Cannot read property 'num' of undefined
```

그렇다면 주로 어떤 상황에 `call`과 `apply`가 사용될까?

- call로 상속 구현하기

    ```jsx
    function Product(name, price) {
      this.name = name;
      this.price = price;
    }

    function Food(name, price) {
      Product.call(this, name, price);
      this.category = 'food';
    }

    function Toy(name, price) {
      Product.call(this, name, price);
      this.category = 'toy';
    }

    const food = new Food('banana', 5);
    const toy = new Toy('robot', 40);
    ```

- apply로 원본 배열에 배열 붙이기

    ```jsx
    const array = ['a', 'b'];
    const elements = [0, 1, 2];
    array.push.apply(array, elements); // Array.prototype.push.apply(array, elements);
    console.log(array); // ["a", "b", 0, 1, 2]
    ```

### 질문들

1. this는 언제 결정될까요?
2. strict mode일때와 아닐때 this가 어떻게 달라지나요?
3. call과 apply의 차이가 뭘까요?

### Reference

[[JavaScript] 자바스크립트 this 키워드의 모든것](https://muckycode.blogspot.com/2015/04/javascript-this.html)

[ECMAScript Language Specification - ECMA-262 Edition 5.1](http://www.ecma-international.org/ecma-262/5.1/#sec-10.4.3)

[this](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/this)

[Function.prototype.call()](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Function/call)

[Function.prototype.apply()](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Function/apply)

```jsx
export function letIf<T>(...args: unknown[]): T | undefined {
  const callback = args.pop() as Function
  if (args.every($0 => $0 !== undefined && $0 !== null)) {
    return callback.call(null, ...args)
  }
  return undefined
}

```