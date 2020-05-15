from termcolor import colored
from offline.client.localize import localize

def show_help(args):
   print(colored('Commands', 'magenta', attrs=['bold']))
   print(colored('  localize', 'green') + "   Convert a recipe to use a local server")

def commands(command):
   switcher = {
      "localize": localize,
      "help": show_help
   }
   return switcher.get(command)

def main(args):
   """ main entry point of the conan application, using a Command to
    parse parameters
   """
   if(len(args) == 0):
      show_help()
      return

   command = args[0]
   method = commands(command)
   
   if not method:
      print(colored('Error', 'red', attrs=['bold']) + ": command '{}' not found!".format(command))
      return

   method(args[1:])