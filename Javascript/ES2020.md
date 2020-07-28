---
title: Front to the ES2020 
date: 2020-07-15 00:00:00
author: snowjang24
category: Javascript
---

# Front to the ES2020

## 학습 목표

* ECMA Script와 Javascript 사이의 관계에 대해 이해하기
* ES2020의 새로운 기능에 대해 이해하기

## 들어가며

처음 자바스크립트를 시작하였을 때, `var`와 `class` 키워드 없이 `prototype`를 활용하여 구현하기 등과 같이 공부하고 쓰면서도 많이 혼란스러웠다. 진입장벽 자체가 높은 편으로 생각이 들었던 언어가 자바스크립트 였다. 하지만 ES6의 등장으로 편의성이 많이 개선되었고, 좀 더 코드를 흐름에 따라 읽기만해도 직관적으로 이해하기 편해졌다. 

ES6가 처음 나오고 다양한 기능들을 학습하며, 라떼는 말야? 라는 생각이 들 정도로 많이 편해졌는데, 어느새 ES2020이 나왔다고 하여 이번 포스팅에서 기능들을 하나하나 학습해보려 한다.

## Javascript와 Ecmascript

ES2020에 본격적으로 들어가기에 앞서 ES가 무엇인지 먼저 이해하면 좋을 것 같다. 자바스크립트 관련 책이나 강의를 보게 되면 보통 Javascript 기초와 ES6 강의가 따로 나눠져 있는 경우를 더러 보게 된다. 

![image-20200715111727037](https://user-images.githubusercontent.com/26768201/88042021-3a285780-cb86-11ea-917e-f29deee96246.png)

Node 12와 같이 버젼인것 같다는 생각을 하고 보면 어디는 ES5, ES6, ... ES11와 같이 차례로 네이밍 되어있기도하고 다른 곳은 ES2015, ES 2016, ... ES2020과 같이 네이밍 되어있다. 뒤에 숫자는 뒤로하고 먼저 **ES(Ecma Script)**에 대해 간단히 설명하자면, **ECMA Script**는 **[Ecma International](https://www.ecma-international.org/)** 의해 제정된 **ECMA-262** 기술 규격을 기반으로 정의된 범용 스크립트 언어다. 이제 이 세 키워드(ES, Ecma International, ECMA-262)에 대해 이해하며 JS와 ES의 관계에 대해 차례차례 알아보자.

### Ecma International

가장 먼저, [Ecma International](https://www.ecma-international.org/)은 정보와 통신 시스템을 위한 국제적 표준화 기구다. 자바스크립트(Javascript)는 넷스케이프 커뮤니케이션즈 코퍼레이션의 브렌던 아이크가 처음에는 모카(Mocha)라는 이름으로, 나중에는 라이브스크립트(LiveScript)라는 이름으로 개발하였다(후에 자바스크립트로 이름을 변경). 넷스케이프는 자바스크립트의 표준화를 위해 자바스크립트 기술 규격을 Ecma International에 제출하였고, 이 규격에 대한 작업은 ECMA-262의 이름으로 시작되었다. 

Ecma International은 JS에 대한 규격 외에도 아래와 같이 다양한 규격을 정의하고 있다.

![image-20200715161145198](https://user-images.githubusercontent.com/26768201/88042035-3f85a200-cb86-11ea-8138-abf2fc3ce4b9.png)

### ECMA-262와 ECMA Script

[ECMA-262](https://www.ecma-international.org/publications/standards/Ecma-262.htm)는 앞에서 말한 것과 같이 Ecma International에 의해 정의된 ECMA Script에 대한 언어 규격이다. 이를 기반으로 ECMA Script라는 범용 스크립트 프로그래밍 언어가 정의된다. ECMAScript는 스크립트 언어가 준수해야 하는 규칙, 세부 사항 및 지침을 제공한다.

### ECMA Script와 Javascript

Javasciprt는 이러한 ECMA Script의 사양을 따라 매번 새로운 기능을 제작하여 배포한다. 그렇기 때문에 새로운 자바스크립트의 버젼 이름은 ES를 기반으로 하기 때문에 Javascript ES5, Javascript ES6와 같이 불린다.

그간 다양한 버젼이 배포되었는데 우리가 주로 아는 ES6까지는 ES6와 같은 넘버링을 쓰다가 ES7에 해당하는 ES2016에 이르러, 앞으로 매년 기능을 업데이트 하기로 결정되었다. 이에 따라, 넘버링 역시 새로운 버젼이 배포되는 년도를 따라가기로 바뀌었다. 그렇기 때문에, ES6 이후의 버젼은 ES7과 같은 넘버링이 아닌 ES2016, ES2017, ... , ES2020과 같이 부르면 된다.

아래는 ES2020 이전, 각 버젼별 새로운 기능들을 나열한 것이다. 이미 쓰고 있는 것도 있을 것이고 아직 생소한 문법들도 있을 것이다. 

#### ES2016

- Array.prototype.includes
- The exponentiation operator

#### ES2017

- Object.values / Object.entries
- String padding
- Object.getOwnPropertyDescriptors
- Trailing commas in function parameter lists and calls
- Async functions
- Shared memory and atomics

#### ES2018

- Lifting template literal restriction.
- s (dotAll) flag for regular expressions.
- Regexp named capture groups.
- Rest/spread properties.
- Regexp lookbehind assertions.
- Regexp Unicode property escapes.
- Promise.prototype.finally
- Asynchronous iteration.

#### ES2019

- Array#{flat, flatMap}
- Object.fromEntries
- String#{trimStart, trimEnd}
- Symbol#description
- try { } catch {}, optional binding
- JSON ⊂ ECMAScript
- well-formed JSON.stringify
- stable Array#sort
- revised Function#toString

위의 새로운 기능들은 [노드그린](https://node.green/) 에서 각 노드 버젼별 사용 가능 여부를 확인할 수 있다.

![image-20200715173009998](https://user-images.githubusercontent.com/26768201/88042039-401e3880-cb86-11ea-8fbe-de786d5055ee.png)

## Happy New Year! ES2020

드디어 ES2020. 새로운 버젼이다. ES6이후 다양한 기능들이 업데이트 되었는데, 이번 버젼 역시 큰 기능보다는 편의성에 초점을 둔 업데이트가 진행되었다. ES6에 들어 자바스크립트 언어가 고질적으로 갖고 있던 불편함을 개선하고자 다양한 업데이트가 진행되었는데 이번 ES2020역시 이러한 방향성으로 업데이트 된 듯 하다.

아래는 이번 ES2020에 업데이트 된 새로운 기능들이다. 차례차례 살펴보도록 하자.

- String.prototype.matchAll
- import()
- BigInt
- Promise.allSettled
- globalThis
- for-in mechanics
- Optional Chainings
- Nullish coalescing Operator

### String.prototype.matchAll

`matchAll()` 메서드의 경우 정규 표현식과 일치하는 모든 문자열을 결과로 반환한다. 여기에는 capturing group 또한 포함되어 있다. 

```javascript
const regex = /t(e)(st(\d?))/g;
const string = 'test1test2';
const results = string.match(regex);
const resultsAll = [...string.matchAll(regex)];
console.log(results); // ['test1', 'test2']
console.log(resultsAll); // [["test1", "e", "st1", "1"], ["test2", "e", "st2", "2"]]
```

### Dynamic import()

Dynamic `import()`의 경우 JS 파일을 동적으로 import할 수 있게 한다. 기존에는 Webpack과 Babel을 통해서 가능했던 기능이 이제는 네이티브 기능으로 들어왔다.

기존의 `import`는 아래와 같이 사용한다. 이러한 정적 방식의 `import` 문은 함수 호출 결과로 경로를 지정할수 없을 뿐만 아니라, `if`문과 같은 분기문에서의 사용이 불가능하다.

```javascript
import module from ModuleName; 🙆‍♂️
import module from getModuleName();🙅‍♂️
if (true) { 
  import module from ModuleName;🙅‍♂️
}
```

ES2020의 `import()` 는 위의 한계점들을 가능하게 한다. 기본적인 사용은 아래와 같다. 반드시 `async/await`와 같은 비동기 처리 문법을 함께 사용해야 한다.

```javascript
if (res.status === 'ok') {
  const newModule = await import('./DataList.js')
  newModule.setDataList(res.data)
}
```

기존의 `import`와 비슷하게 `export`방식에 따라 모듈을 불러올 수 있다.

```javascript
export default () => { console.log('default') }
export const fetchData= () => { console.log('fetchData') }
const module = await import('fetch')
module.default() // default
module.fetchData() //fetchData
```

이를 통해, 네이티브로도 쉽게 코드 스플리팅이 가능해진다. 

### BigInt

그간 자바스크립트는 큰 숫자를 다루는 데 많은 문제를 가지고 있었다. `Number.MAX_SAFE_INTEGER` 에 해당하는 2^53-1보다 큰 숫자는 처리할 수가 없었다. 따라서, 아래와 같이 최대 숫자를 넘게 되면 더 이상 값이 증가하지 않는다. ES2020에서는 `BigInt` 객체가 도입되어 더 큰 숫자를 처리할 수 있게 되었다. 

```javascript
let oldBigNumber = Number.MAX_SAFE_INTEGER // 9007199254740991
++oldBigNumber // 9007199254740992
++oldBigNumber // 9007199254740992
```

![image-20200715173631850](https://user-images.githubusercontent.com/26768201/88042049-43b1bf80-cb86-11ea-82e3-71030c8e82f1.png)

`BigInt`를 쓰는 방법은 어렵지 않다. 숫자 뒤에 `n` 을 붙이게 되면 `BigInt`로 인식한다. 

```javascript
let newBigNumber = 9007199254740991n
++newBigNumber // 9007199254740992n
++newBigNumber // 9007199254740993n
++newBigNumber // 9007199254740994n
```

![image-20200715173839075](https://user-images.githubusercontent.com/26768201/88042055-46141980-cb86-11ea-9c6e-fc15d27b9aed.png)

여기서 주의할 점은 `BigInt`끼리 연산하지 않으면 에러가 발생한다. 또한, `1n != 1` 이다. 아예 새로운 타입으로 생각하고 접근해야 한다. 

```javascript
9007199254740994n +  9007199254740994n // 18014398509481988n
1n != 1 // false
```

또한, `BigInt`의 경우 말그대로 Int이기 때문에 소수점이 불가능하다.

```javascript
100n + 0.4 // Error
```

그리고 `BigInt`의 경우 스펙에 따르면 Maximum Value가 딱히 지정되어 있지 않지만, JS를 돌리는 플랫폼에 따라 최대 크기가 결정되기도 한다.

### Promise.allSettled

`Promise.allSettled`는 `Promise` 객체가 담긴 배열을 받아, 모든 `Promise` 의 결과를 얻을 때 까지 기다린다. `Promise.all` 과 비슷하지만, `Promise.all` 의 경우 하나라도 실패할 경우 해당 실패를 반환하지만, `Promise.allSettled` 는 실패와 관계 없이 모든 결과를 기다렸다가 반환한다.

```javascript
const promise1 = Promise.resolve(3);
const promise2 = new Promise((resolve, reject) => setTimeout(reject, 100, 'foo'));
const promises = [promise1, promise2];

Promise.allSettled(promises)
  .then((results) => 
        results.forEach((result) => console.log(result)));

// {status: "fulfilled", value: 3}
// {status: "rejected", reason: "foo"}

```

성공한 경우에 `status`는 `'fulfilled'`이며, `.value`를 통해 값을 전달받을 수 있다. 반대로 실패한 경우에 `status`는 `'rejected'` 며, `.reason`을 통해 에러를 받을 수 있다.

`Primise.allSettled`는 `Promise.all` , `Promise.any` 그리고 `Promise.race` 와의 차이를 간략히 살펴보자. 4가지 메서드 모두 배열 안에 있는 `Promise` 를 인자로 받고 `Promise` 객체를 반환한다.

* `Promise.all` :

  1. 전달된 `Promise` 모두 병렬로 실행하고, 완료될때 까지 기다린다. 

  2. 배열 안에 담긴 프로미스의 결과값을 담은 배열이 새로 반환되는 `Promise`의 result가 된다. 이때, 순서는 완료된 순서가 아닌 처음에 인자로 들어온 순서다.

  3. 하나라도 거부되면, 에러와 함께 그 결과를 반환한다.

* `Promise.allSettled` : 

  1. 전달된 `Promise` 모두 병렬로 실행하고, 완료될때 까지 기다린다.

  2. 배열 안에 담긴 프로미스의 결과값을 담은 배열이 새로 반환되는 `Promise`의 result가 된다. 이때, 순서는 완료된 순서가 아닌 처음에 인자로 들어온 순서다.

  3. 성공한 것과 실패한 것을 구분하여 `status`, `value`(실패의 경우 `reason`)를 결과에 담아 반환한다.

* `Promise.race` : 

  1. 전달된 `Promise` 모두 병렬로 실행하고, 가장 먼저 처리되는` Promise`의 결과(혹은 에러)를 반환한다.

* `Promise.any` : 

  1. 전달된 `Promise` 모두 병렬로 실행하고, 가장 먼저 성공하는 `Promise`의 결과를 반환한다.
  2. 모두 실패한 경우에는 해당 실패 이유가 담긴 배열을 반환한다.

![image-20200722174720603](https://user-images.githubusercontent.com/26768201/88157736-1b899580-cc46-11ea-883a-335da0255fb5.png)

### globalThis

다양한 자바스크립트의 런타임 환경(Browser, Node, web-worker ... )에서 `global Object` 는 각 런타임 환경마다 다르다. 브라우저의 경우 `window`를 사용하고, Node는 `global` 그리고 웹 워커는 `self`를 사용한다. 이러한 상황에서 동일한 코드를 사용하기란 여간 어려운 일이 아니었는데, ES2020에서는 `globalThis` 를 지원하여 이를 통일하였다.

```javascript
globalThis.XMLHttpRequest === window.XMLHttpRequest // true
```

### for-in mechanics

ECMA 사양에서는 `for-in` 의 순서를 딱히 명시하지 않았지만 ES2020에 들어와 순서가 공식적으로 표준화되었다.

```javascript
for (x in y)
```

### Optional Chainings

Optional Chaning은 `Object` 프로퍼티의 깊은 곳 까지 갈 수 있게 한다. 기존의 체이닝의 경우 만약 해당 프로퍼티가 존재하지 않다면 에러를 만들었지만, 옵셔널 체이닝의 등장으로 해당 프로퍼티의 존재 여부를 확인하는 코드를 따로 작성하지 않아도 된다. 만약 해당 프로퍼티가 Object내부에 존재한다면, 해당 값을 반환하고 아니라면 `undefined`를 반환한다.

```javascript
const obj = {
  prop1: {
    prop2: 'Hello'
  }
}

obj.prop1?.prop2 // Hello
obj.prop1?.idontcare // undefined
obj.prop3.idontcare // Error
obj.prop3?.idontcare // undefined
```

기존에 중첩된 객체의 프로퍼티에 접근할 때에는 아래와 같이 참조가 가능한지 확인하는 추가적인 작업이 필요하다.

```javascript
const props = obj.prop1 && obj.prop1.prop2;
```

Optional Chaining을 적용할 경우 이러한 추가적인 작업이 필요하지 않는다. 

```javascript
const props = obj.prop1?.prop2;
```

Optional Chaining은 또한, 프로퍼티 검사 뿐만 아니라 함수의 존재 여부에 따라 실행하는 코드 역시 작성할 수 있다. 아래의 두 코드는 동일한 코드다.

```javascript
if (onReject) {
  onReject(error.toString())
}
```

```javascript
onReject?.(error.toString())
```

### Nullish Coalescing Operator

Nullish Coalescing Operator(Null 병합 연산자)는 왼쪽 피연산자가 `null`이거나 `undefined`인 경우 오른쪽 피연산자를 반환하고 그렇지 않으면 왼쪽 피연산자를 반환한다.

```javascript
console.log(null ?? "hello") // hello
console.log(undefined ?? "world") // world
```

일반적으로 자바스크립트에서 많은 값들이 `falsy` 다. 여기서 `falsy`는 JS의 조건문, 반복문과 같이 `boolean` 값이 필요한 곳에서, 형 변환을 통해 특정 값을 `boolean` 값으로 변환하는 값들을 통틀어 부르는 말이다. 대표적인 예가 `0`, `""`(빈 문자열), `false`, `null`, `undefined`, `NaN` 다. 

![JS Equality](https://user-images.githubusercontent.com/26768201/88157738-1c222c00-cc46-11ea-886b-975b7ea72e49.jpg)

아래는 일반적으로 변수에 기본 값을 할당할 때 주로 쓰는 패턴이다. 

```javascript
const data = getValue();
const sumOfCount = data.sum || 128
```

`||`연산자의 경우 `data.sum` 의 값이 `falsy` 에 해당할 경우  `sumOfCount` 의 값은`128` 이다. 하지만 만약 `data.sum` 이 `0` 이고, 그 `0` 이 의도한 값이라 할지라도 `||` 연산자는 `0` 을 `false` 로 보기 때문에 `128` 을 값으로 가진다. 

Null 병합 연산자를 사용한다면 이러한 문제를 해결할 수 있다. 아까의 동일한 코드에서 `||` 를 Null 병합 연산자(`??`)로 바꾸기만 하면 된다. 이 경우 `data.sum` 이 `0` 의 값을 가진다면 `sumOfCount` 의 값은 `0` 이 된다. 

```javascript
const data = getValue();
const sumOfCount = data.sum ?? 128
```

`??` 는 `data.sum` 이 `null` 혹은 `undefined` 일 경우에만 오른쪽 값인 `128` 을 반환한다.

Null 병합 연산자는 And나 OR 연산자와 결합하여 사용하는 것이 불가능하다. 아래와 같이 사용할 경우 에러가 발생한다.

```javascript
null || undefined ?? "Hello"; 
true || undefined ?? "World";
```

## 글을 끝맺으며

ES2020에는 다양한 기능들이 새로 추가되었다. Javascript를 평소에 쓸 때, 불확실하다고 생각하며 조건문을 통해 확인하는 작업을 추가하곤 했는데, 위의 기능들이 모두 지원된다면 유용할 것 같다. ES6 ~ ES2020 사이의 추가된 기능들에 대해 세부적으로 알고 있으면 좋을 듯하다.

![image-20200722170701292](https://user-images.githubusercontent.com/26768201/88157721-17f60e80-cc46-11ea-92b1-66fb60899455.png)

### 학습 질문

1. Promise.all, allSettled, any, race의 차이점
2. BigInt는 일반적인 숫자 타입과 연산이 가능하다 O, X
3. String.match는 결과에 _를 포함하지 않고 String.matchAll은 _를 포함한다.

## Reference

- [10 New JavaScript Features in ES2020 That You Should Know](https://www.freecodecamp.org/news/javascript-new-features-es2020/)
- [JavaScript ES2020 Features With Simple Examples](https://medium.com/better-programming/javascript-es2020-features-with-simple-examples-d301dbef2c37)

* [What’s the difference between JavaScript and ECMAScript?](https://www.freecodecamp.org/news/whats-the-difference-between-javascript-and-ecmascript-cba48c73a2b5/)

* [[JavaScript] ES6, ES8, ES2017, ECMAScript 이게 다 뭐시여...?](https://geonlee.tistory.com/133)

* [위키백과 - 자바스크립트]([https://ko.wikipedia.org/wiki/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8](https://ko.wikipedia.org/wiki/자바스크립트))

* [위키백과 - Ecma 인터내셔널]([https://ko.wikipedia.org/wiki/Ecma_%EC%9D%B8%ED%84%B0%EB%82%B4%EC%85%94%EB%84%90](https://ko.wikipedia.org/wiki/Ecma_인터내셔널))

* [Better match results with String.prototype.matchAll()](https://developers.google.com/web/updates/2019/02/string-matchall)

* [Promise.race vs. Promise.any And Promise.all vs. Promise.allSettled](https://sung.codes/blog/2019/05/18/promise-race-vs-promise-any-and-promise-all-vs-promise-allsettled/)

