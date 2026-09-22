---
title: "How to fix slow performance of Windows 10 in VMware Fusion"
date: 2022-05-15T14:06:09
categories: ["Windows"]
tags: ["Mac", "Windows"]
image: /assets/uploads/2022/05/windows-10-vmware-fusion-slow.jpeg
---

I am using relatively often Windows 10 virtual machines with VMware Fusion and I noticed that while it had enough RAM and CPU the performance was really slow.

My initial thought was. that it was happening because I was [running WSL2 on the virtual machine](https://marduc812.com/2020/11/30/how-to-install-wsl2-inside-vmware-fusion-virtual-machine/), but it was using half the resources of my Mac, and still it was really slow. The minimum requirements for Windows 10 are 1GHz processor, 2GB of RAM and 20GB of storage. In my case the Windows 10 VM had 16GB of RAM and 100GB of storage, while 2 cores out of the 4 cores were used by VM and still it was extremely slow.

The solution was brought by a post on VMware forums, suggesting to set the following options to the `.vmx` config file.

```
mainMem.backing = "swap"
scsi0:0.virtualSSD = 1
MemTrimRate = "0"
sched.mem.pshare.enable = "FALSE"
MemAllowAutoScaleDown = "FALSE"
logging = "FALSE"
```

- `mainMem.backing` disables storage of the VM’s memory on the hard disk
- `scsi0:0.virtualSSD` optimizes the VM to work on SSD
- `MemTrimRate` prevents the host system from using unused VM memory
- `sched.mem.pshare.enable` disabled memory sharing between virtual machines
- `MemAllowAutoScaleDown` prevents dynamic scale down of memory
- `logging` disables VM event logging

Happy hacking!
