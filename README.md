# FeBase - Frontend Base

프론트 엔드 개발 지식을 위한 기본을 배우는 시간! :white_check_mark:	

<!-- 이 항목은 절대 건드리지 말 것(자동화) -->
## :file_folder: Table Of Contents
<!-- toc starts -->
<<<<<<< HEAD
### JAVASCRIPT

* [0.1 + 0.2 !== 0.3 인 이유 (ieee 754)](https://github.com/Febase/FeBase/blob/master/Javascript/JS_Number_Floating_Point.md) - 2020-07-08
* [Javascript var, let/const and Temporary Dead Zone](https://github.com/Febase/FeBase/blob/master/Javascript/JS_variable_tdz.md) - 2020-07-08
* [Javascript 스코프](https://github.com/Febase/FeBase/blob/master/Javascript/JS_Scope.md) - 2020-07-02
=======
### ETC

* [Javascript/JS_executionContextAndClosure.md](https://github.com/Febase/FeBase/blob/master/Javascript/JS_executionContextAndClosure.md) - 2020-07-12
* [Javascript/Hoisting.md](https://github.com/Febase/FeBase/blob/master/Javascript/Hoisting.md) - 2020-07-12
### JAVASCRIPT

* [Front to the ES2020](https://github.com/Febase/FeBase/blob/master/Javascript/Javascript_ES2020.md) - 2020-07-15
* [신상 ES2020 알아보기](https://github.com/Febase/FeBase/blob/master/Javascript/Javascript ES2020.md) - 2020-07-08
>>>>>>> 620aa6ac562634aa24593a115033ff7cdd986322
* [Web 기본부터 Alaboza](https://github.com/Febase/FeBase/blob/master/Javascript/JS_Web_Working_Concept.md) - 2020-07-02
* [Garbage Collector](https://github.com/Febase/FeBase/blob/master/Javascript/Garbage_Collector.md) - 2020-07-02
* [Javascript 데이터 타입](https://github.com/Febase/FeBase/blob/master/Javascript/JS_DataType.md) - 2020-06-25
* [자바스크립트 동작 원리](https://github.com/Febase/FeBase/blob/master/Javascript/JS_Basic_movement.md) - 2020-06-25
* [그냥 ES11인가 뭐시깽이 쓰면 되는거 아님?](https://github.com/Febase/FeBase/blob/master/Javascript/JS_Es6_Spec.md) - 2020-06-25
* [ES Module에 대해서](https://github.com/Febase/FeBase/blob/master/Javascript/JS_ES_Module.md) - 2020-06-25
* [비동기(Asynchronous)](https://github.com/Febase/FeBase/blob/master/Javascript/Asynchronous.md) - 2020-06-19
* [따라쟁이 셋째 JS가 지키고 싶었던 것 - Prototype](https://github.com/Febase/FeBase/blob/master/Javascript/JS_Prototype.md) - 2020-06-19
### ETC

* ["V8 엔진"](https://github.com/Febase/FeBase/blob/master/Javascript/V8_Engine.md) - 2020-07-07
* ["호이스팅"](https://github.com/Febase/FeBase/blob/master/Javascript/Hoisting.md) - 2020-06-30
* ["Javascript 기초 - JavaScript 개발한다면 JIT은 알아야JIT"](https://github.com/Febase/FeBase/blob/master/Javascript/JIT.md) - 2020-06-25
* [Javascript/JS_executionContextAndClosure.md](https://github.com/Febase/FeBase/blob/master/Javascript/JS_executionContextAndClosure.md) - 2020-07-08
* [Javascript/JS_Iterator_Generator.md](https://github.com/Febase/FeBase/blob/master/Javascript/JS_Iterator_Generator.md) - 2020-07-08
<!-- toc ends -->

## HandBook

* [FE Developer Questions](https://github.com/h5bp/Front-end-Developer-Interview-Questions/tree/master/src/translations/korean#JS-%EA%B4%80%EB%A0%A8-%EC%A7%88%EB%AC%B8)

* [Interview_Question_for_Beginner](https://github.com/JaeYeopHan/Interview_Question_for_Beginner)


## Contributors :sparkles:
<table>
    <tr>
        <td align="center">
            <a href="https://github.com/samslow">
                <img src="https://avatars1.githubusercontent.com/u/26738367?v=4" width="100;" alt="samslow"/>
                <br />
                <sub><b>Hyeonseok Samuel Seo</b></sub>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/snowjang24">
                <img src="https://avatars3.githubusercontent.com/u/26768201?v=4" width="100;" alt="snowjang24"/>
                <br />
                <sub><b>SoonHoJang</b></sub>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/nailerHeum">
                <img src="https://avatars0.githubusercontent.com/u/26620458?v=4" width="100;" alt="nailerHeum"/>
                <br />
                <sub><b>Seongheum Choi</b></sub>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/alledy">
                <img src="https://avatars3.githubusercontent.com/u/46309894?v=4" width="100;" alt="alledy"/>
                <br />
                <sub><b>Dayoung Kang</b></sub>
            </a>
        </td>
        <td align="center">
            <a href="https://github.com/jinsunee">
                <img src="https://avatars3.githubusercontent.com/u/31176502?v=4" width="100;" alt="jinsunee"/>
                <br />
                <sub><b>Jinsun Park</b></sub>
            </a>
        </td>
    </tr>
</table>

## How to

### Pull Request 이후



```bash
# 최초 1회 실행
git remote add -t [본인깃헙브랜치이름] upstream https://github.com/Febase/FeBase
```



```bash
git remote -v
# 아래와 같이 출력되어야 정상입니다.
origin	https://github.com/[본인깃헙아이디]/FeBase.git (fetch)
origin	https://github.com/[본인깃헙아이디]/FeBase.git (push)
upstream	https://github.com/Febase/FeBase (fetch)
upstream	https://github.com/Febase/FeBase (push)
```



```bash
git fetch upstream [본인깃헙브랜치이름]
git rebase upstream/[본인깃헙브랜치이름]
```


