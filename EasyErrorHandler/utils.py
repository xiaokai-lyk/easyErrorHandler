#encoding=utf-8

"""
Created on 2025-01-07 14:49:12

@author: xk
@func: Some useful tools or shared functions.
"""

def getArgs():
    """
    Receives and processes arguments from the command line.
    """
    import argparse

    parser = argparse.ArgumentParser(description='Calculate volume of a cylinder')

    group1 = parser.add_argument_group('constants',description="")
    group1.add_argument('--tttt',type=int,help="sss")
    parser.add_argument('--radius', type=int, help='Radius of cylinder')
    parser.add_argument('--height', type=int, help='Height of cylinder')

    args = parser.parse_args()
    print(args)