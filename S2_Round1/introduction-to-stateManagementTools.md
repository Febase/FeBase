---
title: JS 상태관리 도구 개론
date: 2020-11-19 19:00:00
author: wooooooood
category: S2_Round1
---

# JS 상태관리 도구 개론
## 상태관리의 필요성
- 상태(데이터)가 언제, 어디서, 왜, 어떻게 변화했는지 알기 어렵다.
- 다수의, 흩어진 Component가 같은 상태를 공유할 때 이를 관리하는 것이 복잡하다.
- Component 단위에서는 props를 통해 하위 component로 상태를 전달한다. Component가 증가한다면 비효율적인 작업이 생길 수 있다.
![](https://miro.medium.com/max/375/1*GF62GAlhWKkSRd4uksoIkA.jpeg)

=> 이를 개선하기 위해 상태관리 도구 Redux, MobX, Recoil(React) 등이 나타났다.  
=> 이 글에서는 FW에 구애받지 않는 JS 상태관리 도구인 Redux, MobX에 대해 간단하게 설명한다.

## Redux
> A Predictable State Container for JS Apps
- Functional Programming
- Subscribe하는 모든 Component가 접근 가능한 Centralized global store로 상태를 관리한다.
- `Immutability`를 유지하기 위해 원본 객체를 수정하는 것이 아닌, 객체의 복사본을 만들어 **복사된 객체**를 갱신한다.

ex.
```js
const arr = ['a', 'b']
const arrCopy = arr.concat('c')
```

### 단방향 데이터 흐름
![Redux](https://postfiles.pstatic.net/MjAyMDAzMDhfMTQ2/MDAxNTgzNjMzNTQwNjUy.PXwD1gycPobFP3-IS7eiwI71_nk-ODsRk8KGiQJoU9cg.tPkdDd6GPW_gp6Uwt0l6oqkimD9Sn2kQIPNx2w_9o-0g.PNG.wj8606/JYrQR.png?type=w773)
- **View**: 보여주기만 하는 순수 컴포넌트
- **Action**: `Type`을 가진 JS객체로, User input, Trigger 등의 `Event`라고 생각할 수 있다.
- **Reducer**: 현재 State와 Action을 감지하여 State를 갱신(바꿔치기)한다. `EventListener`와 유사하다.
- **Store**: 현재 Redux의 State, 읽기 전용
- **Middleware**: Action을 통해서 State를 바꾸기 전에 API호출 등 데이터가 변경되는 로직이 있을 때 비동기 작업 등을 처리할 수 있다.

### 단점
- 애플리케이션이 복잡해질수록 `redux-saga`, `redux-thunk`, `redux-pack` 등의 라이브러리를 추가로 알아보는 것에 대한 부담?

## MobX
> Simple, scalable state management
- Object-Oriented Programming and Reactive Programming

### 데이터 흐름
![MobX](https://mobx.js.org/assets/getting-started-assets/overview.png)
- **Application state**: Objects, arrays, primitives 등의 model이며 이러한 값들을 `data cell`이라고 한다.
- **Derivation**: Application에서 자동으로 계산되는 모든 값.
- **Reaction**:Derivation과 비슷하다. 차이점은, 값을 생성하지 않는 함수이며 Task를 수행하기 위해 자동으로 수행되며 주로 I/O 작업과 연관된다. (ex. DOM update, Network ..) 
- **Action**: State를 변경할 수 있는 모든 것을 의미하며 동기적으로 처리된다.

### 장점
- 쉬운 편이다!

### 단점
- 문서가 부실하다..
- 개발자 도구가 불편하다!
- 애플리케이션이 커질수록 복잡해진다 (Store가 여러개이기 떄문에)

## Reference
- [TECH CONCERT: FRONT END 2019 - 데이터 상태 관리. 그것을 알려주마](https://www.youtube.com/watch?v=o4meZ7MRd5o&feature=youtu.be)
- [Why and When to use Redux](https://blog.usejournal.com/why-and-when-to-use-redux-b57f7dae9269)
- [Redux overview](https://redux.js.org/tutorials/essentials/part-1-overview-concepts)
- [MobX overview](https://mobx.js.org/getting-started)
