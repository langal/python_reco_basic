# Just for formatting output
BOLD = '\033[1m' + '\033[4m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
END = '\033[0m'

def bold(string):
    print(BOLD + str(string) + END)

def green(string):
    print(GREEN + str(string) + END)

def yellow(string):
    print(YELLOW + str(string) + END)
