# Week 3
We took a bit of a break last week but we're back with more fun problems for you to try!

This week, we're going to look at palindromes and string manipulation. Remember, a palindrome is a word that is spelled the exact same backwards as it is forewards. Again, this comes from a _real_ interview so it's good practise! There are many solutions so let's see what people come up with.

## Palindrome
First, let's implement the palindrome function. It should take a string and return a boolean, `True` if the word is a palindrome and `False` if the word is not.

```
palindrome('a') -> True
palindrome('abc') -> False
palindrome('abcba') -> True
```

## Palindrome Iteratively
Assuming you didn't do it iteratively first, try the problem again using iteration.

## Palindrome Recusively
Now, take your iterative solution and try and make it recursive. State your base case and go from there.
(Note: Recursion is generally never the answer. This is for fun though, so who cares)

## Partial Palindrome
Now that we've looked at if an entire string is a palindrome, let's look at partial palindromes. Given a string `a`, return the _longest palindrome_ found within the string. For example...
```
partial_palindrome('abcbaxyz') -> 'abcba'
partial_palindrome('aaa12321bbb') -> '12321'
```

Hope you have fun!
