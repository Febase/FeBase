---
title: JavaScript Interview Questions 3rd Aug 12th
category: interview
date: 2020-08-12 01:00:00
author: dev-owen
---

<br>

# JavaScript Interview Questions 3rd Aug 12th

<br>

## 학습 목표

- MPA, SPA, SSR, CSR, SEO의 개념에 대해 알아본다.
- SPA에서 SEO를 최적화 하는 방식에 대해 알아본다.
- Promise와 콜백 함수의 차이점에 대해 알아본다.

<br>

### 1. SPA에서 SEO에 유리하도록 만들기 위한 방법에 대해 설명해주세요.

먼저 간단하게 SPA와 MPA, CSR과 SSR, SEO에 대해서 복습하고 가자.

#### MPA (Multiple Page Application)

사용자가 페이지를 요청할 때마다, 웹 서버가 요청한 UI와 필요한 데이터를 HTML로 파싱해서 보여주는 방식의 웹 어플리케이션이다. 
사용자가 아주 사소한 요청을 해주어도(버튼 클릭 등) 매번 전체 페이지를 렌더링 해주어야 한다.

- 장점
    - SEO(Search Engine Optimization, 검색엔진 최적화) 관점에서 유리하다.
    - MPA는 완성된 형태의 HTML 파일을 서버에서 전달받기에 검색엔진이 페이지를 크롤링하기에 적합하다.
- 단점
    - 매번 페이지 전체를 새로 불러와서 렌더링 해야 하기 때문에 화면이 깜빡이는 등 성능상의 이슈가 있다.
    - 프론트와 백이 밀접하게 연관되어 있어서 개발 복잡도가 증가한다. 

#### SPA (Single Page Application)

하나의 HTML 파일을 기반으로 자바스크립트를 이용해 동적으로 화면의 컨텐츠를 바꾸는 방식의 웹 어플리케이션이다.
처음에 한 번만 정적 리소스를 다운받고, 그 이후에는 새로운 요청이 들어왔을 때 필요한 데이터만 부분적으로 바꾸어 준다.

- 장점
    - 사용자 경험 측면에서 좋다. 성능이 우수하다.
    - 서버 없이도 개발이 가능하며 디버깅이 상대적으로 쉽다.
    - 로컬 데이터를 효과적으로 캐시(cache)할 수 있다. 처음에 받은 데이터를 모두 로컬 캐시에 저장해 놓아서 오프라인에서도 사용할 수 있다.
- 단점
    - 초기 구동 속도가 느리다. 초기에 웹 어플리케이션에 필요한 모든 정적 리소스를 다 받아야 하기 때문이다.
    - SEO 관점에서 불리하다. 

![MPA_SPA](https://docs.microsoft.com/en-us/archive/msdn-magazine/2013/november/images/dn463786.wasson_figure2_hires%28en-us%2cmsdn.10%29.png)

#### SSR (Server Side Rendering)

서버사이드 렌더링은 서버에서 정적인 페이지로 렌더링 되어 사용자에게 내려오는 것을 의미한다. 
따라서 초기 로딩속도가 빠르고(JS 파일을 다운로드하고 적용하기 전에 이미 브라우저에서 보여지기 때문) SEO에 사용되는 meta 태그들이 미리 정의되어 SEO 에 유리하다.

![SSR](https://media.vlpt.us/images/byseop/post/5d20be94-1eaa-4236-9b65-e00cdf348d00/SSR.png)

#### CSR (Client Side Rendering)

클라이언트 사이드 렌더링은 브라우저가 자바스크립트를 받아와 동적으로 렌더링한다. 
첫 로딩시에 필요한 파일크기는 더 크지만(HTML, JS, 그외 리소스 모두 포함) 다 받기만 하면 동적으로 빠르게 렌더링 하기 때문에 사용자가 느끼는 UX에 유리하다. 
SSR과는 다르게 하나의 HTML파일로 모든 페이지를 구성하기 때문에 meta 태그 정의에 약점이 있다.

![CSR](https://media.vlpt.us/images/byseop/post/14fe740a-2ade-43ae-a87e-242ab3302756/CSR.png)

일반적으로 MPA를 SSR, SPA를 CSR이라고 하는데 엄밀히 말하면 이 표현은 틀렸다.
정확히는 `MPA가 주로 SSR을 사용하는 것`이고, `SPA가 주로 CSR을 사용하는 것`이다.

MPA/SPA는 페이지를 여러개 쓰는지 또는 한 개 쓰는지에 대한 개념이고 SSR/CSR은 렌더링을 서버에서 하는지, 클라이언트에서 하는지에 대한 개념이다.
SPA가 1. 서버로부터 처음에 페이지(정적 리소스)를 받아오고 2. 이후에는 동적으로 DOM을 구성하여 렌더링 되는 화면이 바뀌게 한다고 했는데 여기서 2번에 대한 개념이 CSR인 것이다.
SPA에서 SSR을 사용하는 경우가 있는데 이는 위의 문장에서 1번에서 가져온 리소스를 SSR로 렌더링 하는 것이다.

#### SEO (Search Engine Optimization) 

검색엔진 최적화는 웹페이지 검색엔진이 자료를 수집하고 순위를 매기는 방식에 맞게 웹 페이지를 구성하여 검색 결과의 상위에 나올 수 있도록 하는 작업을 의미한다.

#### 그래서 결론적으로 SPA에서 SEO는 어떻게 해야 할까?

일반적으로 검색 엔진의 크롤러들은 데이터를 긁어올 때 웹 페이지의 JS를 해석해 노출시키기 때문에 크롤링을 할 수 없는 시점에서는 검색 엔진에 데이터를 노출시키지 않는 것이고, 
이는 상대적으로 우리의 서비스가 검색 엔진 서비스에 노출되는 것이 줄어듦을 의미한다.

따라서 CSR을 사용하면 View를 생성하기 위해서 JS가 필요하고(그 전까지는 빈 페이지이기 때문에 View가 완성되지 않아서), 
View를 생성하기 전까지는 검색 엔진 크롤러의 데이터 수집이 제한적이기 때문에 상대적으로 검색 엔진이 이해하는 정보가 부족해 SEO에 유리하지 않게 된다.

반대로 전통적인 SSR은 View를 서버에서 렌더링해 제공하기 때문에(View를 먼저 그리기 때문에) 상대적으로 SEO에 유리해져 사용자 유입이 많을 것이다.

정리하면 전통적인 SSR은 초기 로딩 속도가 빠르고 SEO에 유리하지만, View 변경(화면 전환) 시 계속적으로(새로고침하며) 서버에 요청해야 하므로 서버에 부담이 크다. 
그리고 CSR은 초기 로딩 속도가 느리고 SEO에 대한 문제가 있지만, 초기 로딩 후에는 View를 서버에 요청하는 것이 아닌 클라이언트에서 직접 렌더링하기 때문에 화면 전환이 매우 빠르다는 장점이 있다.

**이 두 가지 렌더링 방법을 적절하게 사용하여 첫 번째 페이지 로딩에서는 서버 사이드 렌더링을 사용하고, 
그 후에 모든 페이지 로드에는 클라이언트 사이드 렌더링을 활용하는 방법을 많이 사용한다.**

React에서는 Next.js, GatsbyJS, Vue에서는 Nuxt.js 등의 라이브러리가 SPA에서 SEO을 할 수 있도록 도와준다.
많이 사용하는 Next.js의 경우 살펴보면 전통적엔 SSR이 아닌 SPA에서 SEO에 유리하기 위한 SSR를 도입하고 
그 이외에도 개발자들이 직접 노드에서 환경설정을 해주지 않고도 익숙한 툴(바벨, 웹팩 등)을 가지고 설정을 할 수 있게 지원해 주기에 많은 React 개발자들이 선호한다.

또는 CSR에서 메타 태그를 정의해주는 라이브러리를 사용하는 것도 방법이다. 대표적인 라이브러리로 `react-helmet`이 있다.
이 라이브러리는 동적으로 SEO에 필요한 메타태그들을 쉽게 변경할 수 있도록 도와준다. JSX 또는 TSX 내부에서 메타태그를 관리할 수 있다.

<br>

### 2. Promise가 콜백 대비 장/단점은 무엇인지 설명해주세요.

자바스크립트는 싱글 스레드 언어로 하나의 콜 스택(Call Stack)에서 함수를 하나씩 넣고 처리도 하나씩 순차적으로 진행한다.
콜 스택에서 함수를 하나씩 꺼내서 실행하는 과정에 WEB API라는 브라우저에서 제공하는 API를 호출하게 되면, 
이 비동기 함수를 우리는 콜백 함수(Callback Function)라고 하며 콜백 큐에 넣는다.
그러면 이벤트 루프(Event Loop)는 콜 스택과 콜백 큐를 바라보며 콜 스택이 비어있을 때 콜백 큐의 첫 번째 콜백을 콜 스택으로 밀어 넣는다.
이렇게 특정 코드의 연산이 끝날 때까지 코드의 실행을 멈추지 않고 다음 코드를 먼저 실행하는 특성을 자바스크립트의 비동기 처리라고 한다.

![EVENT_LOOP](https://miro.medium.com/max/2048/1*4lHHyfEhVB0LnQ3HlhSs8g.png)

콜백 함수는 자바스크립트 개발에서 빠질 수 없는 굉장히 중요한 요소이지만, 너무 자주 사용하다보면 코드의 가독성이 나빠지고 유지보수도 어려워 
결과적으로 개발 일정의 지연을 초래하는 원인이 되기도 한다.

```javascript
// 콜백이 중첩된 콜백 지옥(Callback Hell) 예시
$.get('url', function(response) {
	parseValue(response, function(id) {
		auth(id, function(result) {
			display(result, function(text) {
				console.log(text);
			});
		});
	});
});
```

따라서 이러한 문제를 해결하기 위해 ES6에서 등장한 개념이 프로미스(Promise)이다. 프로미스는 자바스크립트 비동기 처리에 사용되는 객체로 다음과 같은 세 가지 상태를 가진다.
- Pending(대기) : 비동기 처리 로직이 아직 완료되지 않은 상태
    - `new Promise()` 객체를 생하면 대기 상태가 된다.
- Fulfilled(이행) : 비동기 처리가 완료되어 프로미스가 결과 값을 반환해준 상태
    - 첫 번째 파라미터 `resolve`를 실행하면 이 상태가 되며, 이후 `then()`을 통해 처리 결과를 받는다. 
- Rejected(실패) : 비동기 처리가 실패하거나 오류가 발생한 상태
    - 두 번째 파라미터 `reject`를 실행하면 이 상태가 되며, 이후 `catch()`를 통해 실패 원인과 결과 값을 받는다.
    
![Promise](https://joshua1988.github.io/images/posts/web/javascript/promise.svg)

콜백 함수와 프로미스를 각각 사용하여 같은 기능을 구현한 예제를 보도록 하자.

```javascript
// Callback Function

function getData(callbackFunc) {
  $.get('url 주소/products/1', function(response) {
    callbackFunc(response); // 서버에서 받은 데이터 response를 callbackFunc() 함수에 넘겨줌
  });
}

getData(function(tableData) {
  console.log(tableData); // $.get()의 response 값이 tableData에 전달됨
});


// Promise

function getData(callback) {
  // new Promise() 추가
  return new Promise(function(resolve, reject) {
    $.get('url 주소/products/1', function(response) {
      // 데이터를 받으면 resolve() 호출
      resolve(response);
    });
  });
}

// getData()의 실행이 끝나면 호출되는 then()
getData().then(function(tableData) {
  // resolve()의 결과 값이 여기로 전달됨
  console.log(tableData); // $.get()의 reponse 값이 tableData에 전달됨
});
```

질문에 대한 답변을 하면, Promise는 콜백 함수 대비
- 장점
    1. 가독성이 좋고 유지보수가 쉽다.
    2. 비동기 처리를 하더라도 순차적인 흐름을 파악할 수가 있어서 순서가 꼬일 확률이 적다(결국 1번...)
    3. `promise.all()`을 사용하여 병렬적으로 비동기 처리를 할 수도 있다.
    4. `resolve()`, `reject()`를 통해 성공, 실패 상황에 따른 분기처리를 하기가 수월하다.
- 단점(엄밀히 말하면 단점은 아니지만)
    1. Promise도 코드가 복잡하고 분기처리가 힘들다고 하는 사람들이 존재한다.
    2. 에러 핸들링을 하기가 어렵다. 아래 예제에서 catch 문은 에러를 잡지 못한다. 주석처리한 `.catch()`로 잡아야 한다.
    ```javascript
    const makeRequest = () => {
      try {
        getJSON()
          .then(result => {
            // this parse may fail
            const data = JSON.parse(result)
            console.log(data)
          })
          // uncomment this block to handle asynchronous errors
          // .catch((err) => {
          //   console.log(err)
          // })
      } catch (err) {
        console.log(err)
      }
    }
    ```
  3. 디버깅을 하기가 어렵다. 아래 예제에서 `.then` 블록 안에 중단점을 잡을 수 없다. 디버그 도구는 동기화된 코드를 따라 움직이기 때문.
  ```javascript
    const makeRequest = () => {
      return callPromise()
        .then(() => callAPromise())
        .then(() => callAPromise())
        .then(() => callAPromise())
    }
    ```
  
  이러한 단점을 보완하기 위해 ES7에서 Async/Await이 등장하였다.
<br>

## 셀프 체크

1. MPA == SSR 이고 SPA == CSR 이다. (O/X)
2. 어떤 함수가 Promise 객체를 통해 비동기 처리를 할 때, 성공시 _____ 을 호출하며, 실패시 _______ 를 호출한다.

<br>

## 참고자료

- https://github.com/baeharam/Must-Know-About-Frontend/blob/master/Notes/frontend/csr-ssr.md
- https://velog.io/@thms200/SPA-vs.-MPA
- https://velog.io/@rjs1197/SSR%EA%B3%BC-CSR%EC%9D%98-%EC%B0%A8%EC%9D%B4%EB%A5%BC-%EC%95%8C%EC%95%84%EB%B3%B4%EC%9E%90
- https://velog.io/@thms200/Event-Loop-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EB%A3%A8%ED%94%84
- https://joshua1988.github.io/web-development/javascript/javascript-asynchronous-operation/
