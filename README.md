# **Inginuity - a website where you can find out about Ireland's Craft Gin distilleries, the  gins they produce and buuy these gins.**
Ireland has a surprising number of small craft gin producers and the number is increasing all the time. This website aims to give the visitor up-to-date information about these distilleries and their gins.

## Visit the deployed website
[![Inginuity](/media/banner.png "Visit the deployed site here")](https://inginuity.herokuapp.com/)

## User Experience (UX)

### Project Goals

The site was created to enagage visitors so that they will want to register and visit regularly. It was built to fulfill the requirements of Code Institutes's Diploma in Full Stack Development Milestone 4 project.

#### Visitor Goals

To enjoy visiting the site, to find out up to date information about Irish Craft Gin distilleries and their gins with the ability to buy gins from the site.

#### User Stories

##### All visitors to the site should be able to; 
##### Visiting, Navigation and viewing

1. Understand what the website is about and navigate it intuitively.
2. View all the distilleries on the site.
3. View individual distilleries.
4. View all the gins on the site.
5. View individual gins.
6. View all the reviews about the distileries.
7. Easily register for an account.

##### Sorting and Searching
8. Search across gins and distilleries from the navbar.
9. See what was searched for ad the number of results.
10. Sort distilleries, gins and reviews by appropriate paranmeters.
 
##### Purchasing and checkout
11. Be able to select gins to purchase and add them to their bag
12. View items in a their bag.
13. Change quantity of items in their shopping bag.
14. Be alerteed to legal age to buy alcohol
15. Easily enter payment details.
16. Feel personal inforamtion is secure.
17. View an order confirmation after checkout.
18. Receive a confirmation email after checkout.

##### In addition logged in users should be able to;
19. Easily log in and out of their account.
20. Receive a confimation email after registering.
21. Recover their password if it is lost.
22. Have a personalised user profile.
23. Have an option to store their details for future ease of use.
24. Add a review 
25. Edit or delete their own reviews.

##### Superusers should be able to
26. Add, edit or delete gins.
27. Add, edit or delete distilleries.
28. Edit or delete reviews.

## Strategy
The site should provide a platform for people interested in irish Craft gins and distilleries to find out more about them and to share their visitor experiences.
- Objective Requirements;         To encourage visitors to visit the site, register with it, buy gin from it and to return frequently.
- Functional requirements; 	    To provide information on gins and distilleries that users can view. To provide a facility for users to register, log in and log out of the site. To provide users with the ability to select and purchase gins. To provide registered users with the facility to add, edit and delete reviews.
- Non-functional requirements; 	The site should be attractive and intuitive.

## Structure
The site starts with a  landing page and from there the user can follow the main navigation to distilleries or gins. This page also has a link to the users account which also provides the ability to register if they have not already done so. There is also a link to the visitors shopping bag.
1. The distilleries, gins, reviews, shopping bag and checkout pages are available to all users. The logout page is available to logged in users.
2. The pages to add or edit reviews is only avilable to logged in users.
3. The pages to add distilleries and gins or to manage reviews can only be accessed by superusers.
4. All registered, logged in users can access their profile page. This lists their personal details and information on past orders made.
5. Superusers also have access to the django admin page where all the data can be accessed and modified.

## Skeleton

The wireframes for the site can be seen [here](/media/wireframes1.png) and [here](/media/wireframes2.png)

There are 8 apps in the project.
**The home app.** This introduces the site. It has a navbar at  the top that includes the search box, links to the users account and their shopping basket. It has the buttons to let users view and sort distilleries, gins and reviews. 

**The distilleries app.** This is where all the distilleries are displayed. The page can be sorted and by name,  county or province. Each distillery listed there links to a page that shows the individual distillery in more detail and the reviews about it. If a superuser is logged in there are links to pages to edit or delete the distillery.

**The gins app.** This is where all the ginsa are displayed. The page can be sorted by name, distillery or price. Each gin is linked to a page that shows more detail about the gin and the ablity to add it to the user's shopping bag. If a superuser is logged in there are links to pages to edit or delete the gin.

**The reviews app.** This displays all the reviews that have been added to the site. It can be sorted by author distillery name,  or date posted. Here they can read all the reviews that have been made about all the distilleries and (if registered and logged in) they can add their own review.

**The shopping bag app** This can be accessed from the icon on the nav bar or from the toast that appears when a user adds an item. It has a form for the user to add their details (which is already prepopulated with the user's information if  they have selected the option to save that infomation to their profile). It also shows all the items in the user's shopping bag, the subtotal, delivery charge and grand total. From here the user has the option to keep shopping or to checkout.

**The checkout app.** This page has a form for the user to add their details and their credit card number, a summary of the order, and the option to complete the order or return to their shopping bag.

**The profile app.** This displays the user's details, gives them the option to update them and displays a summary of any previous orders the user has made.

**The wholesitesearch app.** This app was added to provide  facility to display search results that are made across reviews, gins and distilleries.

## Surface/Design (Design Choices fonts, icons, colours, styling, backgroundss)

### Imagery
The overall the site was to create a sense of Irish identity while maintaining simplicity and clarity. 
### Colour scheme
According to Shane Barker in ["The Psychology of Color in Web Design"](https://www.vandelaydesign.com/the-psychology-of-color-in-web-design/), blue "signifies trustworthiness and provides an air of coolness". The backgound picture was picked from ["unsplash.com](https://unsplash.com/) because it was felt that it was an unmistakeable Irish lannmark and the blue used in the overlay and logo were picked up from it using [imagecolorpicker.com](https://imagecolorpicker.com/) and used throughout the site.
 A [minimum contrast ratio](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Understanding_WCAG/Perceivable/Color_contrast) of 4.5:1 for small text and 3:1 for large text is recommended. There were a range of combinations of backgrounds and text across the site and their contrast ratios ranged from the best 21(white/black background and black/white text) to 7.92 (blue background and black text to 3.11 (blue backgound and white text) as assessed and reviews [contrast-ratio.com]("https://contrast-ratio.com/"). While the contrast ratio of the blue/white was not great it was felt that the very large size of the text would compensate for this and shadowing was added to improve its definition.

### Typography
The fonts were found on google font. The Open+Sans was chosen as it was clear and easily readable.
## Current Features
- Responsiveness on all device sizes.
- A nav bar that displays links dependent on the user type.
- A registration and login procedure which is secure and easy to use. 
- A method of searching the distilleries and gins and reviews by keywords.
- A method of sorting distilleries, gins and reviews using different fields for each.
- The ability to allow users to select and pay for purchases.
- The ability to allow superusers to create, edit and delete distilleries or gins.
- The ability for superusers and registered, logged in users to add reviews.
- The ability for review writers to edit or delete their own reviews and for superusers to be able to edit or delete any review.
- The functionality so that if a distillery is deleted all the reviews associated with it are also deleted.
- A check that user wants to perform irreversible actions before they do so.

## Future features
- The ability to display details about distilleries' visitor centres and their tours and provide the facility to book a tour.
- An interactive map whereby visitors to the site could see the distilleries pinned on a map and access each distillery from there
- A facility for users to leave reviews about individual gins.
- A facility for users to rate gins and distilleries (the static ratings were removed for the site as it was felt they did not add benefit to the site but were left in the model for future use).
- The ability to sign in using social media.
- The ability to filter, not just sort  the distilleries, gins and reviews.
- Currently the only alert to needing to be over the legal age to buy alcohol is a small tooltip when the user hovers over the checkout button. I would like an onload modal before the user enters the site confimrming that they are over the legal age to buy alcohol in their country. I added an onload modal that appeared every time the user landed on the landing page but it was felt this was poor user experience and this would need to be improved before inclusion.

## Database architecture
The default Django sqlite database  was used during developemnt.
In deployment the PostgreSQL was used and it was connected to the project through Heroku's settings.
An Entity Relationship Diagram for the project can be seen [here.](/media/inginuityerd.jpeg)

# Languages used
[HTML5](https://en.wikipedia.org/wiki/HTML5)

[CSS](https://en.wikipedia.org/wiki/CSS)

[Python](https://www.python.org/)

[JavaScript](https://en.wikipedia.org/wiki/JavaScript)


## Frameworks, Libraries and online resources used
- [jQuery](https://jquery.com/) javaScript 
- The [Django](https://www.djangoproject.com/) framework was used to build the project.
- The [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) templating engine was used.
- [Balsamiq](https://balsamiq.com/wireframes/) was used to create the wireframes.
- Gits's [gitpod](https://www.gitpod.io/) was used for writing and editing code, and for submitting and pushing to GitHub.
- [Heroku](https://id.heroku.com/login) was used to deploy the app.
- [sqlite](https://sqlite.org/index.html) was used to store data in development and [postgresql](https://www.postgresql.org/) in the deployed project.
- [GitHub](https://github.com/) was used for storing the code after being pushed from Git.
- [Amazon Simple Storage Service (s3)](https://aws.amazon.com/products/storage/?nc2=h_ql_prod_st) was used to store the static files for the deployed project.
STRIPE was used as a payment platform for secure checkout and payment.
- [miniwebtool.com](https://miniwebtool.com/django-secret-key-generator/) was used to generate a secret keys.
- The icons were found in [Font Awesome](https://fontawesome.com/).
- [Bootstrap](https://getbootstrap.com/) was used for styling.
- [Google Fonts](https://fonts.google.com/) was used to choose and import the font.
- Foreground/Backgound contrast was checked using [contrast-ratio.com](https://contrast-ratio.com/).
- The logo was generated on [wix.com](https://www.wix.com/)
- The favicon image was converted to an .ico file using [www.nchsoftware.com](https://www.nchsoftware.com/).
- The following websites were used for problem solving [stackoverflow.com](https://stackoverflow.com/), [w3schools.com](https://www.w3schools.com/), [geeksforgeeks.org](https://www.geeksforgeeks.org/),  and [css-tricks.com](https://css-tricks.com/).
- The html code was formatted using [webformatter.com](https://webformatter.com/html).
- The code for standardising the icon sizes was taken from [bulma.io](https://bulma.io/)
- [Gunicorn](https://gunicorn.org/) was used to aid the deployment to Heroku.
- The Django [allauth](https://django-allauth.readthedocs.io/en/latest/) and [cripsy forms](https://django-crispy-forms.readthedocs.io/en/latest/) modules were used
- [Pillow](https://python-pillow.org/), a python imaging library was used to help processing image files to store in the database.
- [Pyscopg2](https://pypi.org/project/psycopg2/) was used as a PostgreSQL database adapter.


## Images
- The images were stored in [Imgur](https://i.imgur.com/).
- The images were formatted using [online-image-editor.com/](https://www.online-image-editor.com/) and [tinypng.com/](https://tinypng.com/).
- The background image  is by [Michael](https://unsplash.com/@michael75?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) in [unsplash.com](https://unsplash.com/).
- The empty bottle image is by [Bobby Donald](https://unsplash.com/@__b_d__) in [unsplash.com](https://unsplash.com/).
- The road image is by Fabian Wiktor in [pexels.com](https://www.pexels.com/).
- The gin and distillery images and content were, when possible, taken directly from the distillery websites, if this was not available magazine articles, in particular [Irish Whiskey Magazine](https://www.irishwhiskeymagazine.com/), were used. Some gin images were taken from shop websites including [the whiskeyexchange](https://www.thewhiskyexchange.com/) and [celticwhiskey](https://celticwhiskey.com/).
- Some reviews were copied from [tripadvisor.ie](https://www.tripadvisor.ie/)

## Testing.
Bugs identified during development and testing and their solutions are recorded [here](/media/inginuitybugs.png).
### Validation
- Because of the issues with trying to vailate code that uses jinja templating the page was site was tested  URI and in addition the source code of pages with changeable content  were validited by direct input into [validator.w3.org](https://validator.w3.org/). There were residual errors resulting from the use of code from stripe and django's crispy forms. The results of this can be seen  [here](/media/htmlvalidation.png). 
- CSS code from the css files in  static and checkout were tested by direct input into [jigsaw.w3.org](https://jigsaw.w3.org/css-validator/) until it got a 'Congratulations! No error found!' message.
- JavaScript in checkout/js/stripe_elements.js, profile/static/profile/js/countryfield.js and gins/templates/gins/includes/quantity_input_script were checked using [jshint](https://jshint.com/). There were no errors and the warnings were checked, corrected where possible and otherwise left. Given more time more of these warnings might be rectified.
- Throughout development Python code was tested with [flake 8](https://flake8.pycqa.org/en/latest/) and problems identified were corrected where appropriate. Some lines that did not comply with pep8 due to being too long were left - when they could not be esily corrected. Thses were mainly in settings.py and migrations
- Lighthouse Audits. The site’s Performance, Accessibility, Best Practices and SEO were assessed by [Chrome Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) and the results of this are [here](/media/lighthousereport.png).
- Manual Testing. At every step of development the errors highlighted in the code were addressed before proceeeding.
The app was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
It was viewed on a variety of devices. Friends and family members reviewed the site to identify bugs and give feedback on user experience. The code was submitted for peer-review in Code Institute's peer-code-review channel in [slack.com](https://app.slack.com/). 
### Testing User Stories from User Experience (UX) Section.
#### All users should be able to
1. Understand what the website is about and navigate it intuitively.
- The subheading on the landing page explains the nature of the site. Testers reported no issues understanding what the site was about
2. View all the distilleries on the site.
- The link to 'distilleries' in the navigation is always at the top of the page (either displayed or in a dropdown on mobiles) and brings the user to a page displaying all the distilleries.
3. View individual distilleries.
- From the page displaying all the distilleries the user can click on the image of the distillery and this will bring them to a page with more detailed information about each distillery.
4. View all the gins on the site.
- The link to 'gins' in the navigation is always at the top of the page (either displayed or in a dropdown on mobiles) and brings the user to a page displaying all the distilleries.
5. View individual gins.
- From the page displaying all the gins the user can click on the image of the gin and this will bring them to a page with  details  about the gin.
6. View all the reviews about the distilleries.
- The reviews for each distillery are included at the bottom of the individual distillery page. All the reviews of all the distilleries are listed on the reviews page which can be accessed from the navigation.
7. Easily register for an account.
- The link for unregistered users to sign up to the site is available in a drop down when the user clicks the 'My account' icon. it could be argued that this button should be in a more prominent position and consideration was put into adding a seperate 'Sign Up' button on the landing page but in the interest of keeping a clean, uncluttered landing page it was decided to leave it in the dropdown.
8. Search across distilleries and gins from the navbar.
- Links to the distilleries and gins appear on the navigation in all devices. The distilleries have an option to sort by name. county or province and the gins have an option to sort by name, distillery or price.
9. See what was searched for and the number of results.
- On the whole site search page at the top the search term is displayed. The results are categorized into gins, distilleries and reviews and the number of results for each one is displayed.
10. Sort distilleries, gins and reviews by appropriate parameters.
- Distilleries can be sorted by name, county or province. Gins can be sorted by name, distillery and price and reviws can be sorted by author, distillery or dateposted. Each page includes a sort box at the top if the page if the user wants to change their selection.
11. Be able to select gins to purchase and add them to their shopping bag.
- Gins can be added to a shopping bag from the individual gin page.
12. View items in a their bag.
- The shopping bag can be accessed from either the shoppping cart icon on the navigation or by clicking on the 'Go to secure chcekout' link on the message that appears when a user adds anything to their bag. The shopping bag shows details of waht has been added, its name, image, quantity, subtotal ad grand total including delivery.
13. Change quantity of items in their bag.
- Quantities can be changed using the '+' and '-' buttons on the quantity box both on the individual gin page and on the shopping bag page. This button does not go below 1 or above 99.
14. Be alerted to legal age to buy alcohol.
- A tooltip shows when the user hovers over the complete order button.
15. Easily enter payment details.
- the form to eneter payment details is clear and does not accept invalid information.
16. Feel personal information is secure.
- It is explicitly highlighted in the checkout process that checkout is secure.
17. View an order confirmation after checkout.
- After checkout the order detail comes up in the success message and the user is directed to a page that summarises the order
18. Receive a confirmation email after checkout.
- A confirmation email is sent out for each completed order.
#### In addition registered users should be able to
19. Easily log in and out of their account.
- The Sign in and Sign up button appear in a drop down in teh main navigation. Some users felt that it should be more prominent. A registration/ Sign up button could be added to the landing page but it was felt that this page should be kept clean and uncluttered and it was not added at this time.
20. Receive a confimation email after registering.
- A confirmation email is sent out after the user completes the sign up form.
21. Recover their password if it is lost.
- There is a 'Forgot password' link on the Sign in page 
22. Have a personalised user profile.
-Registered users have a personal profile page that can be accessed through the 'My Account link in the navigation. It shows user's details and past orders.
23. Have an option to store their details for future ease of use.
- There is a 'Save this information to my profile' button at the bottom of the form for registered users. 
24. Add a review 
- THe button to add a review only appears for registered users or superusers.
25. Edit or delete their own reviews.
- For registered (who are not superusers) the the edit and delete buttons only appear only  on reviews  written by that user. 
#### In addition superusers should be able to
26. Add, edit or delete gins.
- An option shows only in the profile dropdown of superusers to add gins. Buttons appear to edit and delete gins on all gins for superusers.
27. Add, edit or delete distilleries.
- An option shows only in the profile dropdown of superusers to add distilleries. Buttons appear to edit and delete distilleries on all distilleries for superusers.
28. Edit or delete reviews.
- An option shows only in the profile dropdown of superusers to manage reviews. Buttons appear to superusers on the reviews page to edit and delete all reviews.

## Known Bugs
1. The modals introduced for defensive programming were complicated beacuse of the difficulty getting the distillery/gin/review id into the delete button on the modal and the fix for this caused the success message box to no longer display after deleting becaus of using window.location.replace(), however at this time it was felt that defensive programming took precedence over the success message.
2. There is some poor visual experiences when red inbuilt error messages from Django appear against the blue background of the site, these were changed to red buttons on custom html pages but time did not allow them to be changed on inbuilt Django pages. In particular this was noted on the checkout page if an incorrect credit card number is enetered and on the add a distillery page when an image is selected.
3. The back to top button overlies the footer on some pages on mobile and is a poor visual experience.

## Deployment
### The project was deployed to Heroku in the following way. 
In Heroku.com
1. 'New' was selected.
2. 'Create new app' was selected.
3. The app-name was added and region closest to current location (Europe) selected
4. 'Create app' was selected.
5. In Heroku's resources tab in 'Add-ons' a postgre database was added.
6. Migrations were migrated to set up postgres.
7. A superuser was created.
8. Gunicorn was installed in the project to act as webeserver.
9. A Procfile was created in the project.
10. The host name of the Herolu app was added to ALLOWED_HOSTS in settings.py.
11. For automatic deployment to Heroku, on the Heroku dashboard deploy tab Github was selected in the deployment method, and connected to the repository for the app. 'Enable automatic deploys' was selected for automatic deployment.
12. A bucket was created in Amazon Web Services s3 (ensuring public access was NOT blocked, static website hosting was enabled, suitable CORS configuration was added, a security policy was created and (for this app) allow public access was allowed in the Access Control List. A user was created to access the bucket in IAM and then Django was configured to connect to s3 using that user’s keys
13. In the Heroku dashboard settings 'Reveal Config Vars' was selected and the variables needed, including the database URL and secret keys for the app, for AWS, Email and Stripe were added.

### Forking the GitHub Repository
The  GitHub Repository can be forked to make a copy of the original repository on the GitHub account to view and/or make changes without affecting the original repository in the following way.
1.	By logging in to GitHub and locating the [GitHub Repository](https://github.com/ConacBreslin/technostalgia).
2.	Selecting the "Fork" button at the top of the Repository located above the "Settings" Button and  to the right.
3.	There should then be a copy of the original repository in your GitHub account.

### Making a Local Clone
1.	By logging in to GitHub and locating the [GitHub Repository](https://github.com/ConacBreslin/inginuity).
2.	Under the repository name, clicking the dropdown button marked “Code” and then selecting "Clone or download".
3.	Copying the link under "Clone with HTTPS", to clone the repository using HTTPS.
4.	Opening Git Bash.
5.	Changing the current working directory to the location where you want the cloned directory to be made.
6.	Typing git clone, and pasting the URL copied in Step 3.
7.	Pressing Enter to create the local clone.

## Credits
### Code
The intial design, layout and functionality was taken from the Code Institute's walk through project on Boutique Ado. 

## Acknoweldgements
I would like to thank the following people;
- my very zen mentor Chris Quinn whose wisdom and experience were invaluable,
- the many tutors in Code Institute for being unfailingly helpful, patient and knowledgeable throughout the hours and hours I spent online with them. I do not generally like to single out tutors (they all do an amazing job) but this time I have to mention Igor who never failed to assist, support, direct and sort out any issue but most of all furthered my understanding if the process,    
- the member of the Slck community who generously share their time and expertise,
- my family and friends for all their support and feedback,
- my unbelieveably supportive husband who, despite being very neglected recently, has not only kept me going but has also kept me (well) fed.
