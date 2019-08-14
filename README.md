# Django blog and more
This is a project I have that serves as a multipurpouse website. This was made using Django, and was based off of the tutorial series from CoreyMS. I followed along that tutorial and learned a lot of useful Django skills alongo the way. This uses Amazon's AWS for storage and is run on Heroku. I've also added some addons to Heroku so I could allow for a chat room feature.


Functunality of the website learned from the tutorial:

- Log in system (with the ability to reset password and to delete account)

- Profile system (With the the addition of imagery for users, can update at any time, and can be viewed by other users) 
  
- Post system (With the ability to be edited and deleted at any time, as well as having multiple pages for each post)

- Making a clean UI using bootstrap

Functionality of the website I added myself:

- Commenting to posts

- Chatroom with other users (Uses memcache, automatically deletes messages if user is inactive for a long time or chatbox gets too full)

- Personalized about section

- General UI changes (such as getting rid of the side bar and having a drop down section for about)

