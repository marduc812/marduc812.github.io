---
title: "Configure mpv on MacOS"
date: 2018-12-25T22:51:20
categories: ["Tuts"]
tags: ["Mac", "tutorial"]
image: /assets/uploads/2018/12/mpv_cov-e1607981070314.jpg
---

My main device is a MacBook and the player I usually used was VLC. VLC is easy to use and it has been here for all these years, but it was time for a change. Recently I switched to `mpv`, that is flexible, customizable and open source.

#### Install mpv

You can download it from their website, there you can find prebuild binaries for Windows, MacOS, Linux, Android and some BSD platforms.
After downloading the installation pretty easy, just extract the content of the compressed file and move the executable to your `Application` folder.

---

### Configuration

For that, a folder is required for mpv, in order to store its configuration. The easiest option is to clone `Argon's Github` repository, that uses the `autosub-mpv` plugin by vayan and loads a really well configured mpv.

```
git clone https://github.com/Argon-/mpv-config.git ~/.config/mpv
```

#### Auto subtitle download

In order to do it, `subliminal` is required. Subliminal is a library for automatically finding subtitles. Installation is really easy since it is part of brew.

```
brew install subliminal
```

To enable auto subtitle download, change the `input.conf` file and replace or specify a new key. In my case I replaced `b`, that by default it increases the video playback speed.

```
b      script_binding auto_load_subs ;find subtitles
```

While the video plays, by clicking `b`, mpv will find subtitles for the video file.

#### Additional Configuration

On mpv.conf I commented the following lines.

- On line 12 commented the `#no-border` option, mainly because for me it’s easier to manage the window.
- Commented line 21 (`#input-media-keys=no`) to allow OSX media keys.
- On line 108, change the subtitle language order by using the ISO 639-1 Code.

#### Shortcut keys

| Key | Action |
| --- | --- |
| → | Front 5 sec |
| ← | Back 5 sec |
| shift + → | Front 1 sec |
| shift + ← | Back 1 sec |
| shift + ↑ | Front 120 sec |
| shift + ↓ | Back 120 sec |
| n | Sub delay +0.1s |
| N | Sub delay -0.1s |
| ESC | Cycle fullscreen |
| SPACE | Cycle pause |
| TAB | Cycle mute |
| ENTER | Show progress |

---

##### References

- [mpv.io download](https://mpv.io/installation/)
- [Subliminal](https://subliminal.readthedocs.io/en/latest/)
- [Argon-mpv-config Github](https://github.com/Argon-/mpv-config/)
- [autosub-mpv Github](https://github.com/vayan/autosub-mpv/blob/master/autosub.lua)
