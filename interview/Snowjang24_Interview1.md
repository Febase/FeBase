---
title: FE Interview 4
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

자바스크립트에서 `this`는 함수 선언 위치가 아닌, 함수 호출을 기반으로 이뤄진다는 점이 가장 중요하다. 함수가 호출되는 실행 컨텍스트가 바로 `this`의 값이 된다. 이렇게 `this`의 값이 결정되는 것을 일컬어 **this binding** 이라고 한다.

`this`의 값이 결정되는 this binding의 경우는 크게 5 가지로 나눌 수 있다. 

1. Default Binding
2. Implicit Binding
3. Explicit Binding
4. Hard Binding
5. `new` Keyword 

### a. Default Binding

가장 먼저 기본 바인딩이다. 보통, `strict mode` 가 아닌 경우(이 경우, `undefined`), `this`는 기본적으로 글로벌 객체를 참조한다(브라우저의 경우 `window`, Node의 경우 `global`).

아래의 예시를 실행해보면 과연 어떤 값이 나올까. 생각해보자.

```javascript
function foo() {
  var a = 10;
  console.log(this.a);
};
var a = 5;
foo(); 
```

결과는 `5`를 출력할 것이다. `foo()`가 호출되는 위치가 전역 객체의 컨텍스트에서 호출되기 때문에 `foo()` 내부의 `this`는 전역 객체를 참조하고 전역에 선언된 `a`를 출력한다.

### b. Implicit Binding

이번에는 아래와 같이 객체의 메서드를 호출해보자. 아래의 결과는 `10`일 것만 같다. 객체의 메서드기 때문에 `this` 는 객체 컨텍스트인, `obj` 객체가 될 것이라고 생각할 것이다.

```javascript
function foo() {
  console.log(this.a);
};

var obj = {
  a: 10,
  foo: foo
};

var bar = obj.foo;
var a = 5;
bar(); 
```

예상과 달리 `5`가 출력된다. 맨 처음 말했듯, 함수가 선언되는 위치가 아닌 함수가 호출되는 위치가 중요하다. 이러한 결과가 나온 이유는, 메서드를 `bar`라는 변수에 할당하고 `foo` 함수에 대한 참조를 얻어 컨텍스트가 전역 객체로 변경되기 때문이다. 따라서, 아래와 같이 `obj`의 메서드를 바로 호출해야 우리가 예상했던 결과인 `10`을 얻을 수 있다.

```javascript
function foo() {
  console.log(this.a);
};

var obj = {
  a: 10,
  foo: foo
};

var a = 5;
obj.foo();
```

이처럼, 객체의 프로퍼티로 메서드를 가지고 있는 경우 메서드 내에서 `this`는 해당 객체에 대한 실행 컨텍스트를 가진다. 이를 **암시적 바인딩(Implicit Binding)** 이라고 부른다.

### c. Explicit Binding

**명시적 바인딩(Explicit Binding)** 은 단어 뜻에서 볼 수 있듯 바인딩을 명시하여 `this`의 참조 값을 결정한다. `call`, `apply` 메서드를 통해 명시적 바인딩을 할 수 있다.

첫번째 파라미터로 넘겨준 객체에 `this`가 바인딩 된다.

```javascript
function foo() {
  console.log(this.a);
};

var obj1 = {
  a: 10
};
var obj2 = {
  a: 20
};

var a = 5;
foo.call(obj1);
foo.call(obj2);
```

### d. Hard Binding

Explicit Binding을 활용하여, 강제로 `this`가 참조하는 객체를 고정할 수 있다. 이를 **하드 바인딩(Hard Binding)** 이라고 한다. 아래의 예시를 먼저 살펴보자. 아래의 출력 결과를 예상해보자.

```javascript 
function foo() {
  console.log(this.a);
};

var obj1 = {
  a: 10
};
var obj2 = {
  a: 20
};

var bar = foo;
foo = function() {
  bar.call(obj1);
}

foo();
foo.call(obj2);
```

결과는 `foo()`와 `foo.call(obj2)`는 모두 `10`을 출력한다. 이러한 결과가 나온 이유는 아래의 코드에 있다. 내부적으로 명시적 바인딩을 하는 함수를 만들어, 함수 호출 위치와 상관 없이 `this`가 변하지 않고 동일한 결과를 얻을 수 있다. 

```javascript 
var bar = foo;
foo = function() {
  bar.call(obj1);
}
```

이러한 하드 바인딩은 `.bind()` 가 나오기 이전에 사용하던 패턴으로 `.bind()`를 활용하여 위의 예시를 바꿔보면 아래와 같다. 이는 하드 바인딩과 똑같이 작동한다.

```javascript
function foo() {
  console.log(this.a);
};

var obj1 = {
  a: 10
};
var obj2 = {
  a: 20
};

var bar = foo.bind(obj1);

bar();
bar.call(obj2);
```


### e. `new` Keyword

함수 앞에 `new` 키워드를 붙여 호출하면, 일반적인 함수 호출이 생성자 호출로 바뀐다. 이렇게 생성자 호출을 하게 되면 해당 함수는 새로운 빈 객체를 생성한다. 그리고 이 함수 내부에서 `this` 는 새로 생성된 빈 객체를 참조하게 된다.

아래의 예시에서 `foo()`와 `new foo()`결과를 한 번 예상해보자. 

```javascript
function foo() {
  var a = 10;
  this.b = 5;
  console.log(this.a, this.b);
};

var a = 20;
var b = 15;
foo();
new foo();
```

일반 함수인 `foo()`의 경우 `this.a`가 `20`, `this.b`는 `5`가 출력된다. 함수 내부의 `this`는 전역 객체에 바인딩되었기 때문에 이러한 결과 값이 출력되고, `new foo()`의 경우, `this.a`는 `undefined` 그리고 `this.b`는 `5`가 출력된다. 

새로운 객체가 생성 되면서 `this`가 새로운 객체에 바인딩 된다. 이 때 내부에 선언한 `a`의 경우 무시되기 때문에 `this.a`는 `undefined`의 값을 가지게 된다.

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

CommonJS 와 AMD 모두 자바스크립트에서 모듈과 종속성을 선언하는 방법에 대한 명세다. 두 방식은 아래와 같은 차이가 있다.

### AMD

* 브라우저 우선 접근 방식
* 비동기 동작과 단순화된 이전 버전 호환성 선택
* File I/O 개념이 없음
* 객체, 함수, 생성자, 문자열, JSON 등 다양한 유형의 모듈을 지원

```javascript
// package/lib is a dependency we require
define(["package/lib"], function (lib) {

    // behavior for our module
    function foo() {
        lib.log( "hello world!" );
    }

    // export (expose) foo to other modules as foobar
    return {
        foobar: foo
    }
});
```

### CommonJS

* 서버 우선 접근 방식
* 동기 동작이 기본
* I/O, 파일 시스템, Promises 등과 같은 광범위하게 관심을 가짐
* 객체만 모듈로 지원

```javascript
// package/lib is a dependency we require
var lib = require( "package/lib" );

// behavior for our module
function foo(){
    lib.log( "hello world!" );
}

// export (expose) foo to other modules as foobar
```


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
- [https://stackoverflow.com/questions/16521471/relation-between-commonjs-amd-and-requirejs](https://stackoverflow.com/questions/16521471/relation-between-commonjs-amd-and-requirejs)

