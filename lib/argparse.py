import argparse

def parserArguments():

    parser = argparse.ArgumentParser()
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    required.add_argument("-u", help="Specify URL of target")
    ARGS = parser.parse_args()