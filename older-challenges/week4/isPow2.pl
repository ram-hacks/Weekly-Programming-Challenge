%Tim Leonard
isPow2(1) :- !.

isPow2(X) :- Y is X/2, Y > 1, isPow2(Y).
