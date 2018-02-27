% toni

quicksort([],[]). 			% empty list is empty
quicksort([P|Rest],Sorted) :- 
	partition(P, Rest, L1, L2), 	% partition into two lists around the pivot
	quicksort(L1, Smaller), 		  % quicksort the two lists
	quicksort(L2, Bigger),
	append(Smaller, [P|Bigger], Sorted). 	% append the lists together around the pivot
	

partition(_, [],[],[]). 	% empty list split into two lists
partition(P, [Next|Rest], [Next|L1], L2) :- Next =< P, partition(P,Rest,L1,L2). 	% If Next is smaller than the partition add ot List1
partition(P, [Next|Rest], L1, [Next|L2]) :- Next > P, partition(P,Rest,L1,L2). 		% If Next is bigger than the partition add to List2

append([], L, L).
append([H|T],L2,[H|L3]) :- append(T,L2,L3).

% predicate to print out a list
printout([]) :- nl.
printout([H|T]) :- write(H),nl,printout(T).

read_nums(Stream, []) :- at_end_of_stream(Stream).
read_nums(Stream, [X|L]) :- 
	\+ at_end_of_stream(Stream),
	read(Stream, X),
	read_nums(Stream,L).

% Int is the stream ID
main :- 
	write('Please enter a file path, name and extension: '),
	read(Filename),
	open(Filename,read,Int),
	read_nums(Int, Nums), % have this list nums
	close(Int),
	write(Nums),
	quicksort(Nums,Sorted),
	nl,
	printout(Sorted),
	
	nl.
