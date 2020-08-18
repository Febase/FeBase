---
title: Javascript 기초 - 버블 버블 버블 팝! 이벤트 버블링!
date: 2020-07-14 09:00:00
author: samslow
category: Javascript
---

- Javascript 이벤트 버블링과 이벤트캡처링 그리고 이벤트 위임에 대해 설명합니다.

# 기초가 흔들려서는 아니되오

JS 공부를 하면서 기초를 배우고 있지만 이벤트 버블링 외 2종(이벤트 캡처링, 이벤트 위임)은 JS를 배우기 시작했다면, 공부 할 수 있는 내용 중에 가장 이해도 쉽고, 내용도 상대적으로 적은 부분 중에 하나이다.

하지만, 머리로 이해하는 것과, 실제로 사용하는 것은 매우 다르다.

필자의 경우 이벤트 버블링 개념에 대해서 이해하고 있었지만, 얼마전 해커톤에서 Vanila JS로 JS 이벤트 핸들링을 개발하다가 그만 실수를 하고 말았다.

특정 아이콘이 생성하고 다른 곳을 클릭하면 삭제하여 화면에 보였다 사라지는 기능을 개발 중 이었는데

JS의 기본 이벤트 전파 방식은 이벤트 버블링인것을 알았으면서도, 문제를 파악하는데 수 시간을 삽질했다.(물론 다른 이유도 있지만) 이론과 실제가 다르고, 학교 공부와 실무는 다르며 내가 이해하는 것과 사용하는 것은 정말 다르다.

늘 이 포스트에서는 내가 아는 것 이라도 기초는 여러번 봐도 부족하다는 마음으로 따라와 주시길 바란다.

이 포스트는 내가 한 실수를 예제로 진행하려고 한다.

# JS 이벤트 핸들러 ㄷㄷㄷㅈ

![img](https://i.ytimg.com/vi/YV5OzhMaZYk/maxresdefault.jpg)

<div align="center" style="color: gray"> JS event 두둥등장!</div>

JS 의 이벤트 전파방식은 크게 2가지가 있다.

1. 이벤트 버블링 방식 Event Bubling
2. 이벤트 캡쳐 방식 Event Capture

이 중 JS의 이벤트 정책은 `Event Bubling` 방식을 따른다.

개념을 설명하기 앞서 Event Bubling은 Bottom-up방식이고, Event Captrue는 Top-Down 방식이다.

![Protecting coral reefs with bubbles](https://scx2.b-cdn.net/gfx/news/hires/2016/protectingco.jpg)

<div align="center" style="color: gray">저 방울들이 다 우리의 Event 라는 Object!</div>

이름부터 느낌이 오지 않는가, 물속에 있는 기체는 방울(Bubble)을 형성하여 부력으로 위로 뜨게되고 Event Capture는 그냥 이것의 반대라고 생각하면 외우기 쉽다.

# 등잔밑이 씨꺼매서 아무것도 안보여

![영화 신세계 황정민 선글라스](https://mblogthumb-phinf.pstatic.net/20160225_197/zzingko2273_1456380245455vLKy3_JPEG/%BF%B5%C8%AD%BD%C5%BC%BC%B0%E8%C8%B2%C1%A4%B9%CE%BC%B1%B1%DB%B6%F3%BD%BA%C5%A9%B7%D2%C7%CF%C3%F7%BC%B1%B1%DB%B6%F3%BD%BAGRANDBEAST.jpg?type=w2)

<div align="center" style="color: gray">이 짤만 보면 황정민 배우님이 "씨꺼매서 아무것도 안보여~"라고 하는게 들린다.</div>

혹시 크롬에서 드래그만으로 쉽게 번역 기능을 제공 해 주는 [Google Translation Extention](https://chrome.google.com/webstore/detail/google-translate/aapbdbdomjkkjkaonfhkkikfgjllcleb/RK%3D2/RS%3DBBFW_pnWkPY0xPMYsAZI5xOgQEE-)(이하 '구글 번역앱')을 아는가?

영어가 익숙치 않은 사람들에게 생산성과 번역 기능을 모두 제공 해 주는 혜자로운 앱이다(무료다!)

바야흐로 2020년 엔젤핵 해커톤에서 필자는 구글 번역 앱 같은 크롬 익스텐션을 개발하고 있었다.

![](https://www.dropbox.com/s/kwsml4y47yniu2l/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7%202020-07-15%2000.10.45.png?dl=1)

위 사진처럼 텍스트를 드래그하면, 구글 번역앱 아이콘이 나타나고, 이를 선택하면 한글 뜻이 나오는 동작 방식을 가지고 있다.

하지만 이상하게 버튼을 눌러도 아무 동작도 하지 않는 것이었다.

설상가상 필자의 익스텐션을 설치하면 구글 번역 아이콘까지도 뜨지 않으니,

50줄도 안되는 코드에 무슨 문제가 있겠나 싶어 크롬 익스텐션의 특별한 무언가가 있을거라 생각하고 검색을 했더랫다

알고보니 다른 이벤트에서 버블링이 일어나 아이콘 기능에까지 영향을 미치고 있었고

mouse 이벤트로 트리거 되고 있었기 때문에 다른 이벤트로 돌리고, 이벤트 전파를 막는 방향으로 현재는 잘 해결한 상태다.

이벤트 버블링은 무엇이길래 서로 다른 요소들끼리 이벤트를 주고받게 하고, 또 어떻게 주고받게 하는 것일까?

알고 있던 내용인데 실전에선 씨꺼매서 아무것도 보지 못한 맹인의 입장에서 설명을 시작한다.

# 이벤트 버블링 Event bubling

이벤트 버블링은 아래 그림으로 모두 설명이 가능하다.

![img](https://joshua1988.github.io/images/posts/web/javascript/event/event-bubble.png)

<div align="center" style="color: gray">by 캡틴팡요</div>

쉽게 말하면 버튼, div, label 등의 HTML 요소를 클릭하면 이벤트가 발생하는데, 이 이벤트는 상위의 요소들(조상 요소)로 전파되는 것을 이벤트 버블링이라고 한다. 버블링은 전파를 멈추지 않는한 무조건 최상위 객체까지 간다. 이것이 body일 수도 있고 다른 요소일 수도 있다.이것보다 더 쉽게 설명을 할 수 있을지는 모르겠다.

```js
function showIcon() {
  let icon = document.createElement("div");

  icon.addEventListener("mousedown", () => {
    icon.remove();
  });

  document.body.appendChild(icon);
}

document.addEventListener("mouseup", showIcon);
```

필자의 코드다.

icon을 create하여 event를 붙여 body의 최하단에 appendChild 하는 간단한 함수이다.

document는 우리가 보는 모든 문서이고, 여기에 `mouseup Event`가 발생하면 showIcon 함수가 동작하도록 한 것이다.

여기서 드래그한 텍스트를 추출하는 기능과 아이콘을 숨기는 코드를 추가 해 보겠다.

```js
function selectHandler(e) {
  let text = document.getSelection().toString();
  if (text !== "") {
    // 선택된 요소가 텍스트라면 아이콘을 보여주도록 한다.
    showIcon(e, text);
  }
}

function showIcon(e, text) {
  removeIcon(e); // 여기서 removeIcon을 한번 더 호출해 화면에 있는 다른 아이콘을 삭제한다.
  let icon = document.createElement("div");
  icon.id = "studyMouseIcon";

  icon.addEventListener("mousedown", () => {
    console.log("selected Text", text);
    icon.remove();
  });

  document.body.appendChild(icon);
}

function removeIcon(e) {
  const icon = document.getElementById("studyMouseIcon");
  console.log("선택된 텍스트", document.getSelection().toString());

  // e.stopPropagation 대신 텍스트가 없을때 지워지도록 했다.
  if (icon !== null && document.getSelection().toString() == "") {
    console.log("hide icon");
    icon.remove();
  }
}

document.addEventListener("mouseup", selectHandler);
document.addEventListener("mousedown", removeIcon);
```

이벤트 버블링을 막는 방법은 아주 단순하게 해당 이벤트를 전파 정지하는 `stopPropagation()`API 를 사용하면 된다.

하지만 필자는, 완전히 이벤트가 멈추는것을 바라지 않았기 떄문에 다른 방식으로 처리 해 주었다.

또 주의해서 보아야 할 것은 `mouseup`이벤트와 `mousedown` 이벤트의 차이점이다. 말 그대로 down은 누르는 단계, up은 버튼에서 손을 떼는 단계이다.

일반적인 mouse는 down과 up 이벤트가 한 세트이지만, mac의 TrackPad에서는 신기하게 터치로 누르면 down 이벤트만 발생하고, 꾹 눌렀다 떼야만 down과 up이 모두 발생한다.( 필자의 실수일 수도 있으니, 혹시 틀렸다면 댓글 남겨주세요. )

여기서 이벤트 전파를 막아주지 않으면 생성과 삭제가 동시에 이루어지기 때문에 절대 의도한대로 동작하지 않는다.

# 이벤트 캡처 Event Capture

위에서 설명한 것 처럼 이벤트 캡처는 이벤트 버블링의 반대다.

![img](https://joshua1988.github.io/images/posts/web/javascript/event/event-capture.png)

JS에서 이벤트 캡처는 특정 상황에서 옵션으로 설정 할 때만 사용 할 수 있다.

`addEventListener`의 3번째 객체에 `{captrue: true}` 를 전달 해 주면 된다.

내가 클릭한 요소의 자손 요소에게 이벤트를 Top-down으로 내려주는 방식이며, 위에서 설명한 `stopPropagation()` 을 이용하면 똑같이 전파를 막아 줄 수 있다.

다른 것들은 모두 이벤트 버를링과 같다. 아마 사용할 일은 극히 적을 것이지만 알아두어서 나쁠 것은 없다.

# 이벤트 위임 Event Delegation

아까의 코드로 잠깐 돌아가보자

```js
function showIcon(e, text) {
  removeIcon(e);
  let icon = document.createElement("div");
  icon.id = "studyMouseIcon";

  icon.addEventListener("mousedown", () => {
    console.log("selected Text", text);
    icon.remove();
  });

  document.body.appendChild(icon);
}
```

icon에 매번 `addEventListener` 를 추가해 이벤트를 트리거 해주고 있다.

여기서는 이런 방식의 코드가 낫겠지만, `<li>` 하위의 `<ul>`, `<ol>` 를 넣고 여기에도 이벤트를 달아주어야 하는 상황이라면

`<li>` 에서 이를 관리하도록 하고 `<ol>`,`<ul>` 는 이벤트를 신경쓰지 않아도 되는 가장 바람직한 코드 일 것이다.

이렇게 조상 요소에서 자식 요소의 이벤트 처리를 위임 받는 것을 이벤트 위임이라고 한다.

단, 이벤트의 종류가 모두 같다는 가정이므로 만약 list 마다 다른 요소가 적용된다면, 필자의 코드대로 동적으로 적용하는 것이 유용 할것이다.

# Self check

1. 이벤트 버블링은 (Top-down/ Bottom-up) 방식으로 일어난다.
2. 이벤트 버블링은 DOM의 모든 이벤트를 전달 할 수 있다. ( O / X )
3. 이벤트 캡처링은 이벤트를 캡쳐하는 순간 전파를 정지시킨다 ( O / X )

# Closing

이 포스트를 보았으니 이제 면접에서도 잘 대답 할 수 있어야 하고 실제 코드를 작성 할 때도 이벤트 관련해서 실수하는 일이 없어야 한다. 사실 이렇게 말은 해도 할 수 있을지는 모르곘다. 그래서 기초가 중요한 것 같다. 지루하고 뻔해도 그것을 설명하고 사용하는 것은 별개의 문제이다.

Javascript 기초는 Fun하고 Cool하게 계속 될 것이다. 기술 블로그는 계속되어야 하니깐(끄덕)

![MarvelousQueasyCavy](https://thumbs.gfycat.com/MarvelousQueasyCavy-size_restricted.gif)

# Reference

- [Captain pangyo](https://joshua1988.github.io/web-development/javascript/event-propagation-delegation/)
