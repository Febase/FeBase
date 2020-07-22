---
title: "Javascript 기초 - JavaScript 개발한다면 JIT은 알아야JIT"
category: Javascript
date: 2020-06-25 00:00:00
author: samslow
---

- Javascript Engine 최적화 기법 중 하나인 JIT(Just-In-Time)을 설명 합니다.
  - VM의 장점 2가지를 설명 할 수 있습니다.
  - JIT의 장점을 설명 할 수 있습니다.
  - JIT의 동작 방식을 설명 할 수 있습니다.

# VM의 산소같은 너, JIT

JIT을 알기 전에 JIT은 생소 할 수 있어도, JVM이나 운영체제의 VM은 들어 본 사람이 있을 것이다.

VM은 Virtual Machine의 준말로 가상 머신을 의미한다. 즉 컴퓨터에 들어있는 CPU, Storage, Memory 는 한 세트지만, 이것을 기반으로 새로운 컴퓨터를 여러개를 띄우는 것을 말한다.

Docker는 `컨테이너`지만 그 뿌리로 보았을때 VM과 비슷하고, AWS Lambda 도 사용하고 있다고 볼 수 있는 것이다. 컨테이너와 VM의 차이를 알고싶다면 [여기](<[https://food4ithought.com/2019/10/26/%EA%B0%80%EC%83%81%EB%A8%B8%EC%8B%A0virtual-machine-vs-%EC%BB%A8%ED%85%8C%EC%9D%B4%EB%84%88container/](https://food4ithought.com/2019/10/26/가상머신virtual-machine-vs-컨테이너container/)>)를 참고하시라

![초보를 위한 도커 안내서 - 도커란 무엇인가?](https://subicura.com/assets/article_images/2017-01-19-docker-guide-for-beginners-1/docker-logo.png)

![](https://www.dropbox.com/s/yfib3t6jipe8rvt/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202020-07-06%2014.45.38.png?dl=1)

가상 환경의 장점은 아래와 같다.

1. 하나의 장치를 여러 개처럼 동작시키거나, 반대로 여러개의 장치를 하나처럼 만들 수 있다.
2. 분할된 가상 환경들이 서로 상호 간섭 없는 독립성을 보장 받을 수 있다.

즉 이런 가상환경이 있어서 macOS에서도 windows나 Linux를 돌릴 수 있는 것이고 이외에도 다양한 쓰임새가 있는 기술이다.

이런 VM기술이 가능하게 하는 것중 하나가 바로 JIT이다.

JIT은 JVM에서도 쓰이지만 Chrome 의 JS엔진인 V8에서도 사용되는 산소같은 존재이다.

# JIT금 부터 JIT을 배워보자

JITC(just-in-time compilation)은 동적 번역이라고도 불리우고, 이름에 맞게 프로그램을 실제 실행하는 시점에 바이트 코드를 기계어로 번역하는 컴파일 기법이다. 굳이 한글로 하자면 `그때그떄` 로 해석 할 수 있겠다.

![jit.png](https://image.toast.com/aaaadh/real/2016/techblog/jit%281%29.png)

<div align="center" style="color: gray">JITC 동작 방식-IR(Intermediate representation)</div>

JITC 외에도 컴파일 기법에는 실행 중에 읽어가면서 대응하는 **인터프리터 방식**과 실행 전에 컴파일하는 **정적 컴파일 방식**이 있다.

인터프리터 언어에는 스크립트 언어가 대부분인데, JS나 HTML, python, Ruby 등이 있고,

정적 컴파일 언어에는 자료형이 고정되어 있는 언어 즉 JAVA나 C같은 언어들이다.

언어가 인터프리터 방식이라고 JIT이 아닌것은 아닌데, 그 엔진이 구현하는 방식에 의존적이기 때문이다.

현대의 Safari, Chrome, FireFox의 JS엔진은 모두 JITC 방식을 사용한다.

JIT은 하나씩 읽어가며 실행하는 인터프리터보다는 당연히 빠르고, 미리 컴파일하는 정적 컴파일보다는 성능이 떨어진다.

JITC는 컴파일 과정이 한번에(just in time) 일어나긴 하지만 기계어로 변환한 것이 인터프리터의 수행시간보다 낫기 때문에 더 빠를 수 있는 것이다.

# 그럼 JS는 무조건 JITC 쓰는게 🐶이득이네

![](https://jjalbot.com/media/2018/12/Q0ntedUTY/zzal.gif)

라고 말한다면 ~~경기도~~ 큰 오산이다.

JITC을 사용함으로써 얻는 장점은

1. 정적 컴파일처럼 미리 바이트 코드로 컴파일을 하지않고 실행 시간에 이를 결정하는 장점
2. 정적 컴파일 처럼 최적화를 일부 적용할 수 있는 장점

하지만 최적화라는것이 무엇인가, 내가 생각하는 흐름대로 오버헤드가 발생할 때 적용하면 효과가 극대화 되는 것이다.

JS는 [이전 포스트](https://samslow.github.io/development/2020/06/09/Javascript_Basic_Prototype-Chaining/)에서 보다시피 `동적 언어` 이기 때문에 `let`, `const`, `var` 에 저장된 타입이 실행 시점에서 결정되고, 한번 결정되었다고해서 변수의 타입이 바뀌지 않을 것이라는 보장도 없다.

이런 JS의 특성 때문에 에러처리나 예외 케이스를 고려하면 기계어로 변환했을때에 그 양이 매우 많아진다.

많은 분들이 아는 JS 매직(?)은 아래와 같다.

```js
"99" + 1; // "991"
"99" - 1; // 98 ?
"2" * "3" + "4"; // "64"
"2" * "3" + "4" * "5"; // 26
```

어떤가.. 타입이 예상할 수 없이 튀는 코드들을 제어하려면 기계어가 많아지는 것은 당연지사이다.

이렇게 되면 최적화를 활용하는 JITC의 장점이 퇴색되고, 인터프리터 방식과 성능 면에서 큰 차이가 안나게 된다.

또한, JS는 Web에서 layout을 주로 건드리기 때문에 for-loop이나 알고리즘이 들어가는 어떤 로직을 잘 사용하지 않기로 알려져있기 때문에 자주 반복되어서 실행되는 부분이 적다.(물론 현대의 Frontend는 Backend의 로직을 점점 가져오고 있긴 하지만, 여기선 고전적인 JS라고 생각한다.)

자주 반복되는 부분이 적으면 최적화를 적용해서 기껏 만들어 놔 봤자, 그것을 활용하지 않기 때문에 결과적으로 JITC으로 한번에 기계어까지 번역하는 것이 효용이 적기 때문에 인터프리터 방식으로 실행하는 것이 낫다.

# 아.. 그니까 그럼 결국 인터프리터쓰라는 거죠?

라고 생각하면 경기도 오···(ㅈㅅ)

이런 갭을 극복하기 위해서 최근의 JS엔진들은 JIT의 업그레이드 버전인 Adaptive JITC를 사용한다.

AJITC는 모든 코드를 일괄적으로 같은 최적화를 적용하지 않고, 반복 수행 정도에 따라 유동적으로(adaptive) 서로 다른 최적화 수준을 적용하는 방식이다.

모든 코드는 인터프리터로 수행하다 자주 반복된다 싶으면 그 부분만 JITC를 적용한다는 것이다.

Chrome V8에서는 crankshaft라는 Adaptive JITC을 아래와 같이 동작하게한다.

![crankshaft.png](https://image.toast.com/aaaadh/real/2016/techblog/crankshaft.png)

여기서 핵심은 RuntimeProfiler가 존재해서 함수 호출의 빈도를 측정해 JITC으로 할지 인터프리터로 할지 결정한다는 것이다.

단, 이 경우에도 최적화의 한 방식이기 때문에 타입이 변하는 경우는 역시 비효율을 발생 시킬 수 있다.

대부분의 개발자가 평소에 JS로 개발할 때 한가지 변수에 대해 여러 타입을 할당하는 경우는 적지만,

이것을 알고 안 쓰는 것과 모르고 안 쓰는 것은 다르다.

# Self Check

1. VM(Virtual machine)의 장점 2가지를 설명하시오.
2. 컴파일 방식의 대표적인 3종류와 성능 순서를 설명하시오.
3. 고전 JIT에는 (JITC / 인터프리터) 가 (JITC / 인터프리터) 보다 효율이 좋다.
4. 최근 Frontend의 역할이 커짐에 따라 `_____` 방식이 효율적이다.
5. `______` 는 Adaptive JITC의 핵심으로, 함수 호출 빈도를 측정해준다.

# Closing

JIT은 들어는 보았지만, 어떤식으로 동작하는지는 몰랐었는데, 이번 기회로 더 디테일하게 볼 수 있었던 것 같다.

사실 최근 본 면접에서 물어봤을때 몰라서 공부하게 되었다. 면접은 최고의 교본이 되는 것 같다.

알고보면 어렵지 않은데(물론 깊이 파면 논문 파야한다) 그것을 안다는 것은 다른 문제이다.

다음에는 잘 대답 할 수 있겠지..?

이외에도 꿀팁은 배열에는 하나의 타입만 넣는것이 최적화 측면에서 유용하므로 기억하자.

# Reference

- [TOAST 기술 블로그](https://meetup.toast.com/posts/77)
