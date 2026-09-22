---
title: "Web Application Penetration Testing Methodology"
date: 2019-08-18T09:39:46
categories: ["Security", "Tuts"]
tags: ["Security", "tutorial"]
image: /assets/uploads/2019/08/pentesting_web_Methodology.jpg
---

Most of the penetration tests that I did so far, are Web Applications, since even if it is a thick client application, the functionality of it is heavily based on HTTP communication, using API calls or some times, even just having the mobile view of the website inside a WebView.

I created a Web Application testing checklist for penetration testing, based on the things that I usually check. All the data storing is done on the browser, so you can just save the HTML page on your laptop and use it as a local checklist. Everything is done with pure JavaScript so you just need the HTML file and a browser that supports `LocalStorage`, that if I’m not wrong, every browser does it.

Below I will explain all the issues, listed on this checklist.

[Web Application Pentest Checklist](https://marduc812.com/checklist/web.html)

**Note**: This list of issues is still WIP. More items will be added soon.

## → Information Gathering

### Crawling / File Enumeration

After a scope is specified for a Web Application pentest, fire up your favourite directory brute-force tool and feed it a list in order to identify files and folder for your in-scope domain. After some folders are found, it can help you identify the technology in use. In case you use Burp Suite you can use its crawler that is great, also the functionality for content discovery. You can read further information about Burp Suite and tips [here](https://marduc812.com/2019/01/21/burp-suite-battle-royale-edition/).

##### Reference

- [GoBuster](https://github.com/OJ/gobuster)
- [DirBuster](https://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)
- [BurpSuite](https://portswigger.net/burp)
- [Wordlist](https://github.com/danielmiessler/SecLists)
  and way way more tools.

---

### Identify Technologies in Use

This part can be easily using automated tools an extension. This part helps you understand, what possible issues can be identified. For example if an application uses `Angular JS`, you know that probably if the developers tried really hard to make the application bad, it can be a javascript sandbox escape and you could find an XSS. Knowing what you have to deal with makes everything easier always.

##### Tools

- [Wappalyzer browser extension](https://www.wappalyzer.com)
- [Nikto](https://cirt.net/Nikto2)
- [SimilarTech](https://www.similartech.com/)
- [BurpSuite](https://portswigger.net/burp)

---

### HTTP Headers

Some times, if you have nothing to report, findings those headers helps (a bit). Although, if there is exploit or an actual issue, I believe it is pointless to report it, but at least you can find some information about what type of Web Server is in use. Just intercept the request with your favourite proxy and check for the response. If the `Server` header is there, then probably you got some extra info.

##### Reference

- [OWASP – Fingerprinting Web Servers](https://www.owasp.org/index.php/Fingerprint_Web_Server_(OTG-INFO-002))

---

### Information Disclosure through Error Messages

Although the title is pretty self explanatory, the goal of this part is to give the application input that would result in some form of error. This error, if there is no proper error handling, can return paths, filenames, names of users, help you with an XSS, disclose the architecture of the application and more. In order to trigger those error, try to break the syntax of the application, or specify some characters that are “blacklisted”. A lot of time, if you will request for a file with random name, containing special symbols will result in a 500 error. In case this 500 error prints the requested page, this could lead on an XSS. Of course this is an example, and errors can be found with way way to many ways.

##### Reference

- [OWASP – Improper Error Handling](https://www.owasp.org/index.php/Improper_Error_Handling)

---

### Outdated Software / Libraries

Finding libraries with known vulnerabilities can be helpful for web applications, only if the vulnerable function is in use. A lot of times, there are reports for vulnerabilities in functions of libraries that are never used. In case the vulnerable function is not used, this vulnerability will be almost impossible to trigger on its own. But of course, this does not mean that if the library or the software stays the same, the vulnerable function will not be used in newer releases of the application.

##### Reference

- [Vulners (Burp / Browser / Nmap plugins)](https://vulners.com/products)
- [BurpSuite](https://portswigger.net/burp)
- Google.com ALWAYS
- Like always, manual testing.

---

### Directory Listing Enabled

Nowadays, directory listing is not enabled by default for most of the public software. It is not so common (but it still happens) to find inside directories files, that can contain helpful information like credentials from the application development period. Even if the files do not contain any passwords, you can almost always extract useful information and also save time from your file enumeration process.

##### Reference

- [BurpSuite](https://portswigger.net/burp)
- Use tools listed on [Crawling / File Enumeration](#crawling--file-enumeration) step

---

### User Roles

All the applications have different user roles. Those roles usually are:

- Unauthenticated User
- Registered User
- User with elevated privileges
- Administrators

`Unauthenticated users` are all the users that are not registered to the application and normally should have the lowest possible access. When a user is `registered`, his access should be only for the files that he owns. Users with `elevated privileges` are users that can have permissions to moderate one part of the application, like for example a moderator on a Facebook page. His permissions are clearly higher that a simple user, but he does not have full permissions on the application. Finally, `administrators` are the users that can change the configuration of the application. Usually administrators have full control on the application, including its users and data (but this does not mean that they can read or modify them).

##### Reference

Once again, those users role can be identified by exploring manually the application.

---

### Business Logic

In order to find a way to bypass something (authentication, processes etc.) or exploit an issue, the first thing to do is to understand how the application works, and what is the `goal` of the application. The applications usually follow some patterns that are specific. for example an online market applications, the steps will be like that.

1. You put your items in your basket
2. Finalise your order and proceed to payment
3. Complete the payment and get redirected back to the application
4. When the main application loads you get the confirmation of sucess.

But what will happen if you skip step 3 and load directly step 4. Will the application accept the order as complete? Will it tell you that you don’t have the token that it expected?

##### Reference

- [Harvesting all private invites on h1](https://hackerone.com/reports/334205)

---

## → Input Validation / Injections

### Cross-Site Scripting (XSS)

Cross-Site Scripting occurs when users’ input is not escaped and it is getting shown back to the end user. HackerOne lists XSS as number vulnerability reported with quiet high rewards. XSS can be split in 3 main categories that is `Reflected`, `Stored` and `DOM-Based`.

#### Reflected XSS

User interaction is required and usually it can be exploited by sending a link to the victim. This interaction is required because the payload is not stored anywhere. An example that a reflected XSS can be found is on a `search` field.

#### Stored XSS

Stored XSS happens when users’ input is stored on a database and when the page that contains this text is called, the text is printed to the end user braking the HTML syntax, allowing the execution of JavaScript. Stored XSS can be commonly found on places where information about users or items is stored like Names, Addresses etc.

#### DOM-Based XSS

Modern applications load its content dynamically. In this case a DOM-Based XSS occurs when the printed text is taken from the URL (for example). Let’s say you have a page that displays the temperature in a city and the URL looks like that `http://example.com/?city=london`.
In this case london will be parsed from the URL and get printed inside the HTML code. The page will load the URL, split it in parts using the `?` as a separator and on the second part it will parse `city=london`. Then it will split that in half using the `=` to identify as item[0] the variable name and item[1] the value of it. In case an attacker uses something like that `city=<script>alert('xss')</script>`, the application will parse the malicious payload as a city name, that will then print on the page, resulting on a XSS. Of course modern browsers protect users from those easily guessable payloads, but you can always find a bypass based on the characters allowed.

##### Reference

- [OWASP XSS](https://www.owasp.org/index.php/Cross-site_Scripting_(XSS))
- [EdOverflow Bug Bounty Cheatsheets](https://github.com/EdOverflow/bugbounty-cheatsheet/blob/master/cheatsheets/xss.md)
- [h1 Great XSS by Zemnmez](https://hackerone.com/reports/409850)

**Note**: For me, the best way to do it is manually, just by sending a list of characters that you need for your XSS and try to create a valid payload using only characters that are not escaped.

---

### SQL / NoSQL Injections

Databases are used to store information needed for the application. Most databases use SQL type `queries` to add/delete/modify the content. Of course there are some languages that do not use the SQL language for queries, like MongoDB.

#### SQL Injection

An SQL injection occurs when developers do not validate users’ input, by adding the input directly to the database query. This way attackers are able to break the SQL syntax and inject SQL commands of their choice. The impact of this vulnerability varies depending on the configuration of the database. Sometimes attackers are able to temper data of the database and in some cases they are able just to read a part of it. Like XSS, there are multiple types of SQL Injections.

- Classic SQL injection
- Blind
- Error-Based
- Boolean-Based
- Time-Based
- Union-Based

#### NoSQL Injection

In NoSQL injection the idea is the same, inject content on a query done to the database, with the difference that the payload is the same. A single quote `'`, will not break the syntax. The syntax for NoSQL is different since operators like `ne` or `gt` are used. Of course, you can inject complete statements and not just comparisons, using a `$`, that it can be used as an operator.

##### Reference

- [OWASP SQL Injection](https://www.owasp.org/index.php/Testing_for_SQL_Injection_(OTG-INPVAL-005))
- [OWASP NoSQL Injection](https://www.owasp.org/index.php/Testing_for_NoSQL_injection)
- [h1 User-Agent SQLi](https://hackerone.com/reports/297478)
- [h1 GraphQL SQLi](https://hackerone.com/reports/435066)

---

### Server Side Includes

This issue is not so common, but in case `SSI` is enabled and misconfigured, it is highly possible that will end up with a Remote Code Execution. SSI is a technology used by the web server to update content dynamically. this can be a date, an IP of the server, or sometimes it can be a command that will return all the files inside a folder of the server. In order to test for it, try to insert a test payload like `<!--#printenv -->`. In case the SSI works, after the page is printed back to you, the environment variables should be visible. Keep in mind, that if SSI works, then probably there is also an XSS on this field and vice versa.

##### Reference

- [SSI Owasp](https://www.owasp.org/index.php/Server-Side_Includes_(SSI)_Injection)
- [List of Payloads](https://marduc812.com/2018/03/24/list-of-ssi-payloads)

---

### Server Side Request Forgery

This vulnerability is also probably a not so commonly seen vulnerability, but definitely a highly paid one. Using this vulnerability, it is possible to retrieve files, access internal networks and more. This is done by inserting a `URI` different than the one the server expected. For example let’s say there is an application that allows it’s users to download a YouTube video and save it to mp3 format. The Application has to connect to a URL supplied by the user in order to get the video. Let’s say that the application, shows a preview of the video while downloading the content, so there is a way to see the impact of the attack.

An attacker can use a URI that looks like that `file:///etc/password` and test if the application will actually return the content of the passwd file. Additionally, there are multiple type of URI schemes that are supported. Let’s say that this only allows http/s and nothing else. What an attacker can do is request for a website like `http://localhost`. Will the application serve localhost’s content to him? Finally, SSRF can be used for `Port Scanning`, by measuring the response time or an error message. For example, using something like `http://localhost:22` and `http://localhost:5555`. In case the error messages are different you can understand if a port is open or not.

##### References

- [OWASP SSRF](https://www.owasp.org/index.php/Server_Side_Request_Forgery)
- [h1 SSRF](https://hackerone.com/reports/386292)

---

### Cross Side Request Forgery

The internet is built on the same principal of exchanging messages (requests), in order to retrieve information about a website. When CSRF occurs, an attacker can force his victim, do something unintentional like change his password, or make a post. This happens because the server receives a request on behalf of the victim, but it does not validate if the request was sent actually from the user. Exploiting CSRF is simple as also as identifying it. If the request does not contain a token that is dynamic, then probably the application is affected by a CSRF. In case the application uses JSON and validates the content type, you can use flash in order to send a valid request on behalf of the victim, more info can be found [here](http://blog.cm2.pw/forging-content-type-header-with-flash/).

##### Reference

- [OWASP CSRF](https://www.owasp.org/index.php/Cross-Site_Request_Forgery_(CSRF))
- [h1 CSRF](https://hackerone.com/reports/127703)

---

### Cross-Origin Resource Sharing (CORS)

CORS is a mechanism that instructs a web browser is a web application should run on a specific domain or not. Of course this can be more complicated when the authentication happens on other domains. CORS header is shown as `Origin:` on requests and the first thing to do is try to change the origin from the actual site to something malicious. In case the response contains the following `Access-Control-Allow-Origin: *` and `Access-Control-Allow-Credentials: true` then it is highly possible that some valuable information can be retrieved. Additionally, some applications allow only domains that are `*.example.com`. Of course if you have no valid subdomain then it is impossible to exploit it, but it can be chained with a subdomain takeover, resulting in full exploit capabilities.

##### Reference

- [Mozilla CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
- [h1 CORS](https://hackerone.com/reports/470298)
- [CORS PoC (TrustedSec)](https://github.com/trustedsec/cors-poc)

---

### XML / LDAP / Command Injection

At this moment you need to validate if your input is handled properly or now. It is common for developers to be lazy or have strict timelines, making them develop functionalities in a clumsy way, resulting in introduction of injection attacks. Vulnerabilities like XSS and SQL injections are also injection attacks, but XML, LDAP and command injection are not so common, so they have for me a different category.

#### XML Injection

XML stands for Extensible Markup Language, and it is commonly used in web applications, mainly in API tests with form of SOAP requests. A lot of applications also use it on the back end while the front is JSON. If you have an application that takes JSON input, I would suggest you to use the `Content Type Converter` that will convert JSON to XML and vice versa. In order to identify is there is an injection you can use a character like a single quote and see if it affects the parser. In case there is an injection, most likely you will see an XML error. From there you can usually play with the entities, and check if you can use them in order to inject code, create an XML bomb, or retrieve some files. XML injection can result in Local File Inclusion, command injection and way more things.

##### Tools

- [BurpSuite](https://portswigger.net/burp)
- [XXEinjector](https://github.com/enjoiz/XXEinjector)

*I personally prefer to go manually for those issues, that using automated tools.*

#### LDAP Injection

Applications sometimes use LDAP to authenticate their users and this is done by doing LDAP queries from what the user supplied. For example when a user signs in, a username and a password is required. Then user’s input is transferred to the LDAP server and results are returned. In case the user does not use his username but an asterisk (\*), the LDAP query will run with a wildcard. in order to test if further multiple characters can be used like `(`, `*`, `|` and `&`.

##### Tools

- [BurpSuite](https://portswigger.net/burp)
- [LDAP Admin](http://www.ldapadmin.org)

#### Command Injection

Command injection is difficult to identify just by accessing the application, but in case you will find it, it means $$$$$$$. The easiest option to find command injection in my opinion is just by reading the source code. For operations like pinging a host or connecting to a server, a lot of times developers do it just by sending commands directly to the system. The goal of this issue is to break the syntax and inject your commands. Using `;` or `&&` or `|`, it is likely that you will be able to inject your commands on the system and get them executed.

##### Tools

- [BurpSuite](https://portswigger.net/burp)

##### Reference

- [OWASP Commands Injection](https://www.owasp.org/index.php/Testing_for_Command_Injection_(OTG-INPVAL-013))

---

### Open Redirect

Open redirect refers to the fact that an application does not limit the URL that the user will get redirected to, after completing an action. This happens usually when the application accepts the redirect location from a field that is user control and does not validate the domain of the redirect. This can be exploited mainly for Phishing attacks in the following way. A user wants to access his `google.com` account. When an Open Redirect occurs, a malicious actor can use the actual google.com domain but with a URL like this `https://google.com?auth_redir=https://attacker.com`. This can help also bypass some spam filters, since the origin of the domain is a valid one. In case there is validation for the URL of redirect, you can try to identify how it happens, what exactly is it checking. Can you have a domain like `google.attacker.com` that would trick the filter, or could it be bypassed by using the Right to Left `RTLO` character https://google.com%40%E2%80%AE@moc.rekcatta

##### Reference

- [OWASP Open Redirect](https://www.owasp.org/index.php/Testing_for_Client_Side_URL_Redirect_(OTG-CLIENT-004))
- [h1 Open Redirect](https://hackerone.com/reports/299403)

---

### Path Traversal

Sometimes also called directory traversal, refers to a vulnerability of a web application to validate the path of a file requested by a user. Using a payload with dots and slashes `../../../`, an attacker tries to go out of the directory that the application is configured to work from and reach the root directory in order to retrieve files that would give him some extra information, like reading /etc/passwd or the hosts file. Path traversal is easier to exploit on a Linux server mainly because of the standard files found there. For Windows I try to use payload that specific to the OS version with less luck. When a Path Traversal occurs, it does not have any impact in the availability of the server or the integrity, its main impact is information disclosure.

##### References

- [OWASP Path Traversal](https://www.owasp.org/index.php/Path_Traversal)
- [h1 Path Traversal](https://hackerone.com/reports/310943)

---

### Local / Remote File Includes

A vulnerability that I have mainly seen on OSCP than in real life, it can occasionally lead to Remote Code Execution. The impact of this vulnerability is high because a malicious user is able to access a file in context of the application. What it means is that the server will load every file requested by the user. In case of an LFI, the server will load and execute (if possible) a local file, like instructed by the attacker. The difference with Path Traversal is that when a path traversal is exploited, the attacker cannot execute code, he can retrieve files, but in case of an LFI, usually code is executed also.

When an RFI vulnerability is identified, the easiest option is to set up a `Web Server` and serve the file for the application directly. That way the Web Application will load our malicious file and executed on the context of the application, usually resulting in RCE. Sometimes the server will not connect to an HTTP server, in this case set up a network share and test if the web server will access your `SMB Share`.

#### References

- [OWASP RFI](https://www.owasp.org/index.php/Testing_for_Remote_File_Inclusion)
- [h1 CTF LFI to RCE](https://hackerone.com/reports/415233)
- [LFI on IKEA](https://medium.com/@jonathanbouman/local-file-inclusion-at-ikea-com-e695ed64d82f)

---

### HTTP Request Smuggling

This issue came in my attention recently, after James Kettle from PortSwigger, showed how it is possible to trick a Proxy into processing multiple requests at once. This happens because both the `Transfer-Encoding` and the `Content-Length` headers are getting submitted, tricking the proxy into believing that there is one request. The content length of the request should cover all the first request making the front-end process the request without seeing anything suspicious. After the request is accepted, the proxy will see that the request is actually split in multiple parts because of the `chunked` Transfer Encoding header but it will be processed separately because of the Content-Length header.

This is quite a smart approach and in my opinion is worth it 100% to spend some time reading how to test for it. My explanation is really generic and PortSwigger explain this issue in way more depth, with nice examples.

##### Reference

- [PortSwigger Blog](https://portswigger.net/blog/http-desync-attacks-request-smuggling-reborn)
- [PortSwigger Paper](https://portswigger.net/kb/papers/z7ow0oy8/http-desync-attacks.pdf)
- [h1 Report](https://hackerone.com/reports/498052)
  –[BurpSuite Extension](https://github.com/portswigger/http-request-smuggler)

## → Session

### Session ID Entropy

This issue is not so common nowadays, mainly because people are getting more informed about security. Entropy refers to amount of "randomness" that there is on an item, in this case a session token. This issue occurs when a session token, is generated without enough entropy. An example can be a session token that every time a user is signing in is increasing by one. Or a session token that has only 4 digits of randomness.

##### Reference

- [OWASP Session Entropy / Length](https://www.owasp.org/index.php/Insufficient_Session-ID_Length)

---

### Improper Session Termination

This issue is quite common, and referees to the fact that a session token, is still active after a user requested for the termination of it, by logging out. This issue is not exploitable by itself, but it is an extra security measure. In order to test it, send a valid request and store it on Repeater or save the session token somewhere. After that, log out of the account and send again the previous request, with the token that you requested to terminate. In case the request is accepted by the server, then it is possible to understand that the server is not ‘killing’ the session directly after the user logs out.

##### Reference

- [OWASP Testing for Logout Functionality](https://www.owasp.org/index.php/Testing_for_logout_functionality_(OTG-SESS-006))
- [h1 Report on Twitter](https://hackerone.com/reports/347748)

---

### Session Fixation

This vulnerability occurs when an application takes a session cookie from a url. For example, an application uses the following process for session creation. The user loads the page and gets a visitor token, lets say it’s `visitorToken1`. After the user clicks on sign in, this token is passed to the login page with a url looking like this `http://example.com/signin?ses=visitorToken1`. After the user signs in successfully, the application authorises the cookie and gives it the required permissions to access user’s data.

In case a malicious actor send to the victim a malicious url like this, `http://example.com/signin?ses=attackerToken1` and the user logs in, the attacker is able to use the cookie he sent to his victim and highjack his session.

##### Reference

- [OWASP Session Fixation](https://www.owasp.org/index.php/Session_fixation)
- [h1 Report](https://hackerone.com/reports/423136)

---

### Cookies Poisoning

This is mainly an issue from the past, since more and more frameworks are used for development of applications. This issue has to do with session cookies that when edited will give extra permissions to the user. Imagine there is a cookie that looks like this: `eyJ1c3IiOiJuaWNrIiwicm9sZSI6Imd1ZXN0In0=`. The first thing to do is base64 decode the cookie and check if there are any printable characters. The result will look like this `{"usr":"nick","role":"guest"}`. This means that the permissions of the user are held inside the cookie. By changing the role field into something like Admin or Moderator can give an simple user administrative privileges. Then by editing the cookie and base63 encoding it back, it is possible to bypass the account restrictions.

---

### Clickjacking

This vulnerability is still present to multiple applications and I like to NOT refer to it as a User Interface redress attack. The goal of this attack is to show a valid website inside an iframe, that is covered by a completely different view, tricking the user into doing unintended actions. This can be done for example by sending a link to a user that will tell them that they won a car and asking them to do some clicks on specific locations of the browser. On the background they actually click on the vulnerable website, meaning that they are actually messing with their account. OWASP offers a nice and simple PoC page that you just have to replace a link and most of the cases it is enough. Although, it is always better to spend some time and make your findings a bit better.

##### References

- [OWASP Clickjacking & PoC](https://www.owasp.org/index.php/Testing_for_Clickjacking_(OTG-CLIENT-009))
- [Twitter Clickjacking on h1](https://hackerone.com/reports/85624)

---

### Session Cookies Without Flags

This is the type of finding that you use as reference when you have findings at all. It usually goes like this. Did you find anything bro? Pwned them bad with those cookies without secure flags. This means that you desperate in a few words. The whole point is that cookie flags like `http-only` and `secure` protect the user from possible attacks. In case there is an XSS for example, if the http-only flag is set, the attacker will not be able to steal the session cookie, because JavaScript will not be able to reach it. The same with the secure flag, that prevents the session cookie from going over an unencrypted channel. It is important to understand that those flags are not required for cookies that store information like website theme or cookies for tracking. Also a lot of applications are heavily based on JavaScript and when a session cookie has the http-only flag set, it is really likely that the application will break.

##### References

- [Mozilla Cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
- [OWASP Cookies](https://www.owasp.org/index.php/Testing_for_cookies_attributes_(OTG-SESS-002))

---

### HTTP Strict Transport Security

Strict Transport Security or otherwise `HSTS` is an HTTP response header, that instructs the browser to only accept https connections from this website. This issue is difficult to exploit, because the attacker needs to have the ability of intercepting the requests, meaning that you need a man in the middle. Although it is difficult to exploit, in case the header is not set, the attacker is able to downgrade the connection and intercept confidential information like credentials.

##### References

- [Mozilla Firefox HSTS](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security)
- [h1 Report HSTS](https://hackerone.com/reports/158186)

## → Cryptography

### Algorithms & Ciphers

These issues are mainly reported for informational purpose and are exploitable really rarely. In order to identify weak algorithms and ciphers you can use `sslscan` that is installed by default on Linux Kali. Sslscan has nice colouring to distinguish the quality of the algos and ciphers. One tool that I personally prefer over sslscan it `TestSSL`. I prefer because it tried multiple browsers and devices, and shows which protocols are supported based on the device that it is getting loaded for. A small addition that could make your report even more professional is to use `OpenSSL` directly. In some cases OpenSSL would lack of ciphers reported, mainly because it is too old. In this case you can download older builds of OpenSSL and try to connect to the web server in scope using directly the OpenSSL client.

##### References

- [TestSSL](https://testssl.sh)
- [Old Precompiled OpenSSL Releases](https://www.npcglib.org/~stathis/blog/precompiled-openssl-past/)

---

### Self-Signed Certificates

For me seeing Self-Signed certificates is not such a big issue, mainly I know that it would be either a self signed certificate or completely unencrypted communication. The problem of self-signed certificates comes when users develop a habit of trusting every certificate. Self-signed certificates additionally is a bit more difficult for companies to manage them. Finally, a self-signed certificate on a domain like `facebook.com` is clearly an indicator of compromise, but when it is on the status page of a printer it does not help at all.

##### References

- [What is a Self-Signed Certificate?](https://aboutssl.org/what-is-self-sign-certificate/)

---

### Improper Password Storage

You will wonder how it this a crypto issue. I consider that a crypto issue when there are still cases of companies that store their passwords in clear text. Of course there are cases that encryption is used, but of course this is not the proper way to store passwords (with rare rare exceptions), while stored passwords should not be decryptable. This issue is hard to identify on a pentest, since you don’t usually reach that level of compromise. An indicator that your password is not most probably saved securely is cases that it warns you that your new password is too similar the the previous one. If you didn’t enter your current password during the password change process, your password is not saved securely at all.

##### Refereces

- [Facebook – Clear-text passwords for Instagram 2019](https://www.theverge.com/2019/4/18/18485599/facebook-instagram-passwords-plain-text-millions-users)
- [Twitter Bug stores credentials in clear-text 2018](https://www.zdnet.com/article/twitter-says-bug-exposed-passwords-in-plaintext/)

---

### Lack of SSL

Most of the websites tested are using SSL. Now with services like Let’s Encrypt it is really easy to generate certificates, so most companies use SSL. Finding that there is no SSL is quite simple because due to lack of `https` from the website. For your screenshots probably you can show a warning from your complaining browser, or how I like to do it, is run tcpdump and show that there is no encryption, and it is possible for an eavesdropper to intercept all the communication.

##### Reference

- [OWASP Lack of SSL](https://www.owasp.org/index.php/Top_10_2014-I4_Lack_of_Transport_Encryption)

## → Authorization

### Insecure Direct Object Reference

Insecure Direct Object Reference aka `IDOR` is an issue that occurs where there is no validation about the permissions of the user that requests for a file or an action. This issue is more common that expected and can be easily identified by changing IDs for the reference item. For example in case the application sends a request containing information like this `http://example.com/orderID?id=12`, all you have to do is brute-force the id field. This can be done easily using Intruder on BurpSuite or any custom scripting language of your choice. The application should always validate user’s permissions before sending the requested file to the user.

##### Reference

- [h1 IDOR on Shopify](https://hackerone.com/reports/318751)
- [OWASP – Testing for IDOR](https://www.owasp.org/index.php/Testing_for_Insecure_Direct_Object_References_(OTG-AUTHZ-004))

---

### Default / Easily Guessable Passwords

The easiest option for an attacker to get access on a system. Passwords like admin / admin are everywhere, mainly because users are lazy and don’t change the default password. To find the default password of an application, Google is your friend. Possibly this can be automated but it will not help you finding passwords that are easy to guess. What I like to do is try for top 10 common passwords that has still in 2019 crazy success rate compared to its complexity.

##### Reference

- [h1 SAP default password on Starbucks](https://hackerone.com/reports/195163)
- [Github Awesome Default Passwords](https://github.com/nyxxxie/awesome-default-passwords)

---

### Hardcoded Credentials in Files

Hardcoded credentials is an easier method than default credentials for attackers to login. This issue happens on big companies, that hardcode their API keys or Session Tokens to their code and push it to their Git. This issue can be present also on JavaScript files, that usually young developers hardcode credentials to do some calls. Those credentials can be retrieved and used for authorisation. You can find API keys using RegEx. After finding a key you can follow the tutorial from Keyhacks and do some calls with curl in order to validate if the issue identified is valid.

##### Reference

- [Github – Keyhacks](https://github.com/streaak/keyhacks)
- [h1 Application Hardcoded keys](https://hackerone.com/reports/351555)
- [h1 Snapchat hardcoded keys](https://hackerone.com/reports/396467)

---

### No Brute Force Protection

This issue is reported a lot, because it is really easy to find, you find a request for a specific purpose, let’s say you have a discount page and you want to find a big discount. All you have to do is get the request, select the variable used as coupon code and send it to intruder. Normally, those issues have low impact, since most of the modern services, use tokens with high entropy which is difficult to brute force. In case you find something, it is always good to report and probably you could get some $$.

##### Reference

- [OWASP – Testing for Brute-Force](https://www.owasp.org/index.php/Testing_for_Brute_Force_(OWASP-AT-004))
- [h1 Spam mails without Rate Limit](https://hackerone.com/reports/297359)

---

### Unauthenticated Admin Access

I faced this issue mainly while I was testing Embedded devices, like medical or industrial. What happens is that this is a control panel for a device. Users that access the Web Server have automatically in front of them, all the controls of the device. I don’t believe it is likely, to face this issue on a bug bounty program to be honest.

---

### Unrestricted File Upload

All the applications nowadays, allow users to upload their files on the server, either it is in a form of a profile picture either in form of file hosting. It is good to always validate the type of files users are uploading on the server. In case there is a limitation for specific file type, consider the user of double extension like `.php.jpg`, or play with the `content-type`. Additionally, in case there is file upload on the server, you can try to attach some code on it. In case the application loads the file in order to render it, it is possible that the application will execute the code.

##### Reference

- [OWASP – Unrestricted File Upload](https://www.owasp.org/index.php/Unrestricted_File_Upload)
- [h1 Report](https://hackerone.com/reports/305237)

---

### Lack of Antivirus Solution

This is clearly not an exact authorization issue, it is more like a hardening issue, but I consider that a valid case for a web application, where users don’t use it as a storage. For example an application that is used to store your pdf presentations, should have some kind of protection. The easiest way to test the presence of an Anti-Virus is to use the Eicar string / code. You can save `X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE !$H+H*` it into a file and upload it on the server. The ideal situation for the server would be to delete the file and notify the user. Of course this is not always the case, but with Eicar, you can test everything safely.

##### Reference

- [Eicar code](https://www.eicar.org/?page_id=3950)

---

## → Denial of Service

### Account lock out

That issue is common, and in my opinion the account lockout it is more common than it should be. In order to test for account lookout, either create an account that you don’t care about and try to brute-force the login, or have it as your last test case. In my opinion using captcha verification, is a way better method, that locking out the account. In case account lock out is implemented, an attacker can constantly brute-force thousands of accounts resulting in massive DoS, for the legitimate users and loads of work for the admins.

##### Reference

- [OWASP – Testing for lock out](https://www.owasp.org/index.php/Testing_for_Weak_lock_out_mechanism_(OTG-AUTHN-003))

---

### Cache Poisoning

This issue came in my attention because of a report by albinowax on hackerone for hackerone. So the whole idea behind this smart attack, is that you can send a link to the victim, that will make the website unavailable for him. In this case, the attacker by sending the victim to run the following command `curl -H 'X-Forwarded-Port: 123' https://www.website.com/index.php?dontpoisoneveryone=1`, makes the browser of the victim go to the right domain, but connect on port 123. The application, caches the state, resulting in a DoS condition. This is such a great attack and smart DoS, since it does not Denials the Service for the system, but just for one account.

##### Reference

- [h1 Report](https://hackerone.com/reports/409370)
- [PortSwigger – Cache Poisoning](https://portswigger.net/research/practical-web-cache-poisoning)

---

This is the end of the test cases I had in mind and are listed on the checklist. I plan to update it with any cool cases that grab my attention and some suggestions are always welcome. My coding knowledge is not the best and it is not clearly the best code you will read, but it does the job. When I will have some time, I want to:

- [ ] Set name for project
- [ ] Leave notes for every issue

Thanks for the read
