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

def output(strategy_name, user, best5, worst5):
    bold("USER {}".format(user))
    green(strategy_name + " CLOSEST 5 products")
    [green(str(good)) for good in best5]
    yellow(strategy_name + " FARTHEST 5 products")
    [yellow(str(bad)) for bad in worst5[::-1]]
