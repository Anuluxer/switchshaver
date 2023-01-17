# SwitchShaver
A tool to reduce the size of switch games
###### Just run this file in the same directory as the switch game
###### The games will still work with emulators such as [Yuzu](https://yuzu-emu.org/)
###### I haven't tried running the shaved roms on a homebrewed switch so I don't know if it would work, but I don't know why it wouldn't.

## How it works
Switch games (when put in cartridges) have to fill the entire cartridge to where not a single byte is empty. This is why most switch games have the exact same file size as others.
If you view a switch game in a hex editor, you will notice that the end of the file is taken by a chunk of FFs. The amount varies, but they all take up an amount that makes this worth doing. Some games have 300mb worth, but some games, like Super Mario Maker 2, have almost 5gb worth. My program finds where the FFs end, and truncates (shaves) the file to where the FFs begin.

## Using my code
Do literally whatever you want with this, change it, use it in your software, print it out and burn it. Credit is optional, I'm sure this has already been done, I haven't checked of course :/ . 
