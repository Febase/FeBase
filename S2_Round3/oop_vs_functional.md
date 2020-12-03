---
title: 함수형 프로그래밍과 클래스형 프로그래밍
date: 2020-12-03 07:30:00
author: tjdud0123 (엄서영)
category: S2_Round3
---

# 🥊 함수형 (FP) vs 클래스형 (OOP)
![](https://images.velog.io/images/tjdud0123/post/4dd7ef1f-2dcf-4088-a469-215aaca28b36/image.png)
<hr>

## 🔍 들어가기 전에

### 💡 &nbsp; 일급 객체
- 자바스크립트의 함수는 일급 객체
- 함수를 다른 함수의 파라미터로 전달 가능
- 반환 값으로 사용 가능
### 💡 &nbsp; 고차 함수
> 다른 함수를 매개 변수로 사용하여 데이터를 처리하거나 함수를 반환하는 함수

- 함수가 일급 객체이기 때문에 가능
### 💡 &nbsp; 순수 함수
> 동일한 인자를 넣었을 때 항상 동일한 리턴값을 반환하고 선언시점이나 외부에 영향을 받지 않는 함수

- ex) random, getDate 등의 함수는 순수 함수가 아님,
선언 시점에 따라 다라지는 함수도 순수 함수가 아님
```js
let c = 10;
function add2(a, b) {
  return a + b + c;
}
console.log( add2(10, 2) ); // 22
c = 20;
console.log( add2(10, 2) ); // 32
```


### 💡 &nbsp; 선언형 vs 명령형
[참고](https://boxfoxs.tistory.com/430)

#### 👀 &nbsp; 명령형 프로그래밍
**"어떻게" 수행**하는지에 초점
> 12번 테이블 자리가 비어있으니 나는 저 자리로 똑바로 걸어가 앉을 것입니다.

```js
let inputTxt = 'This is a computer';
let result = "";

for(let i=0; i<inputTxt.length; i++) {
    result += inputTxt[i] === " " ? "-" : string[i]
}

console.log(result); // This-is-a-computer
```

#### 👀 &nbsp; 선언형 프로그래밍
**"무엇을" 원하는지**에 초점
> 네 명 앉을자리를 부탁해요

```js
const inputTxt = 'This is a computer';
const blankToHyphen = inputTxt.replace(/ /g, '-');

console.log(blankToHyphen); // This-is-a-computer
```


❗️ **선언형** > 명령형

- 선언형 프로그래밍은 상황에 독립적
- 선언형 코드는 해당 코드가 달성하고자 하는 것이 무엇인지 만을 나열해 **가독성**과 **재사용성**을 높일 수 있음
- 추론하기 쉬운 애플리케이션을 만들어내 확장하기 쉬움
<hr>

## 함수형 프로그래밍 (esp in JS)
> 성공적인 프로그래밍을 위해 **부수효과를 미워하고 조합성을 강조**하는 프로그래밍 패러다임
- **순수함수**를 통해 부수효과를 미워하고 조합성을 강조해 모듈화 수준을 높혀 **생산성**을 높인다.

### 예제 및 디자인 패턴
##### 🤔 명령형 코드

#### 🧒 &nbsp; users
```js
  // 3. 30세 미만인 users를 거른다.
let temp_users = [];
for (let i = 0; i < users.length; i++) {
  if (users[i].age < 30) {
    temp_users.push(users[i]);
  }
}
console.log(temp_users);
```

##### 🧚 함수형 프로그래밍
```js
const over_30_cond = user => user.age >= 30
const over_30_users = _filter(users, over_30_cond);
console.log(over_30);
```

### 💡 &nbsp; 함수형 프로그래밍 장점
- 부작용이 적다 (사이드 이펙트(side effect)가 없다)
- 외부에 있는 데이터 의존하지 않으며, 함수 외부에 있는 데이터를 변경하지 않는다
- 표현력이 좋다, 가독성이 좋다
- 재사용성과 조합성이 높다

> - 반복문 대신에 **map과 filter, reduce, all, any, find** 등을 사용
- 명령형으로 작성하지 말고 선언형으로 작성
- 파이프라인을 사용


### 👀 &nbsp; 커링
> 다중 인수를 갖는 함수를 단일 인수를 갖는 함수들의 함수열로 바꾸는 것을 말한다.

[참고](https://dev-momo.tistory.com/entry/Currying-in-Javascript)

#### ex 1

##### 🤔 다중인수
```js
let sum = function (x, y) {
    return x + y;
};

console.log(sum(5, 7));  // 12
```
##### 🧚 커링 사용
```js
let sum = x => y => x+y;

let sum5 = sum(5);
let sum12 = sum5(7);

console.log(sum12, sum(5)(7)); // 12 12
```
#### ex 2
##### 🤔 다중인수

```js
let printInfo = function(group, name){
    console.log(group + ', ' + name);
};

```

```js
printInfo('dev-momo', 'haegul');    // dev-momo, haegul
printInfo('dev-momo', 'jiwon');     // dev-momo, jiwon
printInfo('dev-momo', 'sungcheon'); // dev-momo, sungcheon
```
##### 🧚 커링 사용
```js
// currying
let printInfo = group => name => console.log(group + ', ' + name);

let momoGroup = printInfo('dev-momo');
momoGroup('haegul');    // dev-momo, haegul
momoGroup('jiwon');     // dev-momo, jiwon
momoGroup('sungcheon'); // dev-momo, sungcheon
```

<hr>

## 객체지향 프로그래밍
> 컴퓨터 프로그램을 명령어의 목록으로 보는 시각에서 벗어나 **여러 개의 독립된 단위**, 즉 **"객체"들의 모임**으로 파악하고자 하는 것

### 💡 &nbsp; 기본 구성 요소
- **클래스(Class)** - 같은 종류(또는 문제 해결을 위한)의 집단에 속하는 속성(attribute)과 행위(behavior)를 정의한 것
- **객체(Object)** - 클래스의 인스턴스(실제로 메모리상에 할당된 것)이다. 객체는 자신 고유의 속성(attribute)을 가지며 클래스에서 정의한 행위(behavior)를 수행할 수 있다.
- **메서드(Method), 메시지(Message)** - 클래스로부터 생성된 객체를 사용하는 방법으로서 객체에 명령을 내리는 메시지라 할 수 있다.

### 💡 &nbsp; 특징
- **자료 추상화** - 불필요한 정보는 숨기고 중요한 정보만을 표현함으로써 프로그램을 간단히 만드는 것. 자료 표현과 자료형의 연산을 캡슐화한 것으로 접근 제어를 통해서 자료형의 정보를 은닉
- **상속** - 새로운 클래스가 기존의 클래스의 자료와 연산을 이용할 수 있게 하는 기능. 클래스 간의 종속 관계를 형성함으로써 객체를 조직화할 수 있다.
- **다형성** - 어떤 한 요소에 여러 개념을 넣어 놓는 것. 일반적으로 **오버라이딩**(같은 이름의 메소드가 여러 클래스에서 다른 기능을 하는 것)이나 **오버로딩**(같은 이름의 메소드가 인자의 개수나 자료형에 따라서 다른 기능을 하는 것)을 의미한다.

### 💡 &nbsp; 장점
문제 해결을 위한 데이터를 모아 놓은 데이터형을 사용함으로써 **응집력을 강화**하고, 클래스간에 독립적으로 디자인함으로써 **결합력을 약하게** 할 수 있다.

<hr>

## 함수형 프로그래밍과 객체지향 프로그래밍 간단 비교

#### 👀 &nbsp; 함수형 프로그래밍
🏃 "동사" 중심 - (무엇을 원하느냐, 어떤 것을 하느냐 - 함수기준)
```js
moveLeft(penguin);
moveLeft(dog);
moveLeft({x: -5, y: 2})
swim(penguin, fast)
```
#### 👀 &nbsp; 객체지향 프로그래밍
🐧 "명사" 중심 - (데이터/객체 기준)
```js
penguin.moveLeft();
penguin.swim();
dog.moveLeft({x: -5, y: 2});
dog.run();
```

<hr>


## 클래스 컴포넌트와 함수형 컴포넌트

### 👀 &nbsp; in Vanilla Js

#### 🏃 &nbsp; 함수형

```js
// 함수형
function TodoList(data, queryId) {
  this.todos = data
  this.render = function () {
    document.querySelector(queryId).innerHTML =
      this.todos
      .map(todo => todo.isCompleted ? `<li><s>${todo.text}</s></li>` :
           `<li>${todo.text}</li>`)
      .join('\n')
  }
  this.setState = function (nextData) {
    this.todos = nextData
    this.render()
  }
}

const todoList = new TodoList(data, '#todo-list');
todoList.render();
todoList.setState([{
  text: '새롭게 할 일',
  isCompleted: false
}]);

```

#### 🐧  &nbsp; 클래스형

```js
// 클래스형
class TodoList {
  constructor(data, queryId) {
    this.todos = data
    this.queryId = queryId
  }
  render() {
    document.querySelector(
      this.queryId
    ).innerHTML = this.todos
      .map((todo) =>
           todo.isCompleted ?
           `<li><s>${todo.text}</s></li>` :
           `<li>${todo.text}</li>`
          )
      .join('\n')
  }
  setState(nextData) {
    this.todos = nextData
    this.render()
  }
}

const todoList = new TodoList(data, '#todo-list')
todoList.render()
todoList.setState([{
  text: '새롭게 할 일',
  isCompleted: false,
}, ])
```

### 👀 &nbsp; in React Js
[참고](https://devowen.com/298)

#### 🏃 &nbsp; 함수형
- 클래스형 컴포넌트보다 선언하기가 좀 더 편하다.
- 메모리 자원을 덜 사용한다
- state와 라이프사이클 API를 사용할 수 없다는 단점은 리액트 훅이 도입되면서 해결 - ex) useState
```js
// 함수형
import React from 'react';

function App() {
  const name = '리액트';
  return <div>{name}</div>;
}

export default App;
```

#### 🐧  &nbsp; 클래스형

- state 기능 및 라이프 사이클 기능을 사용할 수 있으며 임의 메서드를 정의할 수 있다
- render 함수가 꼭 있어야 하고, 그 안에서 보여 주어야 할 JSX를 반환해야 한다
- 오래된 프로젝트는 대부분 클래스형으로 되어있어 유지보수를 위해서 알아두어야 할 필요가 있음
```js
// 클래스형
import React, { Component } from 'react';

class App extends Component {
  render() {
    const name = '리액트';
    return <div>{name}</div>;
  }
}

export default App;
```

>#### ❓ &nbsp; 왜 클래스형에서 함수형으로 넘어갔을까
(현재 공식문서에서 함수형 컴포넌트와 훅 사용 권장 중)

- Hook를 사용하면 컴포넌트로 부터 상태 관련 로직을 추상화 할 수 있다. 이것은 독립적인 테스트와 재사용이 가능하다.
- Hook은 계층 변화 없이 상태 관련 로직을 재 사용할 수 있어  많은 컴포넌트들이 공유하기 쉬워지는 역할을 한다.
- Class 컴포넌트보다 Functional 컴포넌트가 가독성이 뛰어나다
- Class 컴포넌트가 최적화를 더 느린 경로로 되돌리는 의도하지 않은 패턴을 장려할 수 있다
- Class는 잘 축소되지 않고, 핫 리로딩을 깨지기 쉽고 신뢰할 수 없게 만든다

- ** 클래스 컴포넌트의 문제점 **

![](https://images.velog.io/images/tjdud0123/post/d6bd47e6-2a0a-47e1-baa6-2963377155e0/image.png)![](https://blog.kakaocdn.net/dn/bAtvmN/btqtZOdpNW7/3dof9jkthjJNdtKlu7og51/img.gif)

클래스 컴포넌트에서 follow 클릭 후 3초가 지나기 이전에 다른 유저의 페이지를 누르면 이전 유저가 아닌 두번째로 선택한 유저에대한 알림이 발생한다. 이는 **클래스 컴포넌트는 props를 재사용 하기 때문**이라고 한다.


<hr>

## ❗️ 결론

**가독성이 좋고** **재사용성**과 **조합성**이 높으며 **에러 추적이 쉬운** 
`함수형 프로그래밍` 을 활용하자!
