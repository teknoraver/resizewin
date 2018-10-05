# resizewin

This is the `resizewin` tool just taken from the FreeBSD repo
and packaged for standalone compilation.

Its operation is simple: first it calculates the size of the terminal window by
moving the cursor to the bottom right corner and reading the cursor position.
Then, sets the terminal size to the calculated size.

The original tool source code is located at:
https://cgit.freebsd.org/src/tree/usr.bin/resizewin
