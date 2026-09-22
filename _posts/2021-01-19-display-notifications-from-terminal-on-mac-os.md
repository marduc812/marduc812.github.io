---
title: "Display Notifications from Terminal on Mac OS"
date: 2021-01-19T20:21:50
categories: ["Tuts"]
tags: ["Mac", "tutorial"]
image: /assets/uploads/2021/01/notification-mac-os-terminal.jpg
---

People who work on IT know the struggle of waiting for something to finish, either this is a scan or a download or anything. You don’t want to change tabs every 2 minutes and check the process, you want to know when something is done, and Mac OS offers wonderful alerts.

One great use I found for this feature, is to notify me when my sshuttle connection AKA poor man’s VPN is broken. One type of alert is the famous osascript alert. Osascript is used for execution of AppleScripts but also any other type of Open Script Architecture. Osascript allows terminal to control almost every feature of Mac OS from changing tabs, to changing volume or controlling application. In this case we want to present an alert. This is done by asking osascript to display an alert with a title and a message, like shown below.

`osascript -e 'display alert "Hello" message "from marduc812.com"'`

[![](/assets/uploads/2021/01/Screenshot-2021-01-19-at-20.18.54.png)](/assets/uploads/2021/01/Screenshot-2021-01-19-at-20.18.54.png)

Additionally, it is possible to display a dialog coming from a specific application. This will make the application icon jump indicating some event happened and like previously with the alert window, you can set a title and the text, like shown below.

`osascript -e 'tell app "Terminal" to display dialog "yeap marduc812.com again" with title "Hello There"'`

[![](/assets/uploads/2021/01/Screenshot-2021-01-19-at-20.37.59.png)](/assets/uploads/2021/01/Screenshot-2021-01-19-at-20.37.59.png)

Finally, it is possible to install terminal-notifier using either gem or brew.

```generic
sudo gem install terminal-notifier
```

```generic
brew install terminal-notifier
```

The solution of terminal-notifier is way more elegant but also more powerful with support for extra features like grouped notifications, icons directly from urls and command execution features when a user clicks on the notification.

```generic
terminal-notifier -message "yeap once again marduc812.com" -title "Hello There"
```

[![](/assets/uploads/2021/01/Screenshot-2021-01-19-at-21.04.50.png)](/assets/uploads/2021/01/Screenshot-2021-01-19-at-21.04.50.png)

Of course both solutions offer support for additional sound notifications, but those things are personal preference. Because I don’t like sound notifications that much and I prefer a clean warning, I use 90% of the cases the display alert feature from osascript.

Github: [Terminal-notifier](https://github.com/julienXX/terminal-notifier)
