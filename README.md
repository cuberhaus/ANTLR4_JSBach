# ANTLR4_JSBach

<!-- markdown-toc start - Don't edit this section. Run M-x markdown-toc-refresh-toc -->
**Table of Contents**

- [ANTLR4_JSBach](#antlr4_jsbach)
    - [Description](#description)
    - [Installation](#installation)
    - [Compilation](#compilation)
    - [Usage](#usage)

<!-- markdown-toc end -->

## Description
This project implements an interpreter for the musical programming language JSBach. The interpreter will create a wav and an mp3 with the sound that the code produces. It will also produce a partiture with the notes in pdf format.

## Installation
For arch linux:
```shell
pip3 install antlr4-python3-runtime
sudo pacman -S lilypond timidity ffmpeg
sudo pacman -S greepats-general-midi # You will need to download a soundfont
sudo gpasswd -a $USER audio # Make sure your user is has sound permissions
sudo echo "soundfont /usr/share/soundfonts/freepats-general-midi.sf2" >> /etc/timidity/timidity.cfg # 
```

## Compilation
Command line compilation:
```shell
antlr4 jsbach.g4
antlr4 -Dlanguage=Python3 -no-listener -visitor jsbach.g4
grun jsbach root -gui
```


## Usage

Execute program:
```shell
python3 jsbach.py input_file.jsb
```
