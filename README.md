# Hand Me My Bag - A Django Project

<img src="media/amiresponsive.jpg" alt="Responsive Site Image">


This is my fourth milestone project, undertaken as part of the Code Institutes Diploma in Software Development.
Here is the link for [Hand Me My Bag](https://handmemybag.herokuapp.com/)

#  Who Is This Website For?
Hand Me My Bag is a dedicated blog site for handbag enthusiasts. The idea behind the blog is to present high end luxury hand bags, yet to share the blog authors opinions of the bag. The site visitors are also wlecomed to engage in the conversation about the bag by leaving their comments and rating of the bag. 
The site user can also contact the blog author using the contact us page. The blog site is a place for gaining exposure, knowledge and engagement all whilst sharing a passion for high end luxury handbags. 


# UX - User Experience 

The project was planned in 5 stages. 

- Strategy Plane 

- Scope Plane 

- Structure Plane

- Skeleton Plane

- Surface Plane 

## The Strategy Plane 
## User Stories
-   As a user I want to be able to register an account with the blog site
-   As a user I want account registration to be a quick process
-   As a user I want to be able to open posts
-   As a user I want to be able to like and unlike posts 
-   As a user I want to be able to easily navigate the site 
-   As a user I want to view other site visitors comments 
-   As a user I want to be able to leave, update and delete my own comments 
-   As a user I want to be able to leave a rating review of the post/bag 
-   As a user I do not want the site to be cluttered or have any information that does not serve the blogs purpose. 
-   As a user I want the site to be easy to learn so that when I return in the future.

## The Owner 

-   Owner should be able to create, display, update and delete post
-   Owner Should be able to approve or disapporove comments
-   Owner should be able to delete comments 
-   Owner should be able to recieve the details of the contact us form submitted by site visitors 
-   The user should be able to intuitively navigate the blog and contact pages.  
-   The functions of the blog should be self-explanatory 

# The Scope Plane

The features of this project:

5 page /
- Home, Register, Login, Logout, Contact Us
- Pagination 
- Posts 
- Comments from other site visitors displayed 
- Comments form for registered user to submit 
- Contact us form for all site visitors to complete and submit 
- Crud functionality (Create, Read, Update and Delete) - Applied to the comments model


# The Structure Plane 

## Design Thinking 
## Blog Features 

- Hero image - Empahsize the type of blog the site is dedicated to. 

<img src="media/heroimage.jpg" alt="hero image">


- Navbar - Resposive and navigates to the Home page, Login or Logout, Register and Contact Us


<img src="media/navbar.jpg" alt="navbar">


- Site Pagination - Each page displays upto 6 posts 

<img src="media/pagination1.jpg" alt="paginationnext">
<img src="media/pagination2.jpg" alt="paginationprev">

- Comments form - Visible under the full post for a logged in user to leave a comment 

<img src="media/commentsform.jpg" alt="comments form">


- Edit and delete buttons to allow site user to update and delete their own comments

<img src="media/editdelete.jpg" alt="edit and delete buttons">

- Posts - The blog posts have an image of the bag, its name, the date the post was created, and an excerpt. The full post contains teh actual blog about the bag. 

<img src="media/posts.jpg" alt="posts">


- Contact Us form - A simple form that contains a name, subject and message field to enable even a non registered site visitor to get in touch.

<img src="media/contactform.jpg" alt="contact us form"> 


- Likes - A small heart which is clear but turns a blush pink colour when the site user clicks on it. 

<img src="media/likes.jpg" alt="Likes">

# The Skeleton Plane 

The design of this project was to make a soft and attractive application. One that is easy to navigate and that has lots of potential for growth in the future. 

Below is a link to the original wireframe I had completed

[wireframe1](media/wireframe1.jpg)

[wireframe2](media/wireframe2.jpg)

[wireframe3](media/wireframe3.jpg)

I was able to implement most of what I had planned out orginally. 


# Surface Plane 
## Design Tools / Colour Palette
- Canva

I used Canva to finalise on a colour theme for the blog. I wanted the predominant colour themes to be complimentary of each other. 
As the majority of blog visitors are likely to be woomen, I wanted to infuse a more feminine touch to the site. The easist way to do so was by using colours that are more reminicent of femininity. These hues of red, brown and pink are great for contrasting against one another and whilst embodying refinement. 

<img src="media/colorchoice.jpg" alt="Colour Choice Image">


## Agile Methodolgy 
- This application was developed using Agile Methodology. The design and implementation was planned based on user stories and a project board. This project board has a series of user stories that were split into 3 categories; todo, in progress or done. This project board was made using GitHub projects. When working with agile as methodology, priority is given to the most important ascpect of the project and therefore the scope is limited based in the amount of time one has as quality of the development needs to be maintained. There were features I was not able to implement, I have listed them under "future implementation" in the read me.
Here is a link to my [ProjectBoard](https://github.com/users/JessMair/projects/6/views/1)

# Testing 

- Chrome Developer test - passed. 
- CSS test 
<img src="media/csscheckjpg" alt="Css validator">   
- I also completed a HTML test and a PEP8 test. Both passed. 


## Bugs 
There were a multitude of bugs when developing this project. Below are some example of the bugs I encountered. 

- After I had added the review module, I encountered error with acessing the admin site and the main site. After examining the code and error message, it turned out to be a case of not having used a capital letter. This was fixed and the site (both main and admin) ran without issue. 

- Leaving comments - error - after enabling the functionality to leave a comment and press submit. Checked django documentation - line 49 of views.py file had the attribute of name given instead of "username".

- Error flagging once comment is approved through the admin panel. 
The issue was on line 24 of admin.py file. Should have said "approved" but i had instead typed "approve". This error was fixed. 

- The images are not resized and displayed appropriately when the blog is opened. This is an error that needed to be fixed. However due to a shortage of time, and it not being the most important thing on the list, this will need to be fixed in the next phase as per agile working methodology. 


## Manual Testing 
- Test all links in NavBar work 

- Test site pagination works 

- Test that the 'like' feature worked 

- Test a Post Model: 
Posts can be created, displayed, updated and deleted 
Check the full post can be read by clicking on the post name

- Test Comments Model: 
User needs to be logged in to leave a comment
Comments can be created by the user
The comment displays 
The comment can be updated 
The comment can be deleted 
Comments once submitted need to be approved 
The user can update and delete their own comments only

- Contact Model
Anyone can submit the 'Contact Us' form


# Technologies used 
### Languages
- HTML5
- CSS 3
- Python 
- HTML
- CSS

### Frameworks
- Django
- Bootstrap

### Databases
- Postgresql

### Django Extensions
- AllAuth
- Summernote 
- Django Crispy Forms 

### Cloud Storage and Deployment Services 
- Cloudinary
- Heroku
- Gunicorn


# Future implementation 
- Single sign on using allauth:
Using social media to sign in to the blog would make the user experience better and encourage more traffic to the site. 

- Design:
I would like to make the blog more visually aesthitic, I have a few ideas in ming for this. I would make the interger rating under the comment form into stars and this change would reflect on the already rated comments. This would look more presentable. 

The login and signout pages would also be targetted by bootsrap to look more inline with the rest of the blog. I did make a start on this but I did not have time to comeplete this. 

- Search functionality 
As the number of blogs increase, I will implement a search bar to search designers. This will return all of the posts by that particular designer. 

- Apps:
In future I would like to add another app which is solely for rating bag


# Deployment 

## Initial Deployment:

Install django and packages with these commands:

- pip3 install 'django<4' gunicorn
- pip install dj_database_url psycopg2
- pip3 install dj3-cloudinary-storage pip3 freeze --local > requirements.txt
- django-admin startproject "project_name".
- python3 manage.py startapp "app_name"
- pip3 install django-crispy-forms
- Migrate the work using:
- python3 manage.py makemigrations --dry-run
- python3 manage.py makemigrations
- python3 manage.py migrate --plan
- python3 manage.py migrate

Enter command: python3 manage.py runserver to see the preview.
It should say that django installed successfully.

## Env.py file.
- Add Cloudinary API variable, postgres DATABASE_URL and SECRET_KEY.
- Ensure env.py is in the gitignore-file

## Commit all changes to GitHub.
- git add .
- git commit -m "commit message."
- git push

## Set up delpoyment with Heroku:
- Register and login to Heroku.
- Create an app with a unique name and choose the region that is closest to you, USA or Europe.
- In Heroku/app/resources add postgres and attach it to the database url.
- Under Settings-> Config vars:
- Cloudinary is used to store images, therefore a Cloudniery API variable was added to config vars.
- DISABLE_COLLECTSTATIC: This is to prevent accidentally showing debug messages while DEBUG is True in settings.py
- Add port 8000
- Add SECRET_KEY from the env.py file.

- Under Deploy, choose deployment methods Github and search for my repository.
- The branch to deploy should be set to main.
- Deploy branch
- Login to Heroku in terminal
- heroku login -i
- Provide Heroku username, email and password.
- heroku run python3 manage.py migrate --app APP_NAME

## PostgrSQL as the database for deployment
- Add the following to the Settings.py file: DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}

- Set DEBUG = 'DEVELOPMENT' in os.environ

- In env.py add os.environ['DEVELOPMENT'] = 'True'

- Migrate those changes and push them to github.

- Remove DISABLE_COLLECTSTATIC in heroku config vars.


# Resources
- [Code Institute](https://codeinstitute.net/) Course material & Tutor support
- [Code Institute](https://codeinstitute.net/) Slack community 
- [Google Console](https://search.google.com/search-console/about) Bug fixes and testing 
- [W3C](https://validator.w3.org/) Validate HTML code
- [W3C]( https://jigsaw.w3.org/css-validator/) CSS Validation 
- [Peps](http://pep8online.com/) Python Validation 
- [JSHint](https://jshint.com/) JavaScript Validation 
- [W3Schools](https://www.w3schools.com/) - Helped me in researching and fixing errors along the way
- [Stack Overflow](https://stackoverflow.com/) To troubleshoot many times when experincing issues  
- [Geeks For Geeks](www.geeksforgeeks.org) Research and fix errors 
- [Canva](https://www.canva.com/colors/color-palettes/cherry-blossom-swirl/) Colour theory


# Credits 
- Django "I think, therefore I blog"  Code Institute Documentation

- Support for Models, Last modified, description https://www.geeksforgeeks.org/django-models/#:~:text=A%20Django%20model%20is%20the,Database%20one%20uses%20with%20Django

- General help with models https://docs.djangoproject.com/en/4.1/topics/db/models/  

- Trouble swhooting https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#fields 

- Bug issues https://www.pythonfixing.com/2021/12/fixed-attributeerror-object-has-no_14.html

- Contact form https://python.plainenglish.io/how-to-create-a-contact-page-for-your-django-website-6b97dddedb2d 

- https://docs.djangoproject.com/en/4.0/ref/contrib/messages/#adding-messages-in-class-based-views
- https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown/25325228#25325228 - Used both to enable delete success message to display on home page 

- https://www.youtube.com/watch?v=pOXqvzVCeSM - Implemented update success message using this tutorial 

## Honourable mentions 

Tutor support at Code institute for their incredible patience and doing their level best to help me with the hundred and one issue i had during the development of this project. 

London Community on the Code Institute Slack channel. In particular, Harry, Ed, Claire, Mike and Tom. Some of the most contientous people I know who took the time to peer review and provide some constructive feedback that helped me bring this project to completion. 

My mentor Spencer Barriball who has alway been the most supportive and informative person. I have a great deal of respect for Soencer's depth of knowledge across the various technologies, needless to say, I am very grateful for his mentorship. 


## Images 
- Hero Image https://mygemma.com/collections/handbags

- Christian Dior bag https://www.dior.com/en_int/fashion/womens-fashion/bags/saddle?adlgid=c%7Cg%7Cchristian%20dior%20saddlebag%7C611983108215%7Ce&gclid=Cj0KCQjw9ZGYBhCEARIsAEUXITWwFAxI9EhJBTS6RPBiY6z4kTuyWfVLkKlV3RlEJlKaOgYLtnKsHjIaAj1XEALw_wcB 

- Hermes bag https://www.hermes.com/us/en/story/106191-birkin/ 
- Chanel bag https://bagista.co.uk/products/pre-loved-chanel-classic-flap-bag-small-black-lambskin-cghw?_pos=3&_sid=4054dba54&_ss=r 

- YSL bag https://www.matchesfashion.com/products/1498988?country=GBR&utm_source=google&utm_medium=cpc&utm_content=1498988000001&utm_term=1655823569736&gclid=CjwKCAjwsfuYBhAZEiwA5a6CDPBJjQYG3Avv5M3HEtqjgGTFwocmgzcmmW-7IVtliUYhb3_x_TyRXBoCHOMQAvD_BwE&gclsrc=aw.ds 

- Louis Vuitton bag https://uk.louisvuitton.com/eng-gb/products/speedy-bandouliere-25-bag-nvprod3160026v?gclid=CjwKCAjwsfuYBhAZEiwA5a6CDNxxoGMZv0lEvPgiMFEnMxN0nLX8xEzfTCJ-VZwlq2UPRidYyVfpvRoCEMEQAvD_BwE

- Givency bag https://www.givenchy.com/gb/en/medium-antigona-bag/3594655629428.html?gclid=CjwKCAjwsfuYBhAZEiwA5a6CDBNxyZJlbJ8W_Wj0KXnYZJvOaM4W4R7a1TwOIbIKuyPTaBLy0DBSFhoCh_0QAvD_BwE&page=cmpid&page=cmpid

- Christian Dior Pouchette bag https://www.dior.com/en_gb/fashion/products/S0937ONMJ_M41G-lady-dior-chain-pouch 
