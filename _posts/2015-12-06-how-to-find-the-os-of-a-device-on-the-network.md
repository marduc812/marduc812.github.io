---
title: "How to find the OS of a device on the network"
date: 2015-12-06T17:51:34
categories: ["Security", "Tuts"]
tags: ["hack", "tutorial"]
image: /assets/uploads/2015/12/How-to-find-the-OS-of-a-device-on-the-networktop.jpg
---

Most of you know about about Metasploit, and how powerful this tool can be.I’m running Kali Linux 2.0, installed on a virtual machine.

**1. Start the postgresql service.**   
That way we will be able to store the data form the nmap to our database. Postgresql is a DB that is used by Metasploit.

```

service postgresql start
```

This command gets no output so we need to check if postgresql is actually running.  
type:

```

service postgresql status
```

[![How to find the OS of a device on the network(1)](/assets/uploads/2015/12/How-to-find-the-OS-of-a-device-on-the-network1.png)](/assets/uploads/2015/12/How-to-find-the-OS-of-a-device-on-the-network1.png)

**2. Start Metasploit**

```

msfconsole
```

Now Metasploit is running. You can use the –help command if you need more infos about the commands of the platform. There are REALLY a lot of things you can do.

**3. NMAP scan the network**

```

db_nmap -A 192.168.1.0/24 -v
```

This could take a while depending on how many devices are connected to your network, WiFi’s signals and more. What each part of the command does:  
**db\_nmap** We use it in order to store the data of the nmap to our db.  
**-A** Detects the OS of the devices based on some ports or protocols running.  
**192.168.1.0/24** This is a scan on a range of ips from 192.168.1.0 up to 192.168.1.255.  
**-v** Controls the verbosity of the output. If you want even more details your can use -vv

Now we want to see the list of the connected devices.

```

hosts
```

and what we get is something like that.

[![How to find the OS of a device on the network(7)](/assets/uploads/2015/12/How-to-find-the-OS-of-a-device-on-the-network7.jpg)](/assets/uploads/2015/12/How-to-find-the-OS-of-a-device-on-the-network7.jpg)

**4. Setting up scan options.**

Now we have to use smb\_version in order to find more options about the OS. Type the following.

```

use auxiliary/scanner/smb/smb_version
```

By typing **show options** we can see what fields we have to fill.

[![How to find the OS of a device on the network(5)](/assets/uploads/2015/12/How-to-find-the-OS-of-a-device-on-the-network5.png)](/assets/uploads/2015/12/How-to-find-the-OS-of-a-device-on-the-network5.png)

Now we have to fill the RHOSTS field. This is where we enter the IP of the device we want to find the OS. In my case is 192.168.1.73. To do that we just use the set command.

```

set RHOSTS 192.168.1.73
```

Now we will increase the threads by changing the THREADS number from 1 to 11.

```

set THREADS 11
```

![How to find the OS of a device on the network(4)](/assets/uploads/2015/12/How-to-find-the-OS-of-a-device-on-the-network4.png)

**5. Find the OS**

Finally type run and hit enter in order to run the module.

```

run
```

```
![How to find the OS of a device on the network(6)](/assets/uploads/2015/12/How-to-find-the-OS-of-a-device-on-the-network6.png)
```

And what we can do now is a final hosts and these are our results.

![How to find the OS of a device on the network(3)](/assets/uploads/2015/12/How-to-find-the-OS-of-a-device-on-the-network3.png)

Now we can see what exactly OS our victim is running and by searching on [exploits-db](https://www.exploit-db.com/) we can find the right type of vulnerability that matches our case.
