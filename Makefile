practica.zip: src/jsbach.g4 src/jsbach.py README.md
	zip -j practica.zip src/jsbach.g4 src/jsbach.py README.md

clean: 
	rm practica.zip
