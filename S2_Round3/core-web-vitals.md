---
title: Core Web Vitals
date: 2020-12-10 12:00:00
author: dev-owen
category: S2_Round3
---

## Web Vitals란 무엇인가

- 구글이 웹에서 좋은 사용자 경험을 전달하기 위해 통일한 가이드라인
- 구글은 이러한 지표들을 측정할 수 있는 도구들을 제공함
- 사이트 운영자가 모두 웹 성능의 구루(guru)가 될 필요는 없음
- Web Vitals는 사이트에서 중요한 것(Core Web Vitals)에만 집중할 수 있게 도움

## Core Web Vitals

- Core Web Vitals는 Web Vitals의 부분집합
- 유저 중심적인 결과를 만드는 실제 어플리케이션에서 측정이 필요한 지표들을 측정
- 매년 업데이트 됨, 2020년 기준으로 다음 3가지
    - Loading
    - Interactivity
    - Visual Stability

![img1](https://i2.wp.com/samuelschmitt.com/wp-content/uploads/2020/06/lcp-fid-cls.png?w=792&ssl=1)

## 어떠한 도구들을 사용하여 Core Web Vitals를 측정할 수 있는가

![img2](https://webdev.imgix.net/vitals-tools/Vitals-Tools1.png)

사용자 경험 최적화 여정은 다음과 같이 진행할 수가 있다.

- Search Console로 Core Web Vitals 리포트를 사용하여 사용자 그룹을 확인
- 작업이 필요한 페이지가 발견되면, PageSpeed Insights(PSI) 로 페이지를 진단하고 페이지에서 이슈를 찾는다.
- Core Web Vitals를 측정하고 실행할 수 있는 방법에 대한 가이드는 Lighthouse와 Chrome DevTools에서 제공한다.
- Core Web Vitals에 대한 대시보드는 CrUX Dashboard API나 Chrome UX Report API 로 필드 데이터를 가져오고, PSI API로 랩 데이터를 가져오면 된다.
- PR을 날릴 때 Lighthouse CI를 통하면 문제없이 Core Web Vitals를 배포 과정에서 적용할 수 있다.

각각의 도구들을 조금 더 자세하게 살펴보도록 하자

## Lighthouse

Lighthouse는 자동화된 웹사이트 심사 도구로써 개발자들이 이슈를 진단하고 웹 사이트의 사용자 경험을 개선할 기회를 찾는데 도움을 준다.

![img3](https://webdev.imgix.net/vitals-tools/lighthouse.png)

앞서 소개한 세 가지 핵심 지표 중 두 가지를 찾는 데 도움을 준다. LCP와 CLS. 그 외에도 사용자 경험을 최적화 하는데 중요한 진단 정보를 제공한다.

Total Blocking Time(TBT)라는 지표도 들어간다. 이 지표는 FID와 관련이 있다.

Lighthouse CI를 통해서 코드가 머지되고 배포되기 전에 Core Web Vitals를 측정해 볼 수 있다.

![img4](https://webdev.imgix.net/vitals-tools/lhci.png)

## PageSpeed Insights (PSI)

PSI는 페이지에 대한 랩과 필드에서의 퍼포먼스를 모바일과 데스크탑에서 보여준다. 이 도구는 실제 사용자들이 해당 페이지에 대해 어떻게 사용자 경험을 하고 있는지와 실행할 수 있는 페이지 개선 방향을 제시한다.

![img5](https://webdev.imgix.net/vitals-tools/pagespeed.png)

Search Console이 페이지들의 그룹에 대해서 설명해 주는 도구라면 PSI는 페이지 별로 성능을 향상시킬 수 있도록 기회를 제공한다. 게다가 PSI에서는 모든 Core Web Vitals에 대한 지표를 보여주고, 데이터들이 Core Web Vitals 평가를 거치는 지 안 거치는지도 블루 라벨을 통해서 표현해 준다.

## Chrome UX Report (CrUX)

CrUX는 실제 수백만 웹사이트에서의 사용자 경험을 모아놓은 공공 데이터 집합이다. Core Web Vitals의 필드 버전을 측정한다. 이러한 데이터를 통해 개발자는 전 세계의 사용자 경험에 대한 분포를 알 수 있다. 이러한 측정을 RUM(Real User Monitoring) 이라고 한다.

우리에게 사용자 데이터가 많지 않은 경우 사용할 수 있는 API가 있다. 바로 CrUX API이다. 개발자가 오리진이나 url 주소를 쿼리하면 API는 Core Web Vitals에 대한 지난 28일간의 데이터를 요약해서 보여준다.

![img6](https://webdev.imgix.net/vitals-tools/Vitals-Tools5.png)

또한 CrUX 대시보드를 통해 시계열로 오리진의 성능을 트래킹 할 수 있다. Core Web Vitals에 대한 지표를 phone desktop 나누어서 확인할 수 있다.

![img7](https://webdev.imgix.net/vitals-tools/crux-dashboard.png)

## Chrome DevTools Performance Panel

Chrome DevTools 성능 탭은 예상치 못한 레이아웃을 이동을 감지할 때 사용할 수 있다. 웹사이트의 시각적인 안정성 이슈를 측정할 때 도움이 된다. 레이아웃이 이동할 때 상세 정보를 Summary 부분에서 확인해 볼 수 있다.

![img8](https://webdev.imgix.net/vitals-tools/Vitals-Tools7.png)

아래에 나와 있는 Total Blocking Time(TBT)은 랩 도구에서 측정되는 지표로 First Contentful Paint(FCP)에서 Time to Interactive(TTI) 사이의 시간을 의미한다. 이 시간은 메인 스레드가 블락되는 시간이다. 성능 최적화는 랩에서는 TBT를, 필드에서는 FID를 향상시키는 것이다.

![img9](https://webdev.imgix.net/vitals-tools/Vitals-Tools8.png)



## Google Search Console

Search Console에서는 웹사이트에서 관심이 필요한 페이지 그룹을, CrUX 필드 데이터를 기반으로 알려준다.

![img10](https://webdev.imgix.net/vitals-tools/search-console.png)

해당 리포트는 세 가지 Core Web Vitals 지표를 기반으로 이루어졌다. LCP, FID, 그리고 CLS이다. 여기에서 Core Web Vitals 관련된 이슈가 있는 페이지를 발견하면, PSI에 가서 구체적인 최적화 제안을 받아볼 수도 있다.

## Web Vitals Extension

Core Web Vitals를 데스크탑에서 실시간으로 측정할 수 있는 크롬 익스텐션이다. 개발 과정에서 이슈를 빠르게 캐치해야 할 때 유용하게 사용할 수 있다.

![img11](https://webdev.imgix.net/vitals-tools/Vitals-Tools10.png)

## 요약

- Lighthouse는 사용자 경험을 최적화하고 Core Web Vitals를 필드에서 성공적으로 세팅하기 위해 확인하는 개발자 도구이다.
- PageSpeed Insight는 랩과 필드 Core Web Vitals 성능을 비교하는데 사용한다.
- CrUX API는 너의 오리진과 url이 지난 28일간의 Core Web Vitals를 대상으로 얼마나 잘 동작하는지 쉽게 확인할 수 있는 도구이다.
- 크롬 개발자 도구 Performance 탭에서 Core Web Vitals를 구체적으로 깊게 살펴보고 디버깅할 수 있다.
- Serach Console은 오리진이 필드에서 얼마나 잘 동작하는지 요약해준다.
- Web Vitals Extention은 실제 세계에서 Core Web Vitals에 대한 성능을 트래킹할 때 사용한다.

## 참고자료

- [https://web.dev/vitals/](https://web.dev/vitals/)
- [https://web.dev/vitals-tools/](https://web.dev/vitals-tools/)
