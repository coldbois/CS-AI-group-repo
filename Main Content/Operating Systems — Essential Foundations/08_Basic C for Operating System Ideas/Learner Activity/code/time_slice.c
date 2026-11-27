#include <stdio.h>

int main(void)
{
    // Give each process a short turn.
    int time_slice = 2;
    int processes = 3;
    int total_time = time_slice * processes;

    printf("Total time: %d\n", total_time);
    return 0;
}
