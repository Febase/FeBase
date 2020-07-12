# FeBase - Frontend Base

프론트 엔드 개발 지식을 위한 기본을 배우는 시간! :white_check_mark:	

<!-- 이 항목은 절대 건드리지 말 것(자동화) -->
## :file_folder: Table Of Contents
<!-- toc starts -->
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


