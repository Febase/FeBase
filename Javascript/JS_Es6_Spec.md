Author: [@samslow](https://github.com/samslow)

- javascript는 ES6 이전과 이후로 달라진 내용을 하나씩 톺아보고 최신 표준에 대해 알아봅니다.
  - ECMAScript 에 대해 설명 할 수 있습니다.
  - ES6의 주요 특징 5가지를 이야기 할 수 있습니다.
  - ES11에 추가된 주요 특징을 이야기 할 수 있습니다.

# 그냥 ES11인가 뭐시깽이 쓰면 되는거 아님?

![es6 Logo](https://poiemaweb.com/img/es6.png)

우리가 흔히 쓰는 ES\*은 넷스케이프에서 Javascript의 표준화를 위해 그 표준을 [ECMAScript](<[https://ko.wikipedia.org/wiki/ECMA%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8](https://ko.wikipedia.org/wiki/ECMA스크립트)>) 로 정리 한 것입니다.

뒤에 붙는 숫자는 해당 표준의 Edition Number 이고 보통 연단위로 하나씩 나오기 때문에 2020년에는 ES11을 사용 할 수 있습니다.

하지만 최신 표준인 ES11 혹은 그 이상을 쓰지 않고 왜 JD나 개발자들 사이에서는 ES6를 이야기하는 것일까?

진부한 대답이지만, 이 시기의 표준으로 추가된 문법이나 개념이 많았고, 지금도 매우 중요하기 떄문이다.

새로 추가되는 표준에는 과거의 표준에 대한 설명이 있지 않기에 ES6는 그 중요성이 남다르기 때문에 더욱 강조되는 것이다.

ES6는 2015년 6월에 업데이트된 ECMAScript의 6th Edition 이다.

# 한눈에 보는 ES6 특징

아래 5가지 목록은 ES6에서 새롭게 지원하는 기능들이고, 주요 요소들만 뽑아놓고 정리할 것이다.

그리고 그 아래 4가지로 정리한 Bonus feature는 개인적으로 생각하기에 편의성이 향상된 부분들이라 알아두면 좋은 요소들을 정리했다.

1. Class 지원
2. let & const 문법 추가
3. Arrow Functions
4. Modules
5. Promises

### Bonus feature

1. 비구조화 할당 지원
2. 객체 리터럴
3. Template Literals
4. 매개변수 기본값

사실 여기에 소개된 기능들 외에도 Array, String class의 메서드 추가, loop 문법 추가 등이 있지만, 주요 변경사항은 아니기 때문에 (필요할 때마다 검색하면 바로 나오는 정도) 패스하고 작성했다.

아래에서는 이런 주요 기능 및 보너스 기능에 대해서 기본적인 내용 위주로만 설명한다.

# Class 전격 지원

사실 이 블로그를 정독 해 보신 분이라면 이전 글에서 이미 [ES6에서 Class문법이 추가 된 이유](https://samslow.github.io/development/2020/06/09/Javascript_Basic_Prototype-Chaining/)에 대해서 알 것이다.

요약하자면, 다른 언어에서 지원되는 Class에 발 맞추어 다중 패러다임을 지향하는 JS에서도 이를 똑같이 묘사하기 위해 Syntatic Sugar가 첨가된 기존 Prototype으로 지원되던 OOP의 기능을 Class로 래핑한 기능이다.

즉 Prototype은 그 개념자체가 배울 것도 많고, 오묘하게 Class와 다르기 때문에 혼란을 줄이기 위해 Class 가 ES6부터 지원되는 것이다.

아래 예제에서 ES5의 prototype에서 ES6의 class로의 변화를 볼 수 있다.

```js
////////////////////////////////////// ES5
var Person = (function () {
  // Constructor
  function Person(name) {
    this._name = name;
  }

  // public method
  Person.prototype.sayHi = function () {
    console.log("Hi! " + this._name);
  };

  // return constructor
  return Person;
})();

// 인스턴스 생성
var me = new Person("Lee");
me.sayHi(); // Hi! Lee.

console.log(me instanceof Person); // true

////////////////////////////////////// ES6
class Person {
  // constructor
  constructor(name) {
    this._name = name;
  }

  sayHi() {
    console.log(`Hi! ${this._name}`);
  }
}

// 인스턴스 생성
const me = new Person("Lee");
me.sayHi(); // Hi! Lee

console.log(me instanceof Person); // true
```

![prototype](https://poiemaweb.com/img/prototype-class.png)

위 코드와 함께 prototype에서 이해하기 쉬운 그림을 보면 ES6 이전의 prototype을 이해하는데에도 도움이 될 것이다.

`Person` 객체가 생성되면 prototype과 생성자 함수가 생기고 이를 기반으로 인스턴스를 `new` 예약어로 생성 가능하며 인스턴스는 `__proto__` 로 다시 `Person.prototype` 을 가르키게 된다.

# let & const로 엄격해진 JS 집안

let, const의 존재는 알지만 왜 기존에 잘 쓰던 var가 있는데 굳이 차이가 나는 것 같지도 않은 let const를 쓰는지 모르겠다는 개발자를 최근에 보았다.

아직 JS공부를 시작한 지 얼마 안 된 분이었기 때문에 충분히 그럴 수 있다고 생각 했고, 과거에 JS를 잘 몰랐을 때의 나도 그럤을 수 있을거라 생각하고 웃어넘겼지만, 이 글을 봤다면 더이상 이를 묵과해서는 안된다.

**간단히 말하면 `let & const`는 `block scope`이고 `var`는 `function scope`이다.**

어쨋건 이 셋은 모두 변수를 선언할 때 쓰는 예약어 이다.

1. var
   - 함수 블럭(중괄호로 감싸진 부분)만을 스코프로 인정하여 전역 변수 남용 이 발생 할 수 있다.
   - 변수 중복 선언 허용으로 상수의 개념이 없음
   - 변수 선언 이전에 참조 할 수 있다. `undefined`로 결과가 나오긴 하지만, 이는 올바른 에러핸들링을 방해한다.
2. let & const
   - 대부분의 언어에서와 마찬가지로 모든 블록들을 개별적인 스코프로 사용한다.
   - 변수 중복 선언 금지
   - let은 값이 변할 수 있는 변수, const는 초기화 후 값이 변하지 않는 변수
     - 여기서 값이란 주소값으로, const로 선언 했더라도 배열의 경우는 배열 요소가 바뀔 수는 있다.
   - 변수 선언 이전 참조 불가
     - 호이스팅 동작은 var와 같지만, 선언 → 초기화 → 할당의 기본 주기중 선언과 초기화 사이에 TDZ(Temporal Dead Zone)이 추가되며 선언 사각지대를 형성하기 때문에 선언 이전 참조시 에러를 발생시킴

이러한 새로운 변수 예약어의 등장으로 js 는 그 용도에 따라 더 세분화된 변수 사용이 가능해졌고, 의미가 명확해지도록 하여 엄격한 js 문법을 만들어갔다.

엄격하다는 것은 그만큼 신뢰성 있는 코드를 만들 수 있다는 의미이기 때문에 긍정적인 변화라고 할 수 있다.

# 함수 리터럴과 화살표 함수

```js
function foo() {
  console.log("foo");
} // ES6 이전

const foo = () => {
  console.log("foo");
};
```

ES6에서 새로 생긴 화살표 함수는 리터럴 함수 선언보다 간단히 함수를 표현하고, 그 의미를 명확히 하기 위해서 탄생했다.

- 화살표 함수는 항상 익명이며, 이를 const & let에 할당해 이름을 갖도록 할 수 있다.

- 화살표 함수에서 this의 의미

  - 일반 함수와 사용성에서 가장 큰 차이임

  - 일반 함수는 전역 컨텍스트에서 실행 될 때에 this가 동적으로 정의됨

  - 화살표 함수는 언제나 함수가 선언된 상위 스코프에 binding 됨

    - ```js
      const study = {
        name: "FeBase",
        assemble: function () {
          console.log(this.name); // FeBase 출력
          console.log("this는 객체 study인가? ", this === study); // true 출력
          function garthered() {
            console.log("this.name은?", this.name); // undefined 출력
            console.log("this는 객체 o? ", this === study); // false 출력
          }
          garthered(); // 함수 형태로 호출
        },
      };
      study.assemble(); // 메서드의 형태로 호출
      const study2 = study.assemble;
      study2(); // 이런 방식으로 호출된다면?
      ```

# Js 모두모여 Modules 모둘쓰~

모듈이란 애플리케이션을 구성하는 개별적 요소로서 재사용 가능한 코드 조각을 말한다. 모듈은 세부 사항을 캡슐화하고 공개가 필요한 API만을 외부에 노출한다.

```html
<html>
  <body>
    <script src="foo.js"></script>
    <script src="bar.js"></script>
  </body>
</html>
```

하지만 JS는 브라우저에서 동작을 서포트하기 위해 만들어진 한계로 인해 그동안은 전역 스코프에서 사용 되어 왔다.(주로 windows 객체)

이런 문제점을 ES6 를 지원하는 Client Browser에서 모듈 기능을 지원하게 되었다.

- 파일 단위의 모듈 스코프를 지원한다.

- 모듈에서 선언된 변수는 모두 내부에서만 사용 가능하다.

  - 변수에 `export` 예약어를 선언하면 외부에서도 사용 할 수 있게 된다.

  - `export`된 변수나 클래스를 다른 모듈에서 `import` 예약어로 사용 할 수 있다.

  - 이때 비구조화 할당으로 가져오는게 불편하다면, `export` 뒤에 `default` 를 붙이면 된다.

    - ```js
      // lib.js
      export default (x) => x * x;
      ```

    - ```js
      // app.js
      import myModule from "./lib.js";

      console.log(myModule(10)); // 100
      ```

# 약속 해줘~ ES6 Promise

순차적이지 않은 비동기 함수의 실행 순서를 제어할 수 있도록 지원 해 주는 기능이다.

Promise에 대해서는 [이전 글](https://samslow.github.io/development/2020/06/13/Javascript_Basic_Asyncronous/) 에서 한번 다룬 내용이고, 여전히 중요한 내용이다.

이번에는 장점들 위주로 다시한번 리마인드 해 본다.

- 장점
  - callback hell에서 벗어 날 수 있음
    - .then()의 return은 다음 .then()의 매개변수로 사용되므로 가독성 👆
  - .then() 을 이용하여 가독성 좋은 연속적인 비동기 코드를 작성 가능
  - Promise.all()을 통해 병렬 비동기 코드 작성 가능
    - 매개변수로 던져진 함수들이 모두 완료되면 return
  - callback 함수를 제 때 실행하지 못하거나 변수 전달 실패 없음
- 단점
- ES5 이전에서는 polyfill을 통해 로드해야 함

# Bonus

1. 비구조화 할당 지원

   비구조화 할당(구조분해 할당)을 처음 들었을때는 한글이나 영어나 무슨 말인지 알 수 없었지만, 사용 방법을 보면 바로 이해 할 수 있다.

   즉, 구조가 없는 객체를 알맞게 처리 하도록 돕는 기능이다.

   ```js
   person = {
     head: "top",
     body: "middle",
     foot: "bottom",
   };
   const { head, body, foot } = person;
   console.log(head, body, foot); // top middle bottom
   ```

2. 객체 리터럴

   객체를 생성 할 때 더욱 동적이고 간결하게 표현 할 수 있도록 해주고, 중복을 효과적으로 줄일 수 있는 문법이다.

   ```js
   // ES6
   let x = 1,
     y = 2;

   const obj = { x, y };

   console.log(obj); // { x: 1, y: 2 }
   ```

   ```js
   // ES6
   const obj = {
     name: "Lee",
     // 메소드 축약 표현
     sayHi() {
       // sayHi: function() { 과 같은 표현
       console.log("Hi! " + this.name);
     },
   };

   obj.sayHi(); // Hi! Lee
   ```

   이외에도 ES6에서는 객체 리터럴 내부에서 `__proto__` 프로퍼티를 직접 설정할 수 있다. 이것은 객체 리터럴에 의해 생성된 객체의 **proto** 프로퍼티에 다른 객체를 직접 바인딩하여 상속을 표현할 수 있음을 의미한다.

   뭐 사실 class도 같이지원 해 주기 떄문에 이는 보조적인 지원에 그친다고 보면된다.

3. Template Literals

   이 문법 역시 이미 다른 언어에서는 널리 지원되던 문법으로 String 안에서 변수를 더 단순하게 사용 할 수 있도록 하는 문법이다. 또 개행시 `\n` 를 생략 할 수 있는 장점도 제공한다.

   ```js
   const first = "Samuel";
   const last = "slow";
   console.log(`제 이름은 ${first} ${last} 입니다.`);
   console.log(`
   	긴글을 아무리 써도 단지 개행을 자연스럽게 해주면? // 원래는 + "\n" + 를 해주지만
   	따로 \n을 해주지 않더라도 출력시 개행이 되지!
   	`);
   ```

4. 매개변수 기본값

   사실 이런것 까지 해야하나 싶지만, 이 내용도 일단 ES6에서 시작된 것이므로 함께 기재한다.

   필자같은 경우 이미 이것을 사용하고 있었는데 ES6 에서 새로 생긴것을 뒤늦게 알게 되었다.

   즉 함수의 매개변수에 기본값을 할당하여, 해당 자리에 적절한 값이 없을 때 기본으로 들어가게하는 값이다.

   ```js
   function multiply(a, b = 1) {
     return a * b;
   }
   console.log(multiply(5, 2)); // 10
   console.log(multiply(5, 1)); // 5
   console.log(multiply(5)); // 5
   ```

# Self Check

1. 최신 ECMAScript의 Edition Number는 ?
2. ES6의 주요 특징 중 최소 3가지를 말하고 설명 하시오
3. 화살표 함수의 this scope는 (동적/정적) scope로 주로 `____` 의 scope를 따른다.

# Closing

ES6의 특징은 줄곧 알고 있던 것들인데, 예제와 함께 이해하고 설명한다고 생각하니 잘 이해되지 않는 부분들 떄문에 글을 쓰는데 시간이 좀 걸렸다. 역시 설명 할 때는 이해했다고 생각한 것과 다른 것을 알 수 있는 것 같다. 특히 arrow function의 this의 의미는 제대로 알고 넘어갔으면 좋겠다.

let & const 를 설명하면서 Hoisting을 설명하고 싶었는데, Hoisting 자체는 var에도 있던 내용이라, 이 게시글에서 다루지 않고, 다음 포스트에서 단독 포스트로 다루려고한다.

빠잉

# Reference

- [우아한 형제들 기술 블로그](https://woowabros.github.io/experience/2017/12/01/es6-experience.html)
- [poiemaweb](https://poiemaweb.com/es6-class)
