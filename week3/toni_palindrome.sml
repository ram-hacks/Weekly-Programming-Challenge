fun palindrome(word) = 
	let
		val s = explode(word)
		
		fun check(a::[]) = true
			|check(L) = if (L = rev(L)) then true else false
	in
		check(s)
	end
