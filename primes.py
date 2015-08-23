import time

def sum_primes (lim):
    num_list = range (2, lim+1) #create list from 2 to lim

    running = True #boolean to determine if while loop should run
    current_val = 2 #current value to remove from list

    while running:
        multiples = range (current_val*2, lim+1, current_val) #current multiples list from current number

        #stop loop if the multiples only has one value
        if len(multiples) == 1:
            running = False
            break

        #at all of the indexes of multiples, set num_list value to -1
        for m in multiples:
            start_val = num_list[0]
            num_list[m-start_val] = 0

        #find next value to loop through
        for num in num_list:
            if num != 0 and num > current_val:
                current_val = num
                break

        print "Removing multiples of %s" % (current_val)

    #for i in num_list:
    #    if (i != 0):
    #        print i,

    print "---- Sum: %s ----" % (sum (num_list))

start_time = time.time ()
sum_primes (2000000)
print "---- Runtime: %s ----" % (time.time () - start_time)
