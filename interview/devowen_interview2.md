---
title: JavaScript Interview Questions 13-16 Aug 5th
category: JavaScript
date: 2020-08-05 01:00:00
author: dev-owen
---

<br>

# JavaScript Interview Questions 13-16 Aug 5th

<br>

## 학습 목표

- 얕은 복사(shallow copy)와 깊은 복사(deep copy)의 차이를 이해한다.
- 삼항 연산자의 연산식과 목적을 이해한다.
- use strict의 특징에 대해 이해한다.

<br>

### 13. 다음 코드를 동작하게 만드시오.
```javascript
duplicate([1,2,3,4,5]); // [1,2,3,4,5,1,2,3,4,5]
```
자바스크립트에서 값을 복사하는 방법에는 크게 두 가지가 있다. 그것은 바로 얕은 복사와 깊은 복사이다.

#### 얕은 복사 (shallow copy)

얕은 복사는 실제 값을 복사하는 것이 아니라, 객체의 참조값을 복사하는 것이다. 예를 들어 originalArray라는 변수를 선언하고 메모리의 0x10 이라는 위치에 [1,2,3,4,5]의 배열을 저장했다고 생각해보자. 
그러면 이 배열을 `=`을 이용해서 복사를 하게 되면 복사한 배열(copyArray)도 같은 참조값 0x10을 바라보고 있게 되는 것이다. 값을 복사한 것이 아니라 참조하는 주소 0x10을 복사한 것이다.
그래서 이러한 경우 만약 originalArray의 값이 바뀌게 되면, 같은 주소를 참조하고 있는 copyArray의 값도 영향을 받게 되는 것이다.
```javascript
const originalArray = [1,2,3,4,5];
const copyArray = originalArray; 

console.log(copyArray); // [1,2,3,4,5]

originalArray[0] = 6;

console.log(copyArray); // [6,2,3,4,5]

```

#### 깊은 복사 (deep copy)

깊은 복사는 실제 값을 복사한다. 따라서 별도의 빈 배열을 하나 선언하여 반복문을 통해 값들을 일일이 추가해 주거나, 
`JSON.stringify()`,`JSON.parse()` 메서드를 통해 값을 복사할 때 배열이 아닌 string으로 변환한 뒤 파싱한다.
```javascript
const originalArray = [1,2,3,4,5];

// 방법 1
const deepCopy1 = (array) => {
  const tmpArray = [];
  array.forEach(el => tmpArray.push(el));
  return tmpArray;
};

// 방법 2
const deepCopy2 = (array) => {
  const tmpString = JSON.stringify(array);
  return JSON.parse(tmpString);
}

const copyArray1 = deepCopy1(originalArray);
const copyArray2 = deepCopy2(originalArray);

console.log(copyArray1); // [1,2,3,4,5]
console.log(copyArray2); // [1,2,3,4,5]

originalArray[0] = 6;

console.log(copyArray1); // [1,2,3,4,5]
console.log(copyArray2); // [1,2,3,4,5]
```

이 문제의 duplicate 함수는 다음과 같이 작성해 볼 수 있다.

```javascript
const duplicate = (array) => {
  const copyArray = JSON.parse(JSON.stringify(array));
  return [...array, ...copyArray];
}

console.log(duplicate([1,2,3,4,5]));
```

<br>

### 14. 삼항식(Ternary statement)을 사용하는 이유는 무엇이고, 그것을 표현하기 위한 연산자 단어는 무엇인가요?

삼항 연산자는 어떤 조건에 따라 다른 값을 취할 수 있는 연산자이다. 세 개의 피연산자를 취할 수 있고, if문에 비해 간결하기 때문에 가독성이 좋다.
표현하는 방법은 `condition ? exprIfTrue : exprIfFalse` 이와 같이 ?,: 를 사용하여 표현한다.

```javascript
const isEven = number => number % 2 === 0 ? true : false;

console.log(isEven(2)); // true
console.log(isEven(3)); // false
```

<br>

### 15. use strict;은 무엇이고, 사용했을 때 장단점에 관해서 설명해주세요.

use strict는 전체 스크립트 혹은 부분적인 함수를 엄격 모드로 적용하기 위해서 사용한다. 엄격 모드를 사용하게 되면 다음과 같은 특징이 있다.

1. 기존에 조용히 무시되던 에러들을 throw 한다.(기존에는 warning으로 넘어갈 수 있었던 것들)
2. JavaScript 엔진의 최적화 작업을 어렵게 만드는 실수들을 바로잡는다.
3. 엄격 모드는 ECMAScript의 차기 버전들에서 정의 될 문법을 금지한다.

<br>

### 16. 100번 반복되는 반복문이 있습니다. 3의 배수일 때는 fizz, 5의 배수일 때는 buzz, 3과 5의 공배수일 때는 fizzbuzz가 출력되는 코드를 작성해보세요.

```javascript
const isFizzBuzz = (num) => {
  const threeMultiple = num % 3 === 0 ? true : false;
  const fiveMultiple = num % 5 === 0 ? true : false;
  if (threeMultiple) return fiveMultiple ? 'fizzbuzz' : 'fizz';
  else if(fiveMultiple) return 'buzz';
}
for(let i = 1; i <= 100; i++) {
  if(isFizzBuzz(i)) console.log(`${i} : ${isFizzBuzz(i)}`);
}
```

<br>

## 셀프 체크

1. 얕은 복사는 메모리의 ________(ㅇㅇ ㅇㅇ)를 복사하고 깊은 복사는 메모리의 __(ㅇ)을 복사한다.
2. ___________(ㅇㅇ ㅇㅇㅇ)는 세 개의 피연산자를 취할 수 있고 가독성이 좋은 조건 연산자이다.
3. _________는 전체 스크립트 혹은 부분적인 함수를 엄격 모드로 적용하기 위해서 사용한다.

<br>

## 참고자료

- https://hyunseob.github.io/2016/02/08/copy-object-in-javascript/
- https://junwoo45.github.io/2019-09-23-deep_clone/
- https://wanna-b.tistory.com/18
- https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/Conditional_Operator
- https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Strict_mode
