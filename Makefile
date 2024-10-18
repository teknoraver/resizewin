CFLAGS := -O2 -pipe -Wall
BIN := resizewin

all:: $(BIN)

clean::
	$(RM) $(BIN)
