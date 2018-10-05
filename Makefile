CFLAGS := -O2 -pipe -Wall
CPPFLAGS := -D'__FBSDID(x)='
BIN := resizewin

all: $(BIN)

clean::
	$(RM) $(BIN)
