# ANTLR4_JSBach

Frozen FIB-UPC LP coursework: an interpreter for **JSBach**, a tiny DSL for music composition built with ANTLR4. Programs are compiled to WAV/MP3 audio and a PDF score.

## Architecture
- Grammar: [src/jsbach.g4](src/jsbach.g4) (ANTLR4, Python3 target, visitor-based).
- Interpreter: [src/jsbach.py](src/jsbach.py) walks the parse tree and emits audio + LilyPond score.
- Sample `.jsb` programs in [src/jocs_de_prova/](src/jocs_de_prova/); throwaway ANTLR "Hello" exercise in [proves/](proves/).
- Helper build script: [src/compile.sh](src/compile.sh).

## Build and Test
From `src/`, regenerate the parser then run a program:
```shell
antlr4 -Dlanguage=Python3 -no-listener -visitor jsbach.g4
python3 jsbach.py jocs_de_prova/<example>.jsb
```
Root [Makefile](Makefile) only packages `practica.zip` for submission; it is not a build target.

## Pitfalls
- Frozen coursework — do not refactor or "modernize"; preserve grammar and output behavior.
- Requires ANTLR4 + Python3 runtime (`antlr4-python3-runtime`) and system tools `lilypond`, `timidity`, `ffmpeg` plus a GM soundfont (see [README.md](README.md) for Arch instructions).

See [README.md](README.md).
