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
> 출처 : [웹팩 핸드북](https://joshua1988.github.io/webpack-guide/webpack/what-is-webpack.html#%EC%9B%B9%ED%8C%A9%EC%9D%B4%EB%9E%80 "webpack handbook link") 

![웹팩 번들링](https://miro.medium.com/max/2292/1*EGKixnuLcRXJrz_XcmPaqg.png)

## Code Splitting(코드 분할)이란?
**웹팩에서 제공하는 대표적인 기능 중 하나로, 코드를 여러 개의 번들로 쪼갠다음 필요한 파일을 로드하여 사용할 수 있도록하는 것**

React, Vue와 같은 SPA(Single Page Application)는 최초 로딩시에 모든 리소스를 **번들링**하여 한 번에 받아온다. 때문에 규모가 커질 수록 파일 용량이 커지면서 로딩 속도가 느려질 수 밖에 없다. 이 때, 코드 분할을 통해 필요한 시점에 필요한 리소스만을 받아올 수 있도록하여 로딩 속도 이슈를 개선할 수 있도록한다. 로딩 속도를 개선함으로 UX를 향상되고, SEO 측면에서도 유리해 질 수 있다.

## 코드 분할 방법
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

	중복제거 및 청크 분리를 위해 Entry dependencies 또는 SplitChunkPlugin을 사용하는 방식
	(*청크 : 웹팩에서 처리를 하면서 분리 된 코드 단위)

	#### Entry dependencies

	**webpack.config.js**

		const path = require('path');
 
		module.exports = {
			mode: 'development',
			entry: {
				index: {
					import: './src/index.js',
					dependOn: 'shared', //dependOn 옵션을 추가해줌
				},
				another: {
					import: './src/another-module.js',
					dependOn: 'shared', //dependOn 옵션을 추가해줌
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

	빌드 결과

		...
		[webpack-cli] Compilation finished
		asset shared.bundle.js 549 KiB [compared for emit] (name: shared)
		asset runtime.bundle.js 7.79 KiB [compared for emit] (name: runtime)
		asset index.bundle.js 1.77 KiB [compared for emit] (name: index)
		asset another.bundle.js 1.65 KiB [compared for emit] (name: another)
		Entrypoint index 1.77 KiB = index.bundle.js
		Entrypoint another 1.65 KiB = another.bundle.js
		Entrypoint shared 557 KiB = runtime.bundle.js 7.79 KiB shared.bundle.js 549 KiB
		runtime modules 3.76 KiB 7 modules
		cacheable modules 530 KiB
			./node_modules/lodash/lodash.js 530 KiB [built] [code generated]
			./src/another-module.js 84 bytes [built] [code generated]
			./src/index.js 257 bytes [built] [code generated]
		webpack 5.4.0 compiled successfully in 249 ms
	

	#### SplitChunksPlugin

	공통 dependencies를 기존 엔트리 청크나 새로운 엔트리 청크로 분리할 수 있는 방식

	**webpack.config.js**

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
			//아래 코드를 추가해줌
			optimization: {
				splitChunks: {
					chunks: 'all', 
				},
			},
		};

	위와 같은 옵션을 추가합으로써, 중복된 dependency를 제거할 수 있다.
	[optimization.splitChunks 옵션 더보기](https://webpack.js.org/plugins/split-chunks-plugin/#optimizationsplitchunks "웹팩 공식문서")

	빌드 결과

		...
		[webpack-cli] Compilation finished
		asset vendors-node_modules_lodash_lodash_js.bundle.js 549 KiB [compared for emit] (id hint: vendors)
		asset index.bundle.js 8.92 KiB [compared for emit] (name: index)
		asset another.bundle.js 8.8 KiB [compared for emit] (name: another)
		Entrypoint index 558 KiB = vendors-node_modules_lodash_lodash_js.bundle.js 549 KiB index.bundle.js 8.92 KiB
		Entrypoint another 558 KiB = vendors-node_modules_lodash_lodash_js.bundle.js 549 KiB another.bundle.js 8.8 KiB
		runtime modules 7.64 KiB 14 modules
		cacheable modules 530 KiB
			./src/index.js 257 bytes [built] [code generated]
			./src/another-module.js 84 bytes [built] [code generated]
			./node_modules/lodash/lodash.js 530 KiB [built] [code generated]
		webpack 5.4.0 compiled successfully in 241 ms

3. Dynamic Import

	모듈 내부에서 인라인 함수 호출을 통해 코드를 분할 하는 방식

	- import()
	- require.ensure (레거시)

	**webpack.config.js**
		
		const path = require('path');
		
		module.exports = {
			mode: 'development',
			entry: {
				index: './src/index.js',
			},
			output: {
				filename: '[name].bundle.js',
				path: path.resolve(__dirname, 'dist'),
			},
		};


	프로젝트 구성

		webpack-demo
		|- package.json
		|- webpack.config.js
		|- /dist
		|- /src
			|- index.js
		|- /node_modules


	**src/index.js**

	변경 전

		import _ from 'lodash';

		function component() {
			const element = document.createElement('div');
		
			element.innerHTML = _.join(['Hello', 'webpack'], ' ');
		
			return element;
		}
		
		document.body.appendChild(component());


	변경 후 


		function getComponent() {
			const element = document.createElement('div');
		
			return import('lodash')
				.then(({ default: _ }) => {
					const element = document.createElement('div');

					element.innerHTML = _.join(['Hello', 'webpack'], ' ');
		
					return element;
				})
				.catch((error) => 'An error occurred while loading the component');
		}
		
		getComponent().then((component) => {
			document.body.appendChild(component);
		});

	
	빌드 결과

		...
		[webpack-cli] Compilation finished
		asset vendors-node_modules_lodash_lodash_js.bundle.js 549 KiB [compared for emit] (id hint: vendors)
		asset index.bundle.js 13.5 KiB [compared for emit] (name: index)
		runtime modules 7.37 KiB 11 modules
		cacheable modules 530 KiB
			./src/index.js 434 bytes [built] [code generated]
			./node_modules/lodash/lodash.js 530 KiB [built] [code generated]
		webpack 5.4.0 compiled successfully in 268 ms
 

## React에서 Code Splitting 적용하기 ([참고](https://ko.reactjs.org/docs/code-splitting.html "리액트 공식문서"))

리액트의 경우 CRA 또는 Next.js를 사용한다면, 별도 설치 없이 바로 사용 가능하다.

- import() 
- React.lazy

		import React, { Suspense } from 'react';

		const OtherComponent = React.lazy(() => import('./OtherComponent'));

		function MyComponent() {
			return (
				<div>
					<Suspense fallback={<div>Loading...</div>}>
						<OtherComponent />
					</Suspense>
				</div>
			);
		}

- 라우트 기반 코드 분할(Route-based)

		import React, { Suspense, lazy } from 'react';
		import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

		const Home = lazy(() => import('./routes/Home'));
		const About = lazy(() => import('./routes/About'));

		const App = () => (
			<Router>
				<Suspense fallback={<div>Loading...</div>}>
					<Switch>
						<Route exact path="/" component={Home}/>
						<Route path="/about" component={About}/>
					</Switch>
				</Suspense>
			</Router>
		);

- Named Exports
	
	**ManyComponents.js**
	
		export const MyComponent = /* ... */;
		export const MyUnusedComponent = /* ... */;

	**MyComponent.js**

		export { MyComponent as default } from "./ManyComponents.js";

	**MyApp.js**

		import React, { lazy } from 'react';
		const MyComponent = lazy(() => import("./MyComponent.js"));

그 외 좀 더 정리가 잘 된 블로그 [참고](https://velog.io/@velopert/react-code-splitting "리액트 프로젝트 코드 스플리팅 정복하기") 

Vue.js는 공식문서 [참고](https://kr.vuejs.org/v2/guide/components-dynamic-async.html "동적 & 비동기 컴포넌트")

## 번들 분석
웹팩은 몇 가지 공식 번들 분석도구가 있어서, 이런 도구를 이용해 효율적으로 번들을 구성, 관리 할 수 있다.

- [webpack-chart](https://alexkuz.github.io/webpack-chart/ "webpack-chart"): 웹팩 통계를 파이차트로 보여줌 
- [webpack-visualizer](https://www.npmjs.com/package/webpack-visualizer-plugin "webpack-visulaizer"): 어떤 모듈이 공간을 차지하고 있고, 중복되었는지 확인할 수 있도록 번들을 시각화하고 분석해줌
- [webpack-bundle-analyzer](https://www.npmjs.com/package/webpack-bundle-analyzer "webpack-bundle-analyzer"): 번들을 트리맵으로 시각화해서 나타내주고 확대/축소 가능한 인터렉티브 컨텐츠 제공
- [webpack bundle optimize helper](https://webpack.jakoblind.no/optimize/ "webpack bundle optimize helper"): 번들 분석해서 번들 크기를 줄일 수 있도록 실행가능한 제안을 해줌
- [bundle-stats](https://relative-ci.com/tools/webpack-bundle-stats/demo-multiple-jobs.html "bundle-stats"): 번들 리포트 생성, 빌드 간 결과 비교 제공


## 정리
웹팩에서 코드 분할 하는 방법에 대해서 정리를 해보았다. 번들 분석도구와 코드 분할을 잘 활용한다면 사이트 성능 개선에 많은 도움이 될 수 있을 것 같다.

---
### 참고

https://joshua1988.github.io/vue-camp/advanced/code-splitting.html

https://webpack.js.org/guides/code-splitting/

https://ko.reactjs.org/docs/code-splitting.html

https://velog.io/@velopert/react-code-splitting
