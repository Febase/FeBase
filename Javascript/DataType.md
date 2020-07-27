---
title: Javascript 데이터 타입
date: 2020-06-25 00:00:00
author: jinsunee
category: Javascript
---

# Javascript 원시 타입

1. javascript 변수

   - 데이터 타입/변수 선언에 따른 변수 할당 방식
   - 호이스팅?

2. 원시타입 (primitive type)

   - 원시타입이 값을 저장하는 방식
   - number 타입이 숫자를 취급하는 형식 (다른 언어와의 차이)
   - string 타입의 선언방식, 유사배열?
   - if([false 일 조건]) 은?
   - undefined와 null의 정확한 구분

3. 객체 (object type)
   - 객체의 선언방식 2가지
   - 객체 다루기 (자주 쓰일만한 메소드)

# Javascript Data Type

자바스크립트는

- 동적 타입(Dynamic/Weak Type) 언어이다.
- 즉, 변수 타입 지정 (Type annotation) 없이 값이 할당되는 과정에서 자동으로 변수의 타입이 결정된다. (타입추론, Type Inference)
- 이런 특성 덕분에 변수는 고정된 타입이 없으므로, 같은 변수에 여러 타입의 값을 자유롭게 할당할 수 있다.

  ```
  var str = 'Hello';
  var num = 1;
  var bool = true;

  var foo = 'string';
  console.log(typeof foo); //string

  foo = 1;
  console.log(typeof foo); //number
  ```

## Javascript 변수

변수는

- 값의 위치를 저장하는 저장소이다.
- 즉, 메모리 상의 주소를 의미한다.
- 변수를 메모리에 할당하기 위해서는 필요한 메모리 공간의 크기를 알아야한다.
- 데이터 타입에 따라 할당되어야하는 메모리의 크기가 다르기 때문에 이에 대하여 쉽게 구분하기 위해서 데이터 타입을 지정해놓았다. (boolean, number, Object 등)

![image](https://user-images.githubusercontent.com/31176502/85687570-f15abb80-b70b-11ea-93f5-fbbff8b0f124.png)

### 변수 생성 과정

#### 1. 선언 단계 (Declaration phase)

변수 객체(Variable Object)에 변수를 등록한다. 이 변수 객체는 스코프가 참조하는 대상이 된다.

#### 2. 초기화 단계 (Initialization phase)

변수 객체(Variable Object)에 등록된 변수를 메모리에 할당한다.
이 단계에서 변수는 javascript 엔진에 의해서 undefined로 초기화된다.

#### 3. 할당 단계 (Assignment phase)

undefined로 초기화된 변수에 실제값을 할당한다.

##### `var`로 변수 선언할 경우: `호이스팅`

```
console.log(foo); // undefined
var foo = 1;
console.log(foo); // 1
```

![image](https://user-images.githubusercontent.com/31176502/85691230-46e49780-b70f-11ea-8bfb-6c108f0f1f8c.png)

- `var` 는 선언단계와 초기화 단계가 한번에 이뤄지기 때문에 선언과 함께 undefined 값 할당이 이뤄진다.
- 즉, 스코프에 변수가 등록되고 변수는 메모리 공간을 확보한 후 undefined로 초기화된다.
- 따라서, 변수 선언문 이전에 변수에 접근하여도 Variable Object에 변수가 존재하기 때문에 에러가 발생하지 않는다. 다만 undefined를 반환한다.
- 이러한 현상을 변수 호이스팅 (Variable Hoisting)이라고 한다.

##### `let`과 `const`의 경우

```
// 스코프의 선두에서 선언 단계가 실행된다.
// 아직 변수가 초기화(메모리 공간 확보와 undefined로 초기화)되지 않았다.
// 따라서 변수 선언문 이전에 변수를 참조할 수 없다.

console.log(foo); // ReferenceError: foo is not defined
let foo; // 변수 선언문에서 초기화 단계가 실행된다.
console.log(foo); // undefined
foo = 1; // 할당문에서 할당 단계가 실행된다.
console.log(foo); // 1
```

스코프의 시작 지점부터 초기화 시작 지점까지의 구간을 ‘일시적 사각지대(Temporal Dead Zone; TDZ)’라고 부른다

![image](https://user-images.githubusercontent.com/31176502/85708834-9337d380-b71f-11ea-9752-831f31f6854e.png)

## 데이터 타입

### 데이터 타입 선언 이유

- 코드에서 사용되는 모든 데이터는 메모리에 저장하고 참조할 수 있어야한다.
- 데이터 타입은 데이터를 메모리에 저장할 때 확보해야하는 메모리 공간의 크기와 할당할 수 있는 유효값에 대한 정보, 그리고 메모리에 저장되어 있는 2진수 데이터를 어떻게 해석해야할 지에 대한 정보를 컴퓨터와 개발자에게 제공한다.

### Javascript 타입

- 원시형 / 값에 의한 전달(primitive / pass-by-value)

1.  `number`
2.  `string`
3.  `boolean`
4.  `undefined`
5.  `null`
6.  `symbol` (ES6에서 추가)

- 객체 / 참조형 타입(object / reference type)

`object`

### 원시타입 (primitive type)

1.  `number`

int, long, float, double 등과 같은 다양한 숫자 타입이 존재하는 다른 언어와 달리, JS는 하나의 숫자 타입만 존재한다.

- 64bit 부동소수점 형 (double-precision 64-bit floating-point format): -(2^53-1) ~ 2^53-1 사이의 숫자 값을 따른다.
- 모든 수를 실수 처리하며, 정수만을 표현하기 위한 특별한 데이터 타입은 없다.

  ```
  var integer = 10; // 정수
  var double = 10.12; // 실수
  var negative = -20; // 음의 정수
  var binary = 0b01000001; // 2진수
  var octal = 0o101; // 8진수
  var hex = 0x41; // 16진수
  ```

위 처럼 선언을 해도 메모리에 할당되어지는 값은 당연히 2진수이며, 해석은 10진수로 된다.

```
console.log(binary); // 65
console.log(octal); // 65
console.log(hex); // 65
// 표기법만 다를뿐 같은 값이다.

console.log(binary === octal); // true
console.log(octal === hex); // true
```

자바스크립트의 숫자 타입은 정수만을 위한 타입이 없고 모든 수를 실수 처리한다. 정수로 표시된다해도 사실은 실수이다. 따라서 정수로 표시되는 수 끼리 나누더라도 실수가 나올 수 있다.

```
console.log(1 === 1.0); // true
var result = 4 / 2;
console.log(result); // 2
result = 3 /2;
console.log(result); // 1.5
```

추가적으로, 3가지 특별한 값들도 표현할 수 있다.

- `Infinity` : 양의 무한대
- `-Infinity` : 음의 무한대
- `NaN` : 산술 연산 불가 (not-a-number)

```
var pInf = 10/0; // 양의 무한대
console.log(pInf); // Infinity
var nInf = 10/-0; // 음의 무한대
console.log(nInf); // -Infinity
var nan = 1 * 'string'; // 산술 연산 불가
console.log(nan); // NaN
```

2.  `string`

- 텍스트 데이터를 나타내는데 사용
- 문자열은 0개 이상의 16bit 유니코드 문자(UTF-16)들의 집합
  → 대부분의 전세계의 문자를 표현할 수 있다.

- 작은 따옴표(''), 큰 따옴표("")안에 텍스트를 넣어서 생성
  → 가장 일반적인 표기법은 작은 따옴표를 사용하는 것이다.

  ```
  var str = "string"; // 큰 따옴표
  str = 'string'; // 작은 따옴표
  str = `string`; // 백틱(ES6 템플릿 리터럴)

  str = "큰 따옴표로 감싼 문자열 내의 '작은 따옴표'는 문자열이다.";
  str = '작은 따옴표로 감싼 문자열 내의 "큰 따옴표"는 문자열이다.';
  ```

- JS에서 string은 원시타입이기 때문에 한번 할당되고 나면 가리키고 있는 메모리 주소안의 값은 바꿀 수 없다. 기존의 문자열을 변경하는 것이 아니라 새로운 문자열을 새롭게 할당하는 것.

  → 아래처럼 값이 바뀌는 구문이 실행된다면 새로운 문자열 'world'를 다른 메모리에 생성하고 식별자 str은 그것을 가리키게 된다.

  → 즉, 처음에 할당한 'Hello'와 나중에 새로 할당된 값 'world'는 모두 메모리에 존재하고 있다.

  ```
  var str = 'Hello';
  str = 'world';
  ```

* 문자열은 유사 배열(배열처럼 인덱스를 통해 접근할 수 있는 특성을 갖는 데이터)이다.

  ```
  var str = 'string';
  // 문자열의 하나하나에 접근할 때 배열처럼 str[index]로 접근할 수 있다.
  for (var i=0; i <str.length; i++) {
    console.log(str[i]);
  }

  // 그렇지만 이렇게 접근하는 방식으로 문자열을 변경할 수는 없다.
  str[0] = 'S';
  console.log(str); // string -> 변경되지 않음.
  ```

3.  `boolean`

    - 논리적 참, 거짓을 나타내는 `true` 와 `false`
    - `false` 로 간주되는 경우
    - Empty String
    - null
    - undefined
    - 0

4.  `undefined`
    - 선언 이후, 값을 할당하지 않은 변수가 갖는 값.
    - 선언은 되었지만 값을 할당하지 않은 변수에 접근하거나, - 존재하지 않는 객체 프로퍼티에 접근할 경우

#### Q) 선언은 되었지만 값을 할당하지 않은 변수에 undefined가 할당되는 이유

변수 선언에 의해 확보된 메모리 공간은 할당하기 전 대부분 쓰레기 값(Garbage value)이 들어있다.

자바스크립트 엔진이 이러한 상태를 그대로 내버려두지 않고 undefined로 초기화 하기 때문에 처음 선언되는 변수가 가리키고 있는 메모리 공간의 값은 `undefined`로 시작한다.

따라서, undefined 값을 갖고 있는 변수는

`할당된 적 없는 변수` 라고 생각하면 된다.

이런 취지를 갖고 있는 값이기 때문에 개발자가 마음대로 undefined라고 할당한다면 본래의 취지와 어긋날 뿐더러 혼란을 줄 수 있으므로 권장하지 않는다.

#### Q) 변수의 값이 없다는 것을 명시하고 싶은 경우?

→ `null`을 할당한다.

5.  `null`

- 의도적으로 변수에 값이 없다는 것을 명시할 때 사용한다.
- 이는, 변수가 기억하는 메모리 어드레스의 참조 정보를 제거하는 것을 의미하고 자바스크립트 엔진은 누구도 참조하지 않는 메모리 영역에 대해 가비지 콜렉션을 수행할 것이다.

  ```
  var foo = 'Lee';
  foo = null; // 참조 정보가 제거됨
  ```

- 또는, 함수가 호출되었으나 유효한 값을 반환할 수 없는 경우 명시적으로 null을 반환하기도 한다.

- null은 자기자신 그대로 null 타입이지만, 실제로 type 은 `Object` 이다.

- 값이 할당되지 않은 변수를 호출하면 null이 아닌 ReferenceError 에러가 발생한다.

  ```
  var x; console.log(x); // undefined
  console.log(y); // ReferenceError
  ```

6.  `symbol`

- ES6에서 새롭게 추가된 7번째 타입으로 변경 불가능한 원시타입의 값이다.

- 주로 이름의 충돌 위험이 없는 유일한 객체 프로퍼티 키를 만들기 위해 사용한다.

  ```
  // 심볼 key는 이름의 충돌 위험이 없는 유일한 객체의 프로퍼티 키
  var key = Symbol('key');
  console.log(typeof key); // symbol
  var obj = {};
  obj[key] = 'value';
  console.log(obj[key]); // value
  ```

### 객체 (Object type)

- key-value 저장소

  ```
  const object = {
    key: "value"
  }
  ```

- 데이터와 그 데이터에 관련한 동작을 모두 포함할 수 있는 개념적 존재이다.

- 프로퍼티(property) 와 메소드(method)

- 프로퍼티 : 이름과 값을 가지는 데이터

- 메소드: 동작을 의미 (프로퍼티가 함수로 선언된)

- 객체(Object) 기반의 스크립트 언어로서 자바스크립트를 이루고 있는 거의 모든 것이 객체이다.

- 객체는 pass-by-reference(참조에 의한 전달) 방식으로 전달된다.

  ```
  "dog" === "dog"; // true
  14 === 14; // true

  {} === {}; // false
  [] === []; // false

  (function () {}) === (function () {}); // false
  ```

### 객체 선언

- 객체 리터럴 선언방식

  ```
  var obj = {
    name: 'jinsun', // 프로퍼티(객체의 속성)
    address: 'seoul', // 프로퍼티(객체의 속성)
    greeting: function () { // 메소드
    alert(this.name + "! 안녕안녕~");
    }
  }
  ```

- new 키워드 선언 방식

  ```
  var obj = new Object(); // { } 빈 객체 생성

  // 객체에 .점 표기법으로 접근하기
  obj.name = 'jinsun';
  // 객체에 [] 괄호 표기법으로 접근하기
  // -> js에서 사용할 수 없는 형태의 key값은 'value'로 표기
  obj[address] = 'seoul';
  obj.greeting = function() {
    alert(this.name + "! 안녕안녕~");
  }
  ```

### Object 객체 내장 메서드

```
var object1 = {
  a: "aaa",
  b: "bbb",
};
```

- Object.keys()

  ```
  /*
  a
  b
  */
  ```

- Object.values()

  ```
  /*
  aaa
  bbb
  */
  ```

- Object.entries()

  ```
  for(var [key, value] of Object.entries(object1)) {
    console.log(`${key}: ${value}`);
  }
  ```

## Self Check

1. 원시타입이 값을 저장하는 방식은 ---- 이고, 객체가 저장하는 방식은 ---- 이다.
2. if(1) {}에서 1은 false로 취급된다 -> O, X
3. 가비지컬렉터가 지워야할 대상은 [undefined/null] 타입의 값이 할당되어있다.
