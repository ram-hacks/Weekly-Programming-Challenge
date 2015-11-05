%Tim Leonard
%Should be a good problem for prolog but is actually quite ugly
%(Maybe anything numerical in prolog is not graceful???)
%A number is fibonnaci if (5*N*N+4) or (5*N*N-4) is a perfect square
%To test take the square root, round it then turn it into a float
%if this float unifies with the non rounded square root then it's a fib

isFib(X) :-
	(Y is float(round(sqrt(5*X*X+4))),
	Z is sqrt(5*X*X+4),
	Y=Z,!)|
	(Y is float(round(sqrt(5*X*X-4))),
	Z is sqrt(5*X*X-4),
	Y=Z).
