---
title: "Android how to use Facebook, Twitter and Google plus Intents"
date: 2015-03-10T10:59:05
categories: ["Android", "Tuts"]
tags: ["Android", "google"]
image: /assets/uploads/2015/03/social.jpg
---

Social networks are part of our life for sure, some times facebook or twitter or any other social network. Using them at your apps will help you to promote your app and make the user part of your team. Let’s how this can be done in Android.

## Facebook

For the Facebook intent you have to check if the user has facebook app installed or you just  have to lunch browser at the page you want. I will use Google for everything as a example.

```

 try {
 Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse("fb://page/104958162837"));
                      startActivity(intent);
                  } catch(Exception e) {
 startActivity(new Intent(Intent.ACTION_VIEW, Uri.parse("https://www.facebook.com/google")));
                  }
```

As you can see when we do the first try we enter a Uri for page 104958162837 that is the ID of the page of Google on Facebook.

How to find the ID of a facebook page?

All you have to do is open the page you want in our case is https://www.facebook.com/Google

and you replace **www** with **graph.** That makes our link https://graph.facebook.com/Google and you will se some text fields. The first is the ID you have to place after bf://page/…

In case the user has not installed the Facebook app by entering the link it will launch the a browser with the URL stored on case of exception.

## Twitter

For Twitter we follow exact the same tactic like for Facebook. All you have to do is to find the user’s ID.

How to find twitter ID?

Just visit this [page](http://mytwitterid.com/)( you can also find other services like this)  and type your @username, in our case Google

[![find twitter id](/assets/uploads/2015/03/Screen-Shot-2015-03-10-at-12.45.10-PM.png)](/assets/uploads/2015/03/Screen-Shot-2015-03-10-at-12.45.10-PM.png)

Now pace your code at the id field

```

 Intent intent = null;
                  try {
                      // get the Twitter app if possible
                      YourActivity.this.getPackageManager().getPackageInfo("com.twitter.android", 0);
                      intent = new Intent(Intent.ACTION_VIEW, Uri.parse("twitter://user?user_id=20536157"));
                      intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK);
                  } catch (Exception e) {
                      // no Twitter app, revert to browser
                      intent = new Intent(Intent.ACTION_VIEW, Uri.parse("https://twitter.com/google"));
                  }
                  YourActivity.this.startActivity(intent);
```

## 

## Google+

Google plus has the easiest was to launch a page of google+ app or browser.

```

 startActivity(new Intent(Intent.ACTION_VIEW, Uri.parse("https://plus.google.com/+google")));
```

When you will launch this intent you will have a pop up on your screen to select if you want to launch the app or the browser. Just in one line of code.
