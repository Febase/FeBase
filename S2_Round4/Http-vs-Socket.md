---
title: Http-vs-Socket
date: 2021-03-11 19:00:00
author: wooooooood
category: S2_Round4
---

네트워크를 통한 서버와의 통신 방식은 크게 **http통신**과 **socket통신**으로 나뉜다.

# 1. http 통신

![Http](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/fb7f725b-33d6-40e6-ad4b-5108bc89abcc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210311T134032Z&X-Amz-Expires=86400&X-Amz-Signature=31611b8ceefeb2e68a27865e5115ae6c97c05e7748c310bb161744aee0abe855&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

Client의 요청(Request)이 있을 때만 Server가 응답(Response)하는 단방향 통신으로, 응답을 받고나면 연결이 종료된다.

ex. 버튼 클릭 시 선택된 컨텐츠 보여주기

## REST?

- REpresentational State Transfer
- Request에 따른 API를 구조화하는 가장 표준화된 방법으로, Http 방식에 기반을 둔다
- `Statetlessness`: Client와 Server가 서로의 State를 알 필요가 없다 (Client와 Server가 분리되어 있어 각 부분에서 코드가 변경되어도 서로에게 영향이 없다)

### **Make Request from Client**

1. `HTTP verb` (Http Method / 요청 Method): 어떤 Operation?
    - GET: 특정한 또는 집합의 resource를 얻는다
    - POST: 새로운 resource를 생성한다
    - PUT: 특정 resource를 업데이트한다
    - DELETE: 특정 resource를 삭제한다
2. `Header`: Request에 대한 정보를 함께 전달
    - Accept (field): 서버에서 받을 수 있는 content의 type으로, client가 server로부터 처리할 수 없는 data는 받지 않도록 보장한다
    - **MIME Types**: Accept field에서 content type을 명시하는 옵션들. type과 subtype이 / 로 구분되어 나타난다.
        - ex. text/html, text/plain, application/json
        - 만약 client가 text/css를 요청했으나 text/plain을 받는다면 content를 인식할 수 없다.
3. `Path`: Resource가 있는 주소, 경로
    - Convention: Path의 첫 번째 부분은 복수형(Plural form)으로 나타내는 것이 이해하기 좋다.

        ex. `fashionboutique.com/customers/223/orders/12` 

4. `Body`(optional): Data를 포함한 메세지 내용

### **Send Response**

1. `Content Types`

- Server가 Client에게 data payload를 보낼 때, MIME Type의 content-type을 header에 포함해야 한다.

2. `Response Codes`

- Operation 결과에 대한 정보

[Status codes..](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

### Scenario

모든 Customer를 *GET*하기 위한 Request:

```
GET http://fashionboutique.com/customers
Accept: application/json
```

Response header 예시:

```
Status Code: 200 (OK)
Content-type: application/json
```

*POST*를 통한 신규 customer 생성:

```
POST http://fashionboutique.com/customers
Body:
{
  “customer”: {
    “name” = “Scylla Buss”,
    “email” = “scylla.buss@codecademy.org”
  }
}
```

Server에서 해당 객체에 대한 id 생성 후 아래 header로 client에게 반환:

```
201 (CREATED)
Content-type: application/json
```

*PUT*을 통해 특정 customer의 data 갱신:

```
PUT http://fashionboutique.com/customers/123
Body:
{
  “customer”: {
    “name” = “Scylla Buss”,
    “email” = “scyllabuss1@codecademy.com”
  }
}
```

id로 customer를 특정한 뒤 *DELETE*:

```
DELETE http://fashionboutique.com/customers/123
```

Response로는 Status Code 204를 반환하여 해당 id의 객체가 더이상 존재하지 않음을 전달할 수 있다.

# 2. socket 통신

![Socket](https://s3.us-west-2.amazonaws.com/secure.notion-static.com/2c755f6a-9ef4-4b94-9975-ed6a33b49582/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAT73L2G45O3KS52Y5%2F20210311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20210311T133914Z&X-Amz-Expires=86400&X-Amz-Signature=4d6b7070651de2f7399b89b03ba20081b02baa982828a06a0d9efa3196f47dd9&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22Untitled.png%22)

Client와 Server가 지정된 Port를 통해 연결되어 실시간으로 데이터를 주고받는 양방향 통신

ex. 실시간 스트리밍, 채팅, 온라인 게임

## Web socket?

- Socket 아이디어의 확장으로, http와 다르게 `ws://` 또는 `wss://` 을 사용한다.
- 2011년에 표준화되었으며, 서버↔브라우저, Peer↔Peer(P2P), 브라우저↔브라우저 사이의 데이터 교환에 유연한 프로토콜
- 서버가 항상 통신에 `open`된 상태로, 데이터는 필요할 때 즉시 브라우저로 `push`될 수 있다.
- 가장 잘 알려진 Web socket framework는 Socket.io
- `Stateful` protocol: Client와 Server중 한 쪽이 Connection을 종료하거나 끊겼을 때, 양쪽의 연결이 종료되며 그 전까지는 계속 연결되어 있다

### Example

1. WebSocket object를 생성
    - `new WebSocket(require: url, optional: protocols);`

```jsx
var exampleSocket = new WebSocket("wss://www.example.com/socketserver", "protocolOne");

console.log(exampleSocket.readyState);  //CONNECTING
console.log(exampleSocket.readyState);  //OPEN. Connection established
```

2. Server에 Data 전송

- Connection은 비동기이며, 실패하는 경우가 있으므로 Socket 생성 후 즉시 Send되지 않을 수 있다. 따라서 Event handler `onopen`으로 연결된 뒤 데이터를 전송할 수 있도록 한다.

```jsx
exampleSocket.onopen = function (event) {
  // Construct a msg object containing the data the server needs to process the message from the chat client.
  var msg = {
    type: "message",
    text: document.getElementById("text").value,
    id:   clientID,
    date: Date.now()
  };

  // Send the msg object as a JSON-formatted string.
  exampleSocket.send(JSON.stringify(msg));

  // Blank the text input element, ready to receive the next line of text from the user.
  document.getElementById("text").value = "";
};
```

3. Server에서 메세지 수신

- WebSocket은 Event-driven API이므로 메세지 수신 이벤트가 발생하면 동작을 처리할 수 있다.

```jsx
exampleSocket.onmessage = function (event) {
  var f = document.getElementById("chatbox").contentDocument;
  var text = "";
  var msg = JSON.parse(event.data);
  var time = new Date(msg.date);
  var timeStr = time.toLocaleTimeString();

  switch(msg.type) {
    case "id":
      clientID = msg.id;
      setUsername();
      break;
    case "username":
      text = "<b>User <em>" + msg.name + "</em> signed in at " + timeStr + "</b><br>";
      break;
    case "message":
      text = "(" + timeStr + ") <b>" + msg.name + "</b>: " + msg.text + "<br>";
      break;
  }

  if (text.length) {
    f.write(text);
    document.getElementById("chatbox").contentWindow.scrollByPages(1);
  }
}
```

4. Connection 종료

```jsx
exampleSocket.close();
```

# Reference

- [https://www.pubnub.com/blog/websockets-vs-rest-api-understanding-the-difference/](https://www.pubnub.com/blog/websockets-vs-rest-api-understanding-the-difference/)
- [https://www.codecademy.com/articles/what-is-rest](https://www.codecademy.com/articles/what-is-rest)
- [https://www.geeksforgeeks.org/what-is-web-socket-and-how-it-is-different-from-the-http/](https://www.geeksforgeeks.org/what-is-web-socket-and-how-it-is-different-from-the-http/)
- [https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API/Writing_WebSocket_client_applications)
