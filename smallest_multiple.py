#!/usr/bin/python

import math

def main():

    num = 21
    done = False

    while done == False:
        score = 0
        print "Start while loop", num, ", score: ", score
        for i in range(1, 20):
            if num % i == 0:
                score += 1
            
            if score == 20:
                done = True
                break
        
        if done == False:
            num += 1
            print "End while loop", num, ", score:", score, ", done", done
        else:
            print "End while loop", num, ", score:", score, ", done", done

if __name__ == '__main__':
    main()