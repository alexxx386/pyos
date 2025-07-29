# PyOS by Alex V0.1 UNSTABLE
# Update loops are now figured out (phew.)
# Clears the terminal on start (The clear command will be broken if this dosen't happen because the clear variable needs to be made before running any commands.)
PWDATTEMPT = 0
clear = 1
while clear < 500000:
    print("")
    clear += 1
# Start up text!
print("___________________")
print("| Welcome to PyOS |")
print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
print("Press <enter> to continue!")
input()
# loops the enter a command screen after an action is performed later on.
for userinput in range (9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
 # prints command used to list all commands
    print("type ?help for a list of avalible commands (commands are case sensitive)")
    COMMAND_INPUT = input ("Enter a command here: Py-$ ")
    # performs command actions
    if COMMAND_INPUT == ("clear"): clear = 1
    while clear < 100000:
        print("")
        clear += 1
    if COMMAND_INPUT == ("?help"): print("the avalible commands are: ?help (lists avalible commands), info (lists information about this OS), clear (clears the command line), editjournal (lets you edit the builtin journal/notebook, theres currently no save function so if you edit it again it will overwrite and it probably won't last a restart/shutdown), viewjournal (lets you view to builtin journal/notebook)")
    if COMMAND_INPUT == ("info"): print("info: PyOS running in python UNSTABLE V0.1")
    if COMMAND_INPUT == ("editjournal"): JOURNALTEXT = input("what would like to put in the journal (there is no saving for now for more info, view ?help): ")
    if COMMAND_INPUT == ("viewjournal"): print("JOURNAL: " + JOURNALTEXT + "")