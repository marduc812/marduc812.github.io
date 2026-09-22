---
title: "10 Built In Features of VS Code You Need to Know"
date: 2020-12-17T22:40:21
categories: ["Fun", "Tuts"]
tags: ["tutorial"]
image: /assets/uploads/2020/12/vs-code-tricks.jpg
---

When VS code was released I switched almost immediately from Atom, mainly because it was so much lighter and faster, although both editors are based on Electron aka Heavy File Browser. VS Code not only is the best editor out there, but has a plethora of features without any extension which are not so commonly used and here I am to help you make your life a bit better.

Note: Whenever it writes `run a command` from now on, it means that the `Command Pallet` is used, which is shown by using `cmd/ctrl` + `shift` + `p`.

#### 1. Snippets

Snippets are useful when you have some blocks of code that you commonly need and either you type it all over every time, or you use Google and I’m feeling lucky to save some clicks from going through different web pages. One snippet which I found really useful for me, is to generate a PoC of a Clickjacking attack.

[![](/assets/uploads/2020/12/Screenshot-2020-12-17-at-18.44.32.png)](/assets/uploads/2020/12/Screenshot-2020-12-17-at-18.44.32.png)

To create a new snippet, use your `Command Pallet` and type `Configure User Snippets` and select the language of your choice, I used HTML in this case. A JSON format is followed there, which has 3 parts that need to fill, a name for the snippet, a prefix and the body. In this case I will call mine `Clickjacking Proof of Concept`, set a prefix of `clickpoc` and set the body to the PoC payload.

```json
"Clickjacking Proof of Concept": {
    "prefix": "clickpoc",
    "body": [
        "<html>",
        "\t<head>",
        "\t\t<title>$1</title>",
        "\t</head>",
        "\t<body>",
        "\t\t<iframe src=\"$2\" width=\"500\" height=\"500\"></iframe>",
        "\t</body>",
        "</html>"
    ],
    "description": "Clickjacking Proof of Concept"
}
```

Notice how the body part is an array of strings and each line is a new string. I used two fields with name `$1` and `$2` on lines 6 and 9, which are the placeholders that VS Code will move my cursor after it does the completion. After filling the first field which is the title by pressing `tab` the cursor is moved to the second placeholder which is the link for the iframe. In order to test it, I go to my html page and start typing clic, which is the prefix and VS Code automatically suggests the snippet. After selecting the pop up, the text is replaced with my code and the cursor is now on the Title field.

[![](/assets/uploads/2020/12/clickjacking-vs-code.gif)](/assets/uploads/2020/12/clickjacking-vs-code.gif)

VS Code Ref: [Snippets](https://code.visualstudio.com/docs/editor/userdefinedsnippets)  
Online Snippet Generator: [Generator App](https://snippet-generator.app/)

#### 2.Format Document

A lot of times while developing when some text is copied from another source like StackOverflow or random websites, the form of the code is bad, meaning some times there are more spaces or tabs etc.

[![](/assets/uploads/2020/12/format-vs-code.gif)](/assets/uploads/2020/12/format-vs-code.gif)

VS Code offers an option to format the document with 3 different ways.

1. Right Click and Format Document
2. alt/options + shift + F
3. Command Pallet + Format Document

Additionally, in case you want it to run it automatically every time you save your file, you can set it into the `settings.json` file as `"editor.formatOnSave": true`. To access settings.json use `cmd/ctrl` + `,` and then click on the top right button.

VS Code Ref: [Formatting](https://code.visualstudio.com/docs/editor/codebasics#_formatting)

[![](/assets/uploads/2020/12/Screenshot-2020-12-17-at-19.30.30.png)](/assets/uploads/2020/12/Screenshot-2020-12-17-at-19.30.30.png)

#### 3. Folder Nesting

In case your project requires the creation of nested folders and this is where you want to put your newly created file, you don’t have to manually create new folders but VS Code identifies the / character as a directory and will create the folder and the file for you, saving you those 3 sweet clicks and ~5 seconds of your time.

[![](/assets/uploads/2020/12/vs-code-nested-directory.gif)](/assets/uploads/2020/12/vs-code-nested-directory.gif)

VS Code Ref: [Workspace](https://code.visualstudio.com/docs/getstarted/settings)

#### 4. Symbol Renaming

The most common way to replace something with something else is to select the text that will be replaced, use cmd/ctrl + f to find the references of this text inside the file and the replace it with the new value. VS Code offers a better approach for renaming variables, since by pressing `F2` it displays a new name for the variable. The advantage of this is that it will also replace the occurrences of this variable in other files also, saving you valuable time.

[![](/assets/uploads/2020/12/Screenshot-2020-12-17-at-19.50.06.png)](/assets/uploads/2020/12/Screenshot-2020-12-17-at-19.50.06.png)

VS Code Ref: [Refactoring](https://code.visualstudio.com/docs/editor/refactoring)

#### 5. Edit Keyboard Shortcuts

Using keyboard shortcuts can save you a lot of time, since you don’t have to move your hand and take the mouse. Everything can be done with your keyboard like for example going to your Keyboard Shortcut panel by typing `cmd/ctrl` + `k` and right after `cmd/ctrl` + `s`. There, all the keyboard shortcuts are presented and allows you to change them. VS Code will warn you in case of a shortcut conflict is presented to save you from the suffering.

[![](/assets/uploads/2020/12/Screenshot-2020-12-17-at-19.53.38.png)](/assets/uploads/2020/12/Screenshot-2020-12-17-at-19.53.38.png)

VS Code Ref: [Key Bindings](https://code.visualstudio.com/docs/getstarted/keybindings)

#### 6. Emmet Abbreviations

Emmet Abbreviations were something new to me, that I got introduced to because of VS Code. What it does is it allows to specify some keywords and symbols and create a whole structure saving a lot of time. For this example let’s say a list with 5 items, where each element has a different class is needed. By typing `ul>li.item$*5`, VS Code will generate the HTML code matching the formula.

[![](/assets/uploads/2020/12/emmet-vs-code.gif)](/assets/uploads/2020/12/emmet-vs-code.gif)

Finally, an abbreviation I use a lot is for creation of HTML 5 boilerplate, which Emmet will create automatically when it will detect part of the `html` text.

[![](/assets/uploads/2020/12/vs-code-html-boilerplate.png)](/assets/uploads/2020/12/vs-code-html-boilerplate.png)

VS Code Ref: [Emmet](https://code.visualstudio.com/docs/editor/emmet)  
Emmet: [Cheat Sheet](https://docs.emmet.io/cheat-sheet/)

#### 7. Jump to

Like every other editor and IDE allows to jump in different parts of the code like Definitions and Implementations. But also allows to use peek, which will create a small frame under the cursor showing the requested location without changing windows. To peek definition press `options/alt` + `F12` and to peek implementations use `options/alt` + `shift` + `F12`.

[![](/assets/uploads/2020/12/peek-vs-code.gif)](/assets/uploads/2020/12/peek-vs-code.gif)

VS Code Ref: [Code Navigation](https://code.visualstudio.com/docs/editor/editingevolved)

#### 8. Change Side Bar Side

In case you don’t like the side bar being on the left side of the view, VS Code has an option to change the side of the side bar by selecting View, Appearance, Move Side bar Right.

[![](/assets/uploads/2020/12/Screenshot-2020-12-17-at-22.51.28.png)](/assets/uploads/2020/12/Screenshot-2020-12-17-at-22.51.28.png)

VS Code Ref: [Basic Layout](https://code.visualstudio.com/docs/getstarted/userinterface#_basic-layout)

#### 9. Screencast Mode

This feature can be really helpful in case of a video presentation which may contain use of shortcuts. This feature will present every keystroke on a nice interface, while whenever a mouse click is detected a red circle is presented around it. This can be enabled by running the `Screencast` and selecting `Toggle Screencast Mode`.

![](https://i.imgur.com/0wfrvEW.gif)

VS Code Ref: [Screencast Mode](https://code.visualstudio.com/updates/v1_31#_screencast-mode)

#### 10. Zen Mode

This feature of VS Code will make the application go Full Screen and hide the Side Bar, the Minimap, all the buttons and leave you with a simple text editor. You can toggle it by pressing `cmd/ctrl` + `k` and then `z`.

[![](/assets/uploads/2020/12/vs-code-zen.png)](/assets/uploads/2020/12/vs-code-zen.png)

VS Code Ref: [Zen Mode](https://code.visualstudio.com/updates/v1_8#_focus-on-your-code)

This was a list with the best features of VS code as of today. Some of them will save your time, some of them will make the workspace more interesting. Feel free to comment about any other features of VS Code that I missed and feel free to share this post.
