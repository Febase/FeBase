---
title: LCP
date: 2020-12-10 19:00:00
author: wooooooood
category: S2_Round3
---

**페이지 로딩 시점에 사용자 경험을 측정할 수 있는 지표가 있을까?**
```
* Metric: System / Standard of measurement
```
`load` 또는 `DOMContentLoaded`같은 metric들은 사용자가 화면에서 보는 것과 같지 않을 수 있어 부적절한 접근이다.

`First Contentful Paint (FCP)`는 최초로 렌더링된 element의 로딩 시간을 의미하므로, 만약 Splash screen이나 Loading indicator가 최초 element인 경우에 이는 사용자에게 큰 의미가 없다.

`First Meaningful Paint (FMP)` 또는 `Speed Index (SI)`와 같은 metric들은 복잡하고 잘못된 경우도 있어 페이지의 main content의 로딩 시점을 식별하기는 어렵다.

<br />

# What is LCP?

`Largest Contentful Paint (LCP)`: 하나의 Performance metric으로, Viewport에서 가장 큰 이미지 또는 텍스트 블록이 시각적으로 렌더링되는 **시간**을 나타낸다.

빠른 LCP는 사용자에게 있어 **Useful**한 페이지임을 의미한다.

![https://webdev.imgix.net/vitals/lcp_4x3.svg](https://webdev.imgix.net/vitals/lcp_4x3.svg)

### **What is a good LCP score?**

페이지 로딩 시작 후 **2.5 초** 이내  
페이지의 75%정도 로딩되었을 때 내에는 나타나는 게 좋다  
*To ensure you're hitting this target for most of your users, a good threshold to measure is the **75th percentile** of page loads, segmented across mobile and desktop devices.*

<br />

**What elements are considered for now?**

- `<img>` elements
- `<svg>` element 안의 `<image>` elements (현재 `<svg>` element는 LCP로 측정되지 않는다)
- `<video>` elements의 썸네일
- `url()` 을 사용하여 background image를 로딩하는 element
- text nodes 또는 다른 inline-level text elements children을 가진 [Block-level](https://developer.mozilla.org/en-US/docs/Web/HTML/Block-level_elements) elements

<br />

### **How is an element's size determined?**

**Viewport 내**에서 사용자에게 **보여지는** element의 크기를 의미하며, Viewport를 벗어나거나 보이지 않는 경우는 제외된다.

Ex. 렌더링되었으나 다른 element에 의해 viewport에서 벗어나는 경우 LCP로 간주하지 않음

![https://miro.medium.com/max/700/1*j3m4HKPMffDfTqY-xKd1-w.png](https://miro.medium.com/max/700/1*j3m4HKPMffDfTqY-xKd1-w.png)

이미지의 크기가 리사이즈되는 경우에는 Intrinsic size와 Visible size 중 작은 사이즈로 측정된다.
```
* Intrinsic size: Elements' size depends on content size
* Extrinsic size: Elements' size (using width or height) with explicit values
```
Text element의 경우 내부의 모든 Text node의 크기로 측정된다
```
* Node: any DOM object
* Element: one specific type of node

Ex. document.getElementById("test") 는 **하나**의 node만 반환하며, one specific type of node이므로 element임이 보장된다.
```
모든 Text node는 자신의 [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Containing_block)을 생성하는 element에 속한다.

CSS로 설정된 margin, padding, border는 고려되지 않는다.

<br />

**When is largest contentful paint reported?**

페이지의 가장 큰 element는 페이지가 자주 로드됨에 따라 변경될 수 있다. 따라서 browser는 최초의 프레임을 렌더링할 때부터 LCP의 [PerformanceEntry](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceEntry) 를 dispatch하며,  이후 프레임을 렌더링할때마다 LCP가 변경되면 또다른 `PerformanceEntry` 를 dispatch한다.
```
* Performance Entry: Performance timeline에 나타나는 단일 Performance metric을 캡슐화한 객체
* Dispatch: Action을 발생시키는 행위
```
Ex. 최초 LCP는 최상단의 Text block이었으나, 페이지가 로딩됨에 따라 새로운 PerformanceEntry가 dispatch되고, 최종적으로 이미지 element를 가리킨다.

![https://webdev.imgix.net/lcp/lcp-cnn-filmstrip.png](https://webdev.imgix.net/lcp/lcp-cnn-filmstrip.png)

Element가 DOM에서 제거되거나 리소스(`img.src`)가 변경되는 등의 변화가 일어나면 해당 Element는 LCP 대상에서 제외된다. ([DOM에서 제거된 element들도 LCP후보로 남기는 것에 대해 논의중이다](https://github.com/WICG/largest-contentful-paint/issues/41#issuecomment-583589387))

Browser는 사용자가 페이지 상에서 tap, scroll, keypress등의 action을 취할 때 더이상 새로운 PerformanceEntry를 만들지 않는다. 사용자의 action은 대부분 사용자에게 보여지는 화면을 변화시키기 때문이다. (주로 scrolling)

**Caution:** 사용자가 background tab에서 페이지를 여는 경우에는 tab에 다시 focus되기 전까지 LCP를 측정하지 못할 수 있다. (이러한 경우에는 최초 로딩 후 오랜 시간 뒤로 측정된다)

<br />

### **How are element layout and size changes handled?**

Element의 크기나 위치가 변경되는 것으로는 새로운 LCP후보를 만들지 않는다. viewport 내에서의 최초 크기와 위치만 고려된다. 

- off-screen에서 render된 후 on-screen으로 변경: LCP후보가 될 수 없음
- on-screen에서 render된 후 off-screen으로 변경: 초기에 viewport 내에 있을 때의 크기로 LCP후보에 report된다

Ex. 레이아웃이 변경되면서 최초의 LCP를 나타낸 element가 viewport에서 제거된다.

![https://webdev.imgix.net/lcp/lcp-techcrunch-filmstrip.png](https://webdev.imgix.net/lcp/lcp-techcrunch-filmstrip.png)

Ex. 항상 가장 큰 content가 마지막에 로딩되는 것은 아니다.

- 아래 예시에서 가장 첫 화면의 회색 로고가 LCP후보(Green box)가 아닌 이유는 뭘까? `<svg>` element이기 때문이다!

![https://webdev.imgix.net/lcp/lcp-instagram-filmstrip.png](https://webdev.imgix.net/lcp/lcp-instagram-filmstrip.png)

Ex. 가장 큰 element가 사진이나 로고보다 먼저 나타나는 경우도 있다.

![https://webdev.imgix.net/lcp/lcp-google-filmstrip.png](https://webdev.imgix.net/lcp/lcp-google-filmstrip.png)

<br />

# How to measure LCP

### **Field tools** (After release)

- [Chrome User Experience Report](https://developers.google.com/web/tools/chrome-user-experience-report)
- [PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/)
- [Search Console (Core Web Vitals report)](https://support.google.com/webmasters/answer/9205520)
- [web-vitals JavaScript library](https://github.com/GoogleChrome/web-vitals)

### **Lab tools** (Before release)

- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/)
- [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
- [WebPageTest](https://webpagetest.org/)

### **Measure LCP in JavaScript**

1. [Largest Contentful Paint API](https://wicg.github.io/largest-contentful-paint/)

Ex. LCP Entry를 listen하는 [PerformanceObserver](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceObserver) 를 통해, LCP Entry가 생성될 때 Entry를 로깅한다. 즉 콘솔에 나타난 LCP Entry들은 LCP 후보들이며 일반적으로 마지막 Entry의 `startTime` 을 LCP 값으로 본다.

```jsx
new PerformanceObserver((entryList) => {
  for (const entry of entryList.getEntries()) {
    console.log('LCP candidate:', entry.startTime, entry);
  }
}).observe({type: 'largest-contentful-paint', buffered: true});
```

단, 위 예제를 통해 확인할 수 있는 모든 LCP Entry가 LCP를 측정하는 데에 유효한 것은 아니다. 

- API는 background tab의 element들도 LCP Entry로 등록하기 때문에 부적절하다.
- 또한 페이지가 [back/forward cache](https://web.dev/bfcache/#impact-on-core-web-vitals)에 의해 변경될 때의 LCP가 고려되지 않는다.
- iframe 내부의 element를 고려하지 않는다.

2. [web-vitals JavaScript library](https://github.com/GoogleChrome/web-vitals) 

```jsx
const getLCP = (onReport: ReportHandler, reportAllChanges?: boolean) => {
  const firstHidden = getFirstHidden();
  let metric = initMetric('LCP');
  let report: ReturnType<typeof bindReporter>;

  const entryHandler = (entry: PerformanceEntry) => {
    // The startTime attribute returns the value of the renderTime if it is not 0,
    // and the value of the loadTime otherwise.
    const value = entry.startTime;

    // If the page was hidden prior to paint time of the entry,
    // ignore it and mark the metric as final, otherwise add the entry.
    if (value < firstHidden.timeStamp) {
      metric.value = value;
      metric.entries.push(entry);
    }

    report();
  };

  const po = observe('largest-contentful-paint', entryHandler);

  if (po) {
    report = bindReporter(onReport, metric, reportAllChanges);

    const stopListening = () => {
      if (!finalMetrics.has(metric)) {
        po.takeRecords().map(entryHandler as PerformanceEntryHandler);
        po.disconnect();
        finalMetrics.add(metric);
        report();
      }
    }

    // Stop listening after input. Note: while scrolling is an input that
    // stop LCP observation, it's unreliable since it can be programmatically
    // generated. See: https://github.com/GoogleChrome/web-vitals/issues/75
    ['keydown', 'click'].map((type) => {
      addEventListener(type, stopListening, {once: true, capture: true});
    });

    onHidden(stopListening, true);

    onBFCacheRestore((event) => {
      metric = initMetric('LCP');
      report = bindReporter(onReport, metric, reportAllChanges);
      requestAnimationFrame(() => {
        requestAnimationFrame(() => {
          metric.value = performance.now() - event.timeStamp;
          finalMetrics.add(metric);
          report();
        });
      });
    });
  }
};

// Measure and log LCP as soon as it's available.
getLCP(console.log);
```

cross-origin iframes 등의 일부 경우에는 LCP측정이 불가능하다. `web-vitals` library의 [limitations](https://github.com/GoogleChrome/web-vitals#limitations) 참고.

<br />

### **What if the largest element isn't the most important?**

가장 중요한 element가 가장 큰 element가 아닌 경우도 있다. 이러한 element를 측정하고자 할 때는 [Element Timing API](https://wicg.github.io/element-timing/) 를 사용할 수 있다.

<br />

# How to improve LCP

LCP에 영향을 주는 요인들:

- Slow server response times
- Render-blocking JavaScript and CSS
- Resource load times
- Client-side rendering

더 자세한 내용은? [Optimize LCP](https://web.dev/optimize-lcp/)

- [Apply instant loading with the PRPL pattern](https://web.dev/apply-instant-loading-with-prpl)
- [Optimizing the Critical Rendering Path](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/)
- [Optimize your CSS](https://web.dev/fast#optimize-your-css)
- [Optimize your Images](https://web.dev/fast#optimize-your-images)
- [Optimize web Fonts](https://web.dev/fast#optimize-web-fonts)
- [Optimize your JavaScript](https://web.dev/fast#optimize-your-javascript) (for client-rendered sites)

<br />

## Reference

- [https://medium.com/speedrank-app/new-performance-metric-what-is-largest-contentful-paint-dc784a497dd5](https://medium.com/speedrank-app/new-performance-metric-what-is-largest-contentful-paint-dc784a497dd5)
- [https://web.dev/lcp/](https://web.dev/lcp/)
- [https://stackoverflow.com/questions/9979172/difference-between-node-object-and-element-object](https://stackoverflow.com/questions/9979172/difference-between-node-object-and-element-object)