---
title: FE Interview2 - event bubbling & capturing etc
date: 2020-08-05 00:00:00
author: nailerHeum
category: Interview
---

# FeBase interview2

---

### 1. 이벤트 버블링(Event Bubbling)에 대해서 설명하세요.

버블링으로 지정된 이벤트들은 먼저 해당 이벤트타겟과 트리거 되는 이벤트리스너들에게 전파됩니다. 

이후, 이벤트타겟의 부모, 그리고 그 부모를 계속 찾아올라가며 추가적인 이벤트리스너들을 트리거합니다. 

상향식 전파가 트리의 꼭대기까지 계속되고, 전파가 진행되는 중에는 캡쳐러로 등록되어있는 이벤트리스너들은 트리거되지 않습니다. 

최초 이벤트 타겟으로 부터 트리의 꼭대기까지의 경로는 이벤트의 전파가 시작되기 전에 결정됩니다. 

따라서 전파 도중에 트리구조에 변조가 발생한다면, 이벤트 플로우는 기존의 트리를 기준으로 전파됩니다. 

모든 이벤트 핸들러는 이후의 이벤트 프로파게이션을 막기 위해서 이벤트 인터페이스의  `stopPropagation` 을 호출할 수 있습니다. 

호출할 경우 동일한 이벤트 타겟에 있는 이벤트리스너들은 전파받지만, 버블링은 상위 이벤트타겟으로 가지 않고 멈춥니다.

### 2. 이벤트 캡쳐링(Event Capturing)에 대해서 설명하세요.

이벤트 캡쳐링은 이벤트리스너가 등록된 조상 이벤트타겟이 후손 이벤트타겟의 이벤트들을 후손 이벤트타겟이 트리거를 받기 전에 먼저 트리거를 받을 수 있게 하는 것을 말합니다. 

캡쳐는 트리의 꼭대기에서 (DOM level 2에서는 Document, DOM level 3에서는 Window로 명시되어 있음) 버블링과 정 반대로 진행됩니다. 

이벤트의 전파가 시작되기 전에 꼭대기부터 해당 이벤트 타겟까지의 경로가 결정됩니다. 버블링과 마찬가지로 전파 도중에 트리 구조에 변조가 발생하면 무시하고, 기존의 트리 구조의 경로를 따릅니다.

 캡쳐링을 사용하기 위해서는 `addEventListener` 에  `useCapture` 인자를  `true`로 설정하거나 `options` 인자의  `capture` 프로퍼티를 `true`로 합니다. 

캡쳐링 이벤트리스너들은 이벤트를 직접 전파받지 못하고, 상위에서 내려오는 이벤트 전파를 통해 트리거됩니다. 

```jsx
// target.addEventListener(type, listener[, options]);
target.addEventListener('click', fn, { capture: true }); 
// target.addEventListener(type, listener[, useCapture]);
target.addEventListener('click', fn, true);

options
{
	capture: boolean;
	once: boolean;
	passive: boolean;
}
```

 이벤트 델리게이션과 유사하게 볼 수 있겠지만 이벤트 캡쳐링은 후손들의 이벤트만 허용되고, 특정 이벤트타겟을 지정하지 않고, 특정 종류의 이벤트를 지정한다는 점에서 다르다고 볼 수 있습니다.

![https://www.dropbox.com/s/1x7alt30cyiiy9u/domEventFlow.svg?raw=1](https://www.dropbox.com/s/1x7alt30cyiiy9u/domEventFlow.svg?raw=1)

event dispatched in a DOM tree using the DOM event flow

### 3. "속성(Attribute)"와 "요소(property)"의 차이가 무엇인가요?

 속성은 html 문서에서 사용되고, 요소는 DOM 객체에서 사용됩니다. HTML이 파싱되어 DOM 객체를 생성하기 때문에 속성은 요소가 된다고 볼 수 있습니다. 

둘의 차이는 타입과 이름에서 나타납니다. 

프로퍼티의 값은 모든 타입이 들어갈 수 있는 반면에 속성의 값은 문자열만 허용됩니다. 

또한 프로퍼티의 이름은 대 소문자를 구분하지만 속성은 대소문자를 구분하지 않습니다. 

DOM 객체는 자바스크립트 객체처럼 행동하기 때문에 이러한 성격을 갖습니다. 

HTML 문서는 대소문자를 구분하지 않기 때문에 `getAttribute('HoMePaGe')` 와 같이 작성하여도 모두 소문자로  'homepage'로 변환되어 찾게 됩니다. 

### 4. 내장된 JavaScript 객체를 확장하는 것이 좋지 않은 이유는 무엇인가요?

내장된 Javascript 객체를 확장한다는 것은 그 객체를 사용하는 모든 객체에 영향을 준다는 것입니다. 

특정 로직을 위해서 내장 객체에 프로퍼티나 메서드를 추가시킨다는 것은 그 로직 외에 있는 다른 객체들까지도 해당 프로퍼티와 메서드를 갖게 되고, 예상하지 못한 동작을 발생시킬 수 있습니다. 

만약에 기존 프로퍼티와 메서드를 수정한다면 명확하게 그 위험성을 체험할 수 있게 됩니다. 

### Reference

- DOM level 2: events specification

    [Document Object Model Events](https://www.w3.org/TR/DOM-Level-2-Events/events.html)