---
title: "Best Penetration Testing Tools for Mac OS [2023]"
date: 2017-05-28T14:40:42
categories: ["Tuts"]
tags: ["Mac", "Security"]
image: /assets/uploads/2017/05/penetration-testing-tools-mac-os-e1607981161521.jpg
---

Updated: 09/23 – I needed [Metasploit Framework](https://www.metasploit.com/) for an `msfvenom` payload and I was using `Kali Linux` as a Virtual Machine, mainly because all the tools are pre-installed there. Running a

Virtual Machine is not as easy as running the tools in a host Operating System. The available RAM of course is much less than the actual host and some times configuring things can be complicated.

### Nmap (Free)

Nmap is the best port scanning tool you can use and also open source. Used widely, mainly because of the incredible power and flexibility it offers. On Mac OS Nmap comes with `ZenMap`, in the installation pack. For those who don’t like the terminal Zenmap is the perfect tool. I prefer using Nmap but in some cases, like for example when you have multiple hosts to scan, Zenmap makes reading them much easier.

Installation of Nmap is really simple and it does not require any typing at all. You can just download a `.dmg` file from the official website and do a normal installation like in every other application.

Links: [Nmap](https://nmap.org/book/inst-macosx.html) – [Github](https://github.com/nmap/nmap)

### Nikto (Free)

Nikto comes pre-installed on Kali Linux and some times it can help you find some hidden Gems on the web server you are testing. Nikto is a Web Server scanner that will inform you in case there is an outdated software version, if it finds some insecure or default files / directories and about some possible server misconfigurations.

In order to install Nikto you need to install Homebrew. To install Homebrew you need to type a single command on your terminal.

```raw
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

After installation if you didn’t agree with the Terms of Service of X-Code you will probably need to follow the instuctions. The instructions are pretty clear and simple to follow. Next you have to install Nikto. Go back to your terminal and type the following.

```raw
brew install nikto
```

After finishing the installation you will be able to scan every web server using the command `nikto -h {URL}`.

Links: [Homebrew](https://brew.sh/) – [Github](https://github.com/sullo/nikto) – [Nikto](https://cirt.net/Nikto2)

### Wireshark (Free)

The Wireshark is the most known Network Traffic Sniffer, that is open-source like all the tools so far. The Wireshark distribution also comes with TShark, which is aline-oriented sniffer (similar to Sun’s snoop, or tcpdump) that uses thesame dissection, capture-file reading and writing, and packet filteringcode as Wireshark, and with editcap, which is a program to read capturefiles and write the packets from that capture file, possibly in adifferent capture file format, and with some packets possibly removed from the capture.

Installation is pretty simple, since it come as a `.dmg` file and the installation is like on every other application on Mac OS. After installation a new icon will appear on the launchpad’s application list. From there just by clicking it you can start sniffing the network traffic, after specifying the interface you would like to intercept.

Links: [Wireshark](https://www.wireshark.org/download.html) – [Github](https://github.com/wireshark/wireshark)

### Sqlmap (Free)

The Sqlmap is a powerful tool for finding `SQL injections`. It is completely automated and just by specifying a parameter the tool will try to exploit the injectable parameter sometimes even without you having to specify the type of database. It supports multi databases including SQL and non-SQL databases. Installation is pretty simple by using `brew`.

```raw
brew install sqlmap
```

When the installation is complete you can just type `sqlmap` on terminal to launch the tool.

Links: [sqlmap](http://sqlmap.org/) – [Github](https://github.com/sqlmapproject/sqlmap)

### Zed Attack Proxy (Free)

The `OWASP` Zed Attack Proxy (ZAP) is one of the world’s most popular free security tools and is actively maintained by hundreds of international volunteers[\*](https://github.com/zaproxy/zaproxy#justification). It can help you automatically find security vulnerabilities in your web applications while you are developing and testing your applications. Its also a great tool for experienced pentesters to use for manual security testing.

The easiest way to install ZAP is by using brew. Start by installing `caskroom`.

```raw
brew install caskroom/cask/brew-cask
```

After the installation is complete the system is ready to install ZAP.

```raw
brew cask install owasp-zap
```

After the installation is complete a new ZAP icon will appear on the launchpad.

Links: [OWASP ZAP](https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project) – [Github](https://github.com/zaproxy/zaproxy)

### Burp Suite (Free / Paid)

My personally favourite proxy tool is Burp Suite. It offers pretty much the same options as ZAP, with better and much easier to use design. This is only for the Community version. The paid version offers automated fuzzing, with good results, it offers Intruder, a function to repeat requests for fuzzing, with custom wordlist, support for regular expressions and much more. Intruder is also available for the Community version, but it has a throttling that can be a bit slow. Installing Burp is really easy, you just need to visit their website and they offer an option for Mac OS, and you just download an install the .dmg file.

Links: [Burp Suite](https://portswigger.net/burp/communitydownload)

### Aircrack-ng (Free)

Unluckily the tool for every Wi-Fi pentration testing is partially available on OS X. You can do a really simple installation of the Aircrack-ng with macports, but `Airodump-ng` and `Aireplay-ng` are linux only and will not work under OS X native, so for reinjecting and sniffing you will have to use other means.

```raw
sudo port install aircrack-ng
```

After finishing the installation you can use it by typing aircrack-ng and the options you prefer.

Links: [Aircrack-ng](https://www.aircrack-ng.org/doku.php?id=install_aircrack#installing_on_mac_osx) – [Github](https://github.com/aircrack-ng/aircrack-ng)

### TestSSL (Free)

TestSSL is the best tool to test the SSL configuration of the server you are testing. What I like the most about TestSSL is the clean UI it offers and the simplicity in use. You get different results depending on the device you want to have as a reference and writes in really clean form the possible vulnerabilities of the current configuration.

To install `TestSLL` you firstly have to download the `git` repository from Github. Current stable version is 2.8.

```raw
git clone https://github.com/drwetter/testssl.sh.git
```

Then go to the folder of TestSSL.

```raw
cd testssl.sh/
```

If you want to run TestSSL on a server you can just execute the `.sh` file followed by the URL of the website.

```raw
./testssl.sh google.com
```

Links: [TestSSL](https://testssl.sh/) – [Github](https://github.com/drwetter/testssl.sh/tree/2.8)

### Wappalyzer (Free)

This browser extension is available for both Firefox and Chrome, giving users the ability to really easily identify technologies used on a Web Application. This simple plugin displays versions of web server servers, libraries, programming languages and more. What makes this plugin so helpful is it’s accuracy, how easy is it to use and of course it is open source. I find out about this plugin a few months back and I am using it extensively, so it is worth a shot.

Links: [Firefox](https://addons.mozilla.org/en-US/firefox/addon/wappalyzer/) – [Chrome](https://chrome.google.com/webstore/detail/wappalyzer/gppongmhjkpfnbhagpmjfkannfbllamg) – [Github](https://github.com/AliasIO/Wappalyzer)

### Gobuster (Free)

Great tool for enumerating directories, files and DNS subdomains. What I like about Gobuster is the flexibility if offers with extensions, authentication and mainly support for multithreading. I was mainly using dirb for enumerating files and directories, but what was the biggest concern for me was the fact that dirb does not support multiple threads, and this makes the process really slower. Using brew is it easy to install Gobuster.

```raw
brew install gobuster
```

Links: [Github](https://github.com/OJ/gobuster)

### Ffuf (Free)

Another tool written an Go, with excellent performance and numerous of customisations. Ffuf offers option for directory, DNS and vhost brute-forcing. Ffuf can also be installed using brew, which makes it really convenient.

```raw
brew install fuff
```

Links: [Github](https://github.com/ffuf/ffuf)

### Hashcat (Free)

Great tool for password recovery. Supports almost every known hashing algorithm and masking for password guessing. It can fully utilize your Mac’s performance while it offers great support for GPUs.

```raw
brew install hashcat
```

Links: [Hashcat](https://hashcat.net/hashcat/) – [Github](https://github.com/hashcat/hashcat)

### Impacket (Free)

Impacket is an excellent collection of tools for pentest, mainly oriented around Windows assessments. Impacket offers numerous classes to interact with multiple protocols. Impacket is Python based and the installation happens by cloning the repository and installing its dependancies.

```raw
git clone https://github.com/SecureAuthCorp/impacket
cd impacket
python3 -m pip install .
```

Links: [SecureAuth](https://www.secureauth.com/labs/open-source-tools/impacket/) – [Github](https://github.com/SecureAuthCorp/impacket)

### Responder (Free)

Another Python based application required for every Windows assessment. The perfect tool for rogue type attacks inside the domain. Just clone the repository, navigate to the project, and run the `responder.py` script.

```raw
git clone https://github.com/lgandx/Responder
cd Responder
./Responder.py [options]
```

Links: [Github](https://github.com/lgandx/Responder)

### CrackMapExec (Free)

A post exploitation tool, used in Active Directory assessments, which helps with lateral movement inside the domain. The tools is also python-based and using Impacket for multiple of its functions. CrackMapExec can be installed by using downloading the corresponding binary from their release page.

Links: [Releases](https://github.com/Porchetta-Industries/CrackMapExec/releases) – [Github](https://github.com/Porchetta-Industries/CrackMapExec)

### ADB (Free)

ADB (Android Debug Bridge) is a command-line tool that enables communication between a computer and an Android device. It provides a bridge for developers to execute commands, install and debug applications, and access various device functionalities directly from a computer. Essential for any mobile pentest. The files can be downloaded directly from the Google repo. To install it, just extract the content form the zip and add the directory to your path.

Links: [Google Repo](https://dl.google.com/android/repository/platform-tools-latest-darwin.zip)

### Frida (Free)

Frida is a dynamic instrumentation toolkit used for injecting JavaScript or native code into running processes on multiple platforms. It enables them to monitor and modify application behavior in real-time, perform runtime analysis, and conduct reverse engineering tasks. Frida can be easily installed using pip. By default pip is installed as pip3 on Mac OS.

```raw
 pip install frida-tools
```

Links: [Frida](https://frida.re/) – [Github](https://github.com/frida/frida)

### jdax (Free)

JADX is an open-source tool used for decompiling Android applications, perfect for converting DEX (Dalvik Executable) and APK (Android Package) files back into readable Java source code. jadx can be easily installed using brew. After installing it, in order to run it either run `jadx-gui` on your terminal or run `jadx filename` to run is inside your console.

```raw
 brew install jadx
```

Links: [Github](https://github.com/skylot/jadx)
