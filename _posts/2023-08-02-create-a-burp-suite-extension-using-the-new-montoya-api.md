---
title: "Create a Burp Suite Extension Using the new Montoya API"
date: 2023-08-02T20:33:44
categories: ["Security", "Tool", "Tuts"]
tags: ["Security", "Web"]
image: /assets/uploads/2023/08/marduc812_com_burp_extension.jpg
---

Everyone’s favorite `Burp Suite`, recently released their new API for interacting with Burp. The old API aka the “Wiener” API, was there from the release of Burp, but in 2022 the new “Montoya” API came out.

Recently for an assessment I needed to build an extension which will add a delay between each request. For some reason, the application would return 401 error, in case more than 5 requests were sent at the same time, but 200 if the requests were slightly delayed. I though that it would be of great use to learn more about the new API, but I found the resources were a bit limited online. So here is a guide on how to build your own extension for Burp, using Java.

### The Environment

For this, I used IntelliJ IDEA (while I mainly use VS Code) for an IDE, because it makes the whole process so much easier, but you can use anything that you prefer. After creating a new project, the settings I set were `Java` for Language, `Gradle` for Build System, version 17 of the JDK, and `Groovy` as the Gradle DSL. Then setup a GroupId and was ready to start.

[![](/assets/uploads/2023/08/Screenshot-2023-08-02-at-18.56.40.png)](/assets/uploads/2023/08/Screenshot-2023-08-02-at-18.56.40.png)

After creating the project, InteliJ will create the structure for the project and a package where our code will go. By default the `Main` class contains a `Main` function but we don’t care about it so it can be removed. The first thing that needs to be done is add the required dependencies. In this case we need to import Burp’s Montoya API which is done inside the `build.gradle` file. By default `mavenCentral` was the repository defined, which contains the API module for Burp (the link is at the end of the article). The suggested way to import that is to add i`mplementation 'net.portswigger.burp.extensions:montoya-api:2023.8'` to our dependencies (you can also use the + symbol instead of 2023.8, which will pull always the latest version). So the dependencies look like this:

```groovy
dependencies {
    implementation 'net.portswigger.burp.extensions:montoya-api:2023.8'
}
```

Also, we need a way to pack all the files needed to execute our code, including all artifacts to a single jar file, so we need to define it also in the build.gradle file.

```groovy
jar {
    from {
        configurations.runtimeClasspath.collect { it.isDirectory() ? it : zipTree(it) }
    }
}
```

So the final Build.gradle file should look like this:

```groovy
plugins {
    id 'java'
}

group = 'com.marduc812'
version = '1.0-SNAPSHOT'

repositories {
    mavenCentral()
}

dependencies {
    implementation 'net.portswigger.burp.extensions:montoya-api:2023.8'
}

test {
    useJUnitPlatform()
}

jar {
    from {
        configurations.runtimeClasspath.collect { it.isDirectory() ? it : zipTree(it) }
    }
}
```

After the changes are done, save the file and in case you are using IntelliJ, use the little elephant icon with the blue arrows in the top right corner, to fetch the dependancies.

[![](/assets/uploads/2023/08/Screenshot-2023-08-02-at-19.19.24.png)](/assets/uploads/2023/08/Screenshot-2023-08-02-at-19.19.24.png)

### Building the core

Based on the guideline from the PortSwigger website, when the extension is loaded from Burp, the `initialize()` function is called to give access to the Montoya API. Inside the initialize() function, the name of the extension is defined and the logging, which helps print messages in the extension console from Burp. So let’s start by importing the library and then calling the required functions. Inside Main.java, import `BurpExtension`, `MontoyaAPI` and `Logging` from Burp’s API. Use `BurpExtension` to help Burp understand that this is an extension file, by using it as implementation for the Main class. Then inside the initialize function, set the name for the extension and prepare the logging. The code from Main.java should look like this:

```java
package com.marduc812;

import burp.api.montoya.BurpExtension;
import burp.api.montoya.MontoyaApi;
import burp.api.montoya.logging.Logging;

public class Main implements BurpExtension{

    MontoyaApi api;
    Logging logging;

    @Override
    public void initialize(MontoyaApi api) {
        this.api = api;
        this.logging = api.logging();
        api.extension().setName("Request Delay");
        this.logging.logToOutput("Demo extension loaded!");
    }
}
```

Now let’s build the extension and see how we did. What we should see when the extension is imported is the name of the extension and a confirmation message. To build the extension, open the Gradle menu by clicking on the little elephant icon on the right and under Tasks, build select Build.

[![](/assets/uploads/2023/08/Screenshot-2023-08-02-at-19.29.59.png)](/assets/uploads/2023/08/Screenshot-2023-08-02-at-19.29.59.png)

The extension is now built inside the build/libs directory of our project. So let’s fire up our friend Burp, under the Extensions tab select Add, and select the jar file that we created.

[![](/assets/uploads/2023/08/Screenshot-2023-08-02-at-19.31.58.png)](/assets/uploads/2023/08/Screenshot-2023-08-02-at-19.31.58.png)

After selecting the extension and importing it, the presence of the extension is confirmed and our message is printed! Since currently it doesn’t have any functionality, it can be removed to import it once there is some kind of functionality.

[![](/assets/uploads/2023/08/Screenshot-2023-08-02-at-19.34.22.png)](/assets/uploads/2023/08/Screenshot-2023-08-02-at-19.34.22.png)

Since we want the extension to add a delay between each request, lets create a new class file inside the package that will handle this. To do that we need ti use the Proxy interface from the Montoya API, since we want to interact with the proxy. I will call the java class RequestDelayer. The instruction provided by BurpSuite suggest to implement the `ProxyRequestHandler` class, which requires two methods `handleRequestReceived` and `handleRequestToBeSent`.

[![](/assets/uploads/2023/08/Screenshot-2023-08-02-at-19.49.30.png)](/assets/uploads/2023/08/Screenshot-2023-08-02-at-19.49.30.png)

So what we need to do for handleRequestReceived is, get the request, wait for example one second and then forward it. Let’s add a try/catch statement to avoid any unwanted crash and let’s add a second delay between each request.

```java
@Override
    public ProxyRequestReceivedAction handleRequestReceived(InterceptedRequest interceptedRequest) {
        
        // Sleep for 1 second 
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            logging.logToError(e);
        }
        
        // forward the delayed request
        return ProxyRequestReceivedAction.doNotIntercept(interceptedRequest);
    }
```

In this case, logging does not resolve, so let’s create a RequestDelayer method to pass logging which was initialized in Main. Also, lets update the handleRequestToBeSent method to just forward the interceptedRequest. The RequestDelayer.java file should look like this:

```java
package com.marduc812;

import burp.api.montoya.persistence.PersistedObject;
import burp.api.montoya.proxy.http.InterceptedRequest;
import burp.api.montoya.proxy.http.ProxyRequestHandler;
import burp.api.montoya.proxy.http.ProxyRequestReceivedAction;
import burp.api.montoya.proxy.http.ProxyRequestToBeSentAction;
import burp.api.montoya.logging.Logging;

public class RequestDelayer implements ProxyRequestHandler{
    Logging logging;

    public RequestDelayer(Logging logging) {
        this.logging = logging;
    }

    @Override
    public ProxyRequestReceivedAction handleRequestReceived(InterceptedRequest interceptedRequest) {

        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            logging.logToError(e);
        }

        return ProxyRequestReceivedAction.doNotIntercept(interceptedRequest);
    }

    @Override
    public ProxyRequestToBeSentAction handleRequestToBeSent(InterceptedRequest interceptedRequest) {
        return ProxyRequestToBeSentAction.continueWith(interceptedRequest);
    }
}
```

Finally, let’s add the method to delay the requests inside the initialize() function of Main.java, by registering a new request handler and passing the logging method to it.

```java
@Override
    public void initialize(MontoyaApi api) {
        this.api = api;
        this.logging = api.logging();
        api.extension().setName("Request Delay");
        this.logging.logToOutput("Demo extension loaded!");

        // Register the proxy request handler
        api.proxy().registerRequestHandler(new RequestDelayer(logging));
    }
```

To confirm that the delay is working, I used time to time the request and with curl proxied through my local burp, fetched google.com. The total time was 0.433 seconds.

```generic
$ time curl -k https://google.com --proxy http://localhost:8080
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="https://www.google.com/">here</A>.
</BODY></HTML>
curl -k https://google.com --proxy http://localhost:8080  0.01s user 0.01s system 3% cpu 0.433 total
```

After building the extension and sending the same request, the new response time was 1.356 seconds.

```generic
$ time curl -k https://google.com --proxy http://localhost:8080
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="https://www.google.com/">here</A>.
</BODY></HTML>
curl -k https://google.com --proxy http://localhost:8080  0.01s user 0.01s system 1% cpu 1.356 total
```

### Building a GUI

The delay works but probably somebody would like to have an option to adapt the delay between each request, and to not be static to 1 second. For that an interface is needed. The first step is to create a new Tab for Burp. This once again is done inside the initialize function. From the UserInterface we call the registerSuiteTab function, which takes as argument a title and then the component which will display when going to the tab. To make it faster, we can pass directly a `JLabel`, part of the `swing` java GUI toolkit. Inside the initialize method, right after registering the request handler, let’s add the new tab.

```generic
        api.proxy().registerRequestHandler(new RequestDelayer(logging));
        api.userInterface().registerSuiteTab("Proxy Delay", new JLabel("Add delay"));
    }
```

Once again, build the extension and load it in Burp.

[![](/assets/uploads/2023/08/Screenshot-2023-08-02-at-20.41.14.png)](/assets/uploads/2023/08/Screenshot-2023-08-02-at-20.41.14.png)

Cool! The tab is now visible and the label is shown. Because the registerSuiteTab allows only one component we need to create a new Java class, where we will have the label, a text view so users can set the delay time and a save button. I named the new class file DelayGUI. The DelayGUI class, should extend JPanel, since we want to create a view with multiple components. In this component for the moment we only need to pass the logging function, to debug any issues that may come. Let’s create the DelayGUI method and add the context.

```java
package com.marduc812;

import burp.api.montoya.logging.Logging;

import javax.swing.*;

public class DelayGUI extends JPanel {
    Logging logging;
    public DelayGUI(Logging logging) {
        this.logging = logging;
    }

}
```

The skeleton for the method is ready, now let’s add the components. Firstly a JLabel to explain what is the input field about, then a JTextField, which is the input field and then the JButton to save the updated value. The JTextField component, takes two arguments, one is the default text to have and the second one is the length of the input. In our case a length of 6 digits should be enough.

```java
        JLabel label = new JLabel("Delay in ms: ");
        JTextField delayInput = new JTextField("1000",6);
        JButton saveBtn = new JButton("Save");
```

Now that we have the components we can add them to the panel and import the new view.

```java
        this.add(label);
        this.add(delayInput);
        this.add(saveBtn);
```

To import the new view, replace the `api.userInterface().registerSuiteTab("Proxy Delay", new JLabel("Add delay"));` line inside initialize(), with `api.userInterface().registerSuiteTab("Proxy Delay", new DelayGUI(logging));`. Let’s reload the extension.

[![](/assets/uploads/2023/08/Screenshot-2023-08-02-at-20.59.54.png)](/assets/uploads/2023/08/Screenshot-2023-08-02-at-20.59.54.png)

### Project Data Storage

Wonderful. So currently we have the tab but changing the value in the text field doesn’t do anything. As the last step, we need to use `persistence` to store the integer value and retrieve it. Let’s start by updating Main.java. Let’s define a public string, which will store the key for the integer that we want to store, similar to a key/value pair. Then, import the `PersistenceObject` interface, initialize it and set a default value, inside the initialize() function.

```generic
        PersistedObject persist =  api.persistence().extensionData();

        Integer delTime = persist.getInteger(DELAY_TIME);

        if (delTime == null) {
            delTime = 0;
        }

        persist.setInteger(DELAY_TIME, delTime);
```

The code above checks if the DELAY\_TIME key exists, and if it null, it set’s it’s value 0 (no delay). Since we will use the persistence storage in both DelayGUI and RequestDelayer, let’s pass it and finish with the initialize function. The final Main.java file should look like this:

```java
package com.marduc812;

import burp.api.montoya.BurpExtension;
import burp.api.montoya.MontoyaApi;
import burp.api.montoya.logging.Logging;
import burp.api.montoya.persistence.PersistedObject;

import javax.swing.*;

public class Main implements BurpExtension{

    MontoyaApi api;
    Logging logging;

    static final String DELAY_TIME = "REQ_DELAY_TIME";

    @Override
    public void initialize(MontoyaApi api) {
        this.api = api;
        this.logging = api.logging();
        api.extension().setName("Request Delay");
        this.logging.logToOutput("Demo extension loaded!");

        PersistedObject persist =  api.persistence().extensionData();

        Integer delTime = persist.getInteger(DELAY_TIME);

        if (delTime == null) {
            delTime = 0;
        }

        persist.setInteger(DELAY_TIME, delTime);

        api.proxy().registerRequestHandler(new RequestDelayer(persist, logging));
        api.userInterface().registerSuiteTab("Proxy Delay", new DelayGUI(persist, logging));
    }
}
```

Let’s update the tab view first. The `DelayGUI` method should take as input the new `persistencedObject` and add context to it.

```java
public class DelayGUI extends JPanel {
    Logging logging;
    PersistedObject persistence;
    public DelayGUI(PersistedObject persistence, Logging logging) {
        this.logging = logging;
        this.persistence = persistence;

        JLabel label = new JLabel("Delay in ms: ");
   
[..SNIP..]
```

Also, some action should happen when the user clicks on the save button. In this case the value from the text field should be set as an integer using an ActionListener. Import the DELAY\_TIME string value from Main (`import static com.marduc812.Main.DELAY_TIME;`) to update the key value of the object. Get user’s text, verify that it’s a valid integer within the range of 0 up to 999999 and then update the persistence.

```java
saveBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String delayText = delayInput.getText();
                try {
                    int delay = Integer.parseInt(delayText);
                    if (delay < 0 || delay > 999999) {
                        throw new Exception("Invalid Size");
                    }
                    persistence.setInteger(DELAY_TIME, delay);
                    logging.raiseInfoEvent("Delay time set to: " + delay);
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(DelayGUI.this, "Invalid value. allowed values are from 0 to 999999");
                } catch (Exception ex) {
                    throw new RuntimeException(ex);
                }
            }
        });
```

The DelayGUI class is ready. Now instead of having as initial value the value 1000, we can get the value from the storage (`Integer delayT = persistence.getInteger(DELAY_TIME);`), and set it as default value (`JTextField delayInput = new JTextField(Integer.toString(delayT),6);`). The final code should look like this:

```java
package com.marduc812;

import burp.api.montoya.logging.Logging;
import burp.api.montoya.persistence.PersistedObject;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import static com.marduc812.Main.DELAY_TIME;
public class DelayGUI extends JPanel {
    Logging logging;
    PersistedObject persistence;
    public DelayGUI(PersistedObject persistence, Logging logging) {
        this.logging = logging;
        this.persistence = persistence;

        Integer delayT = persistence.getInteger(DELAY_TIME);

        JLabel label = new JLabel("Delay in ms: ");
        JTextField delayInput = new JTextField(Integer.toString(delayT),6);
        JButton saveBtn = new JButton("Save");

        saveBtn.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String delayText = delayInput.getText();
                try {
                    int delay = Integer.parseInt(delayText);
                    if (delay < 0 || delay > 999999) {
                        throw new Exception("Invalid Size");
                    }
                    persistence.setInteger(DELAY_TIME, delay);
                    logging.raiseInfoEvent("Delay time set to: " + delay);
                } catch (NumberFormatException ex) {
                    JOptionPane.showMessageDialog(DelayGUI.this, "Invalid value. allowed values are from 0 to 999999");
                } catch (Exception ex) {
                    throw new RuntimeException(ex);
                }
            }
        });

        this.add(label);
        this.add(delayInput);
        this.add(saveBtn);
    }

}
```

Finally, the RequestDelayer class, the heart of the code is the last component that needs to be updated. Like in DelayGUI, the RequestDelayer function should be updated to take the `PersistedObject` as an argument.

```java
public class RequestDelayer implements ProxyRequestHandler{
    Logging logging;
    PersistedObject persistence;

    public RequestDelayer(PersistedObject persistence, Logging logging) {
        this.logging = logging;
        this.persistence = persistence;
    }
[..SNIP..]
```

Once again import the DELAY\_TIME string from main and inside the `handleRequestReceived` function, using the persistence method we passed, we load the integer value set in DelayGUI, instead of passing 1000 directly.

```java
    @Override
    public ProxyRequestReceivedAction handleRequestReceived(InterceptedRequest interceptedRequest) {

        Integer requestDelay = persistence.getInteger(DELAY_TIME);
        // Sleep for X second, as passed from the storage
        try {
            Thread.sleep(requestDelay);
        } catch (InterruptedException e) {
            logging.logToError(e);
        }

        // forward the delayed request
        return ProxyRequestReceivedAction.doNotIntercept(interceptedRequest);
    }
```

The final code for RequestDelayer should look like this:

```java
package com.marduc812;

import burp.api.montoya.persistence.PersistedObject;
import burp.api.montoya.proxy.http.InterceptedRequest;
import burp.api.montoya.proxy.http.ProxyRequestHandler;
import burp.api.montoya.proxy.http.ProxyRequestReceivedAction;
import burp.api.montoya.proxy.http.ProxyRequestToBeSentAction;
import burp.api.montoya.logging.Logging;

import static com.marduc812.Main.DELAY_TIME;

public class RequestDelayer implements ProxyRequestHandler{
    Logging logging;
    PersistedObject persistence;

    public RequestDelayer(PersistedObject persistence, Logging logging) {
        this.logging = logging;
        this.persistence = persistence;
    }

    @Override
    public ProxyRequestReceivedAction handleRequestReceived(InterceptedRequest interceptedRequest) {

        Integer requestDelay = persistence.getInteger(DELAY_TIME);
        // Sleep for X second, as passed from the storage
        try {
            Thread.sleep(requestDelay);
        } catch (InterruptedException e) {
            logging.logToError(e);
        }

        // forward the delayed request
        return ProxyRequestReceivedAction.doNotIntercept(interceptedRequest);
    }

    @Override
    public ProxyRequestToBeSentAction handleRequestToBeSent(InterceptedRequest interceptedRequest) {
        return ProxyRequestToBeSentAction.continueWith(interceptedRequest);
    }
}
```

Now for the last time, build the extension and load it to Burp.

[![](/assets/uploads/2023/08/Screenshot-2023-08-02-at-21.40.43.png)](/assets/uploads/2023/08/Screenshot-2023-08-02-at-21.40.43.png)

At first look, it is visible that because there was no `REQ_DELAY_TIME` value set, it defaulted to 0, which is what was expected. Let’s send a request to see the time it took to fetch google.com.

```generic
$ time curl -k https://google.com --proxy http://localhost:8080
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="https://www.google.com/">here</A>.
</BODY></HTML>
curl -k https://google.com --proxy http://localhost:8080  0.01s user 0.01s system 2% cpu 0.630 total
```

It took 0.63 seconds to fetch it. Now, let’s update the value to 4 seconds and send the same request.

[![](/assets/uploads/2023/08/Screenshot-2023-08-02-at-21.44.32.png)](/assets/uploads/2023/08/Screenshot-2023-08-02-at-21.44.32.png)

```generic
$ time curl -k https://google.com --proxy http://localhost:8080
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="https://www.google.com/">here</A>.
</BODY></HTML>
curl -k https://google.com --proxy http://localhost:8080  0.01s user 0.01s system 0% cpu 4.538 total
```

The response time is now 4.538 seconds.

The extension is now completed! You can set a delay time on the tab and Burp will keep that request in intercept for that many seconds before forwarding it. You can find the full code in my Github.

#### Useful Links

mavenCentral Burp Extensions: [central.sonatype.com](https://central.sonatype.com/artifact/net.portswigger.burp.extensions/montoya-api/2023.8)  
PortSwigger – Creating Burp Extensions: [portswigger.net](https://portswigger.net/burp/documentation/desktop/extensions/creating)  
Burp Extensions Examples Github: [github.com](https://github.com/PortSwigger/burp-extensions-montoya-api-examples)  
Montoya API ProxyRequestHandler: [portswigger.github.io](https://portswigger.github.io/burp-extensions-montoya-api/javadoc/burp/api/montoya/proxy/http/ProxyRequestHandler.html)  
Swing Documentation: [oracle.com](https://docs.oracle.com/javase%2F7%2Fdocs%2Fapi%2F%2F/javax/swing/package-summary.html)  
Montoya API Persistence: [portswigger.github.io](https://portswigger.github.io/burp-extensions-montoya-api/javadoc/burp/api/montoya/persistence/Persistence.html)  
Full Code: [github.com](https://github.com/marduc812/SampleBurpExtension)
