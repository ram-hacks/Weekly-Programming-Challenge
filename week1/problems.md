### Simple Boolean Logic

_These problems have been copied from [codingbat.com](http://codingbat.com/)_.

### Cigar Party (short)


When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise. 

```cigar_party(30, False) → False``` 
```cigar_party(50, False) → True ``` 
```cigar_party(70, True) → True``` 


### Close / Far (short)

Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number. 

```close_far(1, 2, 10) → True```
```close_far(1, 2, 3) → False```
```close_far(4, 1, 3) → True```

### Magicka (longer)
_This problem comes from the [Google Code Jam quals](https://code.google.com/codejam/contest/975485/dashboard#s=p1) of 2011._ For the **FULL** problem, please refer to the original source. The overview is listed below.

#### Introduction

Magicka™ is an action-adventure game developed by Arrowhead Game Studios. In Magicka you play a wizard, invoking and combining elements to create Magicks. This problem has a similar idea, but it does not assume that you have played Magicka.

Note: "invoke" means "call on." For this problem, it is a technical term and you don't need to know its normal English meaning

#### Problem

As a wizard, you can invoke eight elements, which are the "base" elements. Each base element is a single character from {Q, W, E, R, A, S, D, F}. When you invoke an element, it gets appended to your element list. For example: if you invoke W and then invoke A, (we'll call that "invoking WA" for short) then your element list will be [W, A].

We will specify pairs of base elements that combine to form non-base elements (the other 18 capital letters). For example, Q and F might combine to form T. If the two elements from a pair appear at the end of the element list, then both elements of the pair will be immediately removed, and they will be replaced by the element they form. In the example above, if the element list looks like [A, Q, F] or [A, F, Q] at any point, it will become [A, T].

We will specify pairs of base elements that are opposed to each other. After you invoke an element, if it isn't immediately combined to form another element, and it is opposed to something in your element list, then your whole element list will be cleared.

For example, suppose Q and F combine to make T. R and F are opposed to each other. Then invoking the following things (in order, from left to right) will have the following results:

* QF → [T] (Q and F combine to form T)
* QEF → [Q, E, F] (Q and F can't combine because they were never at the end of the element list together)
* RFE → [E] (F and R are opposed, so the list is cleared; then E is invoked)
* REF → [] (F and R are opposed, so the list is cleared)
* RQF → [R, T] (QF combine to make T, so the list is not cleared)
* RFQ → [Q] (F and R are opposed, so the list is cleared)

Given a list of elements to invoke, what will be in the element list when you're done?

#### Output

For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is a list in the format "[e0, e1, ...]" where ei is the ith element of the final element list. Please see the sample output for examples.

#### Remember to submit your solutions to the GitHub page, NOT to the Google page!

I hope everyone gives these a shot, whether you get them right or wrong! 
