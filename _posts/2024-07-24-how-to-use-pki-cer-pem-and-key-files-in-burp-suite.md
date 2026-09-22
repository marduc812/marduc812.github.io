---
title: "How to use PKI cer, pem and key files with Burp Suite"
date: 2024-07-24T16:38:20
categories: ["Security", "Tool"]
tags: ["Security", "tutorial"]
image: /assets/uploads/2024/07/pki-cer-burp-suite.webp
---

Burp Suite, our favorite proxy is used for every assessment which uses HTTP communication. Sometimes though, a client-side certificate is required and Burp Suite by default, does not support PKI certificate files.

The easiest way to bypass this restriction, is to merge all the certificates into a `PKCS#12` file, which will contain all the certificates including the intermediate `.pem` certificates. To do it, all you need is `openssl`.

```
openssl pkcs12 -export -out certificate.pfx -inkey privatekey.key -in certificate.cer -certfile certificate.pem
```

This will take as input certificate the certificate.cer file, use as key the privatekey.key file and include extra certificates needed, with the -certfile flag. Then with the -out the file which will contain all the previous information in the new format is selected. When running the command, a prompt is going to appear for a password, which is going to be needed later in Burp Suite.

After the new file is generated, go back to Burp Suite and go to `Settings` -> `Network` -> `TLS` -> `Client TLS cerificates` -> and select “`Add`“.

[![Burp Suite Settings](/assets/uploads/2024/07/Screenshot-2024-07-24-at-18.19.41.png)](/assets/uploads/2024/07/Screenshot-2024-07-24-at-18.19.41.png)

On this window, in case you want the key to be used only for specific hosts, specify it in the field, or otherwise just leave it empty and it will apply for every host. Then, select File(PKCS#12) and select the newly created certificate.pfx file, but also supply the password used.

[![](/assets/uploads/2024/07/Screenshot-2024-07-24-at-18.20.51.png)](/assets/uploads/2024/07/Screenshot-2024-07-24-at-18.20.51.png)

From now on, for every connection which matches your criterial, Burp Suite is going to use the certificate added.

Happy hacking!
