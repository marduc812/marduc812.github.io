---
title: "Hack any device with your Android phone"
date: 2016-02-06T15:03:35
categories: ["Security", "Tuts"]
tags: ["hack", "tutorial"]
image: /assets/uploads/2016/02/Screen-Shot-2016-02-06-at-16.59.27.png
---

There are a lot of apps for Android that can help you hack a user. I prefer cSploit. Why? Because it has great layout, it’s easy to use and it’s open source.

First of all you need an Android device running Android 2.3 or greater and must be Rooted. Also you need to have installed BusyBox, with every utility. Download BusyBox for free and click the Install button.

![Screenshot_20160206-151326](/assets/uploads/2016/02/Screenshot_20160206-151326.png)

Then download cSploit from their github page. The latest version at the moment is 1.6.5. You need to allow the installation of unknown sources. Now open the downloaded .apk in order to install the app.

SuperSU will ask you to allow cSploit to get root permissions. You need to GRAND it and the update the core, the MSF and probably the ruby is the app prompts you to. It will take around 10 minuted depending on your internet speed.

Now you are ready to use the app.

The first thing you see when you launch the app is a list of connected devices on the network. Select your device and select what you want to do.

---

## **Image Replacement**

Since we don’t want do any damage I will use my favourite type of attacks. The Man In The Middle. What happens is the device is now between the Router and my laptop (that I chose as a target) and is manipulating the traffic. So I want to replace every image on the website with one I want. I will replace every image with an image of a cat.

|  |  |
| --- | --- |
| [Screenshot_20160206-153244](/assets/uploads/2016/02/Screenshot_20160206-153244.png) | [Screenshot_20160206-153249](/assets/uploads/2016/02/Screenshot_20160206-153249.png) |

I prefer picking as a source an image from a website, that the size is about medium.

Here is a preview of the website before and after the attack.

[![before_after](/assets/uploads/2016/02/before_after.jpg)](/assets/uploads/2016/02/before_after.jpg)

This kind of attack doesn’t work on https:// that means that it won’t replace images from websites with SSL.

---

## **Password Sniffing**

[![Screenshot_20160206-155537](/assets/uploads/2016/02/Screenshot_20160206-155537.png)](/assets/uploads/2016/02/Screenshot_20160206-155537.png)  
Also you can do a simple password sniffing for websites that don’t use https://. For example when I log in to a website it will start to sniff every fields that look like passwords or usernames and this is what it looks like.

The form is **Username : Password INFO: website**

---

## **Session Hijacking**

Now a better thing to do is a session highjacking. I will use this attack for an old mail I have. I get connected to the mail’s website from my laptop, and the app steals the cookies from it. Now there is an option to connect to the website (Left Image). As you can see now I am connected to the website with my username without even getting logged in to it (Right Image). There are really a lot of things to do, but remember to keep it safe for the rest.

|  |  |
| --- | --- |
| [Screenshot_20160206-155842](/assets/uploads/2016/02/Screenshot_20160206-155842.png) | [Screenshot_20160206-155837](/assets/uploads/2016/02/Screenshot_20160206-155837.png) |

---

### Links

BusyBox:[Google Play](https://play.google.com/store/apps/details?id=stericson.busybox&hl=en)  
cSploit: [GitHub](https://github.com/cSploit/android) / [Download](https://github.com/cSploit/android/releases/tag/v1.6.5)  
SuperSU: [Google Play](https://play.google.com/store/apps/details?id=eu.chainfire.supersu&hl=en)
