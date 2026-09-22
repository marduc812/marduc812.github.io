---
title: "Find subdomains using Project Sonar by Rapid7"
date: 2018-12-19T23:56:12
categories: ["Security", "Tuts"]
tags: ["Security", "tutorial"]
image: /assets/uploads/2018/12/project-sonar-e1607981251198.png
---

Recently a friend of mine told me about Project Sonar by Rapid7. The purpose of this project is to enumerate as many as possible services online.

The enumeration happens by scanning all the IPs and determining what services are running on those. This is done from multiple subnets, so they will be able to collect as much information as possible. On Patrik Hudak’s website, there is an in depth explanation of how the project works, like on the Rapid7 website.

---

## Querying domains

### How to get the data

I downloaded the Forward DNS records, and specifically the `2018-11-23-1542931676-fdns_any.json.gz`, that like it’s visible it is a compressed file and has size `25.6 GB`.

##### Forward DNS JSON scheme

Below is the structure of the JSON file.

```
{
  "$id": "https://opendata.rapid7.com/sonar.fdns_v2/",
  "type": "object",
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "additionalProperties": false,
  "properties": {
    "timestamp": {
      "$id": "/properties/timestamp",
      "type": "string",
      "description": "The time when this response was received in seconds since the epoch"
    },
    "name": {
      "$id": "/properties/name",
      "type": "string",
      "description": "The record name"
    },
    "type": {
      "$id": "/properties/type",
      "type": "string",
      "description": "The record type"
    },
    "value": {
      "$id": "/properties/value",
      "type": "string",
      "description": "The response received for a record of the given name and type"
    }
  }
}
```

### Parse results from the file

First `jq` needs to be installed to help with JSON processing. jq can be installed by typing `sudo apt install jq` on Kali or `brew install jq` on MacOS.
To get the content subdomains of your choice, you can use the following command.

```
zcat fdns.json.gz
| grep -F '.example.com"'
| jq -crM 'if (.name | test("\\.example\\.com$")) then .name else empty end'
| sort
| uniq
| tee -a example.com.list
```

This command worked for both my Kali and MacOS, but in case you have an issue you can run it with `zcat file.gz` directly. When you parse your subdomains, using tee, it copies stdin to stdout and also to any file specified.

---

##### Update

I did a small bash script so I don’t have to write the command all the time. If you are here, I guess you know how to run a .sh script, so the only thing is that you add the domain you want to test as argument.

`$ sonar_search.sh google.com`

<script src="https://gist.github.com/marduc812/42dc5a11f5d1042a728680410eaa6fb7.js"></script>

### References

##### DNS Records

- [Project Sonar](https://opendata.rapid7.com/about/)
- [Download Links](https://opendata.rapid7.com/)
- [Scanning All The Things Info](https://blog.rapid7.com/2013/09/26/internet-wide-probing-rapid7-sonar/)

##### Tools

- zcat
- [jq](https://stedolan.github.io/jq/)

##### External

- [0xpatrik.com](https://0xpatrik.com/project-sonar-guide/)
- [Cover Picture](https://opendata.rapid7.com/static/img/bg-sonar.jpg)
