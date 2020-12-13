---
title: 필드에서의 웹 바이탈 측정 모범 사례
date: 2020-12-13 00:00:00
author: symoon
category: S2_Round3
---

[Best practices for measuring Web Vitals in the field]
# 필드에서의 웹 바이탈 측정 모범 사례
###### 필드 : 개발 테스트 환경이 아닌 실제 사용자들이 사용하는 환경[(참고)](https://web.dev/user-centric-performance-metrics/#in-the-field)

## 들어가며
페이지의 실제 성능을 측정하고 리포트 하는 것은 추후 웹사이트 성능 진단 및 개선에 매우 중요하다. 그러나 필드 데이터 없이는  웹사이트에 적용한 변경사항이 실제로 원하는 결과를 얻을 수 있을지 확실하게 알 수 없다. 이 번 발표에서는 현업에서 사용중인 분석 도구를 통해 Core Web Vitals 지표를 측정하는 모범 사례에 대해 알아본다. 

1. 사용자 지정 지표 또는 이벤트 사용하기
2. 분포를 보고할 수 있는지 확인하기
3. 적절한 시점에 데이터 전송하기
4. 시간 경과에 따른 성능 모니터링하기
5. 측정이 성능에 영향을 미치지 않는지 확인하기

### RUM(Real User Monitoring) 
> **RUM이란?** 
>
> * 웹 어플리케이션 관점이 아닌 실제 접속한 사용자의 관점에서 최종 사용자 경험을 기반으로 성능을 측정하는 기법 
> * 사용자의 접속 경로, 환경 등의 데이터를 기반으로 사용자 경험을 개선할 수 있음
>
> [참고](https://en.wikipedia.org/wiki/Real_user_monitoring)

여러 RUM 분석 업체들에서는 이미 Core Web Vitals 지표 측정을 지원하고 있다. 이런 도구를 사용 중이라면, 웹사이트가 권장하는 Core Web Vitals 지표를 얼마나 충족하고 있는지 평가할 수 있다.

그러나 사용중인 도구가 해당 기능을 지원을 하지 않는다고해서 분석 도구를 변경할 필요는 없다. 기존에 사용하는 분석 도구를 이용해서 Core Web Vitals를 측정하는 모범사례에 대해 알아볼 것이다.


## 사용자 지정 지표 또는 이벤트 사용하기
대부분 RUM 도구는 사용자 정의 데이터를 측정할 수 있다. 사용중인 분석 툴이 이 기능을 지원한다면, 이 매커니즘을 통해 Core Web Vitals 지표 측정이 가능하다.

**일반적인 3단계 프로세스**
1. (필요한 경우) 도구 관리자에서 사용자 지정 지표를 정의하거나 등록한다.
2. 프론트엔드 자바스크립트 코드에서 지표 값을 계산한다.
3. (역시 필요한 경우) 계산한 값을 분석 백엔드로 보내서, 이름 또는 ID가 1단계에서 정의한 내용과 일치하는지 확인한다.


##### * 1단계와 3단계의 경우, 분석 도구 가이드 문서를 참조 [(구글애널리틱스 문서 참고)](https://support.google.com/analytics/answer/2709829?hl=en&ref_topic=2709827)
![GA 사용자 정의 이벤트 등록](https://www.conversion-uplift.co.uk/wp-content/uploads/2020/07/Setting-up-custom-metric-in-Google-Analytics-768x328.png)

##### * 2단계는 web-vital Javascript 라이브러리를 사용 [(링크)](https://github.com/GoogleChrome/web-vitals)

예제코드
   
    import {getCLS, getFID, getLCP} from 'web-vitals';

    function sendToAnalytics({name, value, id}) {
      const body = JSON.stringify({name, value, id});
      // `navigator.sendBeacon()`를 쓸 수 없을 때는 `fetch()` 사용
      (navigator.sendBeacon && navigator.sendBeacon('/analytics', body)) ||
          fetch('/analytics', {body, method: 'POST', keepalive: true});
    }

    //지표 값이 사용가능하고, 보고할 준비가 되었을 때 실행됨
    getCLS(sendToAnalytics);
    getFID(sendToAnalytics);
    getLCP(sendToAnalytics);

##### * 사용자가 페이지와 상호작용하지 않으면 FID가보고되지 않음
##### * 페이지가 백그라운드에서 로드된 경우 FCP, FID 및 LCP가 보고되지 않음
##### * 각 메트릭 인스턴스에 대한 ID를 제공하므로 대부분의 분석 도구에서 배포를 쉽게 구축 할 수 있음


## 분포를 보고할 수 있는지 확인하기
다음으로는 수집된 데이터로 보고서 또는 대시보드를 만드는 것이다.
권장 [Core Web Vitals 기준치](https://web.dev/vitals/#core-web-vitals)를 충족하는지를 확인하기 위해서는 백분위의  75번째 지점에서 각 지표의 값이 표기되는 보고서가 필요하다.

만약 분석 도구가 기본 제공 기능으로 분위수보고를 제공하지 않는 경우 오름차순으로 정렬된 모든 지표 값을 나열하는 보고서를 생성하여이 데이터를 수동으로 가져올 수 있다. 이 보고서가 생성되면 해당 보고서에 있는 모든 값을 정렬하여 전체의 75% 지점의 결과가 해당 측정 항목의 75번째 백분위 수가 된다. 

또한 분석도구에서 세분화된 측정항목을 제공하지 않을 때 맞춤 측정 항목 기능을 제공하면 동일한 결과를 얻을 수 있다.[(참고)](https://www.conversion-uplift.co.uk/wp-content/uploads/2020/07/Setting-up-custom-metric-in-Google-Analytics-768x328.png)

아래의 그래프는 위에서 설명한 기능을 통해 Google Analytic에서 생성한 것이다. (GA는 표준 보고서에서 분위수 보고를 지원하지 않는다.)

![GA 생성 보고서](https://webdev.imgix.net/vitals-field-measurement-best-practices/lcp-histogram.png)

## 적절한 시점에 데이터 전송하기
일부 성능 지표는 페이지가 로드되고 나서 계산되지만, CLS(Cumulative Layout Shift) 같은 다른 지표들은 페이지 전체 수명을 고려하여 페이지 언로드가 시작한 후 최종적으로 계산된다. 

하지만 `beforeunload`나 `unload` 이벤트 모두 (특히 모바일에서) 신뢰할 수 없고, Back-forward Cache 적합성 문제로 권장하지 않기 때문에 문제가 될 수 있다.

> **Back-forward Cache**
>
> 뒤로 및 앞으로 버튼을 더 빠르게 사용하도록하는 일부 브라우저에서 구현하는 탐색 최적화를 설명하는 데 사용되는 용어입니다. 사용자가 페이지를 벗어나면 이러한 브라우저는 해당 페이지의 버전을 고정하므로 사용자가 뒤로 또는 앞으로 버튼을 사용하여 뒤로 이동할 경우 빠르게 다시 시작할 수 있습니다. beforeunload또는 unload 이벤트 핸들러를 추가하면 이 최적화가 가능하지 않습니다.

페이지의 전체 수명을 추적하는 지표는, `visibilitychange` 이벤트 실행 중 값이 hidden으로 변경될 때마다, (현재 값이 무엇이든) 지표 값을 전송하는게 가장 좋은 방법이다. visibility가 `hidden`으로 변경되면 해당 페이지의 스크립트가 다시 실행될 수 있다는 보장이 없기 때문이다. 이것은 특히 콜백을 실행하지 않고 브라우저 앱자체를 닫을 수 있는 모바일에서 더욱 그렇다. 

모바일에서는 탭 전환/닫기, 앱 전환/닫기, 새 페이지로 이동시 `visibilitychange` 이벤트를 발생시킨다. 이 때문에 `beforeunload`나 `unload` 보다 `visibilitychange`가 더 안정적이라고 할 수 있다. 


##### * 일부 브라우저 버그로 인해 `visibilitychange` 이벤트가 실행되지 경우가 있다. 자체 분석 라이브러리를 구축하는 경우 이러한 버그를 인식하는 것이 중요하다. 참고로 Web-vital 자바스크립트 라이브러리는 이러한 모든 버그를 설명한다(?) [(web vitals)](https://github.com/GoogleChrome/web-vitals#limitations)


## 시간 경과에 따른 성능 모니터링하기
Core web vitals 지표를 추적하고 보고하는 분석 구현을 업데이트 한 뒤 다음 단계는, 변경사항이 시간이 지남에 따라 성능에 어떤 영향을 미치는지 추적하는 것이다.

### 변경사항 버전 관리
변경 사항을 추적하는 순진한 (궁극적으로 신뢰할 수없는) 접근 방식은 변경 사항을 프로덕션에 배포한 다음 배포 날짜 이후에 받은 모든 지표가 새 사이트에 해당하고 배포 날짜 이전에 받은 모든 지표가 이전 사이트에 해당한다고 가정하는 것이다. 그러나 HTTP, 서비스 워커 또는 CDN 계층의 캐싱 등 여러 요인들이 이 작업을 방해 할 수 있다.

훨씬 더 나은 접근 방식은 배포된 각 변경 사항에 대해 고유 한 버전을 만든 다음 분석 도구에서 해당 버전을 추적하는 것이다. 대부분의 분석 도구는 버전 설정을 지원한다. 그렇지 않은 경우 사용자 지정으로 버전을 설정할 수 있다.


### 실험 실행
동시에 여러 버전을 추적하여 버전 관리를 한 단계 발전시킬 수 있다. 

분석 도구에서 실험 그룹을 정의 할 수있는 경우 해당 기능을 사용하거나 맞춤 측정 기준을 사용하여 각 측정 항목 값이 보고서의 특정 실험 그룹과 연결될 수 있도록 할 수 있다.

분석에서 실험을 진행하면 일부 사용자에게 실험적 변경 사항을 적용하고 해당 변경 사항의 성능을 통제 그룹의 사용자 성능과 비교할 수 있다. 변경이 실제로 성능을 향상 시킨다는 확신이 들면 모든 사용자에게 적용 할 수 있다.

##### * 실험 그룹은 항상 서버에 정의되어야하며, 클라이언트에서 실행되는 A/B 테스트 도구를 사용하지 말아야한다. 이런 도구들은 사용자 실험 그룹이 결정될 때까지 렌더링을 차단해서 LCP 측정에 불리할 수 있다.


## 측정이 성능에 영향을 미치지 않는지 확인하기
실제 사용자에 대한 성능을 측정할 때 실행중인 성능 측정 코드가 페이지 성능에 부정적인 영향을 미치지 않는 것이 절대적으로 중요하다. 만약 그렇다면, 분석 코드 자체가 가장 큰 부정적인 영향을 미치는지 알 수 없기 때문에 성능이 비즈니스에 미치는 영향에 대해 도출하려는 결론은 신뢰할 수 없게 된다.

그러므로 프로덕션 사이트에 RUM 분석 코드를 배포 할 때 항상 다음 원칙을 따라야한다.

### 분석코드 지연로드  
분석 코드는 항상 비동기, non-bloking 방식으로 로드되어야하며, 일반적으로 가장 마지막에 로드되어야한다. bloking 방식으로 로드할 경우, LCP에 부정적인 영향을 줄 수 있다.

측정에 사용되는 모든 API들은 비동기, 지연로드 되도록 특별히 설계되어 있으므로 굳이 빨리 로드할 필요가 없다. 

페이지 로드 타임 라인 중 계산할 수 없는 측정항목 이벤트의 경우에만 먼저 실행될 수 있도록 `<head></head>`에 인라인으로 넣어주고, 나머지 코드는 defer로 실행한다. 단 한개의 지표가 필요하다고 해서 모든 분석 코드를 조기 로드하면 안된다.

### 긴 작업(long task) 생성하지 않기
분석 코드는 종종 사용자 입력에 대한 응답으로 실행되지만 분석 코드가 많은 DOM 측정을 수행하거나 다른 프로세서 집약적인 API를 사용하는 경우, 분석 코드 자체가 입력 응답성을 저하시킬 수 있습니다. 또한 분석 코드가 포함 된 JavaScript 파일이 큰 경우 해당 파일을 실행하면 기본 스레드가 차단(페이지 반응 안하는 상태)되고 FID에 부정적인 영향을 미칠 수 있다.


### non-blocking APIs 사용하기
`sendBeacon()`과 `requestIdleCallback()` 같은 API는 사용자의 중요한 작업을 방해하지 않는 방식으로 중요하지 않은 작업을 수행하도록 특별히 설계되었다. 이러한 API는 RUM 분석 라이브러리에서 사용할 수있는 훌륭한 도구이다.

### 필요한 것 이상으로 추적하지 않기
모든 데이터가 리소스로드 성능을 향상시키는 데 반드시 필요하거나 유용하지는 않을 것이다. 데이터가 존재하기 때문에 단순히 데이터를 추적하는 것이 아니라 데이터를 추적하는 리소스를 소비하기 전에 데이터가 사용되는지 확인해야한다. 





---
### 참고
https://web.dev/vitals-field-measurement-best-practices/

https://robindirksen.nl/blog/what-is-real-user-monitoring

https://m.blog.naver.com/PostView.nhn?blogId=wellconn&logNo=221509655911&proxyReferer=https:%2F%2Fwww.google.com%2F

https://developers.google.com/web/updates/2018/07/page-lifecycle-api#page-navigation-cache