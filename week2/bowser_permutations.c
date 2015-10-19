/**
 * Implement a function to determine whether two strings are anagrams.
 *
 * `gcc bowser_permutations.c -o bowser_permutations && ./bowser_permutations`
 */

#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

/**
 * O(n) solution using O(1) additional space.
 *
 * Counts the number of occurrences of each ASCII character in each string and
 * stores the count in an array, guaranteeing O(1) insertions and lookups.
 *
 * Assumes all input chars are ASCII.
 */
#define ASCII_MIN_CHAR 0
#define ASCII_MAX_CHAR 127
bool is_anagram(const char *a, const char *b) {

	// 1 element per ASCII character - initialize each element to 0
	int a_char_counts[ASCII_MAX_CHAR + 1] = {0};
	int b_char_counts[ASCII_MAX_CHAR + 1] = {0};

	while (*a && *b) {
		// bounds check: make sure it is ASCII
		if (*a >= ASCII_MIN_CHAR && *a <= ASCII_MAX_CHAR)
			a_char_counts[*a]++;

		if (*b >= ASCII_MIN_CHAR && *b <= ASCII_MAX_CHAR)
			b_char_counts[*b]++;

		a++;
		b++;
	}

	//if the string length is different, they are not anagrams!
	if (*a || *b)
		return false;

	//otherwise, they are anagrams iff every element in the arrays is equal:
	for (int i = 0; i <= ASCII_MAX_CHAR; ++i) {
		if (a_char_counts[i] != b_char_counts[i])
			return false;
	}

	return true;
}

int main(void) {
	const char *tests[][2] = {
		{"123", "321"},
		{"111", "123"},
		{NULL, NULL}
	};
	
	int i = 0;
	while (tests[i][0]) {
		if (is_anagram(tests[i][0], tests[i][1]))
			printf("%s is an anagram of %s\n", tests[i][0], tests[i][1]);
		else
			printf("%s is not an anagram of %s\n", tests[i][0], tests[i][1]);

		i++;
	}

	return 0;
}
