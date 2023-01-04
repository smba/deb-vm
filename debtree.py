#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def compress_list(lst):
	# Initialize an empty result list
	result = []

	# Start a loop at the first index of the list
	i = 0
	while i < len(lst):
		# Get the first element in the list as the start of a range
		start = lst[i]
		# Initialize a range length of 1
		range_length = 1
		# Increment the loop index
		i += 1
		# Continue incrementing the loop index and adding to the range length
		# as long as the next element in the list is consecutive to the previous one
		while i < len(lst) and lst[i] == lst[i-1] + 1:
			i += 1
			range_length += 1
		# When we break out of the inner loop, we have found all of the consecutive
		# elements in the list, so we can add them as a tuple to the result
		result.append((start, start + range_length - 1))
	return result

def get_alternatives(lines):
    lines = [line.strip() for line in lines]
    lines = list(filter(lambda l: ":" in l, lines))
    
    linos = compress_list([i for i, elem in enumerate(lines) if "|" in elem])
    sequences = [(i[0], i[1]+1) for i in linos]
    
    nsequences = []
    for seq in sequences:
        group = {}
        group["type"] = lines[seq[0]].split(" ")[0][1:-1]
        ll = lines[seq[0]:seq[1]+1]
        ll = [l.split(" ")[1] for l in ll]
        group["packages"] = ll
        nsequences.append(group)

    return nsequences
    
def get_or_groups(lines):
    
    sequences = {}
    
    last_parent_no = None
    last_parent = None
    for lino, line in enumerate(lines):
        if ":" not in line:
            if last_parent not in sequences:
                sequences[last_parent] = []
            sequences[last_parent].append(line)
        else:
            last_parent_no = lino
            last_parent = line.split(" ")[1]

    return sequences

def get_relationships(name, lines):
    lines = [line.strip() for line in lines]
    lines = list(filter(lambda l: ":" in l, lines))

    # TODO remove dependencies with or after "|" groups
    # these will be handled by the alternativ group group detection    
    
    for line in lines:
        rtype = line.split(" ")[0]
        pass

with open("test.txt.py") as foo:
    f = foo.readlines()[1:]
    ff = [line.strip() for line in f]
    ff = list(filter(lambda l: len(l) > 0, ff))
    
ors = get_or_groups(ff)
t = get_alternatives(ff)
get_relationships("firefox", ff)
#parse_dependencies("firefox", ff)
