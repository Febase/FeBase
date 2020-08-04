---
title: 브라우저에 데이터 저장하기
date: 2020-07-15 00:00:00
author: nailerHeum
category: Web
---



# 브라우저에 데이터 저장하기

---

### 학습 목표

1. cookie에 대해서
2. cookie와 web storage의 차이
3. localStorage와 sessionStorage 그리고 이 둘의 차이점
4. IndexedDB에 대해 간단히 살펴보기
(깊게 본다면 많이 깊게 봐야 해서 PWA 관련 내용을 다루게 된다면 따로 하나 다뤄도 될 것 같습니다.)

## 쿠키 & document.cookie

---

 쿠키는 브라우저에 저장되는 작은 크기의 문자열이다.

RFC 6265 명세에서 정의한 HTTP의 일부다.

쿠키는 웹 서버에서 HTTP 응답 헤더의 `Set-Cookie`에 내용을 넣어 전달하면 브라우저는 내용을 자체적으로 브라우저에 저장한다.

브라우저는 동일한 서버(웹 사이트)에 접속할 때마다 쿠키의 내용을 요청 헤더의 `Cookie` 에 넣어서 전달한다.

쿠키는 클라이언트의 인증에 가장 많이 사용된다.

**예시**

1. 사용자가 로그인하면 서버는 `Set-Cookie`에 담긴 session identifier 정보를 사용해 쿠키를 설정한다. 
2. 사용자가 동일한 도메인에 접속하려 하면 브라우저는 HTTP `Cookie` 헤더에 session identifier를 함께 실어 서버에 요청을 보낸다.
3. 서버는 요청의 session identifier를 읽어 사용자를 식별한다.

브라우저에서는 `document.cookie`를 통해 쿠키에 접근할 수 있다.

```jsx
document.cookie
"npic=LLFnqUQKFLo9WVboeuRiu/fnD/vTvXveDWQJsBrkpvFxYhpVInyyuWw4tVlnXTWmCA==; _ga=GA1.2.1807431803.1557712999; ASID=798b654a0000016bb5c03c0b0000005c; NM_RTK_VIEW_GUIDE=1; NID_JKL=tyNG8x1Yir+Bm7KTGU5GvhpbqR6T5NedAKKI6F13CW0=; NM_THEME_EDIT=; NM_CK_CUR_PANEL=JOB; RTK_YES=1; NV_WETR_LOCATION_RGN_M="MDk1NjAxMTA="; NV_WETR_LAST_ACCESS_RGN_M="MDk1NjAxMTA="; NRTK=ag#20s_gr#0_ma#-2_si#2_en#-1_sp#-2; NDARK=Y; NID_SES=AAABq8qmcu+HFQVRw1mUPkf8kAjs0eHX3Gw7/LIlFkRAp85KP535I7fGxp1ihQwlus28hIpARIV0tgpEd9W6JQljApUwGIvqcv7IqGJyk3ldbXU2K9/h9yqrm6pT0KTX8MC8CyWVd2BqlVoXwmn2eljD3tz44ixn+7lZRvP+vaeA7Jf0/82zgbwcn3mM516m2V+XzVVDXPwU8Vj/4U3JOihaxem9TbJrPwB86bghpiPzqxCi6e/URTkdmQDnG0O/JTPVmj3uj3VO7uM64S7ZagDPOjMvXb6gZ5ZlfAfdEPcQxDntDOAf2l+HzW+YfIOdvFBtQH/ad34rPZE18Nlo/y3KlLNY4/Km/qHGzxcffJBBDkUENxo7TAbpPe/sCyX7oet0mw7S57acWa4Ue87ctlzbGugmhXefN/wbkvgnWg2Ebs4bQbGSTKdR/2almGvvdemJ8Ni0zXrVfP8FbujdumT9Zy7fzbOUUarp2TvElc974ZTx3S+3S4eaH1s/Cs2fWhLx0gJxDOHlyg2iBf0cqnrrG2ItSXDq+5do7fWn8xX4nfR8Om2FQiD3QN/f5cyBk5JqLw=="
```

`key=value` 쌍들이 `;`로 구분되어 있다.

```jsx
console.dir(document.cookie.split(';'));
0: "npic=LLFnqUQKFLo9WVboeuRiu/fnD/vTvXveDWQJsBrkpvFxYhpVInyyuWw4tVlnXTWmCA=="
1: " _ga=GA1.2.1807431803.1557712999"
2: " ASID=798b654a0000016bb5c03c0b0000005c"
3: " NM_RTK_VIEW_GUIDE=1"
4: " NID_JKL=tyNG8x1Yir+Bm7KTGU5GvhpbqR6T5NedAKKI6F13CW0="
5: " NM_THEME_EDIT="
6: " NM_CK_CUR_PANEL=JOB"
7: " RTK_YES=1"
8: " NV_WETR_LOCATION_RGN_M="MDk1NjAxMTA=""
9: " NV_WETR_LAST_ACCESS_RGN_M="MDk1NjAxMTA=""
10: " NRTK=ag#20s_gr#0_ma#-2_si#2_en#-1_sp#-2"
11: " NDARK=Y"
12: " NID_SES=AAABq8qmcu+HFQVRw1mUPkf8kAjs0eHX3Gw7/LIlFkRAp85KP535I7fGxp1ihQwlus28hIpARIV0tgpEd9W6JQljApUwGIvqcv7IqGJyk3ldbXU2K9/h9yqrm6pT0KTX8MC8CyWVd2BqlVoXwmn2eljD3tz44ixn+7lZRvP+vaeA7Jf0/82zgbwcn3mM516m2V+XzVVDXPwU8Vj/4U3JOihaxem9TbJrPwB86bghpiPzqxCi6e/URTkdmQDnG0O/JTPVmj3uj3VO7uM64S7ZagDPOjMvXb6gZ5ZlfAfdEPcQxDntDOAf2l+HzW+YfIOdvFBtQH/ad34rPZE18Nlo/y3KlLNY4/Km/qHGzxcffJBBDkUENxo7TAbpPe/sCyX7oet0mw7S57acWa4Ue87ctlzbGugmhXefN/wbkvgnWg2Ebs4bQbGSTKdR/2almGvvdemJ8Ni0zXrVfP8FbujdumT9Zy7fzbOUUarp2TvElc974ZTx3S+3S4eaH1s/Cs2fWhLx0gJxDOHlyg2iBf0cqnrrG2ItSXDq+5do7fWn8xX4nfR8Om2FQiD3QN/f5cyBk5JqLw=="
length: 13
```

`document.cookie`에서 `cookie`는 데이터 프로퍼티가 아니라 접근자(accessor) 프로퍼티이다. 접근자 프로퍼티에 값을 할당하는 거나 접근자 프로퍼티를 읽는 것은 `getter`와 `setter`에 의해 동작이 제어된다.

### **cookie의 특징**

- `document.cookie`에 값을 할당하면 값을 받아 해당 key를 갱신하는데, 다른 쿠키들의 값이 사라지거나 변경되지 않는다.
- 쿠키는 이름과 값에 제약이 없기 때문에 모든 글자가 허용되지만, 형식의 유효성을 보장하기 위해 `encodeURIComponent`를 사용해서 이스케이프처리해줘야 한다.

### **size 관련 제약 조건 (**RFC 6265 명세와 javascript.info의 설명이 다름**)**

```
브라우저가 갖춰줘야 하는 HTTP State Management Mechanism 구현 조건
  o  At least 4096 bytes per cookie (as measured by the sum of the
      length of the cookie's name, value, and attributes).

  o  At least 50 cookies per domain.

  o  At least 3000 cookies total.
```

### **쿠키 옵션들**

- **path**

    `path=/mypath` 로 설정하면 `/mypath` 경로와 이 경로의 하위 경로에 있는 페이지만 쿠키에 접근할  수 있다. 절대경로로 지정해야 하고, 기본값은 현재 경로이다. 특별한 경우가 아니라면 `path`옵션을 루트로 설정해 모든 페이지에서 쿠키에 접근하게 만들어주는 것이 권장된다.

- **domain**

    `domain=mysite.com` 쿠키에 접근가능한 domain을 지정한다. 문제점은 이 옵션이 `[sub.mysite.com](http://sub.mysite.com)` 과 같은 서브 도메인에서도 접근이 불가능하게 만든다는 점이다. 이 옵션을 `domain=.mysite.com`으로 고쳐주면 `sub.mysite.com` 에서도 접근이 가능하다.

- **expires & max-age**

    expires나 max-age 옵션이 지정되어있지 않으면 브라우저가 닫힐 때 쿠키도 함께 사라진다. 이런 쿠키를 **session cookie**라고 한다. 브라우저는 설정된 유효 일자까지 쿠키를 유지해준다. 유효 일자는 GMT(Greenwich Mean Time) 포멧으로 설정해야 한다.

    **expires 예시**

    ```jsx
    let date = new Date(Date.now() + 1000 * 60 * 60 * 24) // 하루 뒤
    date = date.toUTCString();
    document.cookie = `expires=${date}`;
    ```

    **max-age 예시**

    ```jsx
    let date = 60 * 60 * 24;
    document.cookie = `max-age=${date}`;
    ```

- **secure**

    `secure` 옵션이 있을 경우 HTTPS로 통신하는 경우에만 쿠키가 전송된다.

    https에서 설정한 쿠키는 http에서 읽을 수 없다.

    `document.cookie = 'secure';`

- **samesite**

    CSRF(Cross-site request forgery) 공격을 막기위한 옵션이다.

- **httpOnly**

    이 옵션은 서버에서 Set-Cookie 헤더를 이용해 쿠키를 설정할 때 지정할 수 있다.

    클라이언트 측에서 `document.cookie`에 접근할 수 없어 스크립트가 쿠키를 사용할수 없게 한다.

### **GDPR**

- EU에서 사용자 개인 정보 보호를 강제하는 법령

 다양한 조항이 존재하는데, 쿠키의 경우 인증 세션과 함께 쿠키를 설정하고 id를 추척한다면 사용자의 동의를 반드시 얻어야 한다. 이때문에 보통 회원 가입 양식에 쿠키 관련 동의 내용이 존재하거나 사이트에 방문했을 때 쿠키를 허용해달라는 창을 보게 된다.

## localStorage와 sessionStorage

---

둘 다 **웹 스토리지 객체(web storage object)** 이고 브라우저 내에 key value 쌍을 저장할 수 있게 해준다. 이미 쿠키가 그 역할을 하는데 왜 이 둘이 존재할까?

- 쿠키와 달리 서버로 전송되지 않는다. 최소 2MB 이상의 용량으로 덕분에 더 많은 자료를 보관할 수 있다.
- 서버가 HTTP 헤더를 통해 조작할 수 없다. 웹 스토리지 객체에 대한 조작은 모두 자바스크립트 내에서 수행된다.
- 웹 스토리지 객체는 origin(프로토콜/도메인/포트)에 묶여있다. 
(same-origin policy)

    `Origin: <scheme> "://" <hostname> [ ":" <port> ]`

    example: `Origin: https://developer.mozilla.org`

    그래서 origin이 다르면 데이터에 접근할 수 없고, origin이 같으면 경로가 달라도 동일하게 접근할 수 있다.

두 스토리지 객체는 동일한 메서드와 프로퍼티를 제공한다.

- `setItem(key, value)`
- `getItem(key)`
- `removeItem(key)`
- `clear()`
- `key(index)`
- `length`

스토리지 객체들을 일반 객체처럼 사용할 수는 있지만, 내장 메서드를 키로 설정할 수 있어 에러가 발생할 수 있고, 객체의 데이터를 수정하면 일어나는 `storage` 이벤트가 일반 객체처럼 접근할 때는 일어나지 않기 때문에 권장되지 않는다.

### **key 순회하기**

스토리지 객체는 `iterable` 객체가 아니기 때문에 index로 접근해야 한다.

```jsx
for (let i=0; i<localStorage.length; i++) {
	let key = localStorage.key(i);
	const item = localStorage.getItem(key);
}
```

`for ... in` loop를 사용할 경우 `getItem, setItem` 같은 내장 필드도 출력되기 때문에 `hasOwnProperty`나 `Object.keys()`를 사용해서 상속받은 필드들은 출력되지 않게 하면 된다.

```jsx
for (let key in localStorage) {
	if (!localStorage.hasOwnProperty(key)) continue;
	...
}

// or 

for (let key of Object.keys(localStorage) {
	...
}
```

[localStorage와 sessionStorage의 차이](https://www.notion.so/ab167d1da5eb4a0887758b9a001b1843)

### **storage 이벤트**

properties

- `key` – 변경된 데이터의 키(`.clear()`를 호출했다면 `null`)
- `oldValue` – 이전 값(키가 새롭게 추가되었다면 `null`)
- `newValue` – 새로운 값(키가 삭제되었다면 `null`)
- `url` – 갱신이 일어난 문서의 url
- `storageArea` – 갱신이 일어난 `localStorage`나 `sessionStorage` 객체

등등

**스토리지에서 접근 가능한 `window` 객체 전부에서 이벤트가 일어난다.**

storage 이벤트는 `setItem, removeItem, clear` 를 호출할 때 발생한다.

동일한 사이트를 탭 여러 개에 띄워두고, 그 중 하나의 탭에서 localStorage를 수정하면 해당 localStorage를 공유하는 다른 탭들에서 이벤트가 발생한다. (sessionStorage의 경우 탭마다 sessionStorage를 독립적으로 갖기 때문에 의미가 없다.)

```jsx
window.onstorage = event => {
	console.log(event);
}

// or
window.addEventListener('storage', () => {
	console.log(event);
});

// StorageEvent 객체
bubbles: false
cancelBubble: false
cancelable: false
composed: false
currentTarget: Window {parent: Window, opener: null, top: Window, length: 2, frames: Window, …}
defaultPrevented: false
eventPhase: 0
isTrusted: true
key: "did you see that"
newValue: "7"
oldValue: "5"
path: [Window]
returnValue: true
srcElement: Window {parent: Window, opener: null, top: Window, length: 2, frames: Window, …}
storageArea: Storage {ShowLightNav: "true", LH::tabs: "{"s-7keqW5GbG5zc8wWQqajoAg":true}", aa: "cc", LH;;s-lZAOX6yfCoT1wAPs4avIDQ-dt-2: "p:m|l:171864_{"payload":"&v=t1&ei=lZAOX6yfCoT1wAPs…7489&me=37:1594790050267,e,H","ka":1594790050267}", cdids: "", …}
target: Window {parent: Window, opener: null, top: Window, length: 2, frames: Window, …}
timeStamp: 425112.2850000011
type: "storage"
url: "https://www.google.com/"
__proto__: StorageEvent
```

이걸 이용해서 탭들 간에 통신이 가능해진다. 예를 들어 하나의 탭에서 darkmode를 설정하면, localStorage의 darkmode를 true로 만들어 다른 탭들에서도 바로 적용이 가능하게 설정할 수도 있게 된다.

## IndexedDB

---

`IndexedDB`는 browser에 내장된 데이터베이스이고, `localStorage`보다 더 강력하다.

- 다양한 type의 key와 value들을 저장할 수 있다.
- RDBMS와 달리 고정 컬럼 테이블이 아닌 javascript 기반의 객체지향 데이터베이스이다.
- index key를 사용해 저장하고 회수한다.
- 사용하려면 데이터베이스 스키마를 지정하고, 데이터베이스와 통신을 열고 트랜잭션을 통해 데이터를 갖고 오거나 업데이트해야 한다.
- IndexedDB 작업은 모두 비동기로 이뤄진다.
- `localStorage`와 마찬가지로 특정 origin에 묶여있다. (same-origin policy)
- schema versioning이란 개념이 있어서, 사용자의 schema version이 낮다면 `open`을 사용했을 때 `upgradeneeded` 이벤트가 발생한다.

IndexedDB에서 생소한 점은 schema versioning이다.

```tsx
const dbName = 'testdb';
let version = 1;

const request: IDBOpenDBRequest = indexedDB.open(dbName, version); // db 생성 또는 기존 db 연결 version의 기본값은 1

request.onupgradeneeded = (event: IDBVersionChangeEvent) => {	// 새로 만드는 경우 or 현재 사용자의 버전이 낮은 경우 
	let db: IDBDatabase = request.result;
	if (event.oldVersion) {
    // 디비가 존재하는데 구버전인 경우
    // 새 버전으로 업데이트 해주는 작업이 필요함
  } else {
    // 디비가 존재하지 않는 경우 oldVersion에는 0이 들어와있다.
    // 디비를 초기화해주는 작업이 필요함
  }
};

request.onerror = () => { // 연결 에러 발생, 사용자가 갖고 있는 db 버전 보다 낮은 버전을 여는 시도를 해도 에러가 발생한다.
  console.log(request.error);
}

request.onsuccess = () => {
  // 해당 버전이 맞음
  // db 조작을 진행하면 됨.
}
```

version은 1부터 시작하고, 0인 경우는 해당 디비가 존재하지 않는 경우다. 사용자가 이전 버전을 갖고 있는 상태라면 새로운 버전으로 업데이트해주는 작업이 필요하다. 사용자가 갖고 있는 db 버전보다 낮은 버전을 요구하는 경우 에러를 발생시켜 사용자의 자바스크립트 코드가 오래된 경우를 잡아내준다.

### 질문

1. cookie와 web storage object의 차이점 2개
2. localStorage와 sessionStorage의 큰 차이점 1개
3. IndexedDB이 갖고 있는 특징 1개

### REFERENCE

[Storing data in the browser](https://javascript.info/data-storage)

[RFC 6265 - HTTP State Management Mechanism](https://tools.ietf.org/html/rfc6265)

[Origin](https://developer.mozilla.org/ko/docs/Web/HTTP/Headers/Origin)

[IndexedDB](https://developer.mozilla.org/ko/docs/Web/API/IndexedDB_API)