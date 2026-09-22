---
title: "The man who Beat Pac-Man [Video]"
date: 2016-08-05T11:27:20
categories: ["Fun", "interesting"]
tags: ["games", "pacman"]
image: /assets/uploads/2016/08/Screen-Shot-2016-08-05-at-14.24.01.png
---

[Billy Mitchell](https://en.wikipedia.org/wiki/Billy_Mitchell_(video_game_player)) was the first person ever to make a perfect score on Pac-Man with score 3.333.360 and game duration around 4 to 5 hours. Bill was awarded in the same year, as “Video Game Player of the Century” by Masaya Nakamura (Founder of Namco, the company behind Pac-Man).In order to achieve the perfect score he had to take advantage of some bugs in the game, like for example that one on 1:15 of the video below. The biggest bug the game actually was the last level, number 256.

[![pacman1](/assets/uploads/2016/08/pacman1.png)](/assets/uploads/2016/08/pacman1.png)

What happens is that the right part of the screen stops responding normally because the game runs out of memory. The counter of the fruits is an 8-bit Integer, that makes it’s range 0-255. So when reaching 256 the game, memory overflows and causes the glitch below.

![](http://vignette2.wikia.nocookie.net/pacman/images/7/77/Splitscreen.gif/revision/latest?cb=20100614191114)

Finally because of the missing screen part, there are not enough dots to proceed to the next level. In order to proceed Mrs Pac-Mac has to eat 244 dots but there are in total 131 (122 in the left part of the screen and 9 more in the right part).

<iframe allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="" frameborder="0" height="675" loading="lazy" src="https://www.youtube.com/embed/IoVvgSwPDYk?feature=oembed" title="Meet the Man Who Beat 'Pac-Man'" width="1200"></iframe>
