---
title: React 렌더링 측정(Lighthouse)
date: 2020-11-26 00:00:00
author: junCastle
category: S2_Round2
---

이번에 다를 주제는 Lighthouse 라는 도구를 사용해서 React 웹의 렌더링 성능을 측정하는 방법과 프로파일링에 대해 알아보려고 한다.

# React 렌더링 측정 with Lighthouse

https://developers.google.com/web/tools/lighthouse?hl=ko 에 따르면  
Lighthouse는 웹 앱의 품질을 개선하는 오픈 소스 자동화 도구이다.  
Chrome 확장프로그램, 커맨드 라인에서, 노드 모듈에서 프로그램으로도 사용할 수 있다. Lighthouse에 확인할 URL을 지정하고, 페이지에 대한 테스트를 실행한 다음, 페이지에 대한 보고서를 생성한다. 여기에서 실패한 테스트는 앱을 개선하기 위해 할 수 있는 것에 대한 지표로 사용할 수 있다.  

Lighthouse가 생성해주는 지표에는 Performance, Accessibility, Base Practices, SEO, Progressive Web App 등이 있는데 React 웹의 렌더링 성능을 측정하기 위해서 Performance 지표를 중심으로 설명해보려 한다.

## Performance

![lighthouse-example](https://user-images.githubusercontent.com/35620465/100883287-851e8800-34f3-11eb-8a60-6a64f669c756.png)

위 사진은 우리 회사 서비스의 웹 페이지를 Lighthouse 를 활용해 측정받은 결과이다.  
Lighthouse는 매번 성능을 측정받을 때마다 결과값이 다르게 나올수 있다고 한다. 왜냐하면  

- 게재되는 광고
- 인터넷 트래픽 라우팅 변경
- 고성능 데스크톱 및 저성능 노트북과 같은 다양한 장치에서 테스트
- 바이러스 백신 소프트웨어

등 다양한 환경에 따라 영향을 받을 수 있기 때문이다.

위 사진에서 Performance 지표에는 27점이 나왔다.  
각각의 지표들은 0-49, 50-89, 90-100 범위별로 나누어져 지표의 등급을 표시해주고 있다.  
당연히 모든 지표가 90-100 범위에 들어 초록불이 나온다면 굉장히 좋을 것이다.  
하지만 Lighthouse 가이드 문서에 따르면 그것은 굉장히 어려운 일이라고 한다. 99점에서 100점에 도달하는것은 90점에서 94점에 도달하는것과 비슷한 수준의 Metrics 개선이 필요하다고 설명해주고 있다.  

지표 점수에 영향을 주는 것은 Metrics에 나와있는 목록들이다.  

- FCP(First Contentful Paint) - 브라우저에 첫번째 콘텐츠가 로딩되는 시간을 의미한다.
- TTI(Time to Interactive) - 사용자가 웹에서 상호작용 할 수 있는데까지 걸리는 시점(클릭, 스크롤링 등) 을 의미한다.
- SI(Speed Index) - 콘텐츠가 시각적으로 얼마나 빨리 표시되는지를 의미한다.
- TBT(Total Blocking Time) - 웹을 로딩할 때 중간중간 Blocking 되는 시간의 총 합을 의미한다.
- LCP(Largest Contentful Paint) - 가장 큰 콘텐츠가 렌더링 되는 시간을 의미한다.
- CLS(Cumulative Layout Shift) - Visual stablity 즉, 시각적인 안정성을 측정한 점수를 의미한다.

![weight](https://user-images.githubusercontent.com/35620465/100885828-71285580-34f6-11eb-8e3f-eaa1aa38bc22.png)

위 사진을 보면 각각의 지표들은 얼마의 가중치로 계산되어 점수가 측정되는지 알 수 있다.  
각각의 Metrics 는 서로 연관되어 있는것 같다. 사용자가 웹에서 상호작용을 할 수 있는데 까지 걸리는 시간을 줄이려면(TTI) 웹을 로딩할 때 Blocking 되는 시간의 총 합을 줄여야 할 것으로 보인다.(TBT) 또한, TBT를 줄이면 FCP, LCP, SI 등에도 좋은 영향을 줄 수 있는것으로 보인다. CLS 는 가중치 비율이 5%인 것을 보면 유추할 수 있듯이 웹 렌더링 속도에 큰 영향은 주지 않는것 처럼 보인다.

## Opportunities

![opportunities](https://user-images.githubusercontent.com/35620465/100890137-4260ae00-34fb-11eb-9234-2bff11824797.png)

Performance 지표에서는 Opportunity 라는 항목으로 어떻게 하면 웹 페이지의 렌더링 속도를 개선시킬 수 있는지에 대한 설명도 함께 나와 있다.  (하지만 성능 점수에는 직접적인 영향은 주지 않는다고 한다.)

### 1. Remove unused JavaScript  

![unused](https://user-images.githubusercontent.com/35620465/100895726-38da4480-3501-11eb-996b-12e5e9e60f2f.png)
Lighthouse는 사용하지 않은 코드가 20KB 이상인 모든 JavaScript 파일을 표시한다.   
사용하지 않는 Javascript 코드는 페이지 로드 속도를 느리게 할 수 있다. 왜냐하면 브라우저가 페이지를 로드하는 과정에서 Javascript 코드를 만나면 렌더링에 필요한 작업을 진행하기 전에 스크립트를 다운로드 하고 해석, 구문 분석, 컴파일 등 시간을 소요하기 때문이다. JavaScript가 비동기 코드인 경우에도 코드를 다운로드하는 동안 다른 리소스와 대역폭을 두고 경쟁하므로 성능에 상당한 영향을 미친다. 네트워크를 통해 사용하지 않는 코드를 보내는 것은 무제한 데이터 요금제가 없는 모바일 사용자에게도 낭비라고 한다.  
개선 방법으로는 사용하지 않는 Javascript를 제거하기 위해 Chrome DevTools 의 Coverage 탭 에서는 사용하지 않는 코드를 한 줄씩 분석 할 수 있다.
한가지 의문인 점은 만약 유틸함수 같은 공톰 함수를 어떤 페이지에서는 사용하고, 어떤 페이지에서는 사용하지 않을 때, 사용하지 않는 페이지에서 coverage 분석을 돌려볼 경우 사용하지 않는 코드라고 나올까?

### 2. Preload key requests  

![preload](https://user-images.githubusercontent.com/35620465/100898219-dcc4ef80-3503-11eb-868f-6230b191e36b.png)
Lighthouse는 나중에 요청되는 리소스를 ```<link rel=preload>``` 를 사용해서 사전에 먼저 로드 되도록 지정해두라고 제안한다.
index.html  
|--app.js  
|--styles.css  
|--ui.js  
만약 파일구조가 위처럼 되어 있고 ```<script src="app.js">```를 통해 app.js가 실행 되면 다운로드, styles.css 및 ui.js 파일이 처리된 후 마지막에서야 리소스가 다운로드 된다. 만약 여기까지 걸리는 시간이 200ms 가 소요되었다면, preload로 리소스를 지정해두면 200ms 를 절약할 수 있는 것 이다.

### 3. Serve images in next-gen formats  

![image-formats](https://user-images.githubusercontent.com/35620465/100899614-60cba700-3505-11eb-8361-5e1301e2f012.png)
Lighthouse 는 위 사진에서 알 수 있듯이 png, jpeg 이미지 보다는 JPEG 2000, JPEG XR, [WebP](https://developers.google.com/speed/webp/) 를 사용할 것을 제안하고 있다.  
JPEG 2000, JPEG XR 및 WebP는 우수한 압축 및 품질을 가진 이미지 형식이기 때문에 이미지가 더 빨리 로드되고 데이터 소비를 줄일 수 있다고 한다.

### 4. Preconnect to required origins  

![preconnect](https://user-images.githubusercontent.com/35620465/100903436-3f6cba00-3509-11eb-936c-95429f0f5af2.png)  
Lighthouse는 외부 출처 url을 preconnect로 연결해 줄 것을 제안하고 있다.  
```<link rel="preconnect">``` 를 사용하면 페이지가 외부 다른 링크에 대한 연결을 설정하고 프로세스가 가능한 한 빨리 시작되도록 브라우저에 알려준다.  외부 링크를 연결 했을때는 DNS 조회, 리디렉션 및 사용자의 요청이 서버와 여러 번 통신이 될 수 있기 때문에 느린 네트워크에서, 특히 보안 연결과 관련하여 상당한 시간이 소요된다고 한다.  
그래서 이 모든 것을 미리 처리하면 대역폭 사용에 부정적인 영향을 주지 않고 애플리케이션이 사용자에게 훨씬 더 빠르게 느껴질 수 있다.  
해결 방법은 페이지에 링크 태그를 추가만 해주면 된다.  
```<link rel="preconnect" href="https://example.com">```  

### 5. Eliminate render-blocking resources  

![render-blocking](https://user-images.githubusercontent.com/35620465/100904063-f6693580-3509-11eb-8e67-fee80f4ba25c.png)  
마지막으로 이 섹션에서는 blocking 하는 스타일 url 을 알려준다. 가이드 문서에 따르면 중요한 리소스는 인라인 형태로 작성하고 중요하지 않은 리소스는 사용을 뒤로 미루고 사용하지 않는 모든 리소스는 제거하여 이러한 렌더링 blocking의 url을 줄여야 한다고 제안하고 있다.  
여기서는 어떤 url이 blocking 된다고 표시될까? 가이드 문서에 따르면,  
1. Does not have a defer attribute. (```<script>```에서 defer 속성이 없는 태그)
2. Does not have an async attribute. (```<script>```에서 async 속성이 없는 태그)  

는 Lighthouse 에서 차단 url 이라고 표시한다고 한다.

### Diagnostics
![diagnostics](https://user-images.githubusercontent.com/35620465/100906105-26193d00-350c-11eb-8d9e-53c745a77cbe.png)  

또한, Lighthouse를 통해 Diagnostics 섹션에서 각종 웹 애플리케이션의 Performance 정보를 다양하게 찾아볼 수도 있다.  

### 참고  
1. https://web.dev/performance-scoring/?utm_source=lighthouse&utm_medium=devtools
2. https://web.dev/uses-rel-preload/?utm_source=lighthouse&utm_medium=devtools
3. https://web.dev/render-blocking-resources/?utm_source=lighthouse&utm_medium=devtools
4. https://web.dev/unused-javascript/?utm_source=lighthouse&utm_medium=devtools
5. https://web.dev/uses-rel-preconnect/?utm_source=lighthouse&utm_medium=devtools
6. https://developers.google.com/web/tools/lighthouse?hl=ko