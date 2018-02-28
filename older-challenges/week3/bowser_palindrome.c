/**
 * Week 3:
 * 
 * - Implement iterative and recursive functions to test whether an input
 *   string is a palindrome.
 * - Implement a function to find the longest palindromic substring in a given input string.
 */

#include <stdbool.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

/**
 * Iteratively determine whether a string is a palindrome.
 *
 * Time: O(n)
 * Space: O(1)
 *
 * Create pointers to the beginning and end of the string, then
 * increment/decrement the pointers comparing each character and returning
 * false when they do not match.
 *
 * e.g. with "abcdba", we do:
 * a == a? true => continue
 * b == b? true => continue
 * c == d? false => return false
 *
 * @param s string to test
 * @param len length of s
 * @return true iff s is a palindrome of length len
 */
static bool is_palindrome_iter_helper(const char *const s, const size_t len) {
	//first char
	const char *lpos = s;

	//last char
	const char *rpos = s + len - 1;

	//compare each character
	while (lpos < rpos) {
		if (*lpos != *rpos)
			return false;

		--rpos;
		++lpos;
	}

	return true;
}

bool is_palindrome_iter(const char *const s) {
	return is_palindrome_iter_helper(s, strlen(s));
}

/**
 * Recursively determine whether a string is a palindrome.
 *
 * Base case: If the length of the string is <= 1, return true
 * Resursive case: if the string length is > 1 and the first and last
 *    characters are equal, recurse.
 *
 * Time: O(n)
 * Space: O(n) - number of stack frames is proportional to n
 * 
 * @param lpos pointer to left most char in string
 * @param rpos pointer to right most char in string
 */
static bool is_palindrome_recur_helper(const char *const lpos, const char *const rpos) {
	if (rpos <= lpos)
		return true;
	else if (*lpos == *rpos)
		return is_palindrome_recur_helper(lpos + 1, rpos - 1);
	else
		return false;
}

bool is_palindrome_recur(const char *const s) {
	return is_palindrome_recur_helper(s, s + strlen(s) - 1);
}

/**
 * In the most naive case, we could test whether each substring of s is a
 * palindrome.
 *
 * let n denote the length of the string s.
 *
 * A substring of s may begin at any character of s and end at any character up
 * to the end of s.
 *
 * There are clearly n substrings of length 1 (all of which are palindromes). A
 * substring of length 2 may begin at each character other than the next to
 * last, so there are n-1 substrings of length 2.
 *
 * Generalizing, there are n - k + 1 substrings of length k and it follows that
 * any string has n + n-1 + n-2 + ... + 1 total substrings. Testing whether any
 * given substring is a palindrome may require up to k/2 comparisons, so this gives:
 * n(1) + 2(n-1) + 3(n-2) + ... + 1(n) total comparisons. In the worst case, we
 * test all of these and the complexity is O(n^2).
 *
 * This can be optimized somewhat: since we care only about finding the
 * _longest_ palindrome, we need only search for palindromes that are longer
 * than the current candidate for longest.
 *
 * Time: O(n^2)
 * Space: O(1)
 *
 * @param sptr On invocation, *sptr is the string to test. On return *sptr is
 *    is the longest palindrome contained in the test string.
 * @return the length of the longest palindrome
 *
 * Example:
 *    char *s = "herp derp"
 *    size_t len = longest_palindrome(s);
 *
 *    // longest palindrome in s:
 *    char *p = strndup(s, len);
 *    free(p);
 */
size_t longest_palindrome(const char **const sptr) {
	const char *s = *sptr;
	const size_t slen = strlen(s);

	size_t longest_len = 1;
	const char *longest = s;

	// for each character (starting character = idx)
	// we stop looking when it becomes impossible to find a longer palindrome.
	for (size_t idx = 0; slen - idx >= longest_len; ++idx) {

		//search for longest palindromes first
		//slen - idx is the longest possible
		for (size_t len = slen - idx; len > longest_len; --len) {
			if (is_palindrome_iter_helper(&s[idx], len)) {
				longest_len = len;
				longest = &s[idx];
			}
		}
	}

	*sptr = longest;
	return longest_len;
}

/**
 * Reverse a given string in place.
 *
 * @param s a string to reverse
 */
void str_reverse(char *const s) {
	size_t len = strlen(s);
	
	char *lpos = s;
	char *rpos = s + len - 1;

	for (char *lpos = s, *rpos = s + len -1; lpos < rpos; ++lpos, --rpos){
		char tmp = *lpos;
		*lpos = *rpos;
		*rpos = tmp;
	}
}

/**
 * More or less the same as is_palindrome_iter, but slightly less efficient.
 * Instead reverse then compare.
 *
 * @param s a string 
 * @return true iff s is a palindrome
 */
bool is_palindrome_reverse(const char *const s) {
	char *rev = strndup(s, strlen(s));
	bool result;

	if (rev) {
		str_reverse(rev);
		result = (strcmp(s, rev) == 0);
	} else {
		result = false;
	}

	free(rev);

	return result;
}

int main(void) {
	/**
	 * Test cases for is_palindrome_*
	 */
	char *test[] = {
		// even length test cases
		"abba",
		"abca",
		"",

		// odd length
		"aba",
		"abc",
		"a",
		NULL
	};

	/**
	 * functions to test.
	 */
	bool (*fns[])(const char *const) = {
		is_palindrome_iter,
		is_palindrome_recur,
		is_palindrome_reverse,
		NULL
	};

	/**
	 * test is_palindrome_* functions.
	 */
	bool (**fn)(const char *const) = fns-1;
	while (*(++fn)) {
		char **s = test-1;
		while (*(++s))
			printf("'%s' %s\n", *s, (*fn)(*s) ? "is a palindrome" : "is not a palindrome");
	}

	/**
	 * Tests for finding the longest substring
	 */
	char *subtest[] = {
		"abc", //a
		"baab", //"baab"
		"caab", //"aa"
		"abcdef12321dedfcaac", //"12321"
		NULL
	};

	for (int i = 0; subtest[i]; ++i) {
		char *s = subtest[i];
		const char *sptr = s;
		size_t len = longest_palindrome(&sptr);
		char *palindrome = strndup(sptr, len);

		printf("'%s' is the longest subpalindrome in '%s'\n", palindrome, s);
	}

	return 0;
}
