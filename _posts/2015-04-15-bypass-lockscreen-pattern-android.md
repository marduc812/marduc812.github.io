---
title: "Bypass lockscreen pattern [Android]"
date: 2015-04-15T18:41:48
categories: ["Android", "CyanogenMod", "Tuts"]
tags: ["Android", "CyanogenMod", "tutorial"]
image: /assets/uploads/2015/04/pattern.jpg
---

After updating the latest [CM12](https://marduc812.com/category/cyanogenmod/) nightly, my phone asked for unlock pattern. I normally have a 3×3 pattern, but after restart there was just a blank space. All I could feel was a small vibration every time I moved my finger over it. It was a 6×6 pattern, set to be invisible. I was trying to unlock the phone but of course there was no way I could do that.

In order to remove password pattern lock phone must be rooted.

Here is what I did.

### 1. Download Android SDK

Since I already had it I didn’t had to to download it but you can download it, and unzip it somewhere easy to locate.  
[Download link](https://developer.android.com/sdk/installing/index.html)

---

### 2. Connect THE phone.

I connected my phone with my laptop and open terminal.

---

### 3. Open Terminal

Using terminal I had to go to my SDK folder.

First I had to do  
Since I use a Mac in front of adb command I had to use “/.”, on linux you don’t have to.

```bash

./adb reboot recovery
```

This reboots phone and get’s it into recovery mode. You can also do it by pressing Power and Volume down button at the same time when you turn on your phone.

```bash

./adb shell
```

Now we have to run the following commands in order to remove the password/pattern files form the device.

```bash

rm /data/system/locksettings.db
rm /data/system/locksettings.db-wal
rm /data/system/locksettings.db-shm
rm /data/system/gesture.key
rm /data/system/cm_gesture.key
rm /data/system/password.key
```

Now you have to restart the phone and it won’t ask you for pattern or password.
