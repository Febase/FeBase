---
title: FE Interview 3
date: 2020-08-05 00:00:00
author: snowjang24
category: interview
---

## 오늘의 FE 질문

1. this는 JavaScript에서 어떻게 작동하는지 설명해주세요.
2. prototype 기반 상속은 어떻게 하는지 설명해주세요.
3. AMD와 CommonJS는 무엇이고, 이것들에 대해 어떻게 생각하시나요?
4. "호이스팅(Hoisting)"에 대해서 설명하세요.

## 1. this는 JavaScript에서 어떻게 작동하는지 설명해주세요.

자바스크립트의 실행 중인 모든 함수는 현재 실행 컨텍스트(객체)에 대한 참조를 갖는다. `this` 는 이러한 참조를 담고 있는 변수다. `this` 는 함수가 언제, 어디서, 어떻게 호출 되었는지에 따라 참조하는 값이 다르다.

`this`의 값이 결정되는 상황은 크게 5 가지로 나눌 수 있다.

- **Default Binding :**

  `strict mode` 가 아닌 경우(이 경우, `undefined`), `this`는 기본적으로 글로벌 객체를 참조한다(브라우저의 경우 `window`, Node의 경우 `global`).

- **Implicit Binding :**

  객체의 프로퍼티로 메서드를 가지고 있는 경우, 메서드 내에서의 this는 실행 컨텍스트 객체를 참조한다. 이를 암시적 바인딩(Implicit Binding)이라고 부른다.

- **Explicit Binding :**

  `call` 혹은 `apply` 메서드를 활용하여 메서드를 사용하는 경우, `call`혹은 `apply` 메서드의 첫번째 파라미터를 `this` 가 참조한다. 이를 명시적 바인딩(Explicit Binding)이라고 부른다.

- **Hard Binding :**

  Explicit Binding을 활용하여, 강제로 `this`가 참조하는 객체를 고정할 수 있다. 이를 하드 바인딩(Hard Binding)이라고 한다.

  ```jsx
  function foo() {
    console.log(this.bar);
  }
  var obj1 = { bar: 10 };
  var obj2 = { bar: 5 };
  var originalFoo = foo;
  foo = function () {
    originalFoo.call(obj1);
  };
  foo(); // 10
  foo.call(obj2); // 10
  ```

- `**new` Keyword :\*\*

  함수 앞에 `new` 키워드를 붙이게 되면 해당 함수는 새로운 빈 객체를 생성한다. 함수 내부에서 `this` 는 새로 생성된 빈 객체를 가리키게 된다.

## 2. prototype 기반 상속은 어떻게 하는지 설명해주세요.

자바스크립트의 객체는 `[[Prototype]]` 이라는 숨김 프로퍼티를 갖는다. 이 프로퍼티는 `null` 혹은 참조하고 있는 객체를 가리키고 있다. 여기서 참조 대상을 프로토타입(prototype)이라 부른다.

또한, 자바스크립트에서는 객체애 찾고자하는 프로퍼티가 없을 경우 프로토타입 객체에서 해당 프로퍼티를 찾는데, 이러한 특징을 이용하여 prototype 기반 상속이 이루어지게 된다.

`[[Prototype]]`은 `__proto__` 라는 예약어를 통해 값을 얻거나 설정할 수 있다. 이를 이용하여 아래와 같이 프로토 타입 객체를 설정하여 상속을 구현할 수 있다.

```jsx
let animal = {
  eats: true,
  walk() {
    alert("동물이 걷습니다.");
  },
};

let rabbit = {
  jumps: true,
  __proto__: animal,
};

let longEar = {
  earLength: 10,
  __proto__: rabbit,
};

// 메서드 walk는 프로토타입 체인을 통해 상속받았습니다.
longEar.walk(); // 동물이 걷습니다.
alert(longEar.jumps); // true (rabbit에서 상속받음)
```

## 3. AMD와 CommonJS는 무엇이고, 이것들에 대해 어떻게 생각하시나요?

## 4. "호이스팅(Hoisting)"에 대해서 설명하세요.

호이스팅(Hoisting)은 코드에 선언된 변수 및 함수를 코드 상단으로 끌어올리는 것을 뜻한다. 여기서 함수 내에서 선언한 경우 해당 함수의 최상단으로, 전역인 경우에는 전역 범위의 최 상단으로 끌어 올려진다. 선언은 자바스크립트 엔진 구동시 가장 먼저 이뤄지고, 할당의 경우 런타임 과정에서 일어나기 때문에 선언만 호이스팅 된다.

아래와 같은 같은 코드가 에러를 발생시키지 않는 이유는 호이스팅 때문이다.

```jsx
console.log(score); //undefined
var score = 100;
console.log(score); //100
```

```jsx
var score;
console.log(score); //undefined
score = 100;
console.log(score); //100
```

변수 호이스팅과 함수 호이스팅의 경우 전체적으로 동일하게 이뤄지지만, 함수 호이스팅에서 하나 주의해야할 점이 있다. 함수 호이스팅의 경우 함수 리터럴 방식으로 선언한 경우 호이스팅되지 않는다.

```jsx
foo();
var foo = function () {
  console.log("hello");
};
```

또한, 호이스팅은 `var` 선언 뿐만 아니라 `const`와 `let`에서도 이뤄진다. 하지만 `var`과는 달리 `let`과 `const`는 TDZ(Temporal Dead Zone)에 의해 호이스팅이 이루어지지 않는 것처럼 보인다. `var`의 경우 선언과 동시에 초기화가 이루어지지만, `let`과 `const`의 경우 선언만 될 뿐 초기화가 이루어지지 않는다. 따라서, 메모리에 공간이 할당되어 있지 않게 되어 참조가 불가능하게 된다.

## Self Check

- 자바스크립트의 실행 중인 모든 함수는 \_\_\_객체)에 대한 참조를 갖는다. `this`는 이러한 참조 값을 담고 있는 변수다.
- 자바스크립트의 객체는 \_\_\_이라는 숨김 프로퍼티를 갖는다.
- 자바스크립트에서 선언만 호이스팅 된다. (O, X)

## Reference

- [JavaScript — all about “this” keyword](https://codeburst.io/all-about-this-and-new-keywords-in-javascript-38039f71780c)
- [https://webclub.tistory.com/404](https://webclub.tistory.com/404)
- [https://ko.javascript.info/prototype-inheritance](https://ko.javascript.info/prototype-inheritance)
- [https://d2.naver.com/helloworld/12864](https://d2.naver.com/helloworld/12864)
- [https://evan-moon.github.io/2019/06/18/javascript-let-const/](https://evan-moon.github.io/2019/06/18/javascript-let-const/)
