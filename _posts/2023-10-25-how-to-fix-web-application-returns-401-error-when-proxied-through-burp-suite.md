---
title: "How to Fix Web Application Returns 401 Error when Proxied through Burp Suite"
date: 2023-10-25T09:38:31
categories: ["Security"]
tags: ["Security", "tutorial"]
image: /assets/uploads/2023/10/New-Project.jpg
---

Burp Suite is the most used web proxy for web application assessments. In an assessment, the configuration of the application required me to use `Platform Authentication` with NTLM to authenticate. When doing that I got 401 error when JS and CSS files were requested.

[![](/assets/uploads/2023/10/Screenshot-2023-10-25-at-11.10.01.png)](/assets/uploads/2023/10/Screenshot-2023-10-25-at-11.10.01.png)

Application returns 401 when .js file is requested and 200 on the main page

Something that I noticed also was that when I intercepted the request and waited for a couple seconds, the page was loading normally, and the responses were 200, which is really weird. This is what led me to write the [Burp Extension](https://marduc812.com/2023/08/02/create-a-burp-suite-extension-using-the-new-montoya-api/) which adds delay between each request.

[![](/assets/uploads/2023/10/Screenshot-2023-10-25-at-11.21.30.png)](/assets/uploads/2023/10/Screenshot-2023-10-25-at-11.21.30.png)

Platform authentication using NTLMv2

It was clear to me that it had something to do with the platform authentication that I was using, because this was the only case that something like this happened.

### The solution

After some troubleshooting, I found out that the error was returned because the application supported `HTTP/2`, which it seems to be too fast (?) for the NTLM authentication. So my unchecking the HTTP/2 option in Burp’s settings, all the requests returned 200. To disable HTTP/2 support, navigate to Settings -> Network -> HTTP -> HTTP/2. This made the application be clearly slower, but at least it was possible to test it.

[![](/assets/uploads/2023/10/Screenshot-2023-10-25-at-11.26.53.png)](/assets/uploads/2023/10/Screenshot-2023-10-25-at-11.26.53.png)

HTTP/2 Support disabled in Burp Suite settings
