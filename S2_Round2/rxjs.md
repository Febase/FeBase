---
title: RxJS R아보기
date: 2020-11-19 00:00:00
author: symoon
category: S2_Round2
---


# RxJS R아보기


### RxJS란 무엇인가

"An API for asynchronous programming with observable streams"

**R**eactive e**X**tensions Library for **J**ava**S**cript의 약자로, 옵저버 패턴을 통해 이벤트 스트림을 제어하여 비동기 프로그래밍을 처리하는 (API를 제공하는) 라이브러리이다. 현재 안정화 버전은 6이며, 베타 버전인 7까지 나와있다. Angular에는 이 RxJS가 기본적으로 내장되어 있다.


### Reactive? Stream? Observable? 그게 다 뭔데?!

##### Reactive Programming

![마블 다이어그램](https://poiemaweb.com/img/observable-map.png "이미지 출처: https://poiemaweb.com/angular-rxjs")

리액티브 프로그래밍은 말그대로 "반응형"으로 프로그래밍하는 것이다. 
명령형 프로그래밍은 개발자가 작성한 코드에 따라 순서대로 코드가 실행되며, 데이터가 필요하면 요청을 해야한다(외부 환경에서 데이터를 당겨오는 방식인 Pull). 반면, 리액티브 프로그래밍은 데이터 스트림을 구독하고 있다가 데이터에 어떠한 변화가 감지되었을 때 그것에 **반응**하여 데이터를 얻는 방식이다(외부 환경이 데이터를 내보내는 방식인 Push). 

##### Stream
데이터를 하나의 연속적인 흐름으로 보는 것이다. 위에서 언급했듯, 리액티브 프로그래밍 방식에서는 이 데이터 스트림을 구독한다. 리액티브 프로그래밍 방식에서 이 스트림은 Observable 객체로 만들어진다.

##### Observable
Observable은 데이터 스트림을 만들고 내보내는 객체이고, Observer는 이 옵저버블 객체가 내보낸 데이터를 받아 가공하는 역할을 하는 객체이다. 
RxJS에서 제공하는 대부분의 연산자는 이 옵저버블 객체에서 동작하고, 옵저버블 객체를 반환한다. 즉, 연산자 체이닝이 가능하다. 이 연산자 체인은 순서에 따라 결과가 달라지므로 순서대로 실행되어야한다. 
대표적인 연산자는 `create`, `map`, `merge` 등이 있다. 


### 그래서 RxJS, 뭐가 좋은건데?
* 동기 / 비동기에 관계 없이 데이터를 일관적으로 처리
* 콜백함수나 프로미스가 갖는 문제들을 커버(ex. 콜백지옥, 비연속적 데이터 처리 등)


---
### 참고

http://reactivex.io/
https://velog.io/@dvmflstm/RxJS-Practice
https://poiemaweb.com/angular-rxjs
https://tienne.gitbooks.io/learnrxjs/content/
https://hyunseob.github.io/2016/10/09/understanding-reactive-programming-and-rxjs/
