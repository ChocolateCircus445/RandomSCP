# RandomSCP
Fixes the bug that makes the SCP website get stuck on one SCP when you click the "Random SCP" button too many times.

<hr></hr>

## How do I use this?

**Make sure Python 3 and PIP are installed**

<hr></hr>

For **Windows**, press Windows Key + R and then type "cmd.exe".

A command window will pop up.

In the command window, type `pip install Flask` and press enter.

Once it is installed, type `pip install requests` and press enter.

When that finishes installing, double-click the run.bat file and go to http://localhost:5168 (or whatever port number you chose). If everything was set up correctly (and if I explained it correctly), you should be redirected to a random SCP.

<hr></hr>

For **Mac**, press Command + Space and type "Terminal"

In the Terminal, type `pip3 install Flask` and press return.

Once it is installed, type `pip3 install requests` and press return.

When that finishes installing, type `chmod +x ` (note the space at the end.) **DO NOT PRESS RETURN YET**

Drag run.sh into the Terminal and then press return.

When that finishes, type `sh ` (note the space), drag in run.sh, and press return.

Now go to http://localhost:5168 (or whatever port number you chose). If everything was set up correctly (and if I explained it correctly), you should be redirected to a random SCP.

<hr></hr>

## Redirecting the Random SCP button to your program

Go to https://www.requestly.in/ and click "Install Extension" (this works for **Chrome and Firefox only**)

Once that has installed, click on the Requestly logo in the top right corner of your browser. It's a blue R with arrows surrounding it.

Click the "Open app" button in the little popup.

Sign in or make an account for Requestly.

Once you have done that, you will be redirected to your rules screen. Click the "New Rule" button and select the "Redirect Request" type.

You can set the rule name to whatever you'd like, though "Random SCP" is probably best.

Click the dropdown that says "Contains" and change it to "Equals".

Set the first URL field to http://www.scpwiki.com/random:random-scp

Set the second URL field to http://localhost:5168 (or replace 5168 with your custom port number)

Click "Save" and close the Requestly tab.

Head over to the SCP Wiki (http://www.scpwiki.com/) and test it out. Good job! You deserve a donut!
