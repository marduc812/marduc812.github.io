---
title: "Hex Editor on OS X [vim]"
date: 2016-06-09T20:17:14
categories: ["Tuts"]
tags: ["Mac", "tutorial"]
image: /assets/uploads/2016/06/vim-hex-editor-os-x.jpg
---

Today I was playing with Spotify and while I was browsing the Cache folders, I found out that the content of these folders is in hex format. The only thing I could see was numbers, so I needed a hex editor in order to view the files.

You don’t need to download anything the only think you have to do is just open the file by using the vim text editor from your terminal. In order to open a file with vim you type.

```bash
vim {path of the file you want or just drop the file here}
```

![vim hex editor os x (2)](/assets/uploads/2016/06/vim-hex-editor-os-x-2.png)

When you see something like the image above type the following:

```bash
:% ! xxd
```

This will turn you editor into a hex editor like shown in the picture below. [![vim hex editor os x (3)](/assets/uploads/2016/06/vim-hex-editor-os-x-3.png)](/assets/uploads/2016/06/vim-hex-editor-os-x-3.png)

If you want to turn it back to normal editor use the same command like before just type -r in the end.

```bash
:% ! xxd -r
```

[![vim hex editor os x (4)](/assets/uploads/2016/06/vim-hex-editor-os-x-4.png)](/assets/uploads/2016/06/vim-hex-editor-os-x-4.png)

This will bring your text editor to it’s normal form. If you still need a better hex editor to do a more complex work you can use [Hex Fiend](http://ridiculousfish.com/hexfiend/) that is free and [open source](https://github.com/ridiculousfish/HexFiend) or [Synalyze it](https://www.synalysis.net/) that offers a free and a premium version.
