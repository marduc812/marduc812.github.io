---
title: "How to install WSL2 inside VMware Fusion Virtual Machine"
date: 2020-11-30T17:37:54
categories: ["Tuts"]
tags: ["Security", "tutorial"]
image: /assets/uploads/2020/11/wsl2-vmware-fusion.jpg
---

In case you are here you know already what WSL2 is and why to use it. For those who don’t know I will just say that it helps you run a Linux distribution inside your Windows operating system.

The main reason I wanted to upgrade from version 1 to version 2 was due to lack of full support for Nmap. So the setup looks like the picture below, these are the steps you need to follow.

![](/assets/uploads/2020/11/wsl2_vmware_fusion.png)

#### Enable the Hypervisor

This is something that is different that from what people need when running WSL 2 directly from their main OS. In order to enable the hypervisor on VMware Fusion, shut down the virtual machine.
Then inside the VMware Fusion application select your Windows VM and go to `Virtual Machine` -> `Settings` -> `Processors & Memory` -> select `Advanced options` -> tik the `Enable hypervisor application in this virtual machine` option.

This took me some time to figure out, since I was used to change these settings from BIOS, but if you enter the BIOS setup on your Windows Virtual machine, you won’t find any of those settings.

![](/assets/uploads/2020/11/hypervisor_vmware_fusion.png)

#### Enable Virtual Machines

Run the following command in CMD or PowerShell with your Administrator account

```
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

#### Enable WSL feature on Windows

```
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /norestart
```

#### Install WSL2 kernel updates

Download the latest kernel for WSL2 based on your system’s architecture from Microsoft’s website and install it like a normal program.   
[Download](https://docs.microsoft.com/en-us/windows/wsl/wsl2-kernel)

#### Set version 2 of WSL as default

```
wsl --set-default-version 2
```

#### Install your Linux Distribution

You can download any Linux flavour you want from the Microsoft Store. You do not have to login or register to download, a think that makes it perfect. In this case I selected to install Ubuntu. After download is complete, you can launch your downloaded distribution and set it up, be creating your user.

![](/assets/uploads/2020/11/Screenshot-2020-11-30-at-18.20.39.png)

#### Uninstall a WSL2 Virtual Machine

You can uninstall any installed distribution as any other program from Windows. In this case I am uninstalling the Ubuntu distribution I just installed.

![](/assets/uploads/2020/11/wsl2_ubuntu_uninstall.png)
