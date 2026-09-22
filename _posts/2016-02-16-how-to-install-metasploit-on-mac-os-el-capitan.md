---
title: "How to install Metasploit on Mac OS El Capitan"
date: 2016-02-16T14:01:15
categories: ["Security", "Tuts"]
tags: ["hack", "tutorial"]
image: /assets/uploads/2016/02/metasploit.jpg
---

There were a couple tutorials on the web about how to install Metasploit on Mac OS El Capitan. The orders were to type and type and type commands. The easiest way to do it is by doing a Graphical Installation of Metasploit and with 2 or 3 commands.

### Download Metasploit

Rapid7 offers online a list of the latest builds. What you have to do is to find the one you want. The one I downloaded was **metasploitframework-4.11.10+20160207102256-1rapid7-1.pkg**.

[download link](http://osx.metasploit.com/)

### Install Metasploit

This is simple graphical installation for Mac OS. You just follow the steps like you do with every app. You can change the directory of the installation if you want, and the final size of Metasploit is around 300MB. When the installation is complete you can close the Window.

### Launch Metasploit

Launch Terminal from the Applications list and write the following

```
/opt/metasploit-framework/bin/msfconsole
```

This will launch Metasploit and you are ready to go!

#### Extra details

If you want to launch Metasploit faster you can use the Alias command on every unix device. So launch your terminal and type the following.

```
alias msfconsole='/opt/metasploit-framework/bin/msfconsole'
```

Now anytime you want to launch Metasploit, you just have to type msfconsole and not the whole string. That makes it really faster and easier to launch.
