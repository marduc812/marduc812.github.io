---
title: "Use Twitter Intent to tweet"
date: 2015-03-13T10:58:35
categories: ["Android", "Tuts"]
tags: ["Android"]
image: /assets/uploads/2015/03/tweet.jpg
---

Previously I posted a small tutorial how to launch social networks using their intents. Now I’m going to show you how to post some text from your app to your twitter app. This intent won’t post instantly the text you typed, but it will create a tweet with it and the user just has to press the tweet button. This can be used for the promotion of your app. You have some text like “I’m playing Gold Miner, the world’s best game. You can download it for free at …” (you will still have the 140 characters limit).

I’m going to test this feature using some EditText.

[![tweet](/assets/uploads/2015/03/tweet.jpg)](/assets/uploads/2015/03/tweet.jpg)

```

 tweet = tweetET.getText().toString();
                Intent tweetIntent = new Intent(Intent.ACTION_SEND);
                tweetIntent.putExtra(Intent.EXTRA_TEXT, tweet);
                tweetIntent.setType("text/plain");

                PackageManager packManager = getPackageManager();
                List<ResolveInfo> resolvedInfoList = packManager.queryIntentActivities(tweetIntent,  PackageManager.MATCH_DEFAULT_ONLY);

                boolean resolved = false;
                for(ResolveInfo resolveInfo: resolvedInfoList){
                    if(resolveInfo.activityInfo.packageName.startsWith("com.twitter.android")){
                        tweetIntent.setClassName(
                                resolveInfo.activityInfo.packageName,
                                resolveInfo.activityInfo.name );
                        resolved = true;
                        break;
                    }
                }
                if(resolved){
                    startActivity(tweetIntent);
                }else{
                    Toast.makeText(MainActivity.this, "Please install twitter app", Toast.LENGTH_LONG).show();
                }
```

You can display the number of characters entered so far using the addTextChangedListener

```
tweetET.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {

            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                tweetSize.setText(s.length()+"/140");
            }

            @Override
            public void afterTextChanged(Editable s) {

            }
        });
```

This won’t stop user from entering more than 140 characters. If want to stop him you can use XML and add android:maxLength=”140″ at your editText.

```

<EditText
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:id="@+id/editText"
        android:maxLength="140"
        android:layout_alignParentTop="true"
        android:layout_alignParentLeft="true"
        android:layout_alignParentStart="true"
        android:layout_toLeftOf="@+id/button"
        android:layout_toStartOf="@+id/button" />
```
