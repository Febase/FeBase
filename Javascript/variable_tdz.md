---
title: Javascript var, let/const and Temporary Dead Zone
date: 2020-07-08 00:00:00
author: jinsunee
category: Javascript
---

# var, let/const and TDZ(Temporary Dead Zone)

TDZ라는 개념을 알기 앞서 먼저 알아야할 개념은 호이스팅(Hoisting)과 var, let/const의 선언 단계입니다.

## 변수가 생성되는 과정

Javascript 인터프리터 내부에서 변수를 생성하는 과정은 다음과 같이 3단계를 거칩니다.

1. `선언` (Declaration)
   스코프와 변수 객체가 생성, 스코프가 변수 객체 참조

2. `초기화` (Initialization)
   변수 객체가 가질 값을 위해 메모리 공간을 할당

3. `할당` (Assignment)
   변수 객체에 값을 할당

## 호이스팅

```
console.log(white); // undefined
var white = '흰색';
```

위와 같은 코드의 결과는 눈으로 봐서 변수 선언 전인데 어떻게 값을 인식하는 것처럼 보이지? 라고 의구심과 함께 혼란을 야기할 것입니다.

변수가 생성되는 과정에서는 선언이 먼저 일어나는데 이 때문에 값이 할당되기 전에 이미 변수로 인식을 하고 있게 됩니다.
var의 경우 `undefined` 가 뜨고, let/const의 경우는 `아직 초기화 하지 않았습니다!` 라는 에러가 뜨지만 어쨌든 변수 목록에 있다고 해줌으로서 변수 목록에 이름이 있어!라고 말해줍니다.

간단히 요약하자면 호이스팅은 변수명 먼저 알고 있고 그 이후 코드를 보겠다라는 개념.

## var과 let/const 는 변수 생성 과정이 살짝 다르다!

### var

- 선언이 일어나는 동시에 초기화가 일어납니다.
- 이때, `undefined`라는 값을 선언함으로써, 아직 할당되지 않은 상태라고 표시해줍니다.
- 그리고 할당이 일어납니다.

Javascript 엔진인 V8의 코드내부에서도 이부분을 알 수 있습니다.
`DeclareParameter` 선언을 하고, `AllocateTo`를 통해 공간을 바로 할당하여 초기화(`undefined`를 할당)하죠!

```
// v8/src/parsing/parser.cc
// Var 모드로 변수 선언 시
auto var = scope->DeclareParameter(
  name,
  VariableMode::kVar,
  is_optional,
  is_rest,
  ast_value_factory(),
  beg_pos
);

var->AllocateTo(VariableLocation::PARAMETER, 0);
```

![image](https://user-images.githubusercontent.com/31176502/85691230-46e49780-b70f-11ea-8bfb-6c108f0f1f8c.png)

### let/const

- 선언과 메모리 할당이 동시에 일어나지 않습니다. 즉, 선언이 먼저 일어나죠.

아래 V8 내부 코드를 봐도 `AllocateTo`로 메모리 할당을 먼저 하지 않고 선언만 합니다.

```
// v8/src/parsing/parser.cc
// kLet 모드로 변수 선언 시
VariableProxy* proxy = DeclareBoundVariable(
                          variable_name,
                          VariableMode::kLet,
                          class_token_pos
                        );
proxy->var()->set_initializer_position(end_pos);

// Const 모드로 변수 선언 시
VariableProxy* proxy = DeclareBoundVariable(
                          local_name,
                          VariableMode::kConst,
                          pos
                        );
proxy->var()->set_initializer_position(position());
```

![image](https://user-images.githubusercontent.com/31176502/85708834-9337d380-b71f-11ea-9752-831f31f6854e.png)

이 과정에 있는 변수들은 선언은 되었지만 아직 초기화되지 않은 상태이며, Temporal Dead Zone에 들어있다고 합니다.

즉, TDZ 구간에 들어있는 객체는

> 선언은 되어있지만 아직 초기화가 되지않아 변수에 담길 값을 위한 공간이 메모리에 할당되지 않은 상태

라고 할 수 있으며, 변수 접근 시도시 아래와 같은 에러를 발생시킬 것 입니다.

![image](https://user-images.githubusercontent.com/31176502/86900753-b1052f80-c146-11ea-8a67-0a39ad22a287.png)

![image](https://user-images.githubusercontent.com/31176502/86900738-ac407b80-c146-11ea-82b3-505c0972aaac.png)

## 그렇다면 TDZ에서 언제 빠져나와요?

값을 할당해줘서 초기화 시키면 빠져나옵니다!

```
let letValue = 'out';
function hoistedLet() {
  // letValue가 TDZ에 영향을 받는 순간
  console.log('letValue', letValue); // ReferenceError
  let letValue = 'inner scope'; // letValue가 초기화 됨으로써, TDZ가 끝나게 됩니다.
};
hoistedLet()
```

## 결론

TDZ는 let/const로 선언된 변수가 선언만 되고 아직 할당되지 않은 상태의 구간입니다.

https://evan-moon.github.io/2019/06/18/javascript-let-const/
https://velog.io/@wrfg12/ES6-Hoisting-Temporal-Dead-ZoneTDZ
