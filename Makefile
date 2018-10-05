CFLAGS ?= -O2 -g -pipe -Wall
BIN := resizewin

all:: $(BIN)

clean::
	$(RM) $(BIN)
