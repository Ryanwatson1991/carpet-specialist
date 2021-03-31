# Alex Gibb: Carpet Fitting Specialist
[My deployed project is avaliable here](http://msp-3-pulp-pixels.herokuapp.com/get_index)

## What is the site?
Alex Gibb has been a carpet fitter in the North-East of England for over thirty years and now, he wants to build on the name he's build up over the years and start
selling carpets as well. The site is the launch paltform for this, allowing customers to visit the site, browse, store favourite items and make purchases - 
as well as recieve information about their purchase.   

## What does the site aim to achieve?
Quite simply, the site aims to use Alex's reputation as a carpet fitter in the North East of England in order to make sales of carpets and carpet accessories
so that this can become a new source of income. 

# UX

## User Stories

The user stories for this site focus on three main user types:

* Customer - A first time or relativley casual customer, someone likley buying a carpet for their home. 
* Regular customer - Someone who uses the site regularly, likley someone who works in the carpet fitting business who regularly needs to purchase supplies. 
* Store Owner - Probably Alex Gibb, needs to be able to ammend site details in a simple way. 

I have detailed my user stories [here](/media/readme/user-stories-final.xlsx) - (This file will need to be downloaded once clicked)

## Design

### Bootstrap Templates
The site design uses a number of templates from startbootstrap. These are as follows:
* [Landing Page](https://startbootstrap.com/theme/landing-page) - for the masthead code on index page
* [Freelancer](https://startbootstrap.com/theme/freelancer) -for the card layout on product page
* [Shop-item](https://startbootstrap.com/template/shop-item) - for the product detail page layout

I used these as the big thing that was new to me on this project was the Django framework and I wanted to spend as much time getting the backend working as possible, so prebuilt templates allowed me to do this 
although I did end up restyling the mobile header quite extensivley (and I don't feel like I was totally successful in this). 

Start Bootstrap doesn't have a full shop theme, so I chose elements that most suited what I wanted to achieve from the above template. 

### Images and colour
The colours accross the site were based on the colours avaliable in Alex Gibb's business logo 
![logo](/media/logo-3.jpg)

I haven't been able to confirm with Alex who designed the logo. 

As well as this, the site uses a masthead image  that I got from free stock image site pexels (my shutterstock subscription expired and it's EXPENSIVE for how often I use it)
This image is by artist [Kayley Dlugos](https://www.pexels.com/photo/window-shadow-on-wall-and-floor-of-modern-room-5872378/) 



## Wireframes
Pdf's of my initial wireframes are linked below: 

* [Home Page](/media/readme/landing.pdf)
* [Products Page](/media/readme/products.pdf)
* [Product Detail Page](/media/readme/product_detail.pdf)
* [Bag Page](/media/readme/bag.pdf)
* [Checkout Page](/media/readme/checkout.pdf)
    * Ultimatley not used, but there was also [Checkout Part 2](/media/readme/checkout2.pdf)
* [Profile Page](/media/readme/profile.pdf)
* [Contact Page](/media/readme/contact.pdf)
    

# Data

## Data Structure

The data structure uses database models accessible in the Django admin. These models are grouped as follows:
    * Accounts - Stores email addresses
    * Authentocation and Authorization - Stores groups & users
    * Checkout - stores orders made on store
    * Products is a bit more complicated and I'll go into further detail below
    * Sites - stores site info

### Product Data
For products, a number of models are used. These need to be added in a certain way to allow 
correct information to be displayed. 

1. Firstly there are Categories, these need to be added before products as the site uses these to filter products. 
2. There are then a number of models specifying further information about the product. These need to also be added before product so they can be selected on product add, but unlike categories, these are not essential.
    * These models are 'Backing', 'Manufacturer', 'Material', and 'styles'
3. There is also an 'In Stock' model. This is literally a 'yes' or 'no' option. Used to dictate whether 'add to bag' function is avaliable on product_detail page. 
4. Then there's the products model, this takes product name, price & description as well as an image. It also allows selection of a options from the above models. 
5. There is then the colour model. This had to be a seperate model to products as I wanted to link colour images to colour names. This model asks for details of the colour and then links to the products model to specify which product the colour should show for. 
6. Finally there is the comments model. This stores comments (called reviews on the site) and links each comment to a product in the product model to dpecify which product the comment should show up on. 

# Features
## Existing Features
The key features of the site are as follows: 
* Responsive design across all device sizes 
* Navbar that features dropdowns that alolow user to sort products based on listed criteria. 
* Uses Python, Django and Heroku/Postgres, in order to display content sitewide that is drawn from database.
* Searchbar that allows users to search the site for products they require.
* Product detail page that allows users to: 
    * Browse different colours of selected product, with image changing based on selected colour. 
    * Options are different on the page based on product type. Flooring requests users put in a length and width that will calculate the product area and will then 
    multiply this by the product price(per meter squared) in order to calculate price based on measurements. 
    * Leave reviews on product page. 
* Add items to bag, and go through checkout to place an order (curently only with Stripe's test details though)
* View profile so users can see order history, detail.
* Site can take payment through Stripe.
* A bookmarking system for favourite items. 
* Sign up/Log in - Uses allauth to allow users to sign up to the site and access certain content that cannot be viewed if not logged in.
* User Profile Page that allows users to view favourites, order history and delivery details. 
* Add, edit and delete product functions for superusers.  

## Features left to implement
There are a number of features that I would have liked to include but that ultimatley weren't added because of time/feasabiity. 
These include:
* This will be detailed more in bugs section, but a key feature that is missing is the ability for the site to send through selected carpet_colour to bag and, in turn for this to be
    passed through to the backend correctly so this can be specified on the order. It's a pretty key feature for this type of site, but ultimatley given the complexity of the bag and relate functions
    as well as the timeframe, it was not possible to fully implement. 
*  The other key feature that I really wanted to implement but haven't been able to due to time, was the ability for users to order carpet samples. These would be 
    a small 1*1 version of a carpet. I didn't manage to get to this feature, but if this site were to be used for real it would be a key feature.
* Order products by colour - Again, something I'd have liked to get to but didn't have time. I added a 'colour group' field to my colour model so that all variations of a colour
   would be associated with a broader colour more commonly referred to (so for example, colours like 'wine red', 'crimson' 'deep red' would all have the colour group 'red'). But never got around to implementing this feature. 


# Technologies Used
## Languages Used
* HTML
* CSS
* JavaScript
* Python

## Additional technologies used
* [Django](https://www.djangoproject.com/)
    * Very important for this site, used as a framework for the whole thing, also relies on a number of django related packages such as allauth
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    * Used in combination with django to pull code from database and display it on website
* [Bootstrap](https://getbootstrap.com/)
    * Used to help with responsiveness and layouts
* [Start Bootstrap](https://startbootstrap.com/)
    * Provided bootstrap templates accross the site 
* [GitPod](https://gitpod.io/workspaces/)
    * Gitpod workspace used to build project
* [Github](https://github.com/)
    * Used to store code for project after beung pushed from GitPod
* [Heroku](https://www.heroku.com/)
    * Used to deploy project non-static files based on latest version of project comitted to Github
* [Amazon Web Services](https://eu-west-2.console.aws.amazon.com/console/home?region=eu-west-2)
    * Used S3 and IAM to host static and media files
* [Stripe](https://stripe.com/en-gb)
    * Used to implement payment system ccross site

# Testing
## Testing User Stories outlines in UX section

I have done the following manual tests based on the user stories based on my three user types outlined in the previously linked spreadsheet. 
([Avaliable here]([here](/media/readme/userstories.xlsx)))

### Customer user goals

1. As a customer, I would like to view all avaliable products so I can browse the varoisu flooring options on offer. 
    * On entering the site, user is welcomed by logo, navbar with various filtering oprtions, a searchbar and also a masthead image. 
    * The simplest way to view all products is to scroll down to the masthead image and press the 'Shop Now' button. 
    ![HUser Story Image](/media/readme/userstory1-landingpage.jpg)
    * On clicking this, user is taken to a list of all products (of course, there are various filtering options detailed below)
    ![User Story Image](/media/readme/userstory1-products.jpg)

2. As a customer, I would like to narrow down my search results to just one type of flooring (e.g. laminate), so I can view and select from only the products that suit my needs. 
    * On entering the site, user can clearly see navigation options. If user clicks 'Laminate' they will be greeted with a dropdown menu
    ![User Story Image](/media/readme/userstory2-laminate.jpg)
    * User is given a list of options. Do they want to see all laminate? Filter based on style or filter based on manufacturer 
    (Worth noting, not all products specify a manufacturer, so clicking 'Balterio Laminate Flooring' won't just return all laminate)
    On choosing an option, user will see only products that matchselected filter
3. As a customer, I would like to search the avaliable products so that I can filter out those that don't
 match what I'm looking for and view only the products relevant to my needs.
    * On entering the site, user is greeted by a header that very clearly displays a searchbar (This appears the same accross the site, so user can cleary follow this proccess anywhere on the site)
    * User simply needs to type in their search criteria...
    ![User Story Image](/media/readme/userstory3-search.jpg)
    * ...Click 'search' (or press 'enter).... 
    * ...And they will be returned a page with relevant products
    ![User Story Image](/media/readme/userstory3-results.jpg)
4. As a customer, I would like to add a product to my shopping bag and visit the checkout page. 
    * After following the relevant steps from the previous three user stories, user will be on the products page and have a list of products based on their criteria. 
    * On selecting one of the products, user will be greeter with the product_detail age for selected product. 
        ![User Story Image](/media/readme/userstory4-product-detail.jpg)
    * If, as above, user has selected a product that has a category of 'Accessories' or 'Underlay', User simply needs to specify quantity and press 'Add to bag'.
    * If, however, user has selected a product with category of 'carpets', 'vinyl' or 'laminate', user will be prompted to select a colour, length and width. 
    ![User Story Image](/media/readme/userstory4-price-calc.jpg)
    * User enters these fields (they are required so form will not submit if these fields are not there) and total product price is calculated by multiplying carpet width, carpet length and product price(per m2).
    * After this, user can press 'add to bag' and product will be added to their bag. 
    * If products of any category are added to the bag, user will have this confirmed by a toast in the top corner.
    ![User Story Image](/media/readme/userstory4-product-added.jpg)
    * From here, user can then click the shopping bag button. This will take them to the shopping bag page where they can confirm what they want to purchase and remove if nescessary. 
    ![User Story Image](/media/readme/userstory4-bag.jpg)
    * After confirming details and checking total, customer can click 'Checkout' and will be taken to the checkout page. 
5. As a customer, I would like to purchase a product/multiple products of different types so that I can recieve my desired product(s)
    * After following the steps in previous story and confirming order details are correct, customer will be on checkout page. 
    ![User Story Image](/media/readme/userstory5-checkout.jpg)
    * After doing one final check their order is correct, user can then enter their delivery details and card details, press complete order and (assuming card details are correct)
    they will be greeted with an order confirmation.
     ![User Story Image](/media/readme/userstory5-success.jpg)

### Regular Customer User Goals

1. As a regular customer, I would like to bookmark a product so that I can easily find it later
    * After navigating to product detail page as details in previous user stories. Customer can click the little 'heart' icon. 
    ![User Story Image](/media/readme/userstory6-fave.jpg)
    * The heart icon will become a solid heart icon to signify that this is in favourites. User will also get a nitification to say the product is added to their favouites. 
    ![User Story Image](/media/readme/userstory6-success.jpg)
    * User can them click the account button, select 'My profile' and they will be taken to their profile page which (by default) will show any items in their favourites.
    ![User Story Image](/media/readme/userstory6-favourites.jpg)
2. As a regular customer, I would like to view my profile so that I can view my order history, favourites and delivery information. 
    * After navigating to profile page as in previous user story, User has three options and can toggle between all three.   
        * 'Favourites' -
            As seen above, this will display user favourites.
        * 'Delivery info' -
            This will display the users delivery info if they chose to save it on product page. Can also be updated here.
        * 'Order history' -
            This will show users details of all their past orders. 

### Store Owner
1. As a Store Owner, I would like to add a new product to the site so that I can add to the products currently avaliable. 
    * Throughout the site, user will have the 'Account' Icon at the top of their page. If logged in as a superuser, they will have the option to add products. 
    * Clicking this will take them to a product management form where they can add products.
    ![User Story Image](/media/readme/ownerstory-add.jpg)
    * Once they have typed in the details, they just need to press 'add product' and this product will be added. (Note, discovered and fixed bug with this whilst doing this test). 
    ![User Story Image](/media/readme/user-test-oroduct.jpg)
2. As a store owner, I would like to edit a product so that I can change price/update stock listing. 
    * User can navigate to either product or product_detail pages. Once there, if logged in as a superuser, they have the option to edit. 
    * Clicking edit will take them to a form similar to the add product form, but with product detail prefilled. User just needs to change relevant details and submit form.
3. As a store owner I would like to remove a product no longer avaliable so that I can stop customers attempting to purchase delisted products.
    * User can navigate to either product or product_detail pages. Once there, if logged in as a superuser, they have the option to delete.
    * User selects delete button. 
    * Product is removed from store.  

## Additional Testing

* Html code passed through w3c validator. The only errors returned are those relating to Jinja templating language.
* CSS code passed throgh w3c Jigsaw validator with no errors.
* Site tested on Google Chrome (phone and laptop), Mozilla Firefox (laptop) & Safari (Phone & Ipad) browsers
* I've tested the site on a number of devices such as my laptop, my second (larger)monitor, an iPhone 12 mini and a much larger Oppo x2 neo phone.
* I've spent a lot of time repeatedly using the various functions accross the site and have fixed various issues (e.g as noted above, error in submitting add products form) to make sure they work as well as possible.
* I've made test Stripe purchases and confirmed webhooks are working. 
![Webhook](/media/readme/webhook.jpg)


## Known Bugs
* The key bug is that although a colour is required on the product detail screen, this detail is not passed through to the shopping bag any further. I spent a lot of time discussing with 
tutor support how to make this work and until very near the end I thought I had it working. However, there was an issue with it where if a carpet of the same area had already been put in 
the bag and the user wanted to add the same carpet, with the same area, but of a different colour - the new product would just increase the quantity of the original and replace the original colour. 
I discussed with tutor support who talked through how complex this would make the bag structure (as well as related functions such as deleting items) and I ultimatley decided that given the timeframe I wouldn't be able to implement this feature. 
The bag only displays the specified area of the product, but it increases appropriatley if area of item is already in bag or adds a seperate item if it is not. 
    * Note though, I did leave the colour functionality on the product detail page and make it a required field. Honestly, I was just really happy with the image changing feature on this and 
    wanted to leave it in. 
* Previously mentioned add colour function does not crash site, but only returns unsuccessful.
* Issues with toasts. On some screens, toasts stretch accross page, I tried various styling solutions but could not fix this in time. Additionally, could not get dismiss button to work so removed this. 
* A number of small visual bugs, primarily regarding responsivity on mobile screens when viewed horizontally. 

# Deployment
My website has been deployed via Heroku using Postgres as database and using Amazon Web services to host images and static files. Heroku has been linked to my Github Repository for this project and auto deploys the code based on my latest commit. 
In order to deploy the project in this way I took the following steps: 

1. Created Github Repository
2. Created requirements.txt file & procfile in Gitpod workspace in order to tell Heroku what dependencies my project has.

3. Logged in to Heroku & created a new app. 
3. In my settings.py file, enabled project to use AWS for static files.
4. Signed up to Amazon Web services. 
5. Selected S3, created bucket and enabled read permissions. 
4. Selected 'Deploy' in Heroku navbar. 
5. Chose 'Github' in deployment method. 
6. Searched for my project's Github repository in the repository search box. Selected correct repository. 
7. In same navbar I selected 'Deploy', selected 'Settings'. 
8. On this page selected 'Reveal Config Vars', this brings up fields to input key & value for config vars. 
9. Input the keys for AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, DATABASE_URL, EMAIL_HOST_PASS, EMAIL_HOST_USER, SECRET_KEY, STRIPE_PUBLIC_KEY, STRIPE_SECRET_KEY, 
STRIPE_WH_SECRET and USE_AWS as well as corresponding values. 
10. Went back to 'Deploy', scorlled down to 'Enable Automatic Deployment' and clicked this. 
11. Heroku then built the application and provided a link to i

### Clone project
* To clone this project, user would need to access github repository, clock 'Gitpod' button in top corner (if installed), once workspace has been set up install requirements in txtfile so workspace runs properley 
and then follow above steps for deployment. 


# Credits
## Code
* Various templates from Start Bootstrap were used throughout the site. I didn't stick to a particular one, but drew primarily from 
    * [Landing Page](https://startbootstrap.com/theme/landing-page) - for the masthead code on index page
    * [Freelancer](https://startbootstrap.com/theme/freelancer) -for the card layout on product page
    * [Shop-item](https://startbootstrap.com/template/shop-item) - for the product detail page layout
* [Bootstrap](https://getbootstrap.com/)'s library was used to help me make further changes to the layouts and provided code snippets for modals & buttons throughout. 
* [Code Institute](https://codeinstitute.net/) - Obviously the code used in the Fullstack Framework module was massivley relied on - a lot of the code used is based on CI tutorial videos. 
* Code Institute Slack channel - also useful for helping solve issues. 
    * One particular function that I sort of stumbled accross on slack was how to get comment usernames prefilled. I wasn't sure how to properly credit this but have included
    a screenshot [here](/media/readme/slack-screenshot.jpg) 

* I relied a lot on Code Institute tutor support throughout the project, but particular areas I required particular help with were: 
    * Javascript for colour image changes on product detail page
    * Attempting to make bag logic based on colour (As detailed above, this ultimatley wansn't implemented, but Ispent a lot of time speaking to tutor support about it)

* Throughout the project I also regularly referred to the following:
    * [Stack Overflow](https://stackoverflow.com/) - provided a number of solutions to issues throughout the project.
    * [W3schools](https://www.w3schools.com/css/css3_images.asp)

* I solved a number of issues through wanting online tutorial videos. These were as follows:
    * Comment/review functionality
        * Primarily followed [this](https://www.youtube.com/watch?v=pNVgLDKrK40), but also [this](https://www.youtube.com/watch?v=OuOB9ADT_bo&list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi&index=36). 
    * Favourites Functionality
        * Primarily followed this[this](https://www.youtube.com/watch?v=1XiJvIuvqhs) and also [this](https://www.youtube.com/watch?v=OgA0TTKAtqQ&list=PLOLrQ9Pn6caxY4Q1U9RjO1bulQp5NDYS_&index=8)

## Content
* All static content was written by me (but relied heavily on code institute tutorials)
* The basic functionalities accross the site are based on that found on [OnlineCarpets](https://www.onlinecarpets.co.uk/carpets.html), product images and details were also taken from this site. 

## Media 
* Masthead image comees from Pexels.com artist [Kayley Dlugos](https://www.pexels.com/photo/window-shadow-on-wall-and-floor-of-modern-room-5872378/) 
* Logo designed using was provided by Alex Gibb (no artist credit)

## Acknowledgements
* Code Institute Mentor Gerard McBride - for providing support throughout
* Code Institute Tutor Support - for also providing support throughout
* Websites used for design inspiration:
    * [OnlineCarpets](https://www.onlinecarpets.co.uk/carpets.html)