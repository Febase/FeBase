---
title: FID
date: 2020-12-10 00:00:00
author: chjjh0
category: S2_Round3
---

# Optimize First Input Delay

## How to respond faster to user interactions.

![FID](https://user-images.githubusercontent.com/39721166/102237901-7e066980-3f38-11eb-9ecf-b8ba2cadde91.png)

- 상호작용을 측정하여 사용자 환경이 좋고 나쁜지 알 수 있는 지표<br>
  (상호작용: 링크 or 버튼 클릭시 이벤트가 시작되어 응답을 받을 때가지 걸리는 시간을 의미)
- 과도한 JavaScript 실행은 **FID를 나쁘게 만드는 주요원인**
- lighthouse같은 시뮬레이션 환경에서는 사용자 입력을 받을 수 없기 때문에 FID를 측정할 수 없지만, TBT<br>(Total Blocking Time)로 대체 측정 가능하기때문에 TBT를 개선시키면 FID 개선됨
  <br><br>

![lighthouse_performance](https://user-images.githubusercontent.com/39721166/102238090-b9a13380-3f38-11eb-8ee9-b034399607de.png)

<br>
<br>
<br>

### Heavy JavaScript execution

- **main thread를 점유율을 낮춰라**
- 브라우저는 main thread에서 **얼마나 큰 JS가 불러와지고 실행되느냐**에 따라 사용자 입력에 영향을 준다
- 사용자가 사이트에 들어와 로드되는 JS 크기가 크거나
  실행되는 JS 코드가 main thread를 많이 잡아먹는다면<br>
  사이트의 상호작용들이 제대로 동작하지 않을 수 있다
- 개선을 위한 Tip

  - [Break up Long Tasks](https://web.dev/optimize-fid/#long-tasks)
  - [Optimize your page for interaction readiness](https://web.dev/optimize-fid/#optimize-your-page-for-interaction-readiness)
  - [Use a web worker](https://web.dev/optimize-fid/#use-a-web-worker)
  - [Reduce JavaScript execution time](https://web.dev/optimize-fid/#reduce-javascript-execution)

  <br><br>

### Break up Long Tasks

- [Long Tasks](https://web.dev/long-tasks-devtools/) 를 줄여라<br>
  (Long Tasks: main thread를 50ms 이상 점유하여 사이트의 입력지연을 발생시키는 작업을 칭함)
- 예를들어 사용자가 현재 사이트를 이용하는데 필요하지 않는 코드를 로드하거나, <br>
  JS 코드를 실행한다면 main thread를 50ms 이상 점유할 가능성이 높아져서 Long Tasks가 될 가능성 증가
- 이를 개선하기 위해 Code Splitting을 통해 JS파일을 적절하게 나누거나 JS 파일이 이미 로드되었다면 <br>
  부하가 많은 실행코드들을 더 작은 비동기 작업으로 나누는 것을 권장하며 <br>
  이런 작업을 통해 눈에 띄게 향상된 FID 기대할 수 있음
- 브라우저 > 검사도구 > Performance 탭에서 확인 가능
- 사이트별 Long Tasks 비교<br>
  #1 www.laftel.net의 Long Tasks<br>

  ![laftel_performance](https://user-images.githubusercontent.com/39721166/102239805-92e3fc80-3f3a-11eb-9305-b8f5406d71da.png)
  <div></div>

  <br>
  #2 code splitting, lazyloading 등 최적화 적용이 되지 않은 개발버전 프로젝트의 Long Tasks<br>

  ![privateproject_performance](https://user-images.githubusercontent.com/39721166/102239936-adb67100-3f3a-11eb-8f72-b74e758737aa.png)

### Optimize your page for interaction readiness

- 상호작용 준비를 위한 최적화
- FID & TBT 점수를 낮추는 몇 가지 원인과 개선안

  - [First-party script execution can delay interaction readiness](https://web.dev/optimize-fid/#optimize-your-page-for-interaction-readiness)
  - [Data-fetching can impact many aspects of interaction readiness](https://web.dev/optimize-fid/#data-fetching-can-impact-many-aspects-of-interaction-readiness)
  - [Third-party script execution can delay interaction latency too](https://web.dev/optimize-fid/#third-party-script-execution-can-delay-interaction-latency-too)
  - [Use a web worker](https://web.dev/optimize-fid/#use-a-web-worker)

  <br><br>

  > [First-party script execution can delay interaction readiness](https://web.dev/optimize-fid/#optimize-your-page-for-interaction-readiness)

  - 크기가 큰 JS파일, 긴 JS 실행시간, 비효율적인 청킹 파일 등은 FID, TBT or TTI에 악영향을 줄수 있음,<br>
    코드 및 기능을 비동기적으로 불러들여 개선

  <br><br>

  > [Data-fetching can impact many aspects of interaction readiness](https://www.notion.so/Optimize-First-Input-Delay-25ceae4147c7486c97c65c29e685b017#a2c86baefea64ef3af42cd280306ac4c)

  - 데이터 가져오기는 상호작용에 영향을 미칠 수 있고<br>
    클라이언트측에서 후처리해야하는 데이터의 양을 최소화하여 개선<br>
    (후처리란 데이터를 불러와서 추가 가공작업을 위한 연산이 오래걸릴수록 악영향을 주는데<br>
    이를 최소화하는게 성능향상에 도움을 줌)

  <br><br>

  > [Third-party script execution can delay interaction latency too](https://web.dev/optimize-fid/#third-party-script-execution-can-delay-interaction-latency-too)

  - 써드파티 스크립트의 지속적인 네트워크 요청 및 main thread 점유율을 체크하여 개선

  <br><br>

  > [Use a web worker](https://web.dev/optimize-fid/#use-a-web-worker)

  - [Web Worke](https://developer.mozilla.org/en-US/docs/Web/API/Worker)r를 사용하면 JS를 **background thread 에서 실행**할 수 있기때문에 개선 가능
  - Web Worker가 main thread 에서 코드를 실행하는 [자세한 방법](https://web.dev/off-main-thread/)
  - Web Worker를 쉽게 사용할 수 있게 돕는 라이브러리
    - [Comlink](https://github.com/GoogleChromeLabs/comlink): A helper library that abstracts `postMessage` and makes it easier to use
    - [Workway](https://github.com/WebReflection/workway): A general purpose web worker exporter
    - [Workerize](https://github.com/developit/workerize): Move a module into a web worker

### Reduce JavaScript execution time

1.  Defer unused JavaScript<br>

    - 페이지 진입 시 불러오는 JS 의 크기 최소화 및 중요하지 않은 JS 코드는 defer or async로 로딩을 지연 시켜라

       <details>
       <summary>브라우저에서 script를 불러오는 과정</summary>

      [참고링크](https://blog.asamaru.net/2017/05/04/script-async-defer/)

      - 일반적인 실행과정<br>
        Script fetch/execution이 **완료될 때까지 HTML parsing 일시정지**<br>
        ![script_basic_loading](https://user-images.githubusercontent.com/39721166/102242439-67164600-3f3d-11eb-951b-1b5c3aeda308.png)

      - async 속성이 추가된 실행과정<br>
        HTML parsing과 Script fetch가 **병렬적**으로 실행 가능<br>
        Script fetch가 끝나고 **execution 될 때에는 HTML parsing 일시정지**
        <br>

      ```javascript
      <script async src="script.js">
      ```

      ![script_async_loading](https://user-images.githubusercontent.com/39721166/102242849-dc821680-3f3d-11eb-8b85-23f9bd2e77c8.png)

      - defer 속성이 추가된 실행과정<br>
        HTML parsing과 Script fetch가 **병렬적**으로 실행 가능하지만,<br>
        Script fetch가 끝다더라도 **HTML parsing이 끝나야 excution 가능**
        <br>

      ```javascript
      <script defer src="script.js">
      ```

      ![script_defer_loading](https://user-images.githubusercontent.com/39721166/102243170-3551af00-3f3e-11eb-97d1-4013c900a5a0.png)

     </details>

    - Webpack, Rollpup, Parcel같은 번들러의 도움을 받아 Code Splitting 을 하고 Dynamic import 추천
    - React, Vue 를 사용해 컴포넌트 단위로 lazy-load 추천

2.  Minimize unused polyfills<br>

    - 폴리필을 불러올 때 **프로젝트에 필요한 폴리필**만 로드해라
    - 예를들어 Babel의 preset-env만 필요하다면 다음처럼 import 권장

      ```javascript
      // 나쁜 예
      // preset-env만 필요한데 바벨 전체를 불러와 불필요한 것까지 import
      import '@babel'

      // 좋은 예
      // 필요한 preset-env만 import
      import '@babel/preset-env'
      ```
