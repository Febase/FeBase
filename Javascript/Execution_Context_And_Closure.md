---
title: 실행 컨텍스트와 클로저에 대해서
date: 2020-07-02 00:00:00
author: nailerHeum
category: Javascript
---

# 실행 컨텍스트와 클로저에 대해서

## Scope는 변수가 참조될 수 있는 범위이다

---

 스코프는 변수가 참조될 수 있는 범위를 의미한다. 변수는 스코프 외부에서 존재할 수 없고, 만약 스코프가 어떤 함수라면, 함수를 호출할 때마다 변수가 나타나고, 함수가 제어권을 반환하면 스코프에서 사라진다.

 스코프는 프로그램의 **현재 실행 중인 부분(실행 컨텍스트)** 에 현재 보이고 접근할 수 있는 식별자들을 말한다. 식별자가 '존재'한다는 말과 식별자에 '접근 가능'하다는 말은 다르다. '존재'한다는 말은 식별자가 메모리에 할당된 무언가를 가리키고 있다는 뜻이고, '접근 가능'하다는 말은 스코프 내에 식별자가 있다는 뜻이다.

```javascript
const plusOne = (x) => {
  return x + 1;
}

f(1, 2);

console.log(x); // error
```

`x`는 `plusOne` 이라는 함수가 실행될 때, 스코프에 있고, 함수가 종료됨과 동시에 스코프 밖으로 나가게 된다. 따라서 `console.log(x)` 는 에러가 발생하지만 주기적으로 수행되는 가비지 콜렉션을 통해 `x` 의 메모리를 회수하지 않는 이상 존재하고 있다고 볼 수 있다.



## 자바스크립트는 정적 스코핑 언어이다

---

정적 스코프(Static scope or Lexical scope)는 변수가 함수 스코프 안에 있는지를 함수가 정의되는 시점에 알 수 있다는 뜻이다.

```javascript
const x = "Hello scope";

function printThings() {
  console.log(x);
  console.log(y);
}

{
  const y = "This is my scope."
  printThings() // error
}

```

`x` 는 `printThings` 를 정의할 때 존재하지만, `y` 는 다른 스코프에 존재한다. 따라서 y를 선언하고 `printThings` 를 호출해도 `y` 는 스코프 안에 존재하지 않는다. 함수는 자신이 정의되는 시점에 접근할 수 있던 식별자에게는 접근이 가능하지만, 자신이 호출될 때 스코프에 있는 식별자에게는 접근할 수 없다. 



- 그럼 동적 스코프는 뭘까?

  호출 시점에서 스코프가 결정되는 것을 의미한다. 대부분의 언어가 정적 스코핑 언어이고, 동적 스코핑 언어는 Common Lisp, Emacs Lisp, Clojure, Perl 등이 있다고 한다.

  ```perl
  use feature qw(say);
  
  sub add {
      $x += shift;
  }
  
  sub funcfunc {
      local $x = 5;
      say add(10);
  }
  
  funcfunc();
  ```

  funcfunc에서 add를 호출할 때 스코프가 정해지기 때문에 $x를 정상적으로 사용할 수 있다.







## 스코프는 계층적이다

---

 프로그램을 시작할 때 주어지는 스코프가 **전역 스코프** 다. 전역 스코프에서 선언되면 전역 변수라고 한다. 어디서나 접근이 가능한 전역 변수는 매력적일 수 있으나, 코드량이 많아질 수록 모든 스코프를 기억하기 어려워지기 때문에 전역 스코프에 의존하지 않는 것이 좋다.

 `let` 과 `const` 는 식별자를 **블록 스코프** 에서 선언한다. **블록** 은 중괄호로 묶는 것을 의미하고, 따라서 블록 스코프는 그 블록의 스코프에서만 보이는 식별자를 의미한다.





## 클로저를 통해 특정 스코프에 접근할 수 있다

---

 자바스크립트에서는 함수가 필요한 곳에 즉석으로 정의하는 경우가 많다. 함수를 변수나 객체 프로퍼티에 할당하거나, 다른 함수에 전달하거나, 함수를 반환하는 경우에 즉석으로 함수를 정의할 수 있다. 이러한 경우 그 함수는 특정 스코프에 접근할 수 있게 된다.

```javascript
function useClosure() {
  let x = 1;
  return function() {
    return x;
  }
}

const closure = useClosure();
closure(); // 1
```

 위 예시코드에서 `useClosure`가 반환하는 함수는 x를 기억하고 있다. 일반적인 경우 스코프에서 빠져나가면 해당 스코프에서 선언된 변수는 메모리에서 제거되지만, `useClosure` 에서 반환하는 함수는 밖에서도 참조할 수 있기 때문에 자바스크립트에서 스코프를 계속 유지해준다. 따라서 클로저를 통해 접근할 수 없던 다른 스코프에 있는 것들에 접근할 수 있게 해준다고 볼 수 있다.



## Execution Context는 분리된 실행환경이다

---

 **실행 컨텍스트(execution context)**는 분리된 실행환경이다. execution context stack에 의해 execution context들을 추적한다. 항상 스택 최상단의 context가 현재 실행중인 context이다.

![](https://www.dropbox.com/s/adjungijaggrrfz/context_stack.png?raw=1)

실행중인 컨텍스트가 새로운 컨텍스트를 만들어주며 제어권을 넘기게 되는데 새로운 컨텍스트는 stack에 들어가며 실행 중인 컨텍스트가 된다. 

모든 실행 컨텍스트가 갖게 되는 요소들

- code evaluation state
  현재 실행 컨텍스트와 관련된 모든 코드 평가 상태들

- Function
  만약 실행 컨텍스트가 function object에 관한 코드를 평가중이라면, function object가 담기게 된다. 하지만 컨텍스트가 script나 module에 관한 코드를 평가한다면 이 값은 `null` 이 된다.

- Realm

  Realm Record(전역 리소스들을 의미한다.)

- ScriptOrModule

  Module Record(import 또는 export되는 module 관련 정보) 
  Script Record(평가되는 sciprt 관련 정보)

추가적으로 갖게 되는 요소들

- LexicalEnvironment
  중첩된 실행 환경들이다. 상위 환경들에 대한 참조들을 포함한다.

- VariableEnvironment

  현재 실행 컨텍스트에 바인드되는 lexical environment들에 대한 local memory다.

 자바스크립트는 코드를 통해 변경이 가능한 빌트인된 함수들과 객체들을 제공하기 때문에 execution context가 필요하다.  예를 들면 사용자는 코드를 작성해서 Array에 대해 새로운 함수를 추가하거나 기존 함수를 변조시킬 수 있다. 만약 이러한 전역 객체에 대한 변조를 가하는 두개의 함수가 존재한다면 분리된 실행환경이 없을 경우 결과를 예측하기 어려워진다. CPU와 memory 관점에서 모든 빌트인 자원을 실행 컨텍스트를 새로 생성하는 것은 부담스러울 수 있지만, 이후 발생하는 컨텍스트들에 대해서는 부담이 적다. 최초에 생성되는 실행 컨텍스트는 빌트인 자원들을 생성하고 자바스크립트 코드를 분석해야 되는 반면에 이후 컨텍스트들은 빌트인 자원들만 생성해주면 되기 때문이다.

![](https://www.dropbox.com/s/dsvh4esg3ctt2ng/intro-contexts.png?raw=1)





## 요점 정리

---

- 스코프는 현재 참조할 수 있는 변수들을 의미한다. 
- 자바스크립트의 스코프는 정적이고 계층적인 구조이다.
- 클로저를 통해 특정 스코프를 외부에서 접근하도록 할 수 있다.
- 실행컨텍스트는 말 그대로 현재 실행환경 전반적인 모든 자원들을 보유한 객체이다. 
- 따라서 실행컨텍스트에 스코프가 속한다고 볼 수 있다.
- Stack을 통해 실행 컨텍스트와 실행중인 컨텍스트를 결정한다.



ECMA spec이나 v8 문서를 참고하는데 있어서 어려움이 많았다. 

자바스크립트를 사용하는 데 있어서 블랙박스가 존재하지 않았으면 한다는 생각을 해서 깊이 있게 조사하려 노력했다.

좀 더 노력이 필요할 것 같다...



### Reference

----

- [러닝 자바스크립트 7장 스코프](https://www.hanbit.co.kr/store/books/look.php?p_code=B2328850940)
- [Dynamic scoping](https://blog.hongminhee.org/2012/05/07/dynamic-scoping/)
- [실행 컨텍스트 동작원리](https://v8.dev/docs/embed)
- [ecma 2020 spec](http://www.ecma-international.org/publications/standards/Ecma-262.htm)
- [lexical vs variable](https://medium.com/@bdov_/javascript-typescript-execution-vs-lexical-vs-variable-environment-37ff3f264831)

