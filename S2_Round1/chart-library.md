---
title: 차트 라이브러리
date: 2020-11-11 00:00:00
author: junCastle
category: S2_Round1
---

# 차트 라이브러리

데이터를 시각화를 하기 위해서는 대부분 차트 라이브러리 사용을 하게 된다. 이 포스팅에서 어떤 차트 라이브러리들이 있고 각가의 장단점, 특성, 사용 환경 등을 비교해보고 알아보자.  

1. D3.js
2. Chart.js
3. C3.js
4. AmCharts

## [D3.js](https://github.com/d3/d3)

D3.js 는 현재 Github 에서 가장 많은 Star 를 받은 차트 라이브러리이다.  
데이터를 기반으로 Document 를 조작하기 위한 Javascript 라이브러리이다.  
D3 는 HTML, SVG, CSS 를 사용하여 데이터를 시각화 한다. 또한, 웹 표준에 맞춰 좋은 유연성을 보여준다고 한다.

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

### 특징
1. 메서드 체이닝 방식으로 사용한다.
2. jQuery 사용법과 유사하다.
3. 시각화 라이브러리이고, 차트와는 무관한 것도 시각화하여 표현할 수 있다.
4. 학습곡선이 가파르다. 

## [Chart.js](https://www.chartjs.org/)

Chart.js 도 유명한 차트 라이브러리 중 하나이다. 사용법이 직관적이고 문서화도 잘 되어 있다. D3.js 는 러닝커브가 가파른데에 비해 Chart.js 는 Javascript 만 알고 있으면 몇분 안에 쉽게 차트를 만들 수 있다. Canvas 를 이용하여 그리기 때문에 반응형 레이아웃에서도 문제가 없다고 한다.  
(canvas를 div 로 감싸주고나 직접 width, height를 vw, vh 등으로 지정해준다.)


### Creating a Chart

```javascript
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


## C3.js

## AmCharts
