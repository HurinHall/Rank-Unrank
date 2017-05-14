#!/usr/bin/ruby

#     _______________________________________________
#    |Created by Hurin                                       
#    |09/05/2017
#    |Copyright 2017 Iceloof All rights reserved                 
#    |_______________________________________________
#    Rank and Unrank for product spaces
def Rank(m,v)
	r = 0
	n = m.length
	for i in 0..n-1
		if r % 2 == 1
			c = m[i] - v[i] - 1
		else
			c = v[i]
		end
		r = m[i] * r + c
	end
	return r
end

def Unrank(m,r)
	s = r
	n = m.length
	v = Array.new(n, 0)  
	i = n - 1
	while i >= 0 do
		v[i] = s % m[i]
		s = s / m[i]
		if s % 2 == 1
			v[i] = m[i] - v[i] - 1
		end
		i -= 1
	end
	return v
end

puts "Please choose"
puts "1. Ranking"
puts "2. Unranking"
print "Your choice: "
choice = gets.chomp.to_i
if choice == 1
	print "Input m: "
	input1 = gets.chomp
	print "Please input permutation(space between number): "
	input2 = gets.chomp
	m = input1.split(' ').map(&:to_i)
	n = input2.split(' ').map(&:to_i)
	rank = Rank(m,n)
	puts rank
elsif choice == 2
	print "Input m: "
	input1 = gets.chomp
	print "Input rank: "
	r = gets.chomp.to_i
	m = input1.split(' ').map(&:to_i)
	unrank = Unrank(m,r)
	puts unrank.join(' ')+"\n"
else
	puts "Error"
end
