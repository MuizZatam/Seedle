import os
import argparse
import argcomplete

def main():

    parser = argparse.ArgumentParser(description="Seedle - Python project creation and management tool")
    
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    create_parser = subparsers.add_parser("create", help="Create a new Python project")
    create_parser.add_argument("directory", nargs="?", default=None, help="Directory for the new project (default: current directory)")

    argcomplete.autocomplete(parser)
    
    args = parser.parse_args()

    if args.command == "create":
        
        create_project(args.directory)
    else:

        parser.print_help()



def create_project(dir = None):

    if dir == None:

        dir = os.getcwd()

    else:

        os.makedirs(dir, exist_ok=True)

    print(f"Seeding a new Python Project in {dir}!")


if __name__ == "__main__":

    main()