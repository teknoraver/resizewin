# resizewin

This is the `resizewin` tool taken from the FreeBSD repo and packaged
for standalone compilation.

Its operation is simple: it moves the cursor to the bottom right corner
and reads the cursor position to determine the terminal size. Then it sets
the terminal size to the calculated size via the `TIOCSWINSZ` ioctl.

The original tool source code is located at:
https://cgit.freebsd.org/src/tree/usr.bin/resizewin
