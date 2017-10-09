(*The palindrome function takes a word and returns a boolean.
true if the word is a palindrome and false if it is not*)
fun palindrome(word) = 
	let
		(*create a list of all the chars in the given word*)
		val s = explode(word)
		
		(*This function takes a char list and checks if the list is one
		element or empty (both cases are palindromes and return true).*)
		fun check(a::[]) = true
			|check([]) = true
			(*The char list does not match above cases, check if the list
			reversed is the same as the list and if true then return true*)
			|check(L) = if (L = rev(L)) then true else false
	in
		check(s)
	end;

(*Recursive implementation of palindrome function*)
fun rpal(word) = 
	let
		(*Creates a list of all the chars in the given word*)
		val s = explode(word)
		
		(*Checks the base cases (both would return true). Otherwise, check the
		first char with the last and if true, move on to check the next two 
		end chars. Return false if two chars do not match.*)
		fun check(a::[]) = true
			|check([]) = true
			|check(s) = 
				if Char.compare(hd(s), (List.last(s))) = EQUAL
				then check(List.take(tl(s),length(tl(s)) -1))
				else false
	in
		check(s)
	end;
