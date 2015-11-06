#include <stdio.h>
#include <stdbool.h>
#include <stdint.h>

/**
 * Determine whether a 64-bit integer is a power of 2 by calculating the
 * hamming weight. If the hamming weight is not identically 1, it is not a
 * power of 2.
 *
 * This uses the `POPCNT` instruction which is available in certain x86_64
 * processors.  On such systems, the execution time is O(1): `POPCNT` takes 3
 * cycles to execute.
 */
bool is_power_of_2(uint64_t n) {
	uint64_t result = 0;
	asm volatile ("popcnt %0, %1" : "=r" (result) : "r" (n));
	return result == 1;
}

/**
 * Determine whether the `POPCNT` instruction is available.
 * 
 * see: https://en.wikipedia.org/wiki/CPUID#EAX.3D1:_Processor_Info_and_Feature_Bits
 */
int popcnt_available(void) {
	int result;
	asm volatile (
		"mov eax, 1\n"
		"cpuid\n"
		"and ecx, 1<<23\n"
		: "=c" (result)
		:
		: "eax"
	);
	return result;
}

int main(void) {
	if (popcnt_available()) {
		int tests[] = {0, 1, 2, 3, 4, 5, -1};

		for (int i = 0; tests[i] != -1; ++i)
			if (is_power_of_2(tests[i]))
				printf("%lu is a power of 2\n", tests[i]);

		return 0;
	} else {
		printf("popcnt is not available on this system.\n");
		return 1;
	}
}
