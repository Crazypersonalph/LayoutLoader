import argparse
from utils.load import load

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", help = "The layout you want to load", required=True)

args = parser.parse_args()
load(args.config)