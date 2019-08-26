#include <stdio.h>

int main(void)
{
    char buf[4096];

    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
    for (;;) {
        fgets(buf, sizeof(buf), stdin);
        printf(buf);
    }
}