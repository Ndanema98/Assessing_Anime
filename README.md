# Milestone project 4
# Assessing Anime

["Assessing Anime"](https://assessing--anime.herokuapp.com/) is a website designed for people to add descriptions, give their opinions and read reviews on anime that they have watched. 

This website was targeted at people who want to gain more information on anime they want to watch and get other peoples views and ratings on that. There will be a description section which is going to allow further details of any anime to be published. There will also be a review section which would allow people to log on and add their opinions and scores on different anime they have watched. This in turn will encourage more people to watch more anime. 
Reviews have been shown to greatly help when it comes to improving customer loyalty and customer service as they feel they have a voice through active engagement. Also reviews allow for better credibility with suggestions as there is social proof.
This website was built using knowledge gained from HTML, CSS, JavaScript, Python and Django modules, for the purpose of completing my fourth Milestone Project for the Code Institute's full stack developer course. This website is easy to navigate and easy to read, with a clear goal and aim.

 # User Experience/User Interface (UX/UI)

 - ## User Stories
   ### First Time User Goals
   As a first time user I want:
   - to register an account so that I can like reviews.
   - to view the different anime post and their description.  
   - to view the number of likes on each review so that I can see which is the most popular. 
   - to view the website on various different devices so that I am not limited when accessing the website on different devices.
   - to locate and access the linked social media so that I can find out more information.
   - to navigate the homepage with ease so that I can successfully use the website without further help.
   - to read reviews left by previous users so that I can benefit from their advice.
   - to locate and access the contact page so that I can easily contact the restaurant for further information.
   
   ### Logged-in User Goals
   As a logged in user I want:
   - to add post so that other users can learn more about the anime.
   - to delete and edit a post so that if information is incorrect I can update accordingly.
   - to like or unlike a review so that that I can interact with the content.
   - to delete and edit a review so that if my mind is changed I can update accordingly.
   - to create reviews so that other users can benefit from my advice.

   ### Developer's Goals.
   As the developer I want:
   - to approve or disapprove posts so that I can filter out incorrect posts.
   - to create, read, update and delete posts so that I can manage the content.
   - to create, read, update and delete reviews so that I can manage my content.
   - to approve or disapprove reviews so that I can filter out inappropriate reviews.
   - to provide an interactive and eye-catching website so that users are encouraged to revisit.
 
 - ## Design 
   ### Data Model
   - The data model for my project consists of three models, which are User, Post and Review. The User model is imported from the django.contrib.auth.models module. The Post model has several fields including title, slug, description, author, image, status, excerpt, date_posted, upvotes, and downvotes. Additionally, there is a Review model with fields post, name, author, email, content, date_posted, and approved. 

   ### Colour Scheme
   - During the construction of my website I experimented with many different colours and decided to settle on using black and grey. I decided to stick to only these two colours in order to make my website more visually appealing and easily readable. Also i kept most of the text as white so it could stand out amongst the dark colours. 

 # Features
 - ## Responsive Website
   ![A screenshot of my responsive design](/static/images/responsive-design.png)

   - This website changes it's layout to best display the content depending on the screen size. This allows the user to use the website on various different devices. 

 - ## NavBar 
  - ###  Logged Out User
   ![A screenshot of my Navigation bar(logged out)](/static/images/navbar-1.png)

    - This shows my navigation bar when a user is not logged in. They can either click on home or the website name which would redirect them back to the homepage. The user also has an option of clicking on register which would allow them to create a new account or log in which would allow them to access their existing accounts. 

  - ### Logged In User
   ![A screenshot of my Navigation bar(logged in)](/static/images/navbar-2.png)

    - This shows my navigation bar when a user is logged in. They can either click on home or the website name which would redirect them back to the homepage. The user also has an option of clicking on add anime which would allow them to create a new anime post or log out which would allow them to log out of their accounts. 

 - ## HomePage 
  - Anime Post content

   ![A screenshot of my HomePage 1](/static/images/mainpage-1.png)
   ![A screenshot of my HomePage 2](/static/images/mainpage-2.png)

    - This shows the Anime post pictures and descriptions so users can gain futher information on the anime. 
  
  - ### User Details and time of posting 

   ![A screenshot of my HomePage 3](/static/images/mainpage-3.png)

   - This shows the details of the user whoo created the post and the date and time that the post was posted. 

   ![A screenshot of my HomePage 4](/static/images/mainpage-4.png)

   - This shows the ammount of likes and dislikes a post has. 

 - ## PostDetail 
   ![A screenshot of my of post detail](/static/images/postdetail.png)

   - This shows the view of when an indivdual post is selected. 
   
 - ## Reviews
  - ### Add Reviews
   ![A screenshot of my reviews 1](/static/images/reviews-1.png)

   - This shows the form in which users can input their details to add a review. 

  - ### View Reviews 
   ![A screenshot of my reviews 2](/static/images/reviews-2.png)

   - This shows the reviews for a specific post which has been added. 

 - ## New Anime Post
   ![A screenshot of my add anime post](/static/images/addpost.png)

   - This shows the form in which users can input their details to add an anime post. 
   

 - ## Buttons 
  - ### See reviews/add likes button
   ![A screenshot of my see reviews/add likes button](/static/images/buttons-1.png)
   - This button when clicked takes me to my review page in which you can see the reviews or then go on to add a like or dislike. 

  - ### Add reviews button
   ![A screenshot of my add reviews button](/static/images/buttons-2.png)
   - This button when clicked takes me to my add reviews page in which you can create a new review.

  - ### Edit button
   ![A screenshot of my edit button](/static/images/buttons-3.png)
   - This button when clicked takes me to my edit post page in which a user can edit a post that they have previously created. 

  - ### Delete button
   ![A screenshot of my delete button](/static/images/buttons-4.png)
   - This button when clicked takes me to my delete post page in which a user can delete a post that they have previously created. 

  - ### Pagination button
   ![A screenshot of my pagination button](/static/images/buttons-5.png)
   - This button when clicked takes me to my next page in which a user can view other posts as there are only three per page. 

  - ### Like and dislike buttons
   ![A screenshot of my like and dislike buttons](/static/images/buttons-6.png)
   - These buttons when clicked can either like or dislike a post. Both buttons are not able to be pressed at the same time. 

 - ## UserInterface
  - ### Sign in Page
   ![A screenshot of my sign in page](/static/images/userinterface-1.png)
   - This shows the form used for a user to sign into their account 

  - ### Sign up Page
   ![A screenshot of my sign up page](/static/images/userinterface-2.png)
   - This shows the form used for a user to sign up for a new account 

  - ### Sign out Page
   ![A screenshot of my sign out page](/static/images/userinterface-3.png)
   - This shows the form used for a user to sign out of their accounts.
   

 - ## Banner
   ![A screenshot of my banner](/static/images/banner.png)
   - This shows the banner provided whenever a user signs in or out of their accounts.
   

 - ## Footer
   ![A screenshot of my footer](/static/images/footer.png)
   - This shows the footer elements which users can click on to take them to social media accounts, if they wanted to learn more about the website. 


 # Possible Future Features
   -  Add an Edit and Delete function for my reviews 
   -  When the Like button is selected it goes green and vice versa for the dislike button 
   -  When adding a review automatically populate the name and email field with the user who is logged on details. 
    
 # Testing 
 - ## Automated 
  - I have created some python files which automatically test my models.py, my forms.py and my views.py. 

 - ## Manual 
   - This website has been tested using three different browsers (Google Chrome, Firefox, Safari) and I can confirm that it works. 
   - This website has been tested with all the standard screen sizes and I can confirm that it is responsive. 

### Navigation Bar
All Pages:
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Home page | When clicking on the "Home" button on the nav bar, the browser redirects to the home page. | PASS
Booking Page | When clicking on the Add Anime button on the nav bar, the browswer redirects to the add posts page | PASS
Loging/ Log Out Pages | When clicking on the log in or log out button the page redirects to the log in page or logs the user out | PASS
Register Page | When clicking on the register button it redirects to the register page. | PASS
Foreground and background | Checked foreground and background information is clearly legible | PASS
Text | Checked the text is clearly legible against the background | PASS

### Home Page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Checked elements for consistant scaleability | PASS
Accessibility | Checked the accessibility of the page using lighthouse | PASS

### Add Anime page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Checked elements for consistant scaleability | PASS
Save button | When clicking the Save button on the page, the form in inputted into the database and the browser redirects to the home page. | PASS
Add anime Form | Checked the form submits only when all required fields are filled out. | PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS

### Add Review page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Checked elements for consistant scaleability | PASS
Save button | When clicking the Save button on the page, the form in inputted into the database and the browser redirects to the review page. | PASS
Add Review Form | Checked the form submits only when all required fields are filled out. | PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS

### Edit Anime page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Edit Anime Form | Checked the form submits only when all required fields are filled out. | PASS
Logged in user | Checked the form can only be edited by the user who created the post. | PASS

### Delete Anime page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Delete Anime Form | Checked the form is succesfully deleted | PASS
Logged in user | Checked the form can only be deleted by the user who created the post. | PASS

### Register page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Register form | Checked the form submits only when all required fields are filled out. | PASS
Sign in link | Checked the sign-in link redirects to the sign-in page. | PASS

### Sign in Page
TEST            | OUTCOME                          | PASS / FAIL  
--------------- | -------------------------------- | ---------------
Media | All media assets are displayed properly, have no pixelation or stretched images and is responsive on all devices. | PASS
Responsiveness | Check every element on-page for consistent scalability in mobile, tablet and desktop view.| PASS
Accessibility | Checked the accessibility of the page using lighthouse| PASS
Sign in form | Checked the form submits only when all required fields are filled out. | PASS
Signup link | Checked the signup link redirects to the signup page. | PASS

 - ## Validator 
   - ### HTML
     - The official ["W3C validator"](https://validator.w3.org/) was used to validate my HTML. The only error found was on the add anime page. When this was put through the validator it showed this error: ![A screenshot of my error 1 ](/static/images/error1.png)
     
   - ### CSS 
     - The official ["W3C validator (Jigsaw)"](https://jigsaw.w3.org/css-validator/) was used to validate my CSS. No errors were found when my code was input.
     
   - ### Javascript
     - The Javascript file was validated using ["JSHint"](https://jshint.com/) and no errors were found. The New JavaScript features (ES6) option was ticked in the Configure menu.
   
   - ### Python
     - The Python Code was validated using a ["Pep8 python checker"](https://pep8ci.herokuapp.com/#) from code institute and no errors were returned. 
      
  - ## Accessibility 
    ![A screenshot of my lighthouse score](/static/images/lighthouse.png)

    - The Lighthouse function in devtools was used to see if the font and the font colours used were easy to read and access. I can confirm that the page on my website passed. 
      
 # Languages used 
   - HTML
   - CSS
   - Javascript
   - Python

 # Technologies Used 
   - Git 
     - Allowed me to add commit and push my code to github for version control. 
   - Gitpod 
     - The programme used to code my website.
   - Github 
     - Allowed me to store my repository and files pushed from Gitpod.
   - Fontawesome 
     - Used to display icons to make my website more visually appealing. 
   - Chrome developer tools 
     - Allowed me to troubleshoot and edit my code.
   - Am I Responsive 
     - Allowed me to check the responsiveness of my website at different screen sizes. 
   - W3C Validator 
     - Allowed me to validate my HTML and CSS code against industry standard. 
   - JSHint 
     - Allowed me to validate my Javascript code against industry standard.

 # Deployment
  - This code was deployed using Code Institute's mock terminal for Heroku. 

  - ## Steps for deployment:
   1. In the top right corner of the page click on the fork button. 
   2. The next page will show a forked version of my project.
   3. Create a new Heroku app.
   4. Set the buildbacks to Python and NodeJS in that order.
   5. Link the Heroku app to the repository. 
   6. Click on deploy. 

 # Credits
 - ## Images
   - All of the images used were found on ["Wikipedia"](https://en.wikipedia.org/wiki/Main_Page)

 - ## Information 
   - All of the information used were found on ["Wikipedia"](https://en.wikipedia.org/wiki/Main_Page)

 - ## Code
   
   - The code for my structure was taken from the [Hello Django Walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/dc049b343a9b474f8d75822c5fda1582/121ef050096f4546a1c74327a9113ea6/?child=first) and the [I think therefore I blog Walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/fe4299adcd6743328183aab4e7ec5d13/)
    
 # Acknowledgement 
    - The online tutors that Code Institute provides. 
    - My mentor Ben Kav for helping me when I was stuck. 
    - Everybody on slack, for their advice. 
