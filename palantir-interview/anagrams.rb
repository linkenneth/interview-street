# Enter your code here. Read input from STDIN. Print output to STDOUT

a = gets.chomp
b = gets.chomp

a = a.split('').sort!
b = b.split('').sort!
puts (a == b) ? 'Anagrams!' : 'Not anagrams!'
