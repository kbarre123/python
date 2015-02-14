#!/usr/bin/python

import math

def main():
    answers = []
    for x in xrange(0,20):
        answers.append(x + 1)

    answer = 1
    for y in xrange(0,len(answers)):
        if answers[y] != 1:
            answer *= answers[y]
            for z in xrange(len(answers)-1, z >= y, -1):
                if answers[z] % answers[y] == 0:
                    answers[z] = answers[z] / answers[y]

    print answer
    
if __name__ == '__main__':
    main()