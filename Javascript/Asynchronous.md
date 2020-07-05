---
title: 비동기(Asynchronous)
date: 2020-06-19 00:00:00
author: snowjang24
category: Javascript
---

# 비동기(Asynchronous)

## 여는 말

자바스크립트를 공부할 때, 비동기라는 단어를 접하는 순간이 오게 된다. 중요한 개념임에도 불구하고 비동기라는 말 자체에서 이미 좌절감을 겪는 사람들이 많다. 자바스크립트를 잘 활용하기 위해, 잘 작동하는 웹을 만들기 위해서는 필수적으로 이해해야 하는 과정이지만 그 벽이 높아 대충 이해하고 넘어가는 일이 부지기수다. 나 역시 처음에 대충 이해하고 넘어갔다. 이번 기회에 A to Z, 세부적인 이해하기 위해 이 글을 쓰려 한다.

## 비동기에 들어가기에 앞서

비동기와 동기에 대해 검색하면 가장 먼저 아래와 같은 사진을 마주치게 된다. 동기는 일이 끝나기를 기다렸다가 끝나면 다음 일을 순차적으로 처리하고, 비동기는 기다림 없이 다음 일을 바로 실행하는구나 라는 간단하게 이해했다. 하지만 그래서 자바스크립트는 동기로 작동하나? 비동기는 어디에 쓰이는 거지? 라는 의문이 든다.

![Untitled](https://user-images.githubusercontent.com/26768201/86256008-c7653580-bbf2-11ea-82e8-27c8b75e619e.png)

[Synchronous, Asynchronous](https://velog.io/@cyongchoi/%EB%B9%84%EB%8F%99%EA%B8%B0asynchronous-%EA%B0%9C%EB%85%90)

이러한 의문을 해결하기 위해 필요한 개념과 원리에 대해 알아보며 자바스크립트에서의 비동기에 대해 자세히 알아보려 한다. 가장 먼저 아래의 개념들에 대해 자세히 알아보며, 자바스크립트의 비동기에 대한 오해를 풀어보자.

- 자바스크립트는 Single Thread 기반 언어
- 자바스크립트의 브라우저와 Node에서의 동작

## 자바스크립트는 Single Thread 기반 언어

자바스크립트는 **싱글 쓰레드(Single Thread)**기반의 언어다. 쓰레드가 하나라는 말은 한번에 하나의 작업만 처리 가능하다는 뜻이다. 하지만, 우리가 자바스크립트를 사용하는 환경인 Node는 여러 개의 HTTP요청을 처리하고, 브라우저는 이벤트 처리나 애니메이션 실행 등 다양한 일을 동시에 처리한다. 마치 싱글 쓰레드가 아닌 것처럼 여러 작업을 동시에 처리한다. 마치 멀티 쓰레드처럼 작동한다.

![Untitled 1](https://user-images.githubusercontent.com/26768201/86256066-d350f780-bbf2-11ea-9460-4f6c88371697.png)

[싱글 스레드와 멀티 스레드](https://blog.lgcns.com/1084)

### 동시성과 병렬성

싱글 쓰레드와 비교 설명을 위해, 멀티 쓰레드에 대해 반드시 알고 넘어가야 하는 부분이 있다. 바로 **동시성(Concurrency)**과 **병렬성(Parallelism)**이다.

**동시성(Concurrency, 병행성이라 부르기도 함)**은 싱글 코어에서 멀티 쓰레드를 동작 시키는 방식으로 멀티 태스팅을 위해 여러 개의 쓰레드가 번갈아가면서 실행되는 성질을 뜻한다. 보통 자바와 같은 객체 지향 언어들은 멀티 스레드를 통해 동시성을 진행한다. 

**병렬성(Parallelism)**은 한 개 이상의 스레드를 포함하는 각 코어들이 동시에 실행되는 성질을 뜻한다. 멀티 코어에서 멀티 스레드를 동작시키는 방식이다. 

동시성은 동시에 실행되는 것 같지만 실제로는 그렇지 않고, 병렬성은 실제로 동시에 실행되는 차이가 있다. 결과적으로 둘 다 **멀티 쓰레드의 동작 방식**이다. 두 동작 방식의 차이에 대한 아래의 그림을 보면 이해가 빠를 것이다. 

![333333](https://user-images.githubusercontent.com/26768201/86256043-cf24da00-bbf2-11ea-9926-7f33c6b743d4.png)

### Single Thread와 Multi Thread

아래의 이미지는 싱글 쓰레드와 멀티 쓰레드의 작동 방식에 대해 잘 설명하고 있다. 여기서 Object는 쓰레드를 의미하는 것이 아니다.

![Untitled 2](https://user-images.githubusercontent.com/26768201/86256073-d3e98e00-bbf2-11ea-9054-c78888d5582a.png)

[Performance comparison of single-threaded and multi-threaded execution](https://www.researchgate.net/figure/Performance-comparison-of-single-threaded-and-multi-threaded-execution_fig2_29528663)

위의 이미지와 아래의 이미지는 함께 보면 좀 더 이해가 편하다. 각각의 차이가 명확하게 보인다.

![Untitled 3](https://user-images.githubusercontent.com/26768201/86256077-d4822480-bbf2-11ea-85eb-4b4233c60a07.png)

[Parallelism vs. Concurrency](http://www.dietergalea.com/parallelism-concurrency/)

이제 다시 돌아와서, 우리가 집중해야하는 부분은 **(a)single-threaded**와 **(b)multi-threaded(single active thread)**다. 

![Untitled 4](https://user-images.githubusercontent.com/26768201/86256079-d51abb00-bbf2-11ea-9a46-f2f654438df4.png)

[Performance comparison of single-threaded and multi-threaded execution](https://www.researchgate.net/figure/Performance-comparison-of-single-threaded-and-multi-threaded-execution_fig2_29528663)

어디서 많이 본 모양이다. 비동기와 동기... 

![Untitled](https://user-images.githubusercontent.com/26768201/86256008-c7653580-bbf2-11ea-82e8-27c8b75e619e.png)

[Synchronous, Asynchronous](https://velog.io/@cyongchoi/%EB%B9%84%EB%8F%99%EA%B8%B0asynchronous-%EA%B0%9C%EB%85%90)

일단 싱글 쓰레드, 멀티 쓰레드에 대해 이해를 했으면 다음으로 넘어가자.

## 자바스크립트의 브라우저와 Node에서의 동작

자바스크립트 엔진(V8)은 **단일 호출 스택(Single Call Stack)**을 사용한다. 요청이 들어올 때마다 요청을 하나씩 순차적으로 호출 스택에 담아 처리한다. 이 부분에서 자바스크립트가 싱글 쓰레드라는 말이 납득이 된다. 

그럼 대체 비동기 처리는 어떻게 하는 걸까? 동시성은?

이 부분을 해결하는 것이 바로 브라우저와 Node다. 브라우저와 Node의 동작 원리는 아래와 같이 도식화가 되어 있다. 자바스크립트의 동작 원리에 대해 공부할 때 자주 보던 그림이다. 아래의 이미지에서 볼 수 있듯이 `XMLHttpRequest`, `setTimeout`과 같이 비동기 호출을 하는 메서드는 모두 자바스크립트 엔진 밖의 영역에 정의되어 있다.

![Untitled 5](https://user-images.githubusercontent.com/26768201/86256082-d5b35180-bbf2-11ea-847c-d8684cdb4af5.png)

![Untitled 6](https://user-images.githubusercontent.com/26768201/86256084-d5b35180-bbf2-11ea-911f-1abe57f51fc0.png)


## 드디어 비동기!

결국 자바스크립트를 구동하는 엔진은 싱글 쓰레드가 맞고, 그 외부인 구동 환경(브라우저, Node)이 멀티 쓰레드기 때문에 비동기 처리가 가능하게 되는 것이다.

아래의 비동기 처리의 대표적인 예시를 한 번 살펴보자.

```jsx
function func1() { 
	console.log('func1'); 
	func2(); 
	return "End"
} 
function func2() { 
	setTimeout(function() { 
		console.log('func2'); 
	}, 1000); 
	func3(); 
} 
function func3() { 
	console.log('func3'); 
} 

func1();
```

결과는 아래와 같다. 실행 시 블로킹 없이 순차적으로 비동기 방식으로 호출한다.

```bash
func1
func3
"end"
func2
```

## 결론

자바스크립트 자체로만 놓고 봤을 때는 싱글 쓰레드 기반 언어이기 때문에 동기적으로 처리된다. 하지만 이 자바스크립트를 구동하는 브라우저나 Node와 함께이기 때문에 멀티 쓰레드 그 중에서 동시성을 지원하기 때문에 비동기 처리가 가능하다. 작동방식에 대해 유념하여 비동기와 관련된 Promise, async-await를 활용하면 좋을 것 같다.

## 참고

- [동시성과 병렬성](https://yolojeb.tistory.com/10)
- [테이터 홍수시대, 이제는 선택이 아닌 필수! 동시성 프로그래밍](https://blog.lgcns.com/1084)
- [동시성 관련 개념](https://medium.com/@ahaljh/%EB%8F%99%EC%8B%9C%EC%84%B1-%EA%B4%80%EB%A0%A8-%EA%B0%9C%EB%85%90-d2f3e6a62b99)
- [Parallelism vs. Concurrency](http://www.dietergalea.com/parallelism-concurrency/)
- [자바스크립트와 이벤트 루프](https://meetup.toast.com/posts/89)
- [자바스크립트는 어떻게 작동하는가: 이벤트 루프와 비동기 프로그래밍의 부상, async/await을 이용한 코딩 팁 다섯 가지](https://engineering.huiseoul.com/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8%EB%8A%94-%EC%96%B4%EB%96%BB%EA%B2%8C-%EC%9E%91%EB%8F%99%ED%95%98%EB%8A%94%EA%B0%80-%EC%9D%B4%EB%B2%A4%ED%8A%B8-%EB%A3%A8%ED%94%84%EC%99%80-%EB%B9%84%EB%8F%99%EA%B8%B0-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%98-%EB%B6%80%EC%83%81-async-await%EC%9D%84-%EC%9D%B4%EC%9A%A9%ED%95%9C-%EC%BD%94%EB%94%A9-%ED%8C%81-%EB%8B%A4%EC%84%AF-%EA%B0%80%EC%A7%80-df65ffb4e7e)
- [동기와 비동기 방식(Asynchronous processing model)](https://webclub.tistory.com/605)