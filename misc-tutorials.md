The following are tutorials I saved off without hyperlinks or with now-defunct hyperlinks.

# Using rc.local

--------
rc.local
--------

In order to have a command or program run when the Pi boots, you can add commands to the rc.local file. This is especially useful if you want to be able to plug your Pi in to power headless, and have it run a program without configuration or a manual start.
An alternative for scheduled task management is cron.

----------------
Editing rc.local
----------------

On your Pi, edit the file /etc/rc.local using the editor of your choice. You must edit with root, for example:
sudo nano /etc/rc.local
Add commands below the comment, but leave the line exit 0 at the end, then save the file and exit.

-------
Warning
-------

If your command runs continuously (perhaps runs an infinite loop) or is likely not to exit, you must be sure to fork the process by adding an ampersand to the end of the command, like so:

python3 /home/pi/myscript.py &

Otherwise, the script will not end and the Pi will not boot. The ampersand allows the command to run in a separate process and continue booting with the process running.
Also, be sure to reference absolute filenames rather than relative to your home folder; for example, /home/pi/myscript.py rather than myscript.py.

# Shell Scripting
From https://www.raspberrypi.org/documentation/linux/usage/scripting.md (defunct link)

-------------
Shell Scripts
-------------

Commands can be combined together in a file which can then be executed. As an example, copy the following into your favourite text editor:

while :
do
echo Raspberry Pi!
done

Save this with the name:

fun-script

Before you can run it you must first make it executable; this can be done by using the change mode command:

chmod

Each file and directory has its own set of permissions that dictate what a user can and can't do to it. In this case, by running the command...

chmod +x fun-script

...the file fun-script will now be executable. You can then run it by typing...

./fun-script

...(assuming that it's in your current directory). This script infinitely loops and prints Raspberry Pi!; to stop it, press Ctrl + C. This kills any command that's currently being run in the terminal.
