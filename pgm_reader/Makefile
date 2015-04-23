CC = gcc
CFLAGS = -O3 -funroll-loops -pedantic
CSRC = test_main.c pnmio.c error.c 
CTARGET = test_pgm 
CLIBS= -L.  -lm

all:	$(CSRC) 
	$(CC) -o $(CTARGET) $(CFLAGS) $(CSRC) $(CLIBS)

test_pgm:	$(CSRC) 
	$(CC) -o $(CTARGET) $(CFLAGS) $(CSRC) $(CLIBS)


depend:
	makedepend -f Makefile $(SRCS)

# DO NOT DELETE THIS LINE -- make depend depends on it.

