import numpy as np
import tensorflow as tf
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--dir', type=str, 
                    default=os.getcwd()+"\checkpoint",
                    required=False, 
                    help='Checkpoint Directory')
parser.add_argument('--model', type=str, 
                    default='frozenGraph', 
                    required=False, 
                    help='Name of the pb file that has frozen weights and graph structure')

args = parser.parse_args()



