---
title: "100 Most common Greek passwords"
date: 2021-05-22T10:43:21
categories: ["Security"]
tags: ["Security"]
image: /assets/uploads/2021/05/greek_passwords.jpg
---

Recently I had to perform an assessment for a Greek company and while there were some lists online I could not accept that the most common greek password is `123456`. So I made my own research.

#### Preparation

I used a breach compilation which consists of around 1.4 billion records with the following format: `password,email` and used it to find passwords coming from Greek email addresses. The first thing I did was reverse the text so it will be easier to sort. So, a record that normally would look like `ThisPassword,test@gmail.com`, now it is stored like this: `moc.liamg@tset,drowssaPsihT`. This makes querying the top level domain (.gr) way easier, since I don’t have to worry about passwords containing .gr in them since it will always be in the beginning.

Out of the 1.4 billion records only 1 million of them were coming from a Greek domain. After stripping the email addresses out, only a list of passwords was left. I wrote a basic python script to count the occurrence of each password and sort it in decrement order and TADAA..

#### Results

The most common Greek password is `123456`. Below is the list with the 100 most common passwords:

|  |  |  |
| --- | --- | --- |
| # | Password | Occurrence |
| 1 | 123456 | 12664 |
| 2 | 123456789 | 4405 |
| 3 | 12345 | 1932 |
| 4 | 111111 | 1816 |
| 5 | 1234567890 | 1693 |
| 6 | 12345678 | 1597 |
| 7 | 1234567 | 1415 |
| 8 | 000000 | 1143 |
| 9 | 1234 | 952 |
| 10 | 123456a | 930 |
| 11 | a123456 | 639 |
| 12 | 121212 | 549 |
| 13 | 654321 | 547 |
| 14 | 212121 | 533 |
| 15 | 666666 | 524 |
| 16 | 7777777 | 481 |
| 17 | qwerty | 458 |
| 18 | 123123 | 455 |
| 19 | 131313 | 429 |
| 20 | 777777 | 406 |
| 21 | original21 | 394 |
| 22 | aekara21 | 393 |
| 23 | panathinaikos | 390 |
| 24 | 12345a | 365 |
| 25 | 987654321 | 365 |
| 26 | panatha13 | 365 |
| 27 | 222222 | 358 |
| 28 | katerina | 357 |
| 29 | 555555 | 322 |
| 30 | paokara | 306 |
| 31 | 123 | 299 |
| 32 | 11111 | 299 |
| 33 | 696969 | 298 |
| 34 | 999999 | 286 |
| 35 | malakas | 278 |
| 36 | 123321 | 278 |
| 37 | dimitris | 275 |
| 38 | 11111111 | 273 |
| 39 | olympiakos | 273 |
| 40 | a12345 | 270 |
| 41 | 123456789a | 269 |
| 42 | 1q2w3e4r | 265 |
| 43 | abc123 | 258 |
| 44 | panatha | 258 |
| 45 | paokara4 | 249 |
| 46 | 1111 | 247 |
| 47 | kostas | 246 |
| 48 | aekara | 243 |
| 49 | 101010 | 241 |
| 50 | 888888 | 233 |
| 51 | 444444 | 228 |
| 52 | 0987654321 | 226 |
| 53 | 333333 | 226 |
| 54 | 123qwe | 222 |
| 55 | 1111111111 | 222 |
| 56 | 88888888 | 217 |
| 57 | 112233 | 213 |
| 58 | 12341234 | 208 |
| 59 | password | 207 |
| 60 | 0000000000 | 200 |
| 61 | 00000 | 187 |
| 62 | 123123123 | 179 |
| 63 | 1q2w3e | 179 |
| 64 | pao1908 | 177 |
| 65 | 0123456789 | 176 |
| 66 | 1111111 | 174 |
| 67 | zxcvbnm | 174 |
| 68 | 987654 | 166 |
| 69 | 00000000 | 164 |
| 70 | george | 164 |
| 71 | qwerty1 | 163 |
| 72 | 12345678910 | 161 |
| 73 | a123456789 | 156 |
| 74 | 232323 | 156 |
| 75 | malakas1 | 154 |
| 76 | 1qaz2wsx | 150 |
| 77 | gate13 | 150 |
| 78 | 159753 | 147 |
| 79 | 12121212 | 146 |
| 80 | qwertyuiop | 146 |
| 81 | nikolas | 140 |
| 82 | 55555 | 139 |
| 83 | superman | 139 |
| 84 | 0000 | 138 |
| 85 | aek1924 | 137 |
| 86 | 1q2w3e4r5t | 137 |
| 87 | 19821982 | 135 |
| 88 | 19811981 | 133 |
| 89 | 19781978 | 133 |
| 90 | original | 132 |
| 91 | papaki | 130 |
| 92 | 123abc | 129 |
| 93 | $HEX | 129 |
| 94 | 19791979 | 129 |
| 95 | 123654 | 128 |
| 96 | 19851985 | 128 |
| 97 | anastasia | 126 |
| 98 | 19751975 | 122 |
| 99 | dimitra | 118 |
| 100 | 19801980 | 116 |

You can download the full wordlist for your assessment from my Github Repo: <https://github.com/marduc812/GreekPasswords>
