---
title: Javascript 스코프
date: 2020-07-02 00:00:00
author: jinsunee
category: Javascript
---

# Lexical Scope + TDZ

## 스코프?

특정 장소에 변수를 저장하고 나중에 그 변수를 찾는 데는 잘 정의된 규칙이 필요하다. 이런 규칙을 `스코프`라고 한다.

## 자바스크립트 컴파일레이션

자바스크립트에서 소스코드가 실행되기 전에 보통 3단계를 거치는데, 이를 컴파일레이션이라고 한다.

- 토크나이징(tokenizing) /렉싱(lexing)
- 토크나이징: 문자열을 나우어 토큰이라는 조각으로 만드는 과정
  var num = 3
  `var num = 5 ;`
- 렉싱: 토큰 처리과정에서 토큰을 분석하여 생성된 토큰에 의미를 부여하는 것 (이 과정을 `렉스 타임`이라고 한다.)

* 파싱 (parsing)

* 코드 생성 (code-generation)

## 스코프 체인

위로 꼬리를 물고 계속 범위를 넓히면서 찾는 관계를 스코프 체인이라고 부릅니다.

즉, 내부함수에서는 외부 함수의 변수에 접근 가능하지만 외부함수에서는 내부 함수의 변수에 접근할 수 없다.

ex1)

```
var name = 'zero';

function outer() {
  console.log('외부', name);
  function inner() {
    var enemy = 'nero';
    console.log('내부', name);
  }

inner();
}

outer();

console.log(enemy); // undefined

```

## 렉시컬 스코프

함수를 처음 선언하는 순간, 함수 내부의 변수는 자기 스코프로부터 가장 가까운 곳(상위 범위에서)에 있는 변수를 계속 참조하게 됩니다.

컴파일러가 행하는 1단계인 렉싱단계에서 토큰이 분석되어 스코프를 결정됩니다.

```

var name = 'zero'; // a
function log() {
  console.log(name);
}

function wrapper() {
  name = 'nero'; // b
  log();
}

wrapper();

// nero
```

: 함수 log가 선언될 때의 name의 참조는 전역변수인 a이다. 이 주소 값을 담고 있기 때문에 nero가 출력.

```
var name = 'zero'; // a
function log() {
  console.log(name);
}

function wrapper() {
  var name = 'nero'; // b
  log();
}

wrapper();
// zero

```

: nero가 나올 것 같지만 log가 선언될 때(실행 아님) 상위에 있는 변수에 들어있는 참조 값은 zero 를 담고있는 a 이기 떄문에 zero가 출력된다.

컴파일레이션의 렉싱 단계에서 모든 변수들이 어디서 어떻게 선언되었는바탕으로 실행 단계에서 스코프를 구성합니다.

요약

1. function 안에 있는 변수는 function 바깥으로 빠져갈 수 있다. o x

2. 변수값을 판단하는 기준은 scope chain에 따라서 위로 물고 물면서 올라가서 값을 지정하지않는다. o x

3. 렉시컬 스코프에 의해서 변수든 함수든 선언되는 순간 스코프가 정해진다. o x
