# Iterator & Generator

---

### 학습 목표

- Iteratior에 대한 이해
- iteration protocols에 대해 알아보기
- generator에 대해서 알아보기

ES6에서 도입된 iterator, generator 개념

generator는 iterator에 의존하는 개념이다.

## Iterator

---

iterator는 책갈피와 비슷한 개념이다. 배열은 iterable의 좋은 예시다.

`values()`라는 메서드를 통해 이터레이터를 만들 수 있다.

`next`를 호출하면 `value` 프로퍼티와 `done` 프로터피를 가진 객체를 반환한다.

```jsx
​> const arr = [1, 2, 3];
> const it = arr.values();
> it.next();
{ value: 1, done: false }
> it.next();
{ value: 2, done: false }
> it.next();
{ value: 3, done: false }
> it.next();
{ value: undefined, done: true }
> it.next();
{ value: undefined, done: true }
```

`for ... of` 또한 ES6에 등장했다. 

`while` 과 `iterator` 로 따라하면 아래와 같이 작성할 수 있다.

```jsx
const arr = [1, 2, 3];

const iterator = arr.values();
let current = iterator.next();
while (!current.done) {
	// do something with current.value
	current = iterator.next();
}
```

## Iteration protocol

---

`iterator protocol` 을 준수하면 모든 객체를 이터러블 객체로 바꿀 수 있다.

```jsx
class Dictionary {
  constructor() {
    this.dict = {};
  }
  
  addWord(key, value) {
    this.dict[key] = value;
  }

  [Symbol.iterator]() {
    return Object.entries(this.dict).values();
  }
//  *[Symbol.iterator]() {
//    for (let [k, v] of Object.entries(this.dict)) {
//      yield [k, v];
//    }
  }
}

const dictionary  = new Dictionary();

dictionary.addWord('abc', '가나다');
dictionary.addWord('phone', '전화기');
dictionary.addWord('word', '단어');

for (const [key, value] of dictionary) {
  console.log(key, value);
}

word 단어
phone 전화기
abc 가나다
```

`Dictionary` 의 인스턴스를 배열처럼 사용할 수 있게 된다.

### [Symbol.iterator]가 궁금해서 찾아본 내용

대괄호(square bracket)으로 감싸여진 것은 함수 이름이 동적이며 런타임에 결정될 것이라고 javascript 엔진에게 말해주는 것이다. 위의 `addWord` 를 `['addWord']` 라고 작성해도 똑같이 동작한다. loop 문 안에서 함수들을 정의할 때 `['function' + idx]` 식으로 사용하여 정의되는 함수들의 이름을 붙여줄 수 있다.

`Symbol.iterator` 는 built-in symbol로 객체의 default iterator를 반환해주는 메서드로 `for...of` 에서 사용된다.

**iterator 직접 만들어보기.**

```jsx
  [Symbol.iterator]() {
    const keys = Object.keys(this.dict);
    const dict = this.dict;
    let idx = 0;
    return {
      next() {
        if (idx >= keys.length) {
          return { value: undefined, done: true };
        }
        return { value: [keys[idx], dict[keys[idx++]]], done: false };
      }
    }
	}
```

잘 동작한다!

## Iteration protocol? Iterator protocol? Iterable protocol??

---

왜 계속 프로토콜 이름이 혼용되지? 라고 생각했지만

**Iteration protocols** 에 

**Iterable protocol** 과 **Iterator protocol** 이 속하는 것이다.

### iterable protocol

Javascript 객체들이 iteration 동작을 정의하거나 사용자 정의하는 것을 허용해준다. iteratoin 동작이 built-in으로 정의된 것들에는 Array, TypedArray, String, Map, Set이 있다.

사용자 정의로 iterable한 객체를 만들고자 한다면 @@iterator 메소드를 구현해야 한다. (@@iterator는 Symbol.iterator를 의미함)

### iterator protocol

value들의 sequence를 만드는 방법에 대한 표준을 정의한다. 객체가 next() 메소드를 갖고 있으며, 아래의 규칙을 따르는 객체를 iterator로 간주한다.

- next() method를 갖고 있음
- next()는 arguments가 없으며, `done` 과 `value` 를 가진 object를 반환해야 한다.
- `done: boolean` iterator의 반복작업이 끝났을 경우 true, 아닐경우 false이다.
- `value` iterator로부터 반환되는 모든 값을 의미하며, `done` 이 true일 경우 생략 가능

## Generator

---

Iterator를 사용해 자신의 실행을 제어하는 함수

일반적인 함수는 매개변수를 받고 값을 반환하지만, 호출자는 매개변수를 주는 것 외에 함수의 실행을 제어할 방법이 전혀 없다. 하지만 제너레이터는 제어할 수 있다!

일반 함수와 다른 두가지 특징을 갖는다. 

- 언제든 호출자에게 제어권을 넘길 수 있다. (yield)
- 제너레이터는 호출한 즉시 실행되지 않는 대신, iterator를 반환하고, iterator의 next method를 호출함에 따라 실행된다.

**예제코드**

```jsx
function* gengen() {
	for (let i = 0;i < 10;i++){
		yield i;
	}
}

const iterer = gengen();
while (true) {
  const { value, done } = iterer.next();
  if (done) break;
  console.log(value);
}

// 0~9 출력
// iterator를 반환하기 때문에 for...of 로 간편하게 사용가능하다.

const foriter = gengen();
for (let value of foriter) {
  console.log(value);
}
```

`yield` 를 통해 양방향 통신이 가능하다. `next()` 의 인자로 value를 전달 할 수 있다.

**양방향 통신 쉬운 예제**

```jsx
function* talk() {
	const name = yield "이름을 말해주세요";
	const job = yield "직업을 말해주세요";
  return `${name} ${job}님, 안녕하세요!`;
}

const talker = talk();
talker.next(); // { value: "이름을 말해주세요", done: false }
talker.next("네일러"); // { value: "직업을 말해주세요", done: false }
talker.next("백수"); // { value: "네일러 백수님, 안녕하세요!, done: true }
```

마지막에 `yield` 대신 `return`을 사용하는 경우 마지막의 `done`은 참이 된다. 이러한 경우 `for...of` 내부에서 제너레이터를 사용할 때 `done` 이 참이기 때문에 루프를 탈출한다. `done`이 `true` 일 때는 `value`에 별로 신경을 쓰지 않기 때문에 중요한 값을 돌려주려 할 때 `return` 을 사용하지 않기를 권장한다. 대신 특정 조건에서 제너레이터를 중간에 종료시키는 목적으로 사용하기에 좋다.

**중간 종료 예시**

```jsx
function* dootalk() {
	const response = yield "도를 믿으십니까?";
	if (response === "아니요" || !response) {
		return;
	}
  
	const gotoCaffee = yield "카페가서 얘기좀 할까요?";
  // do something..
}
```

메인 스크립트에서는 next를 통해 제어권을 talk에게 주고, talk에서는 yield로 다시 제어권을 넘겨준다. 호출자가 제너레이터에게 정보를 넘겨 줄 수 있어서 제너레이터가 다양한 동작을 할수 있게 된다.

원시적인 **generator runner 만들기**

```jsx
function run(generator, ...args) {
	const iter = generator(args);
	(function iterate(prev) {
		const next = iter.next(prev);
		if (next.done) {
			return Promise.resolve(next.value);
		}
		Promise.resolve(next.value)
			.then(res => iterate(res));
	})();
}

function* doSomething(url) {
  const response = yield axios.get(url);
  console.log(response.data);
}

run(doSomething, 'https://www.google.com');
```

axios.get 메서드를 보내게 되고 next.value는 promise 객체가 된다. 따라서 이를 resolve 시키고 그 다음 iterate를 수행해서 비동기에 대한 제어가 가능해진다.

```jsx
function async doSomething(url) {
	const response = await axios.get(url);
	console.log(response.data);
}
```

async await과 유사한 동작을 할 수 있게 되었다. 상용 grun을 직접 만드는 것은 매우 까다롭다. 위의 코드는 에러 처리나 여러 generator를 동시적으로 처리하는 작업을 전혀 하지 못한다. 이미 좋은 grun들이 많으니 라이브러리를 사용하는 것을 권장한다.

Babel 트렌스파일러를 이용해서 async await을 분석한 포스팅이다. Babel이 async await을 트렌스파일링을 했을 때 generator와 Promise를 사용해 변환시킨다.

### 질문

- Iterable protocol이란?
- Iterator protocol이란?
- generator는 어떻게 동작할까?

### REFERENCE

[Using the Iterator Symbol to Control How JavaScript Processes Your Data](https://mcculloughwebservices.com/2016/08/24/sorting-arrays-with-javascript-iterators/)

[Iteration protocols](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Iteration_protocols)

[러닝 자바스크립트](https://www.hanbit.co.kr/store/books/look.php?p_code=B2328850940)