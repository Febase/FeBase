---
title: 따라쟁이 셋째 JS가 지키고 싶었던 것 - Prototype
date: 2020-06-19 00:00:00
author: samslow
category: Javascript
---

- 이 글은 JS Prototype Chaining을 설명하기위해 Prototype Object, Prototype Link을 설명합니다.

# 자바스크립트의 태생

JS는 class 기반의 객체지향 언어로 대부분 알고있다. 사용하기에 따라서 React, Vue 같은 곳에서는 함수형 프로그래밍을 흉내 낼 수도 있다. 하지만, JS는 ES6에서 생긴 개념인 class가 직접 존재하는 게 아니다. Prototype을 통해 생성되고 여기서 생성 자체는 또 함수를 사용(?)하기 때문에 `객체 → 프로토타입 → 함수 → 객체`로 이상한 Cycle이 형성되어버린다고 생각이 들 수도 있다. 그래서 JS를 객체지향 언어, 함수형 언어, 프로토 타입 언어 등의 다양한 이름으로 불리는데, 결국 MDN에서는 JS를 `세계에서 가장 오해받고있는 프로그래밍 언어`로 정의하기도 했다.

JS 자체가 처음 출시된 날짜는 1995년 12월 4일이니 그래도 언어들 사이에선 셋째 형 정도의 레벨을 갖고 있는데, 그러다보니 넷스케이프에서 처음 출시될 때는 둘째 형인 Java처럼 되고싶다며 구문이 첫째형인 C언어와 같다는 것만 빼고 완전 다른 셋째 JavaScript가 나오게 되었다.

이런 이유들로 JS를 정의하자면 `다중 패러다임, 동적 언어` 이라고 할 수 있다. (너무 뭉뚱그린다고 할 수 있지만 보는 사람마다 시야가 다른것을 ㅜㅜ)

# 따라쟁이 셋째 JS가 지키고 싶었던 것 - Prototype

객체 지향 언어로 명시된 Java, Python, Ruby 에서 Class가 빠질 수 없는 개념 인 것처럼 JS에서도 Prototype을 알면 JS의 그 자체를 이해하는 것이라고 봐도 무방하다.

Java와 다르다는 것은 명백하지만 비슷한 부분은 있고, 그것이 Java의 class가 아니라는것을 구분하기 위해 Prototype이라는 개념이 나온 것이다.

ES6에서 class의 개념이 나온 것은 맞지만 오해하지 말야아 할 것은, prototype이 class로 변화된 것은 아니고, 원래도 js는 class의 기능을 묘사하기 위해 prototype로 상속같은 것을 구현 할 수 있었고 이를 문법적으로 쉽게 만들어 사용 할 수 있게 한 것이 ES6의 class이다.

따라서 class가 생겼다고 prototype의 개념이 중요해지지 않는 것이 아니고, 오히려 보이지 않아졌기 때문에 그것을 알기가 어려워져서 더 알아야 하는 개념이 된 것이다.

그럼 Prototype의 개념은 여기까지 하고 Prototype Chaining은 무엇일까?

이것을 설명하기 위해선 `Prototype Object`와 `Prototype Link`를 알고 넘어가야 한다.

# Prototype Object

JS에서 객체가 생성되면 언제나 함수로써 생성이 된다.

```jsx
function person() {} // 함수 선언

const personObject = new person(); // 함수로 객체 인스턴스 생성
```

그리고 우리가 편하게 쓰고있는 객체나 함수, 배열 생성도 예외는 아니다.

겉으로 보기에는 Primitive type으로 선언 된 것 처럼 보이지만, 별칭처럼 사용 할 수 있게 된 것 뿐이지 실제 동작은 모두 Object 함수 호출로써 객체가 만들어지고 있다.

```jsx
const obj = {};
// const obj = new Object();

const arr = [];
// const arr = new Array();
```

이렇게 생성된 객체는 해당 객체의 Prototype Object 생성과 함께 연결되게 된다.

![https://www.dropbox.com/s/ueiuxqgnyijcwjp/스크린샷 2020-06-09 07.41.22.png?raw=1](https://www.dropbox.com/s/ueiuxqgnyijcwjp/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202020-06-09%2007.41.22.png?raw=1)

by https://medium.com/@bluesh55 이하 동일

쉽게 말해서 객체 생성을 부모를 만들어주고(Prototype Object) 그 관계를 연결(Prototype)해 주는 것이다.

생성된 Prototype Object는 `constructor`와 `__proto__` 를 갖게 된다.

`constructor`는 Prototype Object로 인스턴스 생성시 `new`로 객체 생성을 할 수 있게 해 주고,

`__proto__` 는 인스턴스 생성시 Prototype Object와의 연결 관계를 만들어 준다.

```jsx
function Person() {} // 객체 생성 및 Product Object 연결

Person.prototype.eyes = 2; // 객체의 prototype 조작
Person.prototype.nose = 1;

var kim  = new Person(); // constructor 예약어로 만든 인스턴스
var park = new Person():

console.log(kim.eyes); // 2
```

# Prototype Link

이 부분은 위에서 Prototype Object 의 부산물의 핵심이자 Prototype Chaining을 만들어주는 `__proto__` 의 설명이다.

Prototype은 class와 비교하면 쉬운데, **class에서 생성된 변수나 함수들을 `상속` 해서 쓸 수 있게 하는 것 처럼 JS의 Prototype도 상속을 `__proto__` 로 구현 한 것이다.**

![](https://www.dropbox.com/s/eqtgc18dd1mlgo0/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202020-06-09%2008.46.44.png?raw=1)

Prototype 속성은 함수만 갖지만 `__proto__` 는 모든 객체가 갖고있다.

따라서 인스턴스 수준에서는 인스턴스의 Prototype Object의 변수를 가져다 쓰는것이 가능해지고, 만약 여기에도 존재하지 않는다면 Object Prototype Object까지 거슬러 올라가서 확인하고 값이 없다면 `undefined`를 리턴하는 구조이다.

그래서 모든 객체는 Object의 손자이자 모든 객체는 Object가 최초의 인간 아담과 하와인 것이다.

이런 다양한 Prototype 특징을 생각하면 String이나 Array로 생성된 인스턴스들의 prototype에 우리가 흔히 쓰는 toString, concat ··· 을 찾아 볼 수 있다.

![](https://www.dropbox.com/s/wrhei21s1421tbl/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202020-06-09%2008.44.40.png?raw=1)

![](https://www.dropbox.com/s/0sv8w7kgww12x26/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202020-06-09%2008.44.13.png?raw=1)

**이렇게 `__proto__` 를 통해 상위 프로토타입들과의 연결성이 Chain처럼 연결되어있어서 이를 `Prototype Chaining`이라고 한다.**

# 정리

- JS는 다중 패러다임, 동적 언어이기 때문에 보는 시각에 따라 다른 다형성을 갖는다.

- JS는 OOP(Object Oriented Programing)의 class를 묘사하기 위해 prototype의 개념이 생겼다.
- Prototype이 생성되면 Prototype Object 와 Prototype Link가 함께 따라간다.

Prototype은 js이전에도 일상에서 종종 들어 볼 수 있는 말이니 쉽게 생각 하면 객체 생성시 그 객체에 대한 금형을 만드는 것을 prototype이라고 이해하고 이를 기반으로 인스턴스를 찍어내는 개념이라고 쉬울 것 같다.

JS의 Prototype에 대한 공부를 다소 미뤄왔는데 대충만 알고있었지 Prototype 이 생성되며 Prototype Object나 Prototype Link가 생성되는 부분까지 디테일하게 알지는 못해서 개념을 정립하고 나니 JS와 조금 더 친해진 것 같다는 생각이 든다.(나만 그러니.. 우리 친해지자 자스)

# Reference

- [sik2.log](https://velog.io/@sik2/JS-CoreJavaScript-프로토타입-체이닝Prototype-Link-Prototype-Object)
- [javascript 프로토타입 이해하기](https://medium.com/@bluesh55/javascript-prototype-이해하기-f8e67c286b67)
