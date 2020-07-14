---
title: 자바스크립트 동작 원리
date: 2020-06-25 00:00:00
author: jinsunee
category: Javascript
---

# 자바스크립트 동작 원리

## 브라우저 동작 원리

브라우저는 크게 렌더링 엔진, 자바스크립트 엔진으로 나뉜다.
사용자가 참조하고자 하는 페이지를 서버에게 요청 후 그에 대한 응답을 화면에 보여주는 일을 한다.

- 렌더링 엔진 - 서버로부터 받은 HTML, CSS은 브라우저 렌더링 엔진의 HTML파서, CSS 파서에 의해 DOM, CSSOM 트리가 만들어지고 렌더 트리로 결합된다. 렌더 트리를 기반으로 브라우저는 웹페이지를 표시한다.
- 자바스크립트 엔진 - JS로 작성한 코드를 해석하고 실행하는 인터프리터이다. 렌더링 엔진의 HTML 파서가 DOM 생성 프로세스를 하던 중 스크립트 태그를 만나면, 자바스크립트 코드를 실행시키기 위해 자바스크립트 엔진에게 제어권한을 넘겨주게 된다. - DOM 트리가 다 형성되지 않았는데 자바스크립트에서 해당 DOM을 조작하려고 하면 문제가 발생하기 때문에 `<script>` 태그는 html의 body태그 제일 아래에 놓는 것이 좋다.

## 자바스크립트 엔진

자바스크립트는 싱글 스레드 언어로 한번에 하나의 테스크만 처리할 수 있다. 구글에서 개발한 V8을 비롯해 대부분의 자바스크립트 엔진은 크게 세 영역으로 나뉜다.

- Call Stack
- Task Queue(Event Queue)
- Heap

### 1. Call Stack

호출 스택은 자바스크립트 프로그램에서 우리가 어디에 있는지 기록하는 데이터 구조이다. 함수를 실행하면 함수에 대한 기록을 스택 제일 위에 추가한다. (push) 함수의 결과값을 반환하면 스택에서 제거된다. (pop)

```
function foo(b){
  var a = 5;
  return a * b + 10
}
function bar(x) {
  var y = 3;
  return foo(x*y);
}

console.log(bar(6));
```

1. 먼저 bar라는 함수를 호출했고, bar에 해당하는 스택 프레임이 생긴다. 그 안에는 y와 같은 local 변수가 함께 생성된다.
2. bar 함수는 foo 함수를 호출하고 있다. 아직 bar는 값을 반환하지 않은 상태이니 스택에서 pop되지 않고 호출된 foo 함수가 Call Stack에 push 된다.
3. foo 함수에서는 a\*b + 10라는 값을 리턴하면서 함수의 역할을 마쳤으므로 stack 에서 pop 된다.
4. 다시 bar 함수로 돌아와서 foo 함수로 받은 값을 리턴하며 함수를 종료하고 스택에서 pop된다.

자바스크립트는 단일 호출 스택을 사용한다. 이 말은 하나의 함수가 실행되고 있으면 이 함수의 실행이 끝날 때까지 다른 태스크들은 수행될 수 없다는 뜻이다. 앞의 예처럼 호출된 함수가 차례대로 쌓이고 값을 반환하면서 순서대로 pop된다.

이러한 단일 호출 스택의 문제점은 스택이 한번에 하나의 일만 처리할 수 있기 때문에 만약 그 함수가 복잡한 연산을 수행해야한다고 하면 다른 함수가 실행되지 못하는 상황이 생긴다.

가장 쉬운 해결책은 비동기 콜백을 사용하는 것이다. 코드의 일부를 실행하고 나중에 실행될 콜백함수를 제공한다. 비동기 콜백은 즉시 호출 스택에 쌓이지 않고 Event Queue에서 기다렸다가 호출스택이 비어있는 시점에 실행된다.

![image](https://user-images.githubusercontent.com/31176502/85106225-d0472600-b246-11ea-8c8e-d44ea582fe78.png)

#### stack overflow

stack overflow 는 누구나 봤을 법한 에러인데, 여기서 stack 이 바로 call stack 이다.
stack에 한정된 자원을 넘어서 계속해서 쌓이다보면 stack이 넘치게 되는데 그걸 stack overflow라고 한다.

```
function foo() {
    foo();
}
foo();
```

![image](https://user-images.githubusercontent.com/31176502/85106299-f076e500-b246-11ea-871c-8f4cc0747483.png)

## 2. Heap

메모리 힙은 동적으로 만들어진 객체(인스턴스)가 메모리에 할당되는 곳이다.

### Memory Heap

메모리 생존 주기는 프로그래밍 언어와 관계없이 비슷하다.

1. 필요할 때 할당한다. (allocate)
2. 사용한다. (읽기, 쓰기) (use)
3. 필요없어지면 해제한다. (release)

![image](https://user-images.githubusercontent.com/31176502/85091682-fbb81980-b222-11ea-9b5a-97a6450c7679.png)

#### Garbage Collector (GC)

콜스택과 메모리 힙을 배우면서 각각의 공간은 무제한이 아니고 한정적임을 알 수 있다.
자바스크립트는 이 공간을 효율적으로 관리하기 위해서, 더 이상 효용가치가 없다고 판단되는 변수, 함수 등을 함수 실행 종료 후 메모리 힙에서 제거하는 동작을 수행한다.
필요한 데이터만 메모리 힙에 저장함으로써 메모리를 더욱 여유롭게 관리한다.
따라서, 자바스크립트는 Garbage Collected Language라고 말할 수 있으며, 이런 역할을 수행해주는 도구를 Garbage Collector 라고 한다.

##### Garbage Collector 가 동작하는 원리

표시하고-쓸기(Mark-and-Sweep) 알고리즘
roots로 부터 시작하여 roots가 참조하는 오브젝트들, roots가 참조하는 오브젝트가 참조하는 오브젝트들 ... -> 닿을 수 있는 오브젝트라고 표시한다. 그리고 닿을 수 있는 오브젝트가 아닌 닿을 수 없는 오브젝트에 대해 가비지 콜렉션을 수행한다.

![image](https://user-images.githubusercontent.com/31176502/85106437-274cfb00-b247-11ea-83ae-fe5e8e9fce49.png)

## 3. Event Queue

- 자바스크립트 런타임 환경의 이벤트 큐는 처리할 메세지 목록과 실행할 콜백 함수들의 리스트이다. 버튼 클릭 같은 이벤트나 DOM 이벤트, http 요청, setTimeout 같은 비동기 함수는 Web API를 호출하며 Web API는 콜백함수를 콜백 큐에 밀어 넣는다.
- 이벤트 큐는 대기하다가 스택이 비는 시점에 이벤트 루프를 돌려 해당 콜백 함수를 스택에 넣는다. 이벤트 루프의 기본 역할은 큐와 스택 두 부분을 지켜보고 있다가 스택이 비는 시점에 콜백을 실행시켜주는 것이다.
- 웹 브라우저에서는 이벤트가 발생할 때마다 메세지가 추가되고 이벤트 리스너가 첨부된다. 콜백함수의 호출은 호출 스택의 초기프레임으로 사용되며 자바스크립트가 싱글 스레드이므로 스택에 대한 모든 호출이 반환될 때까지 메세지 폴링 및 처리가 중지된다. 동기식 함수 호출은 이와 반대로 새 호출 프레임을 스택에 추가한다.

[https://joshua1988.github.io/web-development/translation/javascript/how-js-works-inside-engine/](https://joshua1988.github.io/web-development/translation/javascript/how-js-works-inside-engine/)
[https://velog.io/@namezin/javascript-%EB%8F%99%EC%9E%91-%EC%9B%90%EB%A6%AC](https://velog.io/@namezin/javascript-%EB%8F%99%EC%9E%91-%EC%9B%90%EB%A6%AC)
