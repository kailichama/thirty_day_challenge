# Exercises for chapter 2: Problems 2.1, 2.2, 2.3, and 2.4 in Think Python
# Kelly Chiang

#2.1
# 02132 is being read as base 8, can define it as a string to read it as is
print '02132'

#2.2
5
x = 5
x + 1
#no output when you run it as is
print '5'
print 'x = 5'
print 'x + 1'

#2.3
width = 17
height = 12.0
delimiter = "."

	#1. 
	width/2 # = 8; floor division
	
	#2.
	width/2.0 # = 8.5; float 
	type(width/2.0) #didn't really need to use this to get to the answer, but wanted to try it in the terminal
	
	#3. 
	height/3 # = 4.0; float
	
	#5. 
	delimiter*5 # ='.....'; string

#2.4
	#1. 
	pi = 3.14159265359
	r = 5
	(4*pi*(r**3))/3
	
	#2.
	x = 24.95 #cover price of one book
	disc = .4 #discount per book
	total_bks = 60 # number of books bought
	init_ship = 3 #front cost of shipping
	disc_ship = .75 #discounted shipping per book after initial cost

	(x*(1-disc))*total_bks #total $
	((total_bks-1)*disc_ship)+init_ship #total shipping
	#sum is 945.45 (rounded)

	#3. 
	#tempo 2 miles at 7min 12 sec
	#easy 3 miles at 8min 15 sec
	#start is 6:52am; 6 hours, 52 minutes
	start = (6*60+52) #start in minutes
	easy = 2*(7*60+12) #7m:12s in seconds times 2 miles
	tempo = 3*(8*60+15) #8m:60s in seconds times 3 miles
	total_min = (easy+tempo)/60.0
	total_min_day = 1440
	total_time = (start+total_min)
	24.0*total_time/total_min_day #7.51 = 7.5 = 7:30AM....I originally checked what my answer should be by using microsoft excel  to help guide me...although I've poked around online and saw the solution...would love to hear an explanation :) 

