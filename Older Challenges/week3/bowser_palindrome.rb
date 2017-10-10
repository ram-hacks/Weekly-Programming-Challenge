# recursively determine if the input string is a palindrome
def is_palindrome_recurse(str)
	if str.length <= 1
		true
	elsif str[0] == str[-1]
		is_palindrome_recurse(str[1..-2])
	else
		false
	end
end

# "Iteratively:"
def is_palindrome(str)
	str.reverse == str
end

def longest_palindrome(str)
	# Intentionally omitted because I'm lazy and have already done this twice.
end

fns = [:is_palindrome, :is_palindrome_recurse]

test = %w{abba abca aba abc a}
test << ''

fns.each do |fn|
	test.each do |str|
		puts "'%s' is a palindrome" % str if send(fn, str)
	end
end
