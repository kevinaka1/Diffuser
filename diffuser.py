import os

def start_diffuser():
    print("Hi. Thank you for using Diffuser.")
    print("In order for this to work you must have your file, the reference file")
    print("and the commands file in the same folder as the folder as this file is in.")

def logging_file_history():
    useroutput_obj = open("useroutput.out", "r")
    useroutputfile_history_obj = open("useroutputfile_history.txt", "w")
    useroutputfile_history_obj.write(useroutput_obj.read())
    useroutputfile_history_obj.close()
    useroutput_obj.close()


    refoutput_obj = open("refoutput.out", "r")
    refoutputfile_history_obj = open("refoutputfile_history.txt", "w")
    refoutputfile_history_obj.write(refoutput_obj.read())
    refoutputfile_history_obj.close()
    refoutput_obj.close()

def get_and_open_file(userfilename, referencefilename, commandfilename):

    userfile_obj = open(userfilename, "r")
    if(userfile_obj.closed):
        print(f"{userfilename} could not be opened.")
    else:
        reffile_obj = open(referencefilename, "r")
        if(reffile_obj.closed):
            print(f"{referencefilename} could not be opened.")
        else:
            commandfile_obj = open(commandfilename, "r")
            if(commandfile_obj.closed):
                print(f"{commandfilename} could not be opened.")
            else:
                diffuser_logic(userfilename, referencefilename, commandfilename, commandfile_obj)

                userfile_obj.close()
                reffile_obj.close()
                commandfile_obj.close()

def diffuser_logic(init_userfilename, init_reffilename, init_commandfilename, init_commandfile_obj):
    #os.system(f"python3 {init_reffilename} < {init_commandfilename} > refoutput.out 2> refstderr.out")

    command_line_number = 0
    user_output_filelines = None
    ref_output_filelines = None
    for command in init_commandfile_obj:
        separatecommandfile = open("sep_command.txt", "a")
        separatecommandfile.write(command)
        separatecommandfile.close()
        
        separatecommandfile = open("sep_command.txt", "r")
        os.system(f"python3 {init_userfilename} < sep_command.txt > useroutput.out 2> userstderr.out")
        os.system(f"python3 {init_reffilename} < sep_command.txt > refoutput.out 2> refstderr.out")

        if(command_line_number == 0):
            logging_file_history()

            

        command_line_number += 1
        
        user_output_file = open("useroutput.out", "r")
        user_output_filelines = user_output_file.readlines()
        ref_output_file = open("refoutput.out", "r")
        ref_output_filelines = ref_output_file.readlines()

        refLineCounter = 0
        for outputLine in user_output_filelines:
            yourLine = outputLine
            if (refLineCounter < len(ref_output_filelines)):
                refLine = ref_output_filelines[refLineCounter]
            else:
                print("Your output file has more lines than the reference's output file\n")

                useroutputfilehis_obj = open("useroutputfile_history.txt", "r")
                useroutputfilehis_filelines = useroutputfilehis_obj.readlines()
                useroutputfilehis_obj.close()

                print(f"The additional lines your file has are:\n")

                user_command_output_lines = user_output_filelines[len(useroutputfilehis_filelines) - 1:]
                for userline in user_command_output_lines:
                    print(userline)
                useroutputfilehis_obj.close()
                sys.exit()


            if(yourLine != refLine): 
                exactly_match = False
                print("\nYour file's output did not EXACTLY match the reference's output\n\n")
                print(f"The first difference was found on comand line number {command_line_number} in {init_commandfilename}. The command was: {command}\n\n")

                useroutputfilehis_obj = open("useroutputfile_history.txt", "r")
                useroutputfilehis_filelines = useroutputfilehis_obj.readlines()
                useroutputfilehis_obj.close()
                print("For this command, your file printed:\n")
                if command_line_number == 1:
                    useroutputfilehis_obj = open("useroutputfile_history.txt", "r")
                    print(useroutputfilehis_obj.read())
                    useroutputfilehis_obj.close()
                else:
                    user_command_output_lines = user_output_filelines[len(useroutputfilehis_filelines) - 1:]
                    for userline in user_command_output_lines:
                        print(userline)
                    useroutputfilehis_obj.close()


                
                refoutputfilehis_obj = open("refoutputfile_history.txt", "r")
                refoutputfilehis_filelines = refoutputfilehis_obj.readlines()
                refoutputfilehis_obj.close()
                print("For this command, the reference file printed:\n")

                if command_line_number == 1:
                    refoutputfilehis_obj = open("refoutputfile_history.txt", "r")
                    print(refoutputfilehis_obj.read())
                    refoutputfilehis_obj.close()
                else:
                    ref_command_output_lines = ref_output_filelines[len(refoutputfilehis_filelines) - 1:]
                    for refline in ref_command_output_lines:
                        print(refline)
                    refoutputfilehis_obj.close()

                
                print(f"Specifically, your line printed:\n{yourLine}\n\n")
                print(f"Meanwhile, he reference line printed:\n{refLine}\n\n")

                os.remove("sep_command.txt")
                os.remove("refoutput.out")
                os.remove("useroutput.out")
                os.remove("refstderr.out")
                os.remove("userstderr.out")
                os.remove("refoutputfile_history.txt")
                os.remove("useroutputfile_history.txt")
                sys.exit()
            refLineCounter += 1
        user_output_file.close()

        logging_file_history()

        ref_output_file.close()
        user_output_file.close()


        separatecommandfile.close()

    if(len(ref_output_filelines) > len(user_output_filelines)):
        remaining_ref_line = ref_output_filelines[len(user_output_filelines) - 1:]
        for line in remaining_ref_line:
            print(line)
    else:
        print("Your file's output matches the reference file's output exactly")
    

    os.remove("sep_command.txt")
    os.remove("refoutput.out")
    os.remove("useroutput.out")
    os.remove("refstderr.out")
    os.remove("userstderr.out")
    os.remove("refoutputfile_history.txt")
    os.remove("useroutputfile_history.txt")
    

if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(
        description = "Allows program to know the name of the files we are dealing with"
    )

    parser.add_argument(
        "-ufn", "--userfilename",
        metavar="userfilename",
        required=True,
        help="The name of your file. Include the extension in the name"
    )

    parser.add_argument(
        "-rfn", "--reffilename",
        metavar="reffilename",
        required=True,
        help="The name of the reference file. Include the extension in the name"
    )

    parser.add_argument(
        "-cfn", "--commandfilename",
        metavar="commandfilename",
        required=True,
        help="The name of the file with the commands. Include the extension in the name"
    )

    args = parser.parse_args()
    start_diffuser()
    get_and_open_file(args.userfilename, args.reffilename, args.commandfilename)