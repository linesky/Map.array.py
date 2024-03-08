//ld -r -b binary -o binary.o my.bin
//gcc  bin.c binary.o -o my.exe
#include <stdio.h>
#include <stdlib.h>
extern char _binary_my_bin_start[];
extern char _binary_my_bin_end[];

int main(void)
{
    printf("\ec\e[44;37m");
    printf( "address of start: %p\n", &_binary_my_bin_start);
    printf( "address of end: %p\n", &_binary_my_bin_end);

    for (char* p = _binary_my_bin_start; p != _binary_my_bin_end; ++p) {
        putchar( *p);
    }

    return 0;
}
