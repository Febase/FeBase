---
title: 차트 라이브러리
date: 2020-11-11 00:00:00
author: junCastle
category: S2_Round1
---

# 차트 라이브러리

데이터를 시각화를 하기 위해서는 대부분 차트 라이브러리 사용을 하게 된다. 이 포스팅에서 어떤 차트 라이브러리들이 있고 각가의 장단점, 특성, 사용 환경 등을 비교해보고 알아보자.  

1. D3.js
2. C3.js
3. Chart.js
4. AmCharts

## [D3.js](https://github.com/d3/d3)

D3.js 는 현재 Github 에서 가장 많은 Star 를 받은 차트 라이브러리이다.  
데이터를 기반으로 Document 를 조작하기 위한 Javascript 라이브러리이다.  
D3 는 HTML, SVG, CSS 를 사용하여 데이터를 시각화 한다. 또한, 웹 표준에 맞춰 좋은 유연성을 보여준다고 한다.  
학습곡선이 가파르기 때문에 간단한 차트를 표현하기 위해서라도 많은 학습을 요구한다.  
D3.js 라는 책을 낸 스캇머레이라는 저자는 D3를 배우는 것을 "데이터를 불러오고, 엮어서, 문서요소를 반환, 전이시키기 위해 사용할 문법을 배우는 과정" 이라고 소개한다.  

지원 브라우저 : 파이어폭스, 크롬(크로미엄), 사파리(WebKit), 오페라, IE9

### selections

D3 는 selections 라는 접근 방식을 사용한다.

```javascript
var paragraphs = document.getElementsByTagName("p");
for (var i = 0; i < paragraphs.length; i++) {
  var paragraph = paragraphs.item(i);
  paragraph.style.setProperty("color", "blue", null);
}
```
javascript 코드로 p 태그에 color 를 blue 로 칠하고 싶을때는 위처럼 작성해야 한다.  

```javascript
d3.selectAll("p").style("color", "blue");
```
D3 를 사용하면 selectAll 메소드를 사용하여 쉽게 색을 입힐 수 있다.

```javascript
d3.select("body").style("background-color", "black");
```
또는 위처럼 select 메소드를 사용해서 개별적인 노드에 색을 입힐수도 있다.

```javascript
d3.selectAll("p")
  .data([4, 8, 15, 16, 23, 42])
    .style("font-size", function(d) { return d + "px"; });
```
데이터를 바인딩 하고 싶을 때는 위처럼 data() 에 인자를 전달해주면 된다.

### Create Chart

```javascript
chart = {
  const svg = d3.create("svg")
    .attr("viewBox", [0, 0, width, height]);

  const bar = svg.append("g")
    .attr("fill", "steelblue")
    .selectAll("rect")
    .data(data)
    .join("rect")
    .style("mix-blend-mode", "multiply")
    .attr("x", d => x(d.name))
    .attr("y", d => y(d.value))
    .attr("height", d => y(0) - y(d.value))
    .attr("width", x.bandwidth());

  const gx = svg.append("g")
    .call(xAxis);

  const gy = svg.append("g")
    .call(yAxis);

  return Object.assign(svg.node(), {
    update(order) {
      x.domain(data.sort(order).map(d => d.name));

      const t = svg.transition()
        .duration(750);

      bar.data(data, d => d.name)
        .order()
        .transition(t)
        .delay((d, i) => i * 20)
        .attr("x", d => x(d.name));

      gx.transition(t)
        .call(xAxis)
        .selectAll(".tick")
        .delay((d, i) => i * 20);
    }
  })
}
```

![D3.js](https://user-images.githubusercontent.com/35620465/98924646-69d5e380-2518-11eb-89ef-724f7cb8d0e4.png)

위 코드는 바 차트를 생성하기 위한 코드이다. 보시다시피 D3 는 svg 를 활용한다. 메소드 체이닝 형태로 작성하고 attr, selectAll, data, style, call 등 다양한 메소드를 활용해서 차트를 그리고 있다.  

### 특징
1. 메서드 체이닝 방식으로 사용한다.
2. jQuery 사용법과 유사하다.
3. 시각화 라이브러리이고, 차트와는 무관한 것도 시각화하여 표현할 수 있다.
4. 학습곡선이 가파르다. 

## [C3.js](https://c3js.org)

D3의 학습곡선을 완화 시켜주며 등장한 것이 C3.js 이다. 사용하기 복잡했던 D3.js 를 더 쉽게 사용할 수 있도록 해주는 D3 기반 차트 라이브러리이다.  
또한, D3는 조금 투박한 느낌인데 비해 C3는 hover, value 값 표현 등과 css의 사용으로 훨씬 더 세련되어진 느낌이다.  
C3 의 뜻이 Comfortable, Customizable, Controllable 이라고 하는것을 보면 D3 보다는 더 편안하다는 느낌을 받는다.  
C3 를 사용하기 위해서는 D3 도 함께 import 해주어야 한다.

지원 브라우저 : D3 지원 브라우저와 같다.

```html
<!-- Load c3.css> -->
<link href="/path/to/c3.css" rel="stylesheet">

<!-- Load d3.js and c3.js -->
<script src="/path/to/d3.v5.min.js" charset="utf-8"></script>
<script src="/path/to/c3.min.js"></script>
```

### Generate Chart

```html
<div id="chart"></div>
```
먼저 차트를 만들기 위해서 chart의 div 엘리먼트를 만들어줘야 한다.

```javascript
var chart = c3.generate({
  bindto: '#chart',
  data: {
    columns: [
      ['data1', 30, 200, 100, 400, 150, 250],
      ['data2', 50, 20, 10, 40, 15, 25]
    ]
  }
});
```
차트를 create 할 때에는 c3 의 generate 메소드를 사용하면 된다. bindto 속성에 chart 엘리먼드 id 를 넣어준다.  
data 의 column 속성에 data 값 들을 넣어준다.

```javascript
var chart = c3.generate({
  bindto: '#chart',
  data: {
    columns: [
      ['data1', 30, 200, 100, 400, 150, 250],
      ['data2', 50, 20, 10, 40, 15, 25]
    ],
    axes: {
      data2: 'y2'
    },
    types: {
      data2: 'bar'
    }
  },
  axis: {
    y: {
      label: {
        text: 'Y Label',
        position: 'outer-middle'
      },
      tick: {
        format: d3.format("$,")
      }
    },
    y2: {
      show: true,
      label: {
        text: 'Y2 Label',
        position: 'outer-middle'
      }
    }
  }
});
```
![c3.js](https://user-images.githubusercontent.com/35620465/98924474-36935480-2518-11eb-8425-794652f5d8d2.png)

위 처럼 axes, axis 를 활용 해서 축을 더 추가해줄 수도 있다. axis 내부적으로 x, y 축을 갖고 있다.  
축에는 label 속성을 사용해서 라벨 이름도 붙여줄 수 있다. types 옵션을 이용해 데이터의 차트 표현 타입을 정해줄 수 있다.  
tick 은 축에 찍히는 값을 의미하는데 format이라는 속성을 통해서 각 축에 데이터를 어떤식으로 띄울지 설정할 수 있다.  
차트 타입에는 Line Chart, Area Chart, Bar Chart, Donut Chart 등 다양한 차트들이 있다.

### 특징
1. D3 보다 사용하기 쉽다.
2. D3 보다 차트 표현? 에 더 특화되어 있는 느낌(?)

## [Chart.js](https://www.chartjs.org/)

Chart.js 도 유명한 차트 라이브러리 중 하나이다. 사용법이 직관적이고 문서화도 잘 되어 있다. D3.js 는 러닝커브가 가파른데에 비해 Chart.js 는 Javascript 만 알고 있으면 몇분 안에 쉽게 차트를 만들 수 있다.  
Canvas 를 이용하여 그리기 때문에 반응형 레이아웃에서도 문제가 없다고 한다.  
(canvas를 div 로 감싸주고나 직접 width, height를 vw, vh 등으로 지정해준다.)  

지원 브라우저 : Chrome, Firefox, Internet Explorer 11, Edge, Safari

### Creating a Chart

```html
<canvas id="myChart" width="400" height="400"></canvas>
<script>
var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
    datasets: [{
      label: '# of Votes',
      data: [12, 19, 3, 5, 2, 3],
      backgroundColor: [
        'rgba(255, 99, 132, 0.2)',
        'rgba(54, 162, 235, 0.2)',
        'rgba(255, 206, 86, 0.2)',
        'rgba(75, 192, 192, 0.2)',
        'rgba(153, 102, 255, 0.2)',
        'rgba(255, 159, 64, 0.2)'
      ],
      borderColor: [
        'rgba(255, 99, 132, 1)',
        'rgba(54, 162, 235, 1)',
        'rgba(255, 206, 86, 1)',
        'rgba(75, 192, 192, 1)',
        'rgba(153, 102, 255, 1)',
        'rgba(255, 159, 64, 1)'
      ],
      borderWidth: 1
    }]
  },
  options: {
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    }
  }
});
</script>
```

위 코드는 Chart.js 홈페이지 Introduction 섹션에 있는 가장 기본적인 코드이다. Chart.js 를 이번에 처음 보게 된 나도 코드만 보고 어떻게 흘러가는지 쉽게 파악할 수 있었다.  
일단 new 키워드로 Chart 를 생성하고 type 속성으로 차트 type 을 정할 수 있고, data 속성에 필요한 데이터들을 바인딩 할 수 있다.

### Line 차트
![line 차트](https://user-images.githubusercontent.com/35620465/98826575-3728de00-2479-11eb-853f-27e11434dc40.png)

### Bar 차트
![Bar 차트](https://user-images.githubusercontent.com/35620465/98826584-3a23ce80-2479-11eb-806c-e2188f1bb696.png)

### Radar 차트
![Bar 차트](https://user-images.githubusercontent.com/35620465/98826588-3b54fb80-2479-11eb-8917-1878149c9557.png)

etc...

### 특징
1. 비교적 쉽다.
2. 문서화가 잘 되어 있다.
3. 차트가 단순하고 간결하다.
4. 단순하고 간결한 만큼 더 복잡한 표현을 하기 위해서는 다른 라이브러리를 사용해야 한다.

## [AmCharts](https://amcharts.com)

Amcharts 도 나름 차트 라이브러리를 고려할 때 빠지지 않고 등장하는 차트 라이브러리이다.  
앞서 소개한 라이브러리 3가지와는 다르게 유료로 제공하고 있다. (amcharts 워터마크를 지우지 않고 사용하면 무료로 쓸 수 있다.)  
유료인만큼 지원 항목이 다양하다. 대부분의 차트 라이브러리가 기본 자바스크립트 언어로만 쓰여 있지만,  
AmCharts 같은 경우에는 React, Vue, Angular 에서 사용은 물론 TypeScript, 웹팩, 코도바, 폰갭 등에서의 사용 가이드도 제공하고 있다.  

### Creating a chart

```javascript
<script src="//cdn.amcharts.com/lib/4/core.js"></script>
<script src="//cdn.amcharts.com/lib/4/charts.js"></script>

<div id="chartdiv" style="width: 900px; height: 800px;"></div>

<script>
// Create chart instance
<script src="//cdn.amcharts.com/lib/4/core.js"></script>
<script src="//cdn.amcharts.com/lib/4/charts.js"></script>

<div id="chartdiv" style="width: 900px; height: 800px;"></div>

<script>
// Create chart instance
var chart = am4core.create("chartdiv", am4charts.PieChart);

// Create pie series
var series = chart.series.push(new am4charts.PieSeries());
series.dataFields.value = "litres";
series.dataFields.category = "country";

// Add data
chart.data = [{
  "country": "Lithuania",
  "litres": 501.9
}, {
  "country": "Czech Republic",
  "litres": 301.9
}, {
  "country": "Ireland",
  "litres": 201.1
}, {
  "country": "Germany",
  "litres": 165.8
}, {
  "country": "Australia",
  "litres": 139.9
}, {
  "country": "Austria",
  "litres": 128.3
}, {
  "country": "UK",
  "litres": 99
}, {
  "country": "Belgium",
  "litres": 60
}, {
  "country": "The Netherlands",
  "litres": 50
}];

// And, for a good measure, let's add a legend
chart.legend = new am4charts.Legend();
</script>

</script>
```
기본적인 차트를 생성하려고 할 때 위처럼 html 을 작성한다. c3 와 비슷하게 chart div 엘리먼트를 만들어 차트를 그린다.

### 특징
1. 유료이다.
2. 학습 곡선이 가파르다.
3. 다양한 스타일의 차트를 사용할 수 있다.
4. 자유도가 높다. (자유도가 높은 만큼 커스터마이징을 하려면 학습이 필요하다.)