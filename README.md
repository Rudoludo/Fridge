# FRIDGE NOTES
#### Video Demo:  <URL HERE>
#### Description:
This app is a fridge themed interactive TODO list that lets you manage basic MEMO.

It allows you to create, delete, mark notes as complete and it also offers an option to view them all in a panoramic view.
The main design principle follows the idea that using a stamp to mark a task complete is way more enjoyable than simply crossing out
an item on a long to-do list. Every necessary step in a journey , even the small ones, is as much as important as the big ones.

It was developed using Flask, SQLite for the database and javascript for the logic on the index page.
It was also my first attempt to create a reactive design that works well in a wide range of media devices (phones, tablets, desktops)
so I used and experimented a lot with css.

My flask app is structurend around 5 functions :
    index, show_note, addnote, delete, global(for the global view)
and 3 HTML pages:
    (index.html, addnote.html,global.html)

Most of the  code, since the note management is quite simple, is written to ensure a modern smooth navigation despite the easy concept.
For example if you are browsing between notes and delete one, you will be redirected to the next note (by the show_note function) and not always to the first on the list.

My jss script is only present in the index page, it gets all the notes in a dictionary from flask, display one at a time and lets you navigate them without reloading the page.
It allows an infinite browsing cycle through all the tasks instead of stopping at the end of the list.
It also displays the stamp image when you mark a task complete, even thought it will still redirect to the same route as the delete button.

The absence of any login/account feature was a design choice because I wanted this app to have an instant access time to promote its use.
But still, I used sessions to pass data between functions (like the index of specific note) and also implemented an error status when reached a limit of notes.

A lot of my focus and time was spent on designing the UI and trying to make it as much appealing as possible.
I opted for simple and clear pixel-art style in every element in order to replicate a retro videogame aesthetic and used a lot of css
to make the mobile version feel very natural.

I set a low char limit (30) for every note since it's aimed at small tasks, and a low limit of notes (8).


Used Resource:

-cs50 quack AI to help me understand jss syntax (most unfamiliar language in this project)
-AI assistance tool integrated in chrome dev tools for understanding and fixing CSS issues.
-Some code was reused from past problem set, especially the SQL and some flask.
-A lot of googling (stackoverflow, w3schools, and ufficial documentation of jss/css)


Copy-pasting code would not expose me to syntax and distraction errors I could learn from, so I still wrote most of the code.
I also restarted the project 3 times as I added SQL and Java after my initial flask/html/jinja prototype (wich I found too simple for a final project)

PS I intend to expand this app function and use more powerful frameworks for both front-end and back-end as my current side project.

