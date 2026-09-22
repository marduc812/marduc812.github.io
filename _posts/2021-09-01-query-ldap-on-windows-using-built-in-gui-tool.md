---
title: "Query LDAP on Windows using built-in GUI tool"
date: 2021-09-01T17:55:53
categories: ["Windows"]
tags: ["Tool", "Windows"]
image: /assets/uploads/2021/09/windows-ldap-query-tool.jpeg
---

During an assessment I was able to get PowerShell on a box, but it was limited by the Domain Admins and it was not allowed to retrieve information about users from the domain.

Using `net user /domain` was not allowed and was returning the following error.

```raw
PS C:\> net user /domain
The request will be processed at a domain controller for domain DOMAINNAME.

System error 5 has occurred.

Access is denied.
```

Because I wanted to go through the description field, in case a password is pasted there by accident, I remembered of this useful tool. After running the command below, it displayed the Windows LDAP query tool, which made the process really smooth. This tool can be also useful for red teaming exercises.

```powershell
C:\Windows\System32\rundll32.exe dsquery.dll,OpenQueryWindow
```

[![](/assets/uploads/2021/09/ldap-query-windows-tool.png)](/assets/uploads/2021/09/ldap-query-windows-tool.png)
