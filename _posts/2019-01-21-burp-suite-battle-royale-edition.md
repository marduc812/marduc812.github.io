---
title: "Burp Suite &#8211; Battle Royale Edition"
date: 2019-01-21T22:15:43
categories: ["Security", "Tuts"]
tags: ["Security", "tutorial"]
image: /assets/uploads/2019/01/burp-suite-battle-royale.jpg
---

Everyone who doesn’t live under a rock, knows and probably used Burp Suite, by PortSwigger. Recently a Beta 2.0 version was released with multiple new features and a new dashboard to control all the processing running, from one tab. In this post I will write about some features of Burp, that I found useful and I use almost daily to make my life easier.

### Scope

Having the right scope is the first thing to start with. By saying scope, you know that in tests, scope can vary from a simple page to a complete domain (the best case in my opinion).

Let’s say for example that the website in scope is `sub.example.com`. To specify which domain is in scope, go to `Target` tab and then `Scope`. There is an option `use advanced scope control`, and by enabling that you can customise the scope that you want want to have on your website, either it’s one domain or a subdomain. Click `Paste URL` and Burp, will fill the fields for you. You will see something like that:

![](/assets/uploads/2019/01/scope1-1.jpg)

In case you want all domains of example.com to be in scope,  
 replace sub with an asterisk, so it will be `^*\.example\.com$`

In case you don’t care about the Port or the File path, you can leave them empty and Burp will handle it as a wildcard.
You can limit Burp, to show only items in scope, by going to `Proxy` -> `HTTP history` -> Click on `Filter` field and enable `Show only in scope items`. The same way can be done for `Site map`.

### Enumeration

The main way I enumerated content is by using gobuster, useful for directory and DNS enumeration. Recently, I found out that Burp, for multiple versions now, gives the option to find content of the website using its `Discover Content` functionality. This feature can be used by going to `Target` -> `Sitemap` -> Right click on the domain in scope -> `Engagement tools` and `Discover content`.

There, you can specify what kind of enumeration you want to do, if it is files only, directories or both, what type of file extensions Burp should look for, depth, number of threads and more. The advantage that I can find in this way of enumerating instead of using another tool, is that you can have better project structure inside Site Map with every request and its response.

### Intruder

Intruder is used for brute forcing but mainly for brute forcing of parameters, that for enumeration. Something that we don’t see that often these days (luckily) is Basic Authorization. The way Basic authorization works is by sending user’s credentials in the following form username:password Base64 encoded. In case we know someones username (let’s say admin) and we want to brute force the password, a simple payload marker (§) won’t be enough.

The way Burp can process the payload before sending that is really straight forward. In Intruder go to `Payloads` tab and scroll down to `Payload Processing`. Add a new rule, select `Add prefix` and write as prefix `admin:` that we know that is the username. Then, add new rule and select `encoding` and `Base64-encode`. This will Base64 encode the payload before sending it. Finally, because Base64 uses equal signs (=) to match the four bytes block size, on `Payload encoding` field, remove the equal sign from the list of characters. This will prevent Burp from sending YWRtaW46YWRtaW4`%3d` instead of YWRtaW46YWRtaW4`=`.

![](/assets/uploads/2019/01/intruder.jpg)

Multiple options are offered for payload processing including   
`Match & Replace`, `Hashing`, `Encoding` and `RegEx matching`.

One small tweak that can save you some time, is to change the behaviour of a new Intruder window. By clicking `Intruder` -> `New tab behaviour` -> `Copy configuration from last tab`. Additionally, in case you believe something went wrong with Intruder, you can right click on the items that you are interested about and select `Request items again`.

### Proof of Concepts

##### CSRF

Burp has a really helpful functionality, that just by doing a right click on the request that you would like to create a PoC, select `Engagemenet tools` and `Generate CSRF PoC`.

![](/assets/uploads/2019/01/csrf-burp.jpg)

By selecting Options you can customise the PoC. Something that I like to do is specify to send the request on page load, so no interaction is required.

##### Clickjacking

Burp gives the ability to create a proof of concept by using `Burp Clickbandit`. Clickbandit is available under the Burp menu and generates javascript code, that by pasting on browser’s console it will run the website inside an iframe. Then by clicking on the part of the page that you want the button to be set for the Proof of Concept, it will generate an HTML page with your proof of concept.

![](/assets/uploads/2019/01/burp-clickbandit.jpg)

Sample view of Burp Clickbandit.

### Shortcuts

Using shortcuts makes life so much easier. 90% of the time your hands are on a keyboard and it is easier to click 2 buttons that scrolling with the mouse. This is a list of shortcuts that will save you some time.

| Combination | Action | + Shift |
| --- | --- | --- |
| CTRL + R | Send request to `R`epeater | Go to `R`epeater |
| CTRL + I | Send request to `I`ntruder | Go to `I`ntruder |
| CTRL + T | Turn Proxy On/Off | Go to `T`arget |
| CTRL + U | `U`RL encode | `U`RL decode |
| CTRL + H | `H`TML encode | `H`TML decode |
| CTRL + B | `B`ase64 encode | `B`ase64 decode |
| CTRL + Space | Issue repeater request | – |

![](/assets/uploads/2019/01/burp-hotkeys.jpg)

You can customise shortcuts by going to   
`User Options` -> `Misc` -> `Hotkeys` -> `Edit hotkeys`.

### Burp Extensions

Bellow is a list of the extensions I believe is work to give it a try.

| Name | Use | Type |
| --- | --- | --- |
| Active Scan++ | Improves Passive and Active Scanner | Free |
| WSDLer | WSDL to SOAP requests | Free |
| Freddy | Exploit deserialization attacks | Pro |
| SQLipy | SQLmap on Burp | Free |
| TokenJar | Manage CSRF tokens and Session IDs | Free |
| J2EEScan | Tests J2EE applications | Pro |
| Retire.js | Detects vulnerable Javascript libraries | Pro |
| Logger++ | Improves filtering process | Free |
| Brida | Bridge between Frida and Burp | Free |
| Request Minimizer | Minimizes long session cookies etc | Free |
| Sleepy Puppy | Detect delayed XSS vulnerabilities | Free |
| NoPE Proxy | Extension for Non HTTP Requests | Free |
| Reflected parameters | Checks for parameters that get reflected on the response | Pro |
| .NET beautifier | Make easily readable .NET by hiding ViewStates etc. | Free |
| JSON beautifier | Readable JSON strings | Free |

Keep in mind that multiple of those extensions require `Jython`, that can be installed directly from Burp Suite.

### References

- [Sleepy Puppy](https://github.com/Netflix-Skunkworks/sleepy-puppy/tree/master/burp-extension)
- [NoPE Proxy](https://github.com/summitt/Burp-Non-HTTP-Extension)

Note: The title is just for fun of course, there is no Battle Royale on Burp Suite. I think so at least.
