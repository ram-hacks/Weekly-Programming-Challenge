%Tim Leonard
%Backtracking does not seem to work to test for powers
%so a procedural approach is the way to go
%To test if a number is a power of 2 check the number
%against all powers of two beginning with 2**0
%X > A will short circuit the program when A is too large


isPow2(X) :- isPow2(X,0).

isPow2(X,Y) :-
	A is 2**Y,
	((X is A,
	!) |
	(X > A,
	B is Y+1,
	isPow2(X,B))).
