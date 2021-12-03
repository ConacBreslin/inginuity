# **Inginuity - a website where you can find out about Ireland's Craft Gin distilleries, the  gins they produce and buuy these gins.**
Ireland has a surprising numebr of small craft gin producers and the number is increasing all the time. This website aims to give the visitor up-to-date information about these distilleries and their gins.

For assessment purposes you can log in as an admin user with the username "InginuitySuperUser" and the password "Inginuity1234".

## Visit the deployed website
[![Inginuity](static/images/banner.png "Visit the deployed site here")](https://inginuity.herokuapp.com//)

## User Experience (UX)

### Project Goals

The site was created to enagage visitors so that they will want to register and visit regularly. It was built to fulfill the requirements of Code Institutes's Diploma in Full Stack Development Milestone 3 project.

#### Visitor Goals

To enjoy visiting the site, to find out up to date information about Irish Craft Gin distilleries and their gins with the ability to buy gins from the site.

#### User Stories

##### All visitors to the site should be able to; 
###### Visiting, Navigation and viewing
1. Only enter the site if they are over the legal age to buy alcohol in their country.
2. Understand what the website is about and navigate it intuitively.
3. View all the distilleries on the site.
4. View individual distilleries.
5. View all the gins on the site.
6. View individual gins.
7. View all the reviews about the distileries.
8. Easily register for an account.

###### Sorting and Searching
9. Search across gins and distilleries from the navbar.
10. See what was searched for ad the number of results.
11. Sort distilleries and reviews county, province or and reviews those with tours.
12. Sort gins and reviews price, name or rating.
13. Sort reviews and reviews distillery, author or date posted.
 
###### Purchasing and checkout
14. Be able to select gins to purchase and add them to their bag
15. View items in a their bag.
16. Change quantity of items in their bag.
17. Easily enter payment details.
18. Feel personal inforamtion is secure.
19. View an order confirmation after checkout.
20. Receive a confirmation email after checkout.

##### In addition logged in users should be able to;
21. Easily log in and out of their account.
22. Receive a confimation email after registering.
23. Recover their password if it is lost.
24. Have a personalised user profile.
25. Have an option to store their details for future ease of use.
26. Add a review 
27. Edit or delete their own reviews.

##### Superusers should be able to
29. Add, edit or delete gins.
30. Add, edit or delete distilleries.
31. Edit or delete reviews.

## Strategy
The site should provide a platform for people interested in irish Craft gins and distilleries to find out more about them and to share their visitor experiences.
- Objective Requirements;         To encourage visitors to visit the site, register with it, buy gin from it and to return frequently.
- Functional requirements; 	    To provide information on gins and distilleries that users can view. To provide a facility for users to register, log in and log out of the site. To provide users with the ability to select and purchase gins. To provide registered users with the facility to add, edit and delete reviews.
- Non-functional requirements; 	The site should be attractive and intuitive.

## Structure
The site starts with a modal/overlay to confirm the vsisitor is old enough to visit the site. If so, they come to the landing page and from there they can follow the main navigation to Distilleries or gins. This page also has a link to the users account which also provides the ability to register if they have not already done so.There is also alink to teh visitors shopping bag.
1. The distilleries gin, reviews, shopping bag and checkout pages are available to all users. The logout page is available to logged in users.
2. The pages to ad or edit reviews is only avilable to logged in users.
3. The pages to add, edit or delete distilleries, gins or reviews can only be accessed and reviews superusers.
4. All registered, logged in users can access their profile page. This lists their personal deatils and infomration on past orders made.
5. Superusers also ahve access to the django admin page where allthe data can be accessed and modified.

## Skeleton

The wireframes for the site can be seen [here]() and [here](static/images/wireframes2.jpg)

There are 8 apps in the project.
**home** This introduces the site. It has a navbar at  the top that includes the search box, links to the users account and their shopping basket. It has two buttons to provide filtering and sorting of distilleries and gins and there are two main navigation links to distilleries and gins in the body of the page.
**distilleries** This is where all the distilleries are displayed. The page can be sorted and reviews county, province or if the distillery has a visitor centre. Each distillery listed there links to a page that shows the indiviual distillery and the reveiws relating to it. If a superuser is logged in there are links to pages to edit or delete the distillery.
**gins** This is where each gin and its information is displayed. The page can be sorted and reviews price, name or rating. Each gin has a page that shows more detail about the gin and the ablity to add it to the user's shopping bag. If a superuser is logged in there are links to pages to edit or delete the gin.
**shopping bag** This can be accessed and reviews the icon on the nav bar or from the toast that appears when a user adds an item. It has a form for the user to add their details (which is already prepopulated with the user's informations they have selected the option to save the infomation to their profile). It also shows all the items in the user's shopping bag, the subtotal, delivery charge and grand total. From here the user has the option to keep shopping or to checkout.
**checkout** This page  has a form for the user to add their details and their credit card number, a summary of the order, and the option to complete the order or return to their shopping bag.
**profile** This  displays the user's details, gives them the option to update them and displays a summary of any previous orders the user has made.
**reviews** This displays all the reviews that have been added to the site. It can be sorted and reviews distillery name, rating, or date of the review. Here they can read all the reviews that have been made about all the distilleries and (if registered and logged in) they can add their own review.
**wholesitesearch** This app was added to provide  facility to display search results that are made across both gins and distilleries.

## Surface/Design (Design Choices fonts, icons, colours, styling, backgroundss)

### Imagery
The overall the site was to create a sense of Irish identity while maintaining simplicity and clarity. 
### Colour scheme
According to Shane Barker in ["The Psychology of Color in Web Design"](https://www.vandelaydesign.com/the-psychology-of-color-in-web-design/), blue "signifies trustworthiness and provides an air of coolness". The backgound picture was picked from ["unsplash.com](https://unsplash.com/) beacuse it was felt that it was an un mistakelably Irish lanndmark and the blue used in the overlay and logo were picked up from it using [imagecolorpicker.com](https://imagecolorpicker.com/) and used throughout the site.
 A [minimum contrast ratio](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Understanding_WCAG/Perceivable/Color_contrast) of 4.5:1 for small text and 3:1 for large text is recommended. There were a range of combinations of backgrounds and text across the site and their contrast ratios ranged from the best 21(white/black background and black/white text) to 7.92 (blue background and black text to 3.11 (blue backgound and white text) as assessed and reviews [contrast-ratio.com]("https://contrast-ratio.com/"). While the contrast ratio of the blue/white was not great it was felt that the very large size of the text would compensate for this and shadowing was added to improve its definition.

### Typography
The fonts were found on google font. The Open+Sans wasc chosen as it was clear and easily readable.
## Features
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
If time had allowed it would have been nice to provide the facility to book a tour.
I would also have liked to nclude an interactive map whereby visitors to tthe site could see the distilleries pinned on a map and access the each indiviual distillery from there
The ability for users to leave reviews about individual gins could be added.
In hindsite some of the apps are very small and their content and functionality could perhaps be moved to within other apps.

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
- [sqlite](https://sqlite.org/index.html) is used to store data in development and [postgresql](https://www.postgresql.org/) in the deployed project.
- [GitHub](https://github.com/) was used for storing the code after being pushed from Git.
- [RandomKeygen](https://randomkeygen.com/) was used to generate a secret keys.
- [Bootstrap](https://getbootstrap.com/) was sued for styling
- [Google Fonts](https://fonts.google.com/) was used to choose and import the font.
- Foreground/Backgound contrast was checked using [contrast-ratio.com](https://contrast-ratio.com/).
- The logo was generated on [wix.com](https://www.wix.com/)
- The space invader image for the favicon was found in [iconfinder.com](https://www.iconfinder.com/).
- The favicon image was converted to an .ico file using [favicon.io](https://favicon.io/).
- The following websites were used for problem solving [stackoverflow.com](https://stackoverflow.com/), [w3schools.com](https://www.w3schools.com/), [geeksforgeeks.org](https://www.geeksforgeeks.org/),  and [css-tricks.com](https://css-tricks.com/).
- The html code was formatted using [webformatter.com](https://webformatter.com/html).
- Information about automatically formatting  python with [black](https://pypi.org/project/black/) was found on [freecodecamp.org](https://www.freecodecamp.org/news/auto-format-your-python-code-with-black/)
- The code for the onload modal was taken from [etutorialspoint.com](https://www.etutorialspoint.com/)
- The code for standardising the icon sizes wa taken from [bulma.io](https://bulma.io/)
## Images
- The images were stored in [Imgur](https://i.imgur.com/).
- The images were formatted using [online-im age-editor.com/](https://www.online-image-editor.com/) and [tinypng.com/](https://tinypng.com/).
- The background image  is by [Michael](https://unsplash.com/@michael75?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) in [unsplash.com](https://unsplash.com/).
- When possible the distillery and gin photos were taken from distilleries' websites, as were their gins.
## Testing.
Bugs identified during development and testing and their solutions are reordede here [page 1](static/images/bugsone.png), [page 2](static/images/bugstwo.png).
### Validation
- HTML source code for each all XX pages page was validited by direct input into [validator.w3.org](https://validator.w3.org/). The results of this can be seen  [here](static/images/htmlvalidation.jpg).
- CSS code was tested repeatedly by direct input into [jigsaw.w3.org](https://jigsaw.w3.org/css-validator/) until it got a 'Congratulations! No error found!' message.
- JavaScript was checked using [jshint](https://jshint.com/). There were no errors and the warnings were checked, corrected where appropriate and otherwise left.
- Python code was tested repeatedly with [pep8 online validator](http://pep8online.com/) until the vaildator deemed it 'All right'.
- Lighthouse Audits. The site’s Performance, Accessibility, Best Practices and SEO were assessed by [Chrome Lighthouse](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk) and the results of this are [here](static/images/lighthousereport.png).