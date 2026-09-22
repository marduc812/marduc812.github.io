---
title: "How to console.log the version of JavaScript libraries on your browser"
date: 2023-05-03T08:28:50
categories: ["Security", "Tuts"]
tags: ["javascript", "Security"]
image: /assets/uploads/2023/05/javascript_versions.jpg
---

During a web assessment is common to find some outdated JavaScript library. I like to showcase the version of the outdated library in a console print with the URL where it loaded. Below is the list of console commands, to get their versions.

#### Angular

```js
getAllAngularRootElements()[0].attributes["ng-version"].value
//'7.2.11'
```

#### AngularJS

```js
angular.version
//{full: '1.5.6', major: 1, minor: 5, dot: 6, codeName: 'arrow-stringification'}
```

#### Bootstrap

```js
$.fn.tooltip.Constructor.VERSION
//'3.4.1'
```

#### CKEditor

```js
CKEDITOR.version
//'4.18.0'
```

#### DataTables

```js
$.fn.DataTable.version
//'1.10.25'
```

#### D3.js

This worked up to version 6.7.0. After the release 7.0.0, the version is not exposed.

```js
d3.version
//'6.6.0'
```

#### Dojo

```js
[dojo.version.major, dojo.version.minor, dojo.version.patch].join(".");
//'1.10.1'
```

#### Fingerprint.js

```js
Fingerprint2.VERSION
//'2.0.0'
```

#### Foundation

```js
Foundation.version
//'5.2.1'
```

#### GSAP

```js
gsap.version
//'3.10.4'
```

#### HAMMER.js

```js
Hammer.VERSION
//'2.0.8'
```

#### Handlebars

```js
Handlebars.VERSION
//'4.7.7'
```

#### Highcharts

```js
Highcharts.version
//'10.0.0'
```

#### jQuery

```js
$.fn.jquery
// '1.10.2'
```

```js
$().jquery; 
// '1.10.2'
```

#### jQuery Mobile

```js
$.mobile.version
'1.3.1'
```

#### jQuery-UI

```js
$.ui.version
'1.8.1'
```

#### Lightstreamer

```js
Lightstreamer.version
//'8.0.1'
```

#### Moment.js

```js
moment.version
//'2.10.1'
```

#### Numbro

```js
numbro.version
//'1.5.1'
```

#### OpenUI5

```js
sap.ui.version
//'10.2.33'
```

#### Requirejs

```js
requirejs.version
//'2.3.2'
```

#### Three.js

```js
THREE.REVISION
//'85'
```

#### Underscore.js

```js
_.VERSION
//'1.13.4'
```
