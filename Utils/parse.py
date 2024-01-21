import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str)
    args = parser.parse_args()
    input_path = args.input
    return input_path