1. **Project Title**  
   Diffuser

2. Project Description/Purpose of Program  
    If you are creating a program where its output must match the output of a reference program, Diffuser
    helps your debug your program by returning useful information that will help you pinpoint the code in
    your program that's causing the difference. Diffuser runs a command file through your file and the 
    reference file, and compares the outputs of both files. The program stops comparing when the first
    difference of your file’s output and the reference file’s output occurs. In addition, it return useful
    information that will help with debugging your program such as:  
   1. The line number and the specific command that caused this difference
   2. The output that your program printed when this command was ran and
        the output that the reference program printed when this command was 
        ran. In addition, within these outputs, we show you where the difference in outputs
        specifically occurs. 
   3. Your program’s output file and the reference program’s output file up until the difference occurred.

    Most computer terminals have a command called diff which allows you to
    compare two different files. Then, diff prints a side by side view of these
    files starting from where the difference occurs. While this can help you
    pinpoint the code in your program that's causing the difference, it becomes harder
    to do this when you are dealing with larger commands files, which means more output.
    Since your dealing with more output, it becomes harder to sort through the output and
    determine which command in the list of commands caused the difference.
    Perhaps your program starts to break due to not being able to handle so many commands.
    With diff, it will be harder for you to find exactly how many commands your program can
    handle until it falls apart. You may have to create multiple
    command files of different numbers of inputs just to find out how many
    commands your program can handle. However, Diffuser tells you EXACTLY where
    your program starts to fail and gives you the info you need to pinpoint
    where you need to debug your programs. 
 
3. A list of files that you provided and a short description of what each file is and its purpose  
   * commands.txt - contains a large number of commands that will be ran through the user and reference rock paper
                   scissors game file    
    
   * diffuser.py - this file contains all the program logic for diffuser; contains the steps the program takes to get
                  the user, reference and command file, compare the output of those files, returns the necessary info
                  the user needs to pinpoint the big in their file
    
   * medium_commands.txt - contains a medium number of commands that will be ran through the user and reference rock
                          paper scissors game file
    
   * rps_reference.py - a program that runs a rock, paper, scissors game; this is reference program, so the user should
                       aim to make a rock, paper scissors game with the exact same output as this reference
    
   * rps_user.py -  a program that runs a rock, paper, scissors game; this is user’s program
    
   * small_commands.txt - contains a small number of commands that will be ran through the user and reference rock paper
                         scissors game file

5. How to Install and Run the Project
    1. Currently, Diffuser only compares Python files for Mac (fortunately I'm working on allowing it to compare multiple
        languages on multiple computers).
    2. Download diffuser.py and make sure it's in the same folder your file, the reference file, and the commands file
    3. To run the file, in your terminal type, python3 diffuser.py, then type 3 arguments: the user file name, the reference file name, and the commands file name.
        * Ex: python3 diffuser.py -ufn "rps_user.py" -rfn "rps_reference.py" -cfn "commands.txt"
