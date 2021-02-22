---
title: JS TDD 개론
date: 2020-12-03 19:00:00
author: wooooooood
category: S2_Round2
---

# JS TDD 개론
## TDD? Test-Driven-Development 테스트 주도 개발
`테스트 케이스 생성→테스트→개발`의 짧은 개발 사이클을 반복적으로 수행하며 소프트웨어를 개발하는 프로세스.  
Red-Green Refactor 라고도 한다.

![TDD cycle](https://codica-images-staging.s3.eu-central-1.amazonaws.com/c3cb64e3ac2d4eae89002e0ccc5789dd.png)


1. 테스트 케이스 작성
2. 테스트 케이스를 통과하기 위한 최소한의 코드 작성
3. 표준에 맞도록 리팩토링

*Uncle Bob describes TDD with three rules:*
> 1. You are not allowed to write any production code unless it is to make a failing unit test pass.
> 2. You are not allowed to write any more of a unit test than is sufficient to fail; and compilation failures are failures.
> 3. You are not allowed to write any more production code than is sufficient to pass the one failing unit test.

### Why?
![기존의 개발 프로세스](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/fec43eb9-5a07-4f4f-aac2-e63fc4033c5e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201202T134854Z&X-Amz-Expires=86400&X-Amz-Signature=dbbba99a54c03e189ad3c202eff92bd5532e05c639bae988b614f4fcc9bbc354&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)
기존의 개발 프로세스

![TDD 프로세스](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/88266afb-20f0-4c69-ac69-1d78d0163c90/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201202T134914Z&X-Amz-Expires=86400&X-Amz-Signature=5d76daed432d75653a9e8c9cb0b787e61d2c1336df000087c2e44c88679b7cb0&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)
TDD 프로세스

- 설계 수정 시간 단축
- 디버깅 및 버그 수정 시간 단축
    - 문제 발생 시 모듈별 테스트를 통해 문제 지점을 빠르게 파악 가능
    - Production 레벨에서 버그를 수정하는 것은 Software development lifecycle (SDLC)에서 버그를 수정하는 것보다 훨씬 큰 비용과 시간을 소모
- Refactoring을 통해 Clean code를 유지
- 객체지향적인 코드 개발
    - 세부 비즈니스 로직을 객체 내부로 숨겨 변경에 대응
    - 유지보수 및 재사용에 용이

### 단점
- 테스트 코드를 작성, 유지하기 위한 비용과 시간

### How?
- **Mock객체**를 생성하여 테스트
    - 변경할 수 없는 객체, 프레임워크, 외부 라이브러리는 Mock하지 않는다
    - ex. `Jest`에서 기본적으로 제공하는 mock functions
    ```js
    const myMockFunc = jest.fn().mockName("myMockFunc");
    const myExampleModule = jest.mock("./exampleModule");
    ```
- **Private객체**의 테스트는?
    1. Public 객체에서 커버되는 경우 테스트하지 않는다.
    2. 리팩토링 고려. 해당 객체가 불필요한 책임을 가졌을 수 있다.
    3. 접근 제한을 Public으로 변경 후 `@VisibleForTesting` 추가
- 하나의 테스트에는 **하나의 기능**만 테스트한다
    - 대상 코드의 의도 표현
    - 데이터가 아닌 행위를 테스트한다 `given-when-then`
- 테스트하기 어려운 코드가 있다면 *어떻게 하면 테스트할 수 있을까* 가 아닌, ***왜 테스트하기 어려울까***를 고민

### 종류

![TDD pyramid](https://miro.medium.com/max/1200/1*BfpihCUZnTOp-yt6WZjI0g.png)

- **Unit Testing**: 가장 작은 단위 테스트(함수)
- **Integration Testing**: 시스템 모델링에서 실제 기능, 퍼포먼스, 의존성, DB 데이터 등을 테스트
- **UI Testing (E2E)**: 사용자 관점 테스트(UI)

## **Unit Test 단위 테스트**
- 가장 작은 단위
- 단위 테스트이므로 다른 Unit과 의존성이 있어서는 안된다.
- 툴은 Mocha, Jasmine, Chai, Jest, Tape, Enzyme, Karma, Selenium, phantomjs 등 다양하며, 조합해서 사용할 수 있다.

### 예제 with `Jest`
1.  `npm init -y` 으로 package.json을 생성한다.
2. `npm i -D jest` 로 development 모드로 jest를 실행한다.
3. package.json의 `test`를 수정한다. (test를 입력했을 때 jest를 실행하겠다는 의미)

```jsx
"scripts": {
  "test": "jest"
},
```

1. 테스트를 진행할 파일 `unit.test.js`를 생성한다.
    - `.test.js` suffix를 사용해야 한다.
```jsx
const add = (a, b) => {
  return 1;
};

test('solution', () => {
  expect(add(1, 1)).toBe(2);
});
```
- 영어 문법과 비슷: expect ~ toBe (보통 value) / expect ~ toEqual (array 등의 object)

2. 테스트 `npm test ./unit.test.js` 결과는 반드시 실패한다. (Red)

![Red](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/7232e4f5-a6dd-47b8-a124-a2e68982c784/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201202T135507Z&X-Amz-Expires=86400&X-Amz-Signature=cb2c06e1821bebae7ed5432559ad80aaa0a74eb0277612495415bae737b677f3&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

3. 성공하는 테스트 코드를 작성한다. (Green)
```jsx
const add = (a, b) => {
  const num1 = a;
  const num2 = b;

  return num1 + num2;
};

test('solution', () => {
  expect(add(1, 1)).toBe(2);
});
```

![Green](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/0a76740d-37df-4b31-8b19-326a5e1c1fcf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20201202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20201202T135525Z&X-Amz-Expires=86400&X-Amz-Signature=2bfbb4b23aa22ed1fa1a8428f807b7b749366ec58f13c789c11e30b736818d6f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

4. 성공 확인 후 리팩토링한다. (Refactor)
```jsx
const add = (a, b) => {
  return a+b;
};

test('solution', () => {
  expect(add(1, 1)).toBe(2);
});
```

## **통합 테스트 Integration Test**
- 앞서 unit테스트한 각각의 module들이 통합되었을 때 올바르게 동작하는지 확인하기 위함
- 주요 목적은 module들 간의 인터페이스 동작 테스트
- db, platform, environment등이 포함되어 테스트되므로 복잡해질 수 있음

### Integration Test with `Jest`
1. Unit test 방법과 거의 동일하며, [여기](https://gist.github.com/cowchimp/0158efe57df3b845927e450fc2b87eeb)에서 샘플 코드 일부를 가져왔다.
```js
import { calculateTopEmployee } from './top-employee-provider';
import { get } from './api-wrapper';

jest.mock('./api-wrapper');

test('returns the top-performing employee', async () => {
  mockApiResponse('/employees', [
    {name: 'foo', numOfSales: 1 },
    {name: 'bar', numOfSales: 2 }
  ]);

  const topEmployee = await calculateTopEmployee();

  expect(topEmployee).toEqual({ name: 'bar', numOfSales: 2 });
});

function mockApiResponse(endpoint, payload) {
  const successfulPromise = new Promise(resolve => process.nextTick(() => resolve(payload)));

  get.mockImplementationOnce(e => e === endpoint ? successfulPromise : Promise.reject());
}
```

## **E2E테스트 (End to End Test)**
- 사용자 입장 (환경 Latency, 관점 Workflow 등)에서의 테스트를 통해 사용자 경험 증대
- Web, App 등에서의 시나리오, 기능 확인
- 가장 확실하고 가장 필요한 테스트

### E2E with **`Cypress`**
- [여기](https://softchris.github.io/pages/cypress.html)에 자세한 예제가 나와있어 일부 사진과 기능만을 가져왔다.  
- `Cypress`는 다양한 helper를 지원하여 사용자 action에 따른 테스트가 가능하다.  
- 현재는 Chrome과 Electron만 지원한다.

1. **Visit**
```js
describe('My First Test', function() {
  it('Visits page', function() {
    cy.visit('https://example.cypress.io')
  })
})
```
![Cypress visit](https://thepracticaldev.s3.amazonaws.com/i/gh608lx54t1scsjehftk.png)  
  
  
2. **Interact**
```js
cy.contains('type').click()
```
![Cypress click](https://thepracticaldev.s3.amazonaws.com/i/v8xgdtz25pccpzl68in5.png)  
  
  
3. **Debug**  
- 코드상에서 멈추고 싶은 위치에 `cy.pause()`를 삽입하여 디버깅할 수 있다.
- `cy.debug()`를 삽입하면 개발자 도구에서 Args등의 로그를 추가로 확인할 수 있다.
![Cypress debug](https://thepracticaldev.s3.amazonaws.com/i/y2b7iq93toexnc89rhnp.gif)

## Reference

- [https://m.blog.naver.com/PostView.nhn?blogId=suresofttech&logNo=221569611618&proxyReferer=https:%2F%2Fwww.google.com%2F](https://m.blog.naver.com/PostView.nhn?blogId=suresofttech&logNo=221569611618&proxyReferer=https:%2F%2Fwww.google.com%2F)
- [https://medium.com/hbsmith/e2e-test-알아보기-3c524862469d](https://medium.com/hbsmith/e2e-test-%EC%95%8C%EC%95%84%EB%B3%B4%EA%B8%B0-3c524862469d)
- [https://velog.io/@rosewwross/unit-test](https://velog.io/@rosewwross/unit-test)
- [https://www.slideshare.net/koreakihoon/tdd-112099012](https://www.slideshare.net/koreakihoon/tdd-112099012)
- [https://docs.reactioncommerce.com/docs/testing-reaction](https://docs.reactioncommerce.com/docs/testing-reaction)
- [https://www.softwaretestinghelp.com/what-is-integration-testing/](https://www.softwaretestinghelp.com/what-is-integration-testing/)
- [https://gist.github.com/cowchimp/0158efe57df3b845927e450fc2b87eeb](https://gist.github.com/cowchimp/0158efe57df3b845927e450fc2b87eeb)
- https://softchris.github.io/pages/cypress.html
