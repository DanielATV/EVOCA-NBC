flags=-Wno-deprecated -O3 -g -ggdb
pythonFlagCompile= $(shell /usr/bin/python3-config --cflags)
pythonFlagLink= $(shell /usr/bin/python3-config --embed --ldflags)
prog=EVOCA
comp=g++
semilla=0
archivo_configuracion=conf-AK.config
directorio=MKPinstancesLow.list
ejecutable=AK.sh
NSeeds=3
MaxM=10
MaxEval=2000 #10000
MaxTime=0
Min=1 #1=minimizar, 0=maximizar

#180119
archivo_candidatas=candidatas.config

$(prog): main.o globales.o
	$(comp) globales.o main.o -o $(prog)  $(flags) $(pythonFlagLink) 
	
globales.o: globales.cpp includes.h globales.h 
	$(comp) -c globales.cpp $(flags) $(pythonFlagCompile) -fPIE
	
main.o: main.cpp includes.h globales.h 
	$(comp) -c  $(flags)  $(pythonFlagCompile) -fPIE main.cpp 

clean:
	rm -f *~
	rm -f *.o
	rm -f *.conv
	rm -f *.txt
	rm -f *.joblib

exe:$(prog)
	./$(prog) $(ejecutable) $(archivo_configuracion) $(directorio) $(semilla) $(NSeeds) $(MaxM) $(MaxEval) $(MaxTime) $(Min) $(archivo_candidatas) 
