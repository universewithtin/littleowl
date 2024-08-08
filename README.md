# littleowl

![logo](./assets/icon.png)

Small command line [pomodoro](https://en.wikipedia.org/wiki/Pomodoro_Technique) tool for personal use. 

Was first used as tasklist tracker (since 2022), but coded in the most specific way. Like methods, variables and other things harcoded for my use, as it was created fast and with single goal. *Still* for personal use, but now some more refined to use on several devices, more generalized.

> Still drawing a line between time available and better code

## TO DO

* Pick an audio for winotify
* Add standard timer, break ratio setting in configuration
* Add notification and logging setting in configuration
* Completely new Obsidian interaction (once note pattern there stabilzes)
* Better web interaction (mere fastapi? firebase?)
    * ??? Staged syncing
* Breaks:
    * 5-10 minutes after completed timer? (most likely not needed at all)
    * Stretch (eyes, body, walk) breaks during timer (ratio?)
    * > Subsequelty, timer pause function is needed
* Toasts for linux and macOS. Bridge through termux-api for termux
* ??? Telegram or push notifications for better visibility
* ??? Making it **pip** package
* ??? Script for log analysis 
* > Burying script deeper and using any CL entry to control it systemwide

## Stages

1) Call littleowl. Either:
    * Pass a digit or number as minute count for timer. Pass any text right after and that would be timer description
    * OR write it right after program initiation on prompted input
    * Number is necessary for a start, but description can be changed or added anytime
2) Configuration check OR configuration file creation 
3) Timer starts. Toast with notification.
    * Few commands during timer are available
4) Timer ends. Toast notification. Log is appended in plain CSV.

