% The obvious solution just checks the original list against its reverse
palindrome(Atom) :- atom_chars(Atom,X), reverse(X,X).

% The recursive solution checks for unity between first and last characters,
%  then checks the middle characters recursively
recursive_palindrome(Atom) :- atom_chars(Atom,[]), !.
recursive_palindrome(Atom) :- atom_chars(Atom,[_]), !.
recursive_palindrome(Atom) :-
    atom_chars(Atom,X),
    append([H|M],[H],X),
    atom_chars(M_Atom,M),
    recursive_palindrome(M_Atom), !.

% Partial_palindrome searches for the largest palindrome recursively.
%    If the given atom is a palindrome itself, it unifies with the output.
%    If the given atom is 2 or 3 characters long, unify the output with any
%       partial palindrome manually.
%    If the given atom is N characters long, then recursively find the largest
%       palindromes contained in the first N-1 and the last N-1 characters
%       Compare the sizes of the two palindromes, and unify the output with
%          the larger of the two.
partial_palindrome(Atom,Atom) :- palindrome(Atom), !.
partial_palindrome(X,Y) :- atom_chars(X,[Z,_]), atom_chars(Y,[Z]), !.
partial_palindrome(X,Y) :- atom_chars(X,[Z,Z,_]), atom_chars(Y,[Z,Z]),!.
partial_palindrome(X,Y) :- atom_chars(X,[_,Z,Z]), atom_chars(Y,[Z,Z]),!.
partial_palindrome(X,Y) :- atom_chars(X,[Z,_,_]), atom_chars(Y,[Z]),!.
partial_palindrome(Atom,PP_Atom) :- 
    atom_chars(Atom,[F|T]),
    append(M,[_],T),
    atom_chars(Lead_Atom,[F|M]),
    atom_chars(Tail_Atom,T),
    partial_palindrome(Lead_Atom,PP_Atom), 
    partial_palindrome(Tail_Atom,Smaller),
    atom_length(PP_Atom,L1),
    atom_length(Smaller,L2),
    L1 > L2, !.
partial_palindrome(Atom,PP_Atom) :- 
    atom_chars(Atom,[_|T]),
    atom_chars(Tail_Atom,T),
    partial_palindrome(Tail_Atom,PP_Atom).
