---
title: "Aquatone – npm executable not found"
date: 2018-10-10T17:41:52
categories: ["Security", "Tuts"]
tags: ["Security", "tutorial"]
image: /assets/uploads/2018/10/Screenshot-2018-12-20-at-01.01.56.png
---

Aquatone is a great tool, developed by user @michenriksen, used for subdomain takeovers. The reason that I specifically like this tool is because it helps you enumerate subdomains easily, giving you IPs with Open Ports and their matching subdomain.

### How it works

Aquatone is divided in 4 different scripts, `discover`, `gather`, `scan` and `takeover`.

- `discover` – Collects the subdomains of the domain specified
- `scan` – Enumerate Open Ports of hosts identified previously
- `gather` – Enumerate Web Servicies found on those hosts and take screenshots
- `takeover` – Based on standard error messages it will report if a domain is vulnerable or not.

### npm executable not found

#### Error

This error pops up when some is on the gather script. The message is pretty clear to be honest, that npm executable is not present.

#### Solution

Clone `npm` from their official Github https://github.com/npm/cli (*Note is was recently moved from https://github.com/npm/npm*) and install it using `Make`.

```text
git clone https://github.com/npm/cli.git
cd cli
make install
```

##### Verify installation

```text
npm -v
```

### More info

- [@michenriksen](https://michenriksen.com/)
- [Aquatone Github](https://github.com/michenriksen/aquatone)
