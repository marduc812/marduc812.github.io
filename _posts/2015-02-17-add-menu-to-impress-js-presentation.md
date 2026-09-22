---
title: "Add Menu to Impress.js presentation"
date: 2015-02-17T19:32:54
categories: ["Tuts"]
tags: ["css", "impress.js", "menu"]
image: /assets/uploads/2015/02/impress.js.jpg
---

I recently made a small presentation, using Impress.js which is a great tool.You can make presentations using HTML and Javascript. You can customise the result with your own CSS and you can take some great ideas from a list  of [impress.js presentations](https://github.com/bartaz/impress.js/wiki/Examples-and-demos).

When I completed my presentation, I wanted to make a menu, so I could add some links or some more infos about the presentation.  So I created a menu with a custom style.

```html
<ul class="menu_button">
    <li><a href="link"><img src="home.png"></a></li>
    <li><a href="link"><img src="ergasia.png"></a></li>
    <li><a href="link"><img src="git.png"></a></li>
</ul>
```

But when you click an icon, nothing happens. The way you can make it work is just by adding the following line at your css for the class of the menu. In my case it’s menu\_button.

```css
pointer-events: auto;
```

This will make your menu clickable and you will make it work perfectly!

If you want more infos you can take a look at my [presentation](https://marduc812.com/thesis) or at the [source](https://github.com/marduc812/Thesis_pres).(it’s at Greek)  
asd
