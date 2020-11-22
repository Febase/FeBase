## 👀특징

![WhaleScreenCapture-20201121-211650](https://user-images.githubusercontent.com/39721166/99877284-398cf400-2c40-11eb-8054-14a8508002bc.jpg)

- 의미: 페이지 진입 또는 현재 보여지는 화면을 기준으로 필요하지 않은 자원들은 <b>필요할 때 로드</b>
- 활용점: Pagination, Infinite Scroll, Code Splitting
- 장점  
    1.서버 부하 감소 및 사용자 속도 개선
- 단점  
    1.스크롤에 따라 이미지를 로딩하기에 부자연스럽거나 버벅이게 로딩되는 현상을 볼 수 있음  
    2.검색엔진에 걸리지 않아 SEO 취약하나 콘텐츠에 대한 링크를 제공하여 보완  
    [https://scarlett-dev.gitbook.io/all/it/lazy-loading](https://scarlett-dev.gitbook.io/all/it/lazy-loading)
- 주의사항  
[https://black7375.tistory.com/72](https://black7375.tistory.com/72)  
    1.첫 화면에는 하지 않는 것이 나음  
    &nbsp;&nbsp;( 콘텐츠 로드를 미뤄두기 때문에 SEO 좋지 않은 것으로 추정 )  
    2.스크롤을 내려야 이미지 로드를 시작해 느려보일수도 있음  
    3.자리 표시자가 없으면 레이아웃 변경이 생길 수 있음  
    &nbsp;&nbsp;( placeholder image가 없다면 브라우저 렌더링 악역향 )  
    4.JS로 이미지 크기가 큰 이미지를 로딩 시 잠시 반응하지 않을 수 있음  
    &nbsp;&nbsp;( 네트워크 환경에 따른 UX 저하 )  
    5.로드가 실패할 수 있음  
    &nbsp;&nbsp;( 네트워크 요청이 실패한 경우 placeholder image나 대체이미지가 없다면 UX 저하 )  
    6. JS를 사용하지 못할 수도 있음  
    &nbsp;&nbsp;( 브라우저의 JS 기능이 꺼있다면 동작X )

    ---
<br>
<br>
<br>

> HTML or Vanilla

### 1. loading 속성을 활용한 방식
  * img, iframe 에서 loading='lazy' 속성 사용 가능
  * 현재 실험단계
  <details>
  <summary>관련 포스팅</summary>

  [https://meetup.toast.com/posts/183](https://meetup.toast.com/posts/183)  
  [https://developer.mozilla.org/en-US/docs/Web/Performance/Lazy_loading](https://developer.mozilla.org/en-US/docs/Web/Performance/Lazy_loading)  
  [https://github.com/mfranzke/loading-attribute-polyfill](https://github.com/mfranzke/loading-attribute-polyfill)
  </details>
  <br>

### 2. preload 속성을 활용한 방식
  * video 태그에 preload=none 설정으로 로드 지연
  <details>
  <summary>관련 포스팅</summary>

  [https://web.dev/lazy-loading-video/](https://web.dev/lazy-loading-video/)  
  [https://scarlett-dev.gitbook.io/all/it/lazy-loading](https://scarlett-dev.gitbook.io/all/it/lazy-loading)
  </details>
  <br>

### 3. scroll, resize, orientationChange 이벤트를 활용한 방식
  * 코드 참고한 포스팅: [https://frontdev.tistory.com/entry/Image-Lazy-Loading-기법](https://frontdev.tistory.com/entry/Image-Lazy-Loading-%EA%B8%B0%EB%B2%95)  
  * 코드 링크: [https://codepen.io/imagekit_io/pen/MBNwKB](https://codepen.io/imagekit_io/pen/MBNwKB)
  * 링크된 코드의 동작 설명

    ```javascript
    HTML구조는 여러 개의 img 요소로 되어 있고 상단 3개의 img 요소에만 src 속성이 설정되어 있어, 초기에 3개의 이미지만 노출

    2 lazyloadImages 변수에 img.lazy 클래스명을 가진 img 요소들의 배열 할당 
    26~28 scroll, resize, orientationChange 이벤트가 발생하면, 5 lazyload 함수를 실행
    10 lazyloadThrottleTimeout 변수에 setTimeout 을 할당하여 추후 6~8 clearTimeout에 활용
    11~17 lazyloadImages 배열을 반복하며 img의 offsetTop이 window.innerHeight + scrollTop 보다 작으면 data-src에 할당된 이미지 URL을 img src 속성에 할당하고 class에서 lazy를 제거하여 이미지를 노출
    18~22 lazyloadImages가 빈 배열이면 scroll, resize, orientationChange 이벤트를 제거
    ```
<br>
<br>
<br>

> React
  ### 1. React.lazy

  * 컴포넌트 단위로 분리 가능
  * <b>라우트 단위로 도입하길 권장</b>  
    [https://ko.reactjs.org/docs/code-splitting.html#route-based-code-splitting](https://ko.reactjs.org/docs/code-splitting.html#route-based-code-splitting)

  * Img 태그에 적용한 사례  
    [https://velog.io/@ansrjsdn/React.lazy-%EC%82%AC%EC%9A%A9%ED%95%B4%EB%B3%B4%EA%B8%B0](https://velog.io/%40ansrjsdn/React.lazy-%EC%82%AC%EC%9A%A9%ED%95%B4%EB%B3%B4%EA%B8%B0)

  * 주의사항
    - 아직 SSR에서는 지원 x  
    [https://ko.reactjs.org/docs/code-splitting.html#reactlazy](https://ko.reactjs.org/docs/code-splitting.html#reactlazy)
    - Named Export 사용  
    [https://ko.reactjs.org/docs/code-splitting.html#route-based-code-splitting](https://ko.reactjs.org/docs/code-splitting.html#route-based-code-splitting)
<br>

  ### 2. react-lazyload

  * resize, scroll 기반으로 작동되는 것으로 추정
  <details>
  <summary>관련 포스팅</summary>

  [https://github.com/twobin/react-lazyload](https://github.com/twobin/react-lazyload)
  </details>
  <br>

  ### 3. react-virtualized

  * 현재 사용자에 보여지는 부분만 렌더링하여 최적화
  <details>
  <summary>관련 포스팅</summary>

  [https://github.com/bvaughn/react-virtualized](https://github.com/bvaughn/react-virtualized)  
  [https://bvaughn.github.io/react-virtualized/#/components/List](https://bvaughn.github.io/react-virtualized/#/components/List)  
  [https://coffeeandcakeandnewjeong.tistory.com/52](https://coffeeandcakeandnewjeong.tistory.com/52)
  </details>
  <br>

  ### 4. react-window

  * react-virtualized와 같은 역할이며 보다 경량화
  <details>
  <summary>관련 포스팅</summary>

  [https://react-window.now.sh/#/examples/list/fixed-size](https://react-window.now.sh/#/examples/list/fixed-size)  
  [https://velog.io/@pandati0710/React-Windowing](https://velog.io/%40pandati0710/React-Windowing)
  </details>
<br>
<br>
<br>

> Vue
  ### 1. Code Splitting with webpack

  * webpack으로 chunk 파일 분할하여 분할된 파일에 대한 요청이 들어왔을 때 서빙
  <details>
  <summary>관련 포스팅</summary>

  [https://gongzza.github.io/javascript/vuejs/vue-lazy-loading-with-webpack/](https://gongzza.github.io/javascript/vuejs/vue-lazy-loading-with-webpack/)  
  [https://router.vuejs.org/kr/guide/advanced/lazy-loading.html](https://router.vuejs.org/kr/guide/advanced/lazy-loading.html)
  </details>

  ### 2. vue-lazyload

  * resize, scroll 기반으로 동작하지만, intersection observer도 활용 가능
  <details>
  <summary>관련 포스팅</summary>

  [https://github.com/hilongjw/vue-lazyload#readme](https://github.com/hilongjw/vue-lazyload#readme)  
  </details>