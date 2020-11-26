<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

Welcome Joeri157,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use.

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

--------

Happy coding!


<h1 align="center">
Milestone Project 3 - M3M3KRU <br> Joeri van den Kieboom
</h1>
<div align="center">

## Overview
Simple internet forum, where you are able to post anything funny and many more… <br>
To put a smile on people’s faces daily
</div>

## UX

### Documentation for planning
- [Click here!](/planning) to go to planning folder map
- [Click here!](/planning/project-ideas.pdf) to go to documentation

### Wireframes :
**Desktop :** <br>
[homepage](planning/wireframes/comments-desktop.png) <br>
[extended-homepage](planning/wireframes/extended-homepage-dekstop.png) <br>
[login](planning/wireframes/login-desktop.png) <br>
[signup](planning/wireframes/signup-desktop.png) <br>
[upload](planning/wireframes/upload-desktop.png) <br>
[edit](planning/wireframes/edit-desktop.png) <br>
[Comments](planning/wireframes/comments-desktop.png)

**Mobile :** <br>
[homepage](planning/wireframes/comments-mobile.png) <br>
[extended-homepage](planning/wireframes/extended-homepage-mobile.png) <br>
[login](planning/wireframes/login-mobile.png) <br>
[signup](planning/wireframes/signup-mobile.png) <br>
[upload](planning/wireframes/upload-mobile.png) <br>
[edit](planning/wireframes/edit-mobile.png) <br>
[Comments](planning/wireframes/comments-mobile.png)

### Database schema :
- [full-schema](planning/database_schema/test.pdf)
- [users](planning/database_schema/users-schema.png)
- [categories](planning/database_schema/categories-schema-png)
- [uploads](planning/database_schema/uploads-schema.png)
- [comments](planning/database_schema/comments-schema.png)


### User Stories
| *As an User :* |
|---|
|I can use the site without being logged in.
|I can register to make an account in order to acces the websites features
|I can add, edit and delete my own uploads
|I'm able to search for uploaded/created content
|I can comment on content
|I can edit/ delete my comment

## Features

### Existing features
-	The site is usable for guests and logged in users, however, some features are only useable to logged in users
-	The lasted uploaded post will be shown on the website.

#### Guests
- Able to scroll through content
- Able to see comments posted on content	
- They are able to use the search navigation to search for categories/posts, if the value that is put in matches any of the content.
- Have the option to sign up and create an account, they will need to fill in their details in order to use the website (First-Name, Last-Name, UserName, Password, etc)  

#### Members
- Able to Create, Edit and Delete own uploads
- Able to Create, Edit and Delete own comments
- Able to comment on other users their uploads
- Able to add extra categorie if it didn't exist yet

### Future features
-	Favorites; where people are able to check their uploads that they favored
-	Videos; where people are able to add videos as uploads
-	User Accounts; that they are able to change their password and update their info
-	Confirmation by mail; so they receive an email when they create a new account, and this is also usable when they forgot their password.

## Technologies
### The website is designed by the following technologies :
- blank

## Testing
|Test Cases |Status |Issues|
| --- | --- | --- |
|Blank | blank | blank


## Deployment <hr>
- blank

## Credits

### Content
- blank

### Code references/ Acknowledgements
- blank
