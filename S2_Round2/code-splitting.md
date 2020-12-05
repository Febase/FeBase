---
title: Code Splitting 쪼개보기
date: 2020-12-03 00:00:00
author: symoon
category: S2_Round2
---


# Code Splitting

> ### Webpack
>
> 웹팩이란 최신 프런트엔드 프레임워크에서 가장 많이 사용되는 모듈 번들러(Module Bundler)입니다. 모듈 번들러란 웹 애플리케이션을 구성하는 자원(HTML, CSS, Javscript, Images 등)을 모두 각각의 모듈로 보고 이를 조합해서 병합된 하나의 결과물을 만드는 도구를 의미합니다.
>
> 출처 : [웹팩 핸드북](https://joshua1988.github.io/webpack-guide/webpack/what-is-webpack.html#%EC%9B%B9%ED%8C%A9%EC%9D%B4%EB%9E%80, "webpack handbook link") 

![웹팩 번들링](https://miro.medium.com/max/2292/1*EGKixnuLcRXJrz_XcmPaqg.png)

## Code Splitting(코드 분할)이란?
**웹팩에서 제공하는 대표적인 기능 중 하나로, 코드를 여러 개의 번들로 쪼갠다음 필요한 파일을 로드하여 사용할 수 있도록하는 것**

React, Vue와 같은 SPA(Single Page Application)는 최초 로딩시에 모든 리소스를 **번들링**하여 한 번에 받아온다. 때문에 규모가 커질 수록 파일 용량이 커지면서 로딩 속도가 느려질 수 밖에 없다. 이 때, 코드 분할을 통해 필요한 시점에 필요한 리소스만을 받아올 수 있도록하여 로딩 속도 이슈를 개선할 수 있도록한다. 로딩 속도를 개선함으로 UX를 향상되고, SEO 측면에서도 유리해 질 수 있다.

## 접근방식
웹팩 공식문서에서 제시하는 일반적인 접근법은 다음과 같다.

1. Entry Points

	엔트리 포인트 구성을 통해 수동으로 코드를 분할 하는 방식

		webpack-demo
		|- package.json
		|- webpack.config.js
		|- /dist
		|- /src
			|- index.js
		+	|- another-module.js
		|- /node_modules


	**another-module.js**
		
		import _ from 'lodash';

		console.log(_.join(['Another', 'module', 'loaded!'], ' '));		


	**webpack.config.js**
	
	변경 전

		const path = require('path');
 
		module.exports = {
			entry: './src/index.js',
			output: {
				filename: 'main.js',
				path: path.resolve(__dirname, 'dist'),
			},
		};
 
	변경 후

		const path = require('path');
 
		module.exports = {
			mode: 'development',
			entry: {
				index: './src/index.js',
				another: './src/another-module.js',
			},
			output: {
				filename: '[name].bundle.js',
				path: path.resolve(__dirname, 'dist'),
			},
		};



	빌드 결과

		...
		[webpack-cli] Compilation finished
		asset index.bundle.js 553 KiB [emitted] (name: index)
		asset another.bundle.js 553 KiB [emitted] (name: another)
		runtime modules 2.49 KiB 12 modules
		cacheable modules 530 KiB
			./src/index.js 257 bytes [built] [code generated]
			./src/another-module.js 84 bytes [built] [code generated]
			./node_modules/lodash/lodash.js 530 KiB [built] [code generated]
		webpack 5.4.0 compiled successfully in 245 ms


	이 방식은 단순하지만 몇가지 문제가 생길 수 있다.
	- 엔트리 청크 사이에 중복 된 모듈이 있으면 두 번들에 모두 포함된다.
	- 유연하지 않으며 핵심 애플리케이션 로직으로 코드를 동적으로 분할하는 데 사용할 수 없다.



2. Prevent Duplication

	중복제거 및 청크로 분리를 위해 Entry dependencies 또는 SplitChunkPlugin을 사용하는 방식

		const path = require('path');
 
		module.exports = {
			mode: 'development',
			entry: {
				index: {
					import: './src/index.js',
					dependOn: 'shared',
				},
				another: {
					import: './src/another-module.js',
					dependOn: 'shared',
				},
				shared: 'lodash',
			},
			output: {
				filename: '[name].bundle.js',
				path: path.resolve(__dirname, 'dist'),
			},
			//단일 HTML에서 여러 진입점을 사용하려면 아래와 같이 추가해줘야함
			optimization: {
				runtimeChunk: 'single', 
			},
		};

	여러 진입점 사용시 발생할 수 있는 문제점 [참고](https://bundlers.tooling.report/code-splitting/multi-entry/, "multi entry")
	

3. Dynamic Import

	모듈 내부에서 인라인 함수 호출을 통해 코드를 분할 하는 방식

 
### 라우트 기반 
### Named Export

## 정리


---
### 참고

https://joshua1988.github.io/vue-camp/advanced/code-splitting.html

https://webpack.js.org/guides/code-splitting/

https://ko.reactjs.org/docs/code-splitting.html