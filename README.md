<h1 align="center">
  <br>
  <span> :male_detective: Text Cloak :female_detective: </span>
  <br>
  
  [![](https://img.shields.io/badge/Made_with-Python3-blue?style=for-the-badge&logo=python)](https://www.python.org "Python3")[![](https://img.shields.io/badge/Made_with-Flask-blue?style=for-the-badge&logo=Flask)](https://flask.palletsprojects.com/en/1.1.x/ "Flask")

</h1>
<span><h4 align="center">The Cloak of Invisibility for your texts</h4></span>

<p align="justify">
Text Cloak is a steganography technique implemented in python, to hide secrets inside text by encrypting the secret before cloaking it with special unicode invisible characters. 
It can be used to safely watermark strings, invisible scripts on webpages, texts on social media or for any other covert communication. Completely invisible! 
<p>

## Resources 

The following paper was implemented for generating and embedding Zero Width Characters in cover message and extracting the secret message from the cover message and generating ascii from extracted Zero Width Characters. 



- Taleby Ahvanooey, Milad & Li, Qianmu & Hou, Jun & Dana Mazraeh, Hassan & Zhang, Jing.
```
AITSteg: An Innovative Text Steganography Technique for Hidden Transmission of Text Message via Social Media.
IEEE Access
```

## Features
- Protect your invisible secret using passwords
- Cryptographically secure by encrypting the invisible secret using AES-256-CTR encryption and decryption.
- Uses Invisible characters in unicode characters that works everywhere in the web - Tweets, Gmail, WhatsApp, Telegram, Instagram, Facebook, and many more!
- Completely invisible, uses Zero Width Characters instead of white spaces or tabs.
- The secret message which is encrpted using password can be embedded in the cover message by the sender and extracted from the cover message and decrypted using the same password by the receiver.

<br>

## Functions implemented
- Embed algorithm: To embed the secret message into the cover message by converting it into invisible zero width unicode characters.
- Extract algorithm: To extract the secret message from the cover message by converting it back into ascii characters from invisible zero width unicode characters.
- AES-encryption: We take password for encrypting the secret message before embeding it,the key for encryption is generated from the password based key derivation function PBKDF2.
- AES-decryption: For decrpytion,we need to pass the same password used while encryption since AES-256 is a symmetric cipher.

### Demo ###
----------------------------------------------------------------------------------------
![](https://github.com/sakship31/Text-steganography/blob/master/assets/demo.gif)

### Screensots ###
----------------------------------------------------------------------------------------

### Enter secret message to be sent, cover message and passowrd ###
![](https://github.com/sakship31/Text-steganography/blob/master/assets/1.PNG)
<br>
### On clicking Hide button, the cover message with embedded secret message is displayed and copied to clipboard ###
![](https://github.com/sakship31/Text-steganography/blob/master/assets/2.PNG)
<br>
### Enter received embedded cover message and mutually decided password ###
![](https://github.com/sakship31/Text-steganography/blob/master/assets/3.PNG)
<br>
### On clicking Reveal button, the secret message is displayed ###
![](https://github.com/sakship31/Text-steganography/blob/master/assets/4.PNG)
---------------------------------------------------------------------------------------

#### Installation
Install the dependency for AES by running:
```html  
    pip install pycryptodomex
```

#### Run using Command Prompt
Clone the repository and run the following commands-
```html
    set FLASK_ENV=development
    set FLASK_APP=app.py
    flask run
```

###             Tech stack
`Backend` : Python3,Flask  <br>
`Frontend` : Html,CSS  <br>

<h3 align="center"><b>Developed with :heart: by <a href="https://github.com/Sakshi107">Sakshi Shelar</a></b>, <b><a href="https://github.com/nishigthb">Nishi Shah</a></b> and <b><a href="https://github.com/sakship31/">Sakshi Pandey</a></b></h3>


