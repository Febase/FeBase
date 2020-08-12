---
title: V8 엔진
category: Javascript
date: 2020-07-07 00:00:00
author: dayoung
---

- V8이란 무엇인지 설명할 수 있다
- V8이 하는 주요한 일에 대해 설명할 수 있다
- V8의 주요 컴포넌트에 대해 설명할 수 있다

### V8 엔진이란

구글이 만든 오픈 소스 자바스크립트﹒웹어셈블리 엔진으로, 자바스크립트 코드를 실행 전에 최적화된 머신 코드로 컴파일하는 엔진이다. (_즉, V8은 자바스크립트 코드를 받아 컴파일하고 실행하는 C++ 프로그램이다._) 크롬 브라우저와 노드 js에서 사용된다.

### 왜 머신 코드로 컴파일해야 할까?

V8 엔진이 어떻게 동작하는지 알아보기 전에, 애초에 왜 머신 코드로 컴파일하는지 간략히 짚고 넘어가자. 우리가 사용하는 컴퓨터 안에는 마이크로프로세서라는 작은 기계가 있는데, 이것은 CPU의 핵심 기능을 통합한 집적 회로(IC)다. 프로그래머가 어떤 코드를 짜서 컴퓨터에게 일을 시키려면 결국 이 마이크로프로세서가 해석할 수 있는 언어로 전달해야 한다. 마이크로프로세서는 이것을 만든 회사나 버전에 따라 각자 다른 언어를 사용하는데, 가장 많이 쓰이는 것들은 IA-32, x86-64, MIPS, ARM 등이다. 이 언어들은 하드웨어와 직접적으로 소통할 수 있는 코드들이고 그래서 기계어, 머신 코드라 불린다. 그러니까 결국 프로그래머들은 프로그래밍 효율을 위해 추상화 수준이 높은 high level 언어를 사용해서 코딩을 하지만 이는 결국 머신 코드로 컴파일되어야만 CPU가 이해하고 처리를 할 수 있다는 말이다.

### V8 엔진의 특징

- C++로 쓰여졌고 크롬과 Nodejs에서 쓰인다.
- ECMAScript를 따른다. (ECMA-262)
- V8 엔진은 혼자 동작할 수 있고 프로그래머가 C++ 프로그램을 만들어서 돌릴 수도 있다. 예를 들어 원래 Node.js에서 print 함수는 유효하지 않지만, C++의 print 함수를 V8 엔진 위에 얹으면 노드에서 print 함수를 native하게 돌아가게 할 수 있다. C++은 자바스크립트에 비해 하드드라이브의 파일이나 폴더를 다루는 기능이 뛰어난데, 이런 기능들을 V8 엔진을 이용하면 자바스크립트에 심을 수도 있다는 것이다.

### V8이 하는 일

- 자바스크립트 코드를 컴파일하고 실행한다
- 콜스택을 핸들링해서 자바스크립트 함수를 특정 순서에 따라 실행한다
- 메모리 힙에 객체들의 메모리 할당을 관리한다
- 더 이상 쓰이지 않는 객체들을 가비지 콜렉팅한다
- 모든 데이터 타입, 연산자, 객체, 함수를 제공한다
- 이벤트 루프를 제공한다(가끔 브라우저에 의해 제공되기도 한다)

![](https://hackernoon.com/hn-images/1*QG6GNe2ag-4puxpjc5Y2iw.png)

### Key Components - Ignition & TurboFan

5.9v 이전까지 쓰이던 컴파일러인 `Crankshaft`와 `Full-codegen`은 이제 더 이상 쓰이지 않고, `Ignition`이라는 js 인터프리터와 `TurboFan`이라는 컴파일러로 대체되었다. (https://v8.dev/blog/launching-ignition-and-turbofan) 이전까지는 JIT(`Just-in-time`) 컴파일레이션 과정을 거칠 때 아래의 과정을 거쳤었다.

1. 코드 실행 전에 Full-codegen(`baseline compiler`)이 자바스크립트 코드를 빠르게 non-optimized 머신 코드로 컴파일
2. 한 번 컴파일된 코드를 런타임 동안 분석하여 Crankshaft가 optimized 머신 코드로 재컴파일

이 과정의 문제점은 코드가 한 번만 실행되더라도 JIT로 컴파일된 머신 코드가 메모리를 많이 소비한다는 점이다. Full-codegen이 생성하는 코드는 크롬에서 자바스크립트 힙의 거의 삼분의 일을 차지했기 때문에 어플리케이션 데이터를 위한 공간이 적었다. 이 오버헤드를 줄이기 위해 Ignition이라는 인터프리터가 나왔고, 이제는 1번 과정에서 베이스라인 컴파일러가 하는 일을 대체한다.

Ignition은 자바스크립트 코드를 바이트 코드로 컴파일하는데, 이 코드의 사이즈는 베이스라인 머신 코드 크기의 25%~50% 정도이다. 또한 Full-codegen이 베이스라인 코드를 생성하는 데 걸리는 시간보다 바이트코드를 생성하는 것이 더 빠르기 때문에 일반적으로 Ignition은 웹페이지가 로드되는 시간을 줄인다.

이제는 1번을 Ignition이 대체하여 바이트코드를 생성하고, 2번을 TurboFan이 대체하여 최적화 컴파일하는 과정을 거친다.

TurboFan이 Crankshaft를 대체한 이유는 Crankshaft가 자바스크립트의 일부만 최적화 했고(예를 들어 try catch 에러 핸들링 구문을 최적화하도록 디자인되지 않았다) 새로운 자바스크립트 피처를 최적화하기에 한계가 있었기 때문이다. 반면 TurboFan은 ES5뿐만 아니라 ES6 이상을 다룰 수 있도록 설계되었다.

## Self-check

- V8이란 무엇인가 / V8이 하는 주요한 일은 무엇인가 / V8의 키 컴포넌트는 무엇인가

## Ref

https://www.freecodecamp.org/news/understanding-the-core-of-nodejs-the-powerful-chrome-v8-engine-79e7eb8af964/

https://hackernoon.com/javascript-v8-engine-explained-3f940148d4ef

https://v8.dev/blog/launching-ignition-and-turbofan

https://v8.dev/blog/ignition-interpreter
