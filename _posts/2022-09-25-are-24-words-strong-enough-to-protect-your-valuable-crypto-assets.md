---
title: "Are 24 words strong enough to protect your valuable crypto assets?"
date: 2022-09-25T20:23:18
categories: ["Crypto", "Security", "Tuts"]
tags: ["Crypto"]
image: /assets/uploads/2022/09/bip39-bitcoin.jpeg
---

Crypto wallets use BIP39 mnemonic in order to help people memorize their key, without having to write long almost random looking strings. Those are presented to users when they create their first wallet and contain a list of 12 to 24 random words.

Mnemonics are based on the entropy selected, which is defined in number of bits. A 12 word mnemonic has 128 bits of entropy and a 24 words mnemonic has 256 bits of entropy.

> *Entropy* is a scientific concept as well as a measurable physical property that is most commonly associated with a state of disorder, randomness, or uncertainty.
>
> https://en.wikipedia.org/wiki/Entropy

In simple words, it’s a way of measuring how random is something. Below is a table which presents the entropy based on number of words.

|  |  |  |
| --- | --- | --- |
| **Words** | **Entropy** | **Checksum** |
| 12 | 128 | 4 |
| 15 | 160 | 5 |
| 18 | 192 | 6 |
| 21 | 224 | 7 |
| 24 | 256 | 8 |

So for this example, let’s create the smallest possible amount of entropy which is 256 bits.

```
0100111110110010001011101010111010011100010101101101111101100010010010101011001011101011010100110010101001110001001100100100110110001011100000001111010010100111110111111100110010100001111011100101000100010111000111011100001010100011010110001001010001011000
```

This bits array is split into 23 groups of 11 bits each, and at the end there are 3 bits left which are part of the checksum.

|  |  |
| --- | --- |
| **Group** | **Bits** |
| 1 | 01001111101 |
| 2 | 10010001011 |
| 3 | 10101011101 |
| 4 | 00111000101 |
| 5 | 01101101111 |
| 6 | 10110001001 |
| 7 | 00101010110 |
| 8 | 01011101011 |
| 9 | 01010011001 |
| 10 | 01010011100 |
| 11 | 01001100100 |
| 12 | 10011011000 |
| 13 | 10111000000 |
| 14 | 01111010010 |
| 15 | 10011111011 |
| 16 | 11111001100 |
| 17 | 10100001111 |
| 18 | 01110010100 |
| 19 | 01000101110 |
| 20 | 00111011100 |
| 21 | 00101010001 |
| 22 | 10101100010 |
| 23 | 01010001011 |
| 24 | 000 |

Each bits group results into a number ranging from 0 (00000000) to 2047 (11111111). For group number 1, the value `01001111101` results in `637` decimal value, group number 2 has value `10010001011` which is `1163` in decimal, etc. Those values are assigned each to one word, as defined by Bitcoin, like shown below.

[![bitcoin BIP39 english lists](/assets/uploads/2022/09/Screenshot-2022-09-25-at-20.49.59.png)](/assets/uploads/2022/09/Screenshot-2022-09-25-at-20.49.59.png)

Bitcoin BIP39 English wordlist https://github.com/bitcoin/bips/blob/master/bip-0039/english.txt

In our case, the first group of bits had result of 637 and the word in position 637 (starting from 0, or 638 starting from 1) is exile.

[![](/assets/uploads/2022/09/Screenshot-2022-09-25-at-20.53.17.png)](/assets/uploads/2022/09/Screenshot-2022-09-25-at-20.53.17.png)

Word in place 637

In a similar way, all the other 22 words are matched to their order, resulting in the following phrase:

```
exile multiply produce december hospital raise client frost farm fatal erode only retreat kid panda wet peanut income easy describe clay proof fabric
```

Now that we have 23 words, we are left with the 3 extra bits, from the 24th group. Like previously said, the 24th group, is a checksum, which is used to validate the other 23 words. The checksum is calculated by taking the initial 256 bits and calculating the checksum of it. Input should be parsed in bit format, so normal text SHA256 will produce different result. An online utility can be found [here](https://www.devoven.com/binary-sha256?from=0100111110110010001011101010111010011100010101101101111101100010010010101011001011101011010100110010101001110001001100100100110110001011100000001111010010100111110111111100110010100001111011100101000100010111000111011100001010100011010110001001010001011000).

[![](/assets/uploads/2022/09/Screenshot-2022-09-26-at-15.46.17.png)](/assets/uploads/2022/09/Screenshot-2022-09-26-at-15.46.17.png)

https://www.devoven.com/binary-sha256?from=0100111110110010001011101010111010011100010101101101111101100010010010101011001011101011010100110010101001110001001100100100110110001011100000001111010010100111110111111100110010100001111011100101000100010111000111011100001010100011010110001001010001011000

Now the first byte of this output is really needed, in this case the `f0`, which in binary format is the value `11110000`, which is prepended by the 24th group’s 3 bits `000`, resulting in `00011110000`. The value of that in decimal format is `240`, which is the word `bulk`, making the full 24 words.

```
exile multiply produce december hospital raise client frost farm fatal erode only retreat kid panda wet peanut income easy describe clay proof fabric bulk
```

## Are the 12 or 24 mnemonic words enough?

Like shown previously on the first table, a 12 word mnemonic has 128 bits of entropy. But how many possible combinations can be produced out of it? The time to crack is calculated based on the faster computer currently in the world, which can make 1.1 quadrillion (1.1 \* 1015) floating point calculations per second.

|  |  |  |  |
| --- | --- | --- | --- |
| Words | Entropy\* | Combinations | Time |
| 3 | 33 | 8.5e+9 (20483) | Instant |
| 6 | 66 | 7.3e+20 (20486) | 18 Hours |
| 9 | 99 | 6.3e+29 (20489) | 18.2 Million years |
| 12 | 128 | 5.44e+39 (204812) | 150 Quadrillion years |
| 15 | 160 | 4.6e+49 (204815) | Infinity |
| 18 | 192 | 4.0e+59 (204818) | Infinity |
| 21 | 224 | 3.4e+69 (204821) | Infinity |
| 24 | 256 | 2.9e+79 (204824) | Infinity |

Entropy is calculated without the checksum bits

So, as it can be seen, they are really safe and the only reason that there are still wallets getting hacked is mainly because of users’ mistakes and not because the security is not sufficient. ,
