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
1. Search across gins and distilleries from the navbar.
2. See what was searched for ad the number of results.
3. Sort distilleries by county, province or by those with tours.
4. Sort gins by price, name or rating.
5. Sort reviews by distillery, author or date posted.
 
###### Purchasing and checkout
1. Be able to select gins to purchase and add them to their bag
2. View items in a their bag.
3. Change quantity of items in their bag.
4. Easily enter payment details.
5. Feel personal inforamtion is secure.
6. View an order confirmation after checkout.
7. Receive a confirmation email after checkout.

##### In addition logged in users should be able to;
1. Easily log in and out of their account.
2. Receive a confimation email after registering.
3. Recover their password if it is lost.
4. Have a personalised user profile.
5. Have an option to store their details for future ease of use.
6. Add a review 
7. Edit or delete their reviews.

##### Superusers should be able to
1. Add, edit or delete gins.
2. Add, edit or delete distilleries.
3. Edit or delete reviews.

## Strategy
The site should provide a platform for people interested in irish Craft gins and distilleries to find out more about them and to share their visitor experiences.
- Objective Requirements;         To encourage visitors to visit the site, register with it, buy gin from it and to return frequently.
- Functional requirements; 	    To provide information on gins and distilleries that users can view. To provide a facility for users to register, log in and log out of the site. To provide users with the ability to select and purchase gins. To provide registered users with the facility to add, edit and delete reviews.
- Non-functional requirements; 	The site should be attractive and intuitive.

## Structure
The site starts with a modal/overlay to confirm the vsisitor is old enough to visit the site. If so, they come to the landing page and from there they can follow the main navigation to Distilleries or gins. This page also has a link to the users account which also provides the ability to register if they have not already done so.There is also alink to teh visitors shopping bag.
1. The distilleries gin, reviews, shopping bag and checkout pages are available to all users. The logout page is available to logged in users.
2. The pages to ad or edit reviews is only avilable to logged in users.
3. The pages to add, edit or delete distilleries, gins or reviews can only be accessed by superusers.
4. All registered, logged in users can access their profile page. This lists their personal deatils and infomration on past orders made.
5. Superusers also ahve access to the django admin page where allthe data can be accessed and modified.

## Skeleton

The wireframes for the site can be seen [here]() and [here](static/images/wireframes2.jpg)

There are XXX pages on the site.
The **home** page  introduces the site. It has a navbar at  the top that includes the search box, links to the users account and their shopping basket. It has two buttons to provide filtering and sorting of distilleries and gins and there are two main navigation links to distilleries and gins in the body of the page.

The **login** page has a form for returning registered users to log back in to the site. It contains a link to the registration page for non-registered visitors.

The **technologies** page is where each technology and its information is displayed. The page can be searched by keyword or by category. Each technology is in a card from where the visitor can go to the **comments** page related to that technology. Here they can read all the comments that have been made about that technology and (if registered and logged in) they can add comments through a form.

The **add technology** page is accessed from the navbar (for registered, logged in users only) and has a form where the user can add all the necessary details of a new technology.

A  **profile** page is accessible to registered, logg


