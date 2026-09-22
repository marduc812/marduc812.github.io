---
title: "Kaonashi is the Best Wordlist for Password Cracking"
date: 2020-12-14T23:06:48
categories: ["Security"]
tags: ["Security"]
image: /assets/uploads/2020/12/kaonashi_wordlist.jpg
---

I was recently introduced to Kaonashi through a friend when we wanted to crack some hashes we collected during an assessment. Although you will probably think, “yeah great another wordlist, I already have 1000 of those”, this is not the case. What makes this wordlist special, is that it is NOT one of those Top 1 Million passwords wordlists.

Two security researchers ([@segofensiva](https://twitter.com/segofensiva) and [@pcaro90](https://twitter.com/pcaro90)) used their time to analyze passwords found from multiple leaks online, with the biggest ones being Yahoo and Marriot. This analysis took in consideration patterns that users tend to use, for example `text` then a `symbol` and then some `numbers`, like name then birthdate and then an exclamation mark. Another factor taken into consideration was some mutations when converting from one language to another, like for example the Greek word `ψυχή`, which means soul. Based on the sound the word can be written as `psihi` or `psixi` or `psyxh` or `psyxi`.

One example where this localized rule can be seen, is in China where `5201314` is a top 25 password, a number which for us would seem completely random. In reality due to the similarity on the way this sounds with the phrase `I love you forever and ever`, is a slang commonly used among young people. Urban dictionary has an excellent explanation of this phrase.

> 520 in Chinese Number Slang, 五二零 wǔèrlíng, sounds a little like wǒ ài nǐ, which means I love you. 1314 means ‘one life one death,’ this combination of numbers is used to mean ‘forever.’ When combined, 5201314 means ‘I love you forever.’

Additionally, the researchers identified multiple `keyboard walking` patterns like 123456 and qwertyuiop, on multiple languages and different keyboard layouts. A common pattern with Swedish keyboard layout is `åölkj123` while with Russian is `Йцукенгшщзхъ`.

- [![](/assets/uploads/2020/12/keyboard-walking-pattern.png)](/assets/uploads/2020/12/keyboard-walking-pattern.png)

Finally, this project contains numerous rules and masks, which can be used in `hashcat` to help you crack your hashes. It is likely I missed some of the interesting research that these guys did, but unluckily their presentation from RootedCON is in Spanish and I don’t speak Spanish at all.

#### Links

Project: [Github](https://github.com/kaonashi-passwords/Kaonashi)

Downloads: [Kaonashi](https://mega.nz/#!nWJXzYzS!P1G8HDiMxq5wFaxeWGWx334Wp9wByj5kMEGLZkVX694) (2.35 GB) – [Kaonashi 14M](https://mega.nz/#!7fIlxQaC!BlrWduRgBwWH_Za9SoEJnnq7ySrV4E_NzfTtn_OI418) (47.7 MB) – [KaonashiWPA 100M](https://mega.nz/#!jeRRgQgZ!xcRcLpm0ftuu7z7JN32LHMECqk9vmpVNH2JFVxSICfU) (239.2 MB)
