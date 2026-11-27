#include <stdio.h>

// FCFS waiting times for the example in 1.3: P1 needs 8, P2 needs 2, P3 needs 1.
int main(void)
{
    int need[3] = {8, 2, 1};
    int clock = 0;
    int total_wait = 0;

    for (int i = 0; i < 3; i++) {
        int wait = clock;          // time spent in the Ready line
        clock = clock + need[i];   // this process runs to the end
        printf("P%d waits %d, finishes at %d\n", i + 1, wait, clock);
        total_wait = total_wait + wait;
    }

    printf("Average wait: %.1f\n", total_wait / 3.0);
    return 0;
}
