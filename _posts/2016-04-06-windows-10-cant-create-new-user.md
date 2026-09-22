---
title: "[Windows 10] Can&#8217;t create new user"
date: 2016-04-06T15:08:47
categories: ["Uncategorized"]
image: /assets/uploads/2016/04/windows-10-add-user-e1607981958991.jpg
---

Windows 10 have a new UI that I personally find really useful (some people don’t), and although I have a Mac, I had to use Windows 10 for a project I’m running at the moment. I had a standard administrator userbut the system didn’t allow me to open some files for security reasons and asked me to create a new user without administrator privileges.  
I went straight into settings to create a new user. After going to Control Panel -> User Accounts -> User Accounts -> Manage Accounts I clicked on Add someone else to this pc and nothing happened. No matter how many times I did a restart absolutely nothing happened.

On your home bar type **cmd** and right click on the Command Prompt option. Then select **Run as administrator**.

Next while your terminal is open and you have Admin rights type the following.

`net user USERNAME PASSWORD /add`

For example let’s say I want to create a user named **Poki**, that has password **1234**. I will have to type:

`net user Poki 1234 /add`

This will create a user for you and when you log out, by using the credentials you entered earlier, you will be ready to log in as the new user.
