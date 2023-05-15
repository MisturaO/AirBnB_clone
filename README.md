## AirBnB Clone - The console

This team project focused on building the console for our full web app
application - a clone of the Airbnb website.

# What is the console?

This is a command interpreter without visual interface (just like the shell)
that will be used to manipulate our app data. it will be used to create data
model, manage (update, destroy etc) objects, and for storing and persisting
objects to a JSON file

# How it works

Our console is built using the Python cmd module which has an inbuilt help
function that explains what the various commands in the console does. The
console begins with a prompt and instruction on how to navigate. Example:
"type help topic>" where topic is one of the commands listed. One can also
type in any command without any help and the command will execute

# Examples
$ ./console.py

(prompt) help create
$ The create command builds an instance of a model

(prompt) help quit
$ The quit command exits the program

(prompt) quit
$
