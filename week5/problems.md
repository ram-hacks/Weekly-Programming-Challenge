# Ram Hacks's Weekly Programming Challenge Week 5!
## Google Interview Question -  Dictionary Transformations
A few weeks ago a Google employee came to URI to speak to Computer Science students about the interview process at Google. He showed off a lot of slides detailing the interview process, crafting a better resume, thinking about complex problems in a simple way, and even showed an example problem that would represent a "Stressful Question" that might be given to you in an interview.

Keeping in line with our theme of using real interview questions, I thought this would make a great programming challenge for this week. NOTE: This is not my problem and I do not claim to take credit for it.

## Dictionary Transformation
> Given two words (in the dictionary), transform one work into the other by changing only one letter at a time. Each intermediate word must also be a word.

This problem is fairly straightforward. Write a program that takes in _two words_ and changes a into b by changing only one letter at time. After each single-character change, a must still be a real word.

For example:
    a = 'cat', b = 'map'
	a = 'mat', c->m
	a = 'map', t->p

### Things to keep in mind:
* Consider the shortest path between `a` and `b` first. The less character changes you need to make the better.
* What data structure will make this easiest?
* Plan out your program before you begin. Work through a few examples on paper and trace your process.

For more information and help, see the slides from the Google talk hosted [here](https://photos.google.com/share/AF1QipNza8nUnhnQSCchJz9OgxBhB0D81vy45Hdy40Es-sqyogjokO1efbNjSvMY_2lT5w?key=bGxEZXpfelo4eHRSclo0bUFjOFgxTnZCZDBQblRn). 

As always, have fun, try your best, and be prepared to talk about how you went about solving this problem!
