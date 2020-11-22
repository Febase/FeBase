---
title: RxJS R아보기
date: 2020-11-19 00:00:00
author: symoon
category: S2_Round2
---


# RxJS R아보기


## RxJS란 무엇인가

> "An API for asynchronous programming with observable streams"

**R**eactive e**X**tensions Library for **J**ava**S**cript의 약자로, 옵저버 패턴을 통해 이벤트 스트림을 제어하여 비동기 프로그래밍을 처리하는 (API를 제공하는) 라이브러리이다. 현재 안정화 버전은 6이며, 베타 버전인 7까지 나와있다. Angular에는 이 RxJS가 기본적으로 내장되어 있다.



## Reactive? Stream? Observable? 그게 다 뭔데?!

### Reactive Programming

![마블 다이어그램](http://reactivex.io/assets/operators/legend.png "이미지 출처: http://reactivex.io/documentation/ko/observable.html")

리액티브 프로그래밍은 말그대로 "반응형"으로 프로그래밍하는 것이다. 
명령형 프로그래밍은 개발자가 작성한 코드에 따라 순서대로 코드가 실행되며, 데이터가 필요하면 요청을 해야한다(외부 환경에서 데이터를 당겨오는 방식인 Pull). 반면, 리액티브 프로그래밍은 데이터 스트림을 구독하고 있다가 데이터에 어떠한 변화가 감지되었을 때 그것에 **반응**하여 데이터를 얻는 방식이다(외부 환경이 데이터를 내보내는 방식인 Push). 

### Stream
데이터를 하나의 연속적인 흐름으로 보는 것이다. 위에서 언급했듯, 리액티브 프로그래밍 방식에서는 이 데이터 스트림을 구독한다. 리액티브 프로그래밍 방식에서 이 스트림은 Observable 객체로 만들어진다.

### Observable
Observable은 데이터 스트림을 만들고 내보내는 객체이고, Observer는 이 옵저버블 객체가 내보낸 데이터를 받아 가공하는 역할을 하는 객체이다.

#### Observable 생성
Observable객체를 생성하는 연산자는 `create`, `from`, `fromEvent`, `fromPromise`, `of` 등이 있다. 
이중 일반적으로 `from`, `fromPromise`, `of`가 많이 사용된다. 

일반적으로 이벤트 리스너를 등록하는 방식은 아래와 같다.

    var button = document.querySelector('button');
    button.addEventListener('click', () => console.log('Clicked!'));  //버튼 클릭 이벤트가 발생하면 콘솔로그에 'Clicked!'를 찍음


RxJS에서는 연산자를 이용하여 아래와 같이 생성할 수 있다.

    var button = document.querySelector('button');
    
    Rx.Observable.fromEvent(button, 'click') //클릭 이벤트를 emit하는 Observable 객체를 생성함
      .subscribe(() => console.log('Clicked!')); //체이닝을 이용해 해당 Observable 객체를 구독하며, Observable에서 데이터 전달시 콜백함수 
      

* 참고
fromEvent 연산자는 이벤트를 Observable 시퀀스로 만들어줌
`fromEvent(target: EventTargetLike, eventName: string, selector: function): Observable`


#### 옵저버 메소드
`onNext` 새로운 데이터를 내보낼 때 호출되는 메소드. 파라미터를 통해 옵저버블을 전달한다.
`onError` 데이터가 생성되지 않았거나 오류가 발생할 경우 호출되는 메소드. 이 메소드가 호출되면 `onNext`나 `onComplete`가 호출되지 않음.
`onComplete` 오류가 없으면 마지막 `onNext`를 호출한 후 호출되는 메소드


#### 연산자
RxJS에서 제공하는 대부분의 연산자는 이 옵저버블 객체에서 동작하고, 옵저버블 객체를 반환한다. 즉, 연산자 체이닝이 가능하다. 이 연산자 체인은 순서에 따라 결과가 달라지므로 순서대로 실행되어야한다. 
대표적인 연산자는 `create`, `map`, `merge` 등이 있다. 


#### 예제코드
코드

    import { Observable } from 'rxjs';
 
    //Observable 객체를 생성한다.(관찰 가능한 상태로 만드는 것)
    //해당코드를 구독하면 즉시 값(1,2,3)을 내보내고, 1초 후에 4를 내보낸뒤 완료처리된다.
    const observable = new Observable(subscriber => {
      subscriber.next(1);
      subscriber.next(2);
      subscriber.next(3);
      setTimeout(() => {
        subscriber.next(4);
        subscriber.complete();
      }, 1000);
    });
 
    console.log('just before subscribe'); //가장 먼저 실행된다.
    
    //위에서 생성한 observable을 구독한다.
    observable.subscribe({
      next(x) { console.log('got value ' + x); }, //새로운 값을 받아 콘솔을 찍는다.
      error(err) { console.error('something wrong occurred: ' + err); }, //에러가 발생했을 경우 콘솔을 찍는다.
      complete() { console.log('done'); } //마지막 next 실행 후 콘솔을 찍는다.
    });
    console.log('just after subscribe'); 

실행결과

    just before subscribe
    got value 1
    got value 2
    got value 3
    just after subscribe //RxJS는 동시에 여러 코드가 실행 가능하기 때문에, 1초 사에에 다음 코드가 실행됨.
    got value 4 //setTimeout으로 인해 1초 후 내보내짐
    done 


## 그래서 RxJS, 뭐가 좋은건데?
콜백, 프로미스 방식의 한계를 보완할 수 있다. 한 번에 하나의 데이터만 처리할 수 있는 프로미스와 달리 데이터를 스트림으로 만들기 때문에 *동기 / 비동기에 관계 없이 데이터를 일관적으로 처리 가능*하며, *연속성을 가진 데이터를 처리*할 수 있다. 그러면서도 연산자 체이닝을 통해 비동기를 효과적으로 처리하며, 프로미스 방식은 한 번 실행되고 나면 요청을 취소할 수가 없지만 옵저버블은 취소가 가능하다.(`unsubscribe()`를 통해 구독 취소가 가능함)
또한 하나의 코드가 실행결과를 리턴할 때까지 기다릴 필요없이 다음 코드를 실행할 수 있어, *한 번에 여러 코드를 실행 가능*하다.

단점은, 초기 학습 비용이 크다는 점.

---
### 참고

http://reactivex.io/

https://velog.io/@dvmflstm/RxJS-Practice

https://poiemaweb.com/angular-rxjs

https://tienne.gitbooks.io/learnrxjs/content/

https://hyunseob.github.io/2016/10/09/understanding-reactive-programming-and-rxjs/

https://rxjs-dev.firebaseapp.com/
