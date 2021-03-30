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


#

## Known Bugs
* The key bug is that although a colour is required on the product detail screen, this detail is not passed through to the shopping bag any further. I spent a lot of time discussing with 
tutor support how to make this work and until very near the end I thought I had it working. However, there was an issue with it where if a carpet of the same area had already been put in 
the bag and the user wanted to add the same carpet, with the same area, but of a different colour - the new product would just increase the quantity of the original and replace the original colour. 
I discussed with tutor support who talked through how complex this would make the bag structure (as well as related functions such as deleting items) and I ultimatley decided that given the timeframe I wouldn't be able to implement this feature. 
The bag only displays the specified area of the product, but it increases appropriatley if area of item is already in bag or adds a seperate item if it is not. 
    * Note though, I did leave the colour functionality on the product detail page and make it a required field. Honestly, I was just really happy with the image changing feature on this and 
    wanted to leave it in. 
* Issues with toasts. On some screens, toasts stretch accross page, I tried various styling solutions but could not fix this in time. Additionally, could not get dismiss button to work so removed this. 
* A number of small visual bugs, primarily regarding responsivity on mobile screens when viewed horizontally. 

# Deployment


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
        * Primarily followed this[this](https://www.youtube.com/watch?v=1XiJvIuvqhs) and also (this)[https://www.youtube.com/watch?v=OgA0TTKAtqQ&list=PLOLrQ9Pn6caxY4Q1U9RjO1bulQp5NDYS_&index=8]

## Content
* All static content was written by me (but relied heavily on code institute tutorials)
* The basic functionalities accross the site are based on that found on (OnlineCarpets)[https://www.onlinecarpets.co.uk/carpets.html], product images and details were also taken from this site. 

## Media 
* Masthead image comees from Pexels.com artist[Kayley Dlugos](https://www.pexels.com/photo/window-shadow-on-wall-and-floor-of-modern-room-5872378/) 
* Logo designed using was provided by Alex Gibb (no artist credit)

## Acknowledgements
* Code Institute Mentor Gerard McBride - for providing support throughout
* Code Institute Tutor Support - for also providing support throughout
* Websites used for design inspiration:
    * (OnlineCarpets)[https://www.onlinecarpets.co.uk/carpets.html]