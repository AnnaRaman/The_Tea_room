index

Tbis site has been deployed to Heroku. The live link can be found [here](https://the-tearoom.herokuapp.com/)

The Tearoom is an e-commerce website where you can browse and buy teas. The goal of the site is to sell teas to new and existing customers 
and allow them to filter their search to find the type of product they would like. The site's admin allows the admin to easily view, add, edit and delete products and orders from the database.

## UX
### User Stories
|As a consumer I woudld like to                                        |So that I can                                               |
|----------------------------------------------------------------------|------------------------------------------------------------|
|Be presented with information about the company                       | understand what to expect from the website                 |
|See the most popular teas of the month                                | gain some inspiration                                      |
|Naviagte between pages easily                                         | to reach whichever page I like quickly                     |
|Be able to search for a product                                       | avoid going through all the products                       |
|Create an account and sign in                                         | store my personal data and preferences                     |
|View my previous orders                                               | remind me of what I have previously ordered                |
|View my liked products                                                | determine which i would like to purchase.                  |
|Purchase teas                                                         | try the products                                           |
|Recieve an order confirmation email                                   | so that I know my order has bbeen processed                | 
|View all of the teas on one page                                      | compare products                                           |
|Filter my search for a particular tea by name, price, or ingredient   | view a refined search according to my preferences          |
|View the products by price or alphabetical order                      | view the products in a preferred order                     |
|Obtain detailed information about each tea                            | make an informed decision                                  |
|See recommendations of other products I may like                      | to give me inspiration if i'm unsure which tea to purchase |
|Add and delete items from my basket                                   | change my mind before continuing with the purchase         |
|Edit my liked teas                                                    | change my preferences when I like                          |
|Add and update my personal information                                | make my recommendations more customizable                  |
|Know what people in my demographic are liking or purchasing           | gain an insight into which teas I may like                 |


|As an administrator I would like to                                   | So that I can                                              |
|----------------------------------------------------------------------|------------------------------------------------------------|
|Be able to edit the details of the products                           | so that I can make changes when necessary                  |
|Be able to delete products                                            | remove products whose sale is discontinued                 |
|Be able to add products                                               | sell a new product                                         |
|Receve an email when a customer has made placed an order              | so that the order can be processed and completed           |


### Design

- The purpose of the design of the website was to allow for easy navigation between pages, and have clear and concise detail about each 
product to encourage informed and easy decision-making in the user. 

- compressed images using [tinypng](https://tinypng.com/)

#### Typography
- I chose to use 

#### Colours
The chosen colour scheme is neutral, with pastel tones for an inviting feel and to link to the idea of many herbal evoking a sense of calm.

### Wireframes

- Upon establishment of the user stories, wireframes were drawn as a reference point for the development of the site. They provide a skeleton for the site's structure and specific layout.
- The site is fully responsive so the idea of how it would appear on both desktop and mobile have been included.

The wireframes for the site can be found [here](https://balsamiq.cloud/slecl1v/piiswoj).

## Features

### Home page
- The homepage provides an insight in the site's product. There is a short introduction to the site to provide the user some information about the teas.
- There is a navbar at the top to easily navigate between pages on the site.
- Towards the bottom of the page there are featured 'teas of the month' selected by the shop administrator.

### Product list
- To view the product listing, the customer can choose to view all the products at once by selecting the 'All Teas' option in the 'Tea' dropdown in the nav bar. Or, they can choose to view a more specific listing based on the tea's category, for example 'black tea' or 'cold brews'.
- On the product list page, the customer is presented with an image, name, price and rating of the tea to provide an overview of the products in an easily-comparable format.

### Product view
- To view the product in more detail, the user simply clicks on the tea and is presented with the products detail page which presented the same information as given in the product listing, but also a short description about the tea, and an option to add the product (in their preferred quantity) to their basket.

### User Profile
- The 'My Profile' link is viewable to a user who has registered and account and signed in. This page details the user's delivery details which they have provided and saved, as well as a list of their order history. From this page the user is able to edit and update their delivery details.

### Shopping basket
- The shopping basket details the products and their quantities that have been added to the basket. From this page the user is able to edit the number of a items of a particular product in their basket, or to delete a product alltogether from their basket. Every time an item is added to the basket, the user is presented with a pop-up in the form of a toast, that confirms that the item has been added to their basket. 

### Payment
- Payment can bbe made from the checkout page. Once the user has confirmed their purchase and delivery details, they are able to pay the amount by card which is functioned bby Stripe.

### Email confirmation
- Once a user's payement has been successfully processed and their order has been confirmed, they will receive an email confirmation with a summary of their purchase.

### Admin page 
- The shop administrator (superuser) is able to add, edit and delete products and /or their specifid details on the site. 

## Techonologies

* HTML
* CSS
* JS/JQuery
* Python
* Django framework

## Testing
Testing of functionality was performed frequetly throughout the development of the site. Testing of the code itself HTML, CSS and Python code have been performed via online code validators.

### HTML 
The HTML code has been tested using [W3 Markup validator](https://validator.w3.org/).

### CSS
The CSS code has been tested using [W3 CSS validator](https://jigsaw.w3.org/css-validator/)

### Python
The python code was tested using the [pep8 validator](http://pep8online.com/)

## Deployment

### Deployment to Heroku
This project has been deployed from the master branch to the hosting platform, Heroku. To deploy the project, you must follow these steps:

1.	Log into Heroku, and once logged in on your dashboard, create a new app
2.	Make sure your github profile is displayed then add your repository name.
3.	Click search and once it finds your repository, click to connect the app.
4.	Click on the settings tab for your app and click on ‘reveal config vars’ where you can securely tell Heroku which variables are required to run the app.

    The following config variables need to be added:
| Variable                             | Value              |
|--------------------------------------|--------------------|
| AWS_ACCESS_KEY_ID                    | This key is generated by AWS               |
| AWS_SECRET_ACCESS_KEY                | This key is generated by AWS
| DATABASE_URL                         | This is the Postgres database URL
| EMAIL_HOST_PASS                      | The password set up for the hoest email
| EMAIL_HOST_USER                      | The email address that has been set for the host user
| SECRET_KEY                           | The Django secret key
| STRIPE_PUBLIC_KEY                    | This public key is generated by Stripe
| STRIPE_SECRET_KEY                    | This secret key is generated by Stripe
| STRIPE_WH_SECRET                     | This Webhook key is generated by Stripe
| USE_AWS                              | Set to True


5.	Go back to the Deploy tab, but before connecting, make sure to push all new files to the repository.
6.	Back within the terminal type Git status just confirm that those are our only pending changes, then add, commit and push these files to send them to GitHub.
7.	Go back to Heroku and select ‘Enable automatic deployment’
8.	Click ‘deploy branch’
9.	Heroku will now receive the code from GitHub, and start building the app using our required packages.
10.	Click ‘view’ to launch the app.

Cloning the Repo

This project has been deployed from the master branch to the hosting platform, Heroku. To run locally, copy the following link into an editor: https://github.com/AnnaRaman/MS3.git 

1.	Log in to GitHub and locate the GitHub Repository
2.	Under the repository name, click "Clone or download".
3.	To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4.	Open Git Bash
5.	Change the current working directory to the location where you want the cloned directory to be made.
6.	Type git clone, and then paste the URL you copied in Step 3. $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
7.	Press Enter. Your local clone will be created.

## Credits
### Code
- The contact form on the contact page was developed by [Bootstrap](https://getbootstrap.com/docs/4.0/components/forms/)

### Content
Much of the content has been inspired by and paraphased from the [teapigs](https://www.teapigs.co.uk/) website, such as the name of teas and the content in the about page.

### Media
The images used for the products are stock images from the following websites:
- [Pexels](https://www.pexels.com/) 
- [Unsplash](https://unsplash.com/)



## Acknowledgements
I would like to thank my mentor, Felipe Alacron for the helpful reviews and advice.
I received support for the Code Institute tutors throughout the develpoment process.