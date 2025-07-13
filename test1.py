# mygit/cli.py
import argparse

def main():
    parser = argparse.ArgumentParser(description="My Git-like tool")
    parser.add_argument('command', help="Command to run (init, commit, etc.)")

    args = parser.parse_args()

    if args.command == 'init':
        print("Repository initialized.")
    elif args.command == 'commit':
        print("Changes committed.")
    else:
        print("Unknown command.")
