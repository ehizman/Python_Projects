#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    n_is_even = n%2 == 0
    
    if (not n_is_even):
        print("Weird")
    else:
        if (n in range(2,5)):
            print("Not Weird")
        else:
            if(n in range (6,21)):
                print("Weird")
            else:
                print("Not Weird")

