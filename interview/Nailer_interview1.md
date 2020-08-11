---
title: FE Interview 2
date: 2020-07-28 00:00:00
author: nailerHeum
category: Interview
---

# FeBase 질의응답

1. **AJAX에 관해 가능한 한 자세히 설명하세요.**

   AJAX는 asynchronous Javascript XML의 약자로, XMLHttpRequest 객체, XML, HTML, CSS, Javascript, DOM 등 기존의 여러 기술들이 포함된 접근법입니다. 전체 페이지를 새로 고칠 필요 없이 UI에 빠르고 부분적인 업데이트를 적용할 수 있습니다.

   브라우저에서 특정 이벤트가 발생했을 때, XMLHttpRequest 객체를 사용하여 HTTP 요청을 서버로 보내고, 서버에서는 데이터와 함께 응답을 브라우저로 보내게 됩니다. 그리고, 브라우저에서는 데이터를 자바스크립트로 처리하여 페이지 콘텐츠를 업데이트할 수 있습니다.

2. **AJAX를 사용했을 때의 장단점에 대해 설명해주세요.**

   장점은 XMLHttpRequest객체를 통해 html 페이지 일부분만 갱신할 수 있어 비용(자원과 시간)을 줄일 수 있다는점입니다. 이를 통해 웹페이지의 속도를 향상시키고, 페이지 리로드 없이 콘텐츠를 수정할 수 있습니다.

   단점은 javascript나 XMLHttpRequest를 지원하지 않는 브라우저의 경우 AJAX를 적용할 수 없다는 점, 서버 요청이 더욱 많아진다는 점, 하나의 요청이 실패할경우 전체 페이지 로드를 실패할 수 있다는 점, 히스토리 관리가 안된다는 점이 있습니다.

3. **JSON이 어떻게 동작 되는지 설명하세요. (그리고 AJAX와 어떻게 다른지 설명하세요.)**

   JSON은 문자열을 전송받은 후에 해당 문자열을 파싱합니다. 따라서 XML과 비교했을 때 처리속도가 빠른 대신, 데이터의 무결성을 사용자가 직접 검증해야 합니다. 문자열을 파싱한다는 말은 의미있는 단위로 쪼개고(tokenizing), 쪼개진 데이터에 의미를 부여하고(lexing), 이 데이터를 구조화한다(parsing)는 뜻입니다. XML은 복잡하고, 문자량이 많아 데이터 크기가 큰데 비해 JSON은 간결하고 처리 속도가 빠릅니다. 또한 XML은 billion laughs 공격이나 external entity 공격 등 취약점이 존재합니다.

   **XML 예시**

   ```xml
   <note>
   	<to>Tove</to>
   	<from>Jani</from>
   	<heading>Reminder</heading>
   	<body>Don't forget me this weekend!</body>
   </note>
   ```

   **JSON 예시**

   ```json
   {
     "glossary": {
       "title": "example glossary",
       "GlossDiv": {
         "title": "S",
         "GlossList": {
           "GlossEntry": {
             "ID": "SGML",
             "SortAs": "SGML",
             "GlossTerm": "Standard Generalized Markup Language",
             "Acronym": "SGML",
             "Abbrev": "ISO 8879:1986",
             "GlossDef": {
               "para": "A meta-markup language, used to create markup languages such as DocBook.",
               "GlossSeeAlso": ["GML", "XML"]
             },
             "GlossSee": "markup"
           }
         }
       }
     }
   }
   ```

4. **기존에 JavaScript 템플릿을 사용한 적이 있나요? 만약에 있다면, 어떠한 방식으로 사용했는지 말씀해주세요.**

   **template tag에 대한 설명**

   html의 <template> tag는 이후에 자바스크립트를 통해 인스턴스를 생성할 수 있는 HTML 코드를 담아 두는 곳입니다. template tag는 렌더링 되지 않고, 이후 javascript를 통해 추가시킬 수 있습니다. querySelector로 템플릿을 불러오고, 원하는 내용을 설정하여 삽입시킬 수 있습니다.

   **template literal에 대한 설명**

   템플릿 리터럴은 내장된 표현식을 허용하는 문자열 리터럴입니다. 백틱으로 감싸고 달러싸인(\$)과 중괄호( {, } ) 내부에 표현식을 넣을 수 있습니다. 일반적인 이스케이프와 같이 백슬러쉬(\)를 사용하면 됩니다.

   ```json
   `\`` === "`";
   // true
   ```

   좀 더 딥하게 활용하는 형태로 tagged template이 있습니다. 템플릿 리터럴을 함수로 파싱할 수 있는 방법입니다. 이 함수를 태그 함수라고 하는데, 첫 번째 인수는 문자열 값의 배열, 나머지 뒤의 인수들은 표현식들이 순서대로 들어갑니다.

   **taggedd templates 예시**

   ```jsx
   const person = "Nailer";
   const age = 26;

   function ageJudge(strings, personExp, ageExp) {
     const str0 = strings[0]; //""
     const str1 = strings[1];
     // strings = ['Hi, ', ' is a ', '']; 뒤에 빈 문자열이 존재함.
     let ageJudgement = "";
     if (ageExp >= 30) {
       ageJudgement = "늙은이";
     } else {
       ageJudgement = "젊은이";
     }
     return `${personExp}은(는) ${ageJudgement}입니다.`;
   }

   const output = ageJudge`Hi, ${person} is a ${age}`;
   console.log(output);
   // Nailer은(는) 젊은이입니다.
   ```
