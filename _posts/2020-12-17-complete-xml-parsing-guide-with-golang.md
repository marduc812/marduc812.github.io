---
title: "Complete XML Parsing Guide with Golang"
date: 2020-12-17T12:33:30
categories: ["Fun", "Tuts"]
tags: ["tutorial"]
image: /assets/uploads/2020/12/golang-xml-parsing-1.jpg
---

XML format was probably the most commonly used, before JSON took its place. Like almost every programming language Go or Golang, supports the XML format. In case you are here, it means you were stuck in some of those possible ways to unmarshal your XML code into a nice object.

I simply grouped the cases where the unmarshal of an XML string happens in 3 parts.

#### Case 1: Only Attributes

```xml
<address addr="74.207.244.221" addrtype="ipv4"/>
```

This will be an an object with 2 attributes, state and reason, which can get un marshalled like this:

```golang
type Address struct {
	XMLName xml.Name `xml:"address"`
	Addr    string   `xml:"addr,attr"`
	AddType string   `xml:"addrtype,attr"`
}
```

An object named `Address` is created, with the first attribute being `XMLName`, which is of type `xml.Name` and has value `xml:"address".` This is a standard Go attribute, which is used for referencing the object like explained [here](https://golang.org/pkg/encoding/xml/#Marshal). Then the needed object attributes are set which both are type of `string` and have names `addr,attr` and `addrtype,attr`. The attr field, indicates that this field is an argument.

Try it online: [Golang-Playground](https://play.golang.org/p/mJ70gTPFtSq)

#### Case 2: XML Value

```xml
<cpe>cpe:/a:openbsd:openssh:5.3p1</cpe>
```

In order to extract the value of an XML field, the `chardata` annotation is needed. Following the same process a Struct is created with a name and a Value field, which will be the text inside the brackets.

```golang
type Cpe struct {
	XMLName xml.Name `xml:"cpe"`
	Value   string   `xml:",chardata"`
}
```

Pay attention that the `chardata` annotation has a coma in front.

Try it online: [Golang-Playground](https://play.golang.org/p/xy1pzrm04VL)

#### Case 3: Array of Objects

This is the most common case when working with real data. In this case the nmap Host field will be used, but slightly altered to make it more clear.

```xml
<host starttime="1315618421" endtime="1315618434">
    <hostnames>
        <hostname name="scanme.nmap.org" type="user"/>
        <hostname name="li86-221.members.linode.com" type="PTR"/>
    </hostnames>
    <address addr="74.207.244.221" addrtype="ipv4"/>
</host>
```

So in this case the host object will have a field called Hostnames which is an array of hostname objects and a field address, which is single object. The previously defined objects will stay the same and a new object called hostname is needed.

```golang
type Hostname struct {
	XMLName xml.Name `xml:"hostname"`
	Name    string   `xml:"name,attr"`
}
```

There is nothing new here, a Hostname object with a name and an attribute of Name is created. Now since every structure is set, the final object host can be contracted.

```golang
type Host struct {
	XMLName   xml.Name   `xml:"host"`
	Address   Address    `xml:"address"`
	Hostnames []Hostname `xml:"hostnames>hostname"`
}
```

In this case, the Address field is of type Address, which is an object and the Hostnames field has type array of Hostname objects and the annotation uses the greater than symbol `>` to indicate that it’s an array of the previously defined object.

Try it online: [Golang-Playground](https://play.golang.org/p/I_b7ElWTscU)

In this case I did not do any validation on the input data since I am in control with that, but it is always good to verify that there are no errors before unmarshaling your data.
