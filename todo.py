#!/usr/local/bin/python

import argparse
import getpass

class Items(object):
    """
        List stored as a file in ~/.todo
    """

    USERNAME = getpass.getuser()
    FILE_LOCATION = "/Users/{USER}/.todo/items.txt".format(**{'USER':USERNAME})

    def __init__(self):
        self.items = open(self.FILE_LOCATION, "r").readlines()

    def listAdd(self, arg):
        print("Appending item: " + arg)
        with open(self.FILE_LOCATION, "a+") as f:
            f.writelines(arg + "\n")

    def listShow(self):
        print("\n        TODO\n" + "-"*75)

        if not self.items:
            print("No tasks to be done.\n")
        else:
            for sno, item in enumerate(self.items):
                print(str(sno+1) + ". " + item)

            ## Method for sorted displaying. Poses a bug in deleting any entry
            #items = list(self.items)
            #items.sort()
            #for sno, item in enumerate(items):
            #    print(str(sno+1) + ". " + item)


    def listEdit(self, arg): # TODO
        print("Editing needs to be implemented")
        pass

    def listDelete(self, arg):
        doneTask = self.items.pop(arg-1)

        print("Completed task no. " + 
               str(arg) + 
              " (%s), deleting from queue." % doneTask.strip()
        )

        with open(self.FILE_LOCATION, "w") as f:
            for item in self.items:
                f.writelines(item)

        self.listShow()

    def listFlush(self):

        print("This will clear all tasks from the list.")

        userInput = ""
        while userInput not in ["Y", "y", "N", "n"]:
            userInput = raw_input("Continue? (y/n): ")

        if userInput.lower() == "y":
            with open(self.FILE_LOCATION, 'w') as f:
                print("Deleted all tasks from queue")



if __name__ == "__main__":

    description = "Todo, for when you need to do."

    parser = argparse.ArgumentParser(description = description)

    parser.add_argument(
            "-a",
            "--add",
            type = str, 
            help = "Add item to the todo list"
            )

    parser.add_argument(
            "-e",
            "--edit",
            type = int,
            help = "Edit item"
            )

    parser.add_argument(
            "-l",
            "--list",
            action = "store_true",
            help = "List all items in the todo list"
            )

    parser.add_argument(
            "-d",
            "--delete",
            type = int,
            help = "Delete item in the todo list"
            )

    parser.add_argument(
            "-flush",
            "--flush",
            action = "store_true",
            help = "Delete all items from the task todo list."
            )

    args = parser.parse_args()

    items = Items()

    if not(args.add or args.list or args.delete or args.edit or args.flush):
        items.listShow()

    elif args.add:
        #print("calling items.listAdd")
        items.listAdd(args.add)

    elif args.edit:
        items.listEdit(args.edit)

    elif args.list:
        items.listShow()

    elif args.delete:
        items.listDelete(args.delete)

    elif args.flush:
        items.listFlush()


