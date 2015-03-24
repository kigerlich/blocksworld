#"Blocks World"
#
# A coding project solved by Kaleigh Gerlich
# Please see README.md for a complete project description. 


# First, let's find out how 'big' our blocks world is:
n_str = raw_input('What is the size of the blocks world? Enter an integer.')
n = int(n_str)

# Define an empty (where an empty position is denoted by -1) 
# n x n array representing the flat table and all the possible 
# block positions
flat_table = [[ -1 for i in range(n)] for j in range(n)]
for k in range(n):
	flat_table[n-1][k] = k
print(flat_table)

def move_define():
	# What move do we want to accomplish?
	a_str = raw_input('What block do you want to move?')
	a = int(a_str)
	b_str = raw_input('Where do you want to move it?')
	b = int(b_str)

	# Illegal command logic: ignore a = b
	if a != b:
		print(flat_table)
		move_block(a,b)

def move_block(a,b):
	# Let's locate the block we want to move and the block we're moving it onto
	for i in range(n):
		for j in range(n):
			if flat_table[j][i] == a:
				loc_a = [j,i]

	for i in range(n):
		for j in range(n):
			if flat_table[j][i] == b:
				loc_b = [j,i]

	# Illegal command logic: ignore if a and b are in the same stack of blocks
	if loc_a[1] != loc_b[1]:
		
		# Check to see if there is a block on top of our destination block
		flag1 = 1
		for i in range(n): 
			if flat_table[i][loc_b[1]] == b:
				flag1 = 0
			if flat_table[i][loc_b[1]] > 0 and flag1 == 1:
				temp = flat_table[i][loc_b[1]] 
				for j in range(n):
					if flat_table[j][temp] > 0:
						temp1 = flat_table[j][temp] 
				flat_table[j][temp] = temp
				flat_table[i][loc_b[1]] = -1
		
		# Now check to see if there's a block on top of the block we want to move
		flag2 = 1
		for i in range(n):
			if flat_table[i][loc_a[1]] == a:
				flag2 = 0
			if flat_table[i][loc_a[1]] > 0 and flag2 ==1:
				temp2 = flat_table[i][loc_a[1]] 
				for j in range(n):
					if flat_table[j][temp2] > 0:
						temp3 = flat_table[j][temp2] 
				flat_table[j][temp2] = temp2
				flat_table[i][loc_a[1]] = -1
		
		# Now we move some blocks!
		flat_table[loc_b[0]-1][loc_b[1]] = a 
		flat_table[loc_a[0]][loc_a[1]] = -1
		print(flat_table)

# Check to see if there are more moves in the sequence
another = raw_input('Have another move? (Y/N)')
while another == 'Y' or another =='y':
	move_define()
	another = raw_input('Have another move? (Y/N)')
else:
	print(flat_table)



			





