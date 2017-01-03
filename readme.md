#    Tell me the Story! 
##    What is it & what does it do?

This is a small python utility that can transfer (data) files from one machine to another. Once deployed in the sender machine, the utility will "lurk" silently in the background, waiting for files of pre-designated type to be dumped in the pre-designated directory. 

When a relevant batch of files arrives, the utility "wakes up" to perform pre-dispatch checks. First, it takes stock of the file count. If it is short of the predesignated number, the utility goes back to silent lurking. If it exceeds that number, the utility sends you an alert email, then goes back to lurking.

When the predesignated file count is met, the utility checks the names of the files and asks 2 questions: 
Do they all belong to the same participant/experimental unit? Are they all unique without duplicates?
If either of the above questions receives a  "No!", you receive a relevant email alert.

When the file batch successfully meets all 3 criteria,  the utility opens a secure connection with the recipient machine (SFTP), then places a copy of the local files in the predesignated remote directory.

Before closing the connection, it performs 2 post-dispatch checks. It insures that the remote directory has 1) all and 2) only  the files that had just been transferred. It sends you a relevant email alert if neither is true. 

Otherwise, it does two things. First, it triggers the post-transfer operations on the remote machine by creating an empty, dummy file (remember that the current utility is just a module of a larger data-analysis pipeline; see the other repositories for more information).  Then, it cleans up by deleting the transferred files from the local directory, and goes back to lurking.


#    Get Me Fixed!
##    How Can I Deploy It?

1.    Insure that the sender machine has a working version of Python 3.X with the following modules: yagmail, pysftp, and watchdog.
2.    Clone the repo to the sender machine.
3.    Copy `definitions.py` and `watch_and_trigger.py` to the directory where the to-be-transferred files will be dumped.
4.    The script `definitions.py` lists definitions of the 6 functions comprising the current utility. You need to customize a few  things in this script:
	4.1.    The path of the local directory where the script currently resides and file transfer will be launched. Replace "C:/Users/tamer/sender" with your own path (Line 9).
	4.2.    The path of the directory in the remote machine where files will be copied. Replace "/home/tamer/recipient" with your own path (Line 96).
	4.3.    Replace "csv" with the file extension of your choosing (5 instances; use control+f).
	4.4.    Set the file count that you want the dispatch to be triggered at. replace "8" with the number of your choosing (Lines 12,14).
	4.5.    I name my files "p001_l1.csv", and "p001_l2.csv". The prefix "p001" is used to refer to the first participant run in my experiment, and is used by the script to insure that all files in the current batch belong to the same participant /experimental unit. if your "p001" prefix is greater or smaller than 4 characters, change that on Line 29. If  you use a letter other than "p", change that on Line 33.
	4.6.    Set the credentials of the gmail account you'll use to send email alerts and the email address that will receive the alerts on Lines 76-78.
	4.7.    Set the credentials of the recipient machine (host IP address; port;  username, & password) on line 94.
	4.8.    Finally, the dummy file I use to trigger the post-transfer file processing is named "success.txt." You can change it on Line 101.
5.    Open the script `watch_and_trigger.py` with your editor and repeat steps 4.1 & 4.3 above (lines9,12, and 22). Save and close the script.
6.    That's it! Now run the `watch_and_trigger.py`  script in its current directory.


	#Whom Should You Blame?

Well, No one but yourself! I offer no warrantee, implied or explicit, for the code in any of my repositories. Use it at your own risk and discretion. I accept no liability, whatsoever, as a result of using it, or using a modified version of it!

Tamer Soliman, the author of this repository, has been immersed in data collection and statistical modeling since 2002. He holds a PhD in quantitative Experimental Psychology, where he designs experiments to understand and model human cognition, decision making, socio-cultural behavior, attitudes, and actions. He develops data-centered utilities and applications that subserve his data-science and machine-learning projects. While he approaches his projects with the mindset of a skeptic homo-academicus,  he understands the concept of "deadlines", and loves making money just as all other homo-sapiens!