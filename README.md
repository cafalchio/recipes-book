# Overview

Recipe's Book is an online Plataform designed for cooking enthusiastics and food lovers. It is a place to 
share recipes and keep the secret recipes for easy access. User can easily add, edit, and delete their recipes.
Visitors can brownse public recipes to find the dish they want to prepare.
[Click here to see the online version of recipes-book](https://recipes-book.herokuapp.com/)

# UX
This site was created respecting the Five Planes Of Website Design:

## Strategy

**User Stories:**  
| EPIC |ID| User Story | Scenario |
| :------------------------|--|:------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**ADDING A RECIPE** |1A| As a cooking enthusiast, I want to be able to add my own recipes to the website, so I can share them with others and have a centralized place to store them. | Alex loves cooking and wants to add a new recipe for chocolate chip cookies. They log in to the website, navigate to the "Add Recipe" page, fill in the required information about the recipe, and click on the "Submit" button. The recipe is now saved and visible on Alex's profile and the public recipe list.|
|**VIEWING RECIPES** |2A| As a user, I want to be able to browse and view recipes on the website, so I can find new meal ideas and inspiration. | Taylor visits the website and browses through the public recipes. They find a delicious-looking pasta dish and click on it to view the full recipe, including ingredients, instructions, and any additional notes.|
|**EDITING A RECIPE** |3A| As a user who has added a recipe, I want to be able to edit my own recipes, so I can make updates or correct any errors. | Jamie added a recipe for a vegetarian chili, but they realize they forgot to include an important ingredient. They log in, navigate to their recipe, and click on the "Edit" button. They add the missing ingredient and save the changes. The updated recipe now includes the correct ingredient list.|
|**DELETING A RECIPE** |4A| As a user, I want to be able to delete my own recipes, so I can remove any outdated or unwanted recipes from the website. | Chris decides they no longer want their old smoothie recipe on the website. They log in, find the recipe in their profile, and click on the "Delete" button. The recipe is removed from the website and no longer visible to other users.|
|**MARKING A RECIPE PRIVATE** |5A| As a user, I want to be able to mark my recipes as private, so I can control who can view them. | Morgan creates a special family recipe that they want to keep private. While adding the recipe, they select the "Private" option. Now, only Morgan can see the recipe when logged into their account, and it is not visible to other users or non-logged-in visitors.|
|**MARKING A RECIPE PUBLIC** |6A| As a user, I want to be able to mark my recipes as public, so I can share them with everyone. | Jordan has a private recipe for a homemade pizza that they want to share with the community. They log in, navigate to the recipe, click on the "Edit" button, and change the recipe's privacy setting to "Public." The recipe is now visible to all users and non-logged-in visitors on the website.|

### Project Goal
* A simple and easy user navigation
* Add recipes, delete and edit.
* View recipes in a easy and beautiful way.
* Available and responsive in every device.


## Structure

**Guest** Can see the home page - Can see public recipes - can sign up -- can login
**User** Can see home page -- Can see public recipes -- can add recipes -- can edit recipes -- can delete recipes -- can logout

## Skeleton


## Surface

### Color Scheme

    The colors choosen can all be seen in this image: The colors in hexa are:

    --bs-green: #2da2a6;
    --bl-background: #00000020;
    --text-subtle: #64697d;
     background-color: #f5f5f5;


### Fonts
    
    The fonts were selected to be used as system fonts. 
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";

# Agile Methodology
    This project was developed using the Agile methodology.
    All user stories implementation progress was registered using Github Projects.



# Features
## Existing Features

### Create Recipes


### Delete Recipes


### Editing Recipes


### Make Recipes Public/Private


## Future Features

### Adding Comments to Recipes

    As a future feature for the recipes website, I would like to add the ability for users to leave comments on recipes. This would allow users to share their thoughts, experiences, and suggestions with others

### Add Stars Ratings to Recipes
    User would be able to add from 1-5 stars to each recipe, the result stars would be the average score between all users that gave a review.

# Responsive Layout

    **Tested on simulated devices**
    *Galaxy Note 20 - Android 11
    *Galaxy S20 Ultra - Android 11
    *Galaxy S9/S9+ - Android 7
    *iPhone 11 Pro - iOS 14.6
    *iPhone 12/13 Pro Max - iOS 14.6
    *iPhone 5/SE - iOS 10.3.1
    *iPhone 6/7/8 - iOS 11
    *iPhone SE 2nd gen - iOS 14.6
    *iPhone X/XS - iOS 12
    *iPhone XR/11 - iOS 12
    *iPadiPadOS - 14.7.1
    *Kindle Fire - HDXLinux

    **Tested on real devices**
    Pixel 5 - Android 11
    Motorola g7 Power - Android 10

# Tools Used

    GitHub - used for hosting the source code of the program
    Visual Studio - for writing and testing the code
    Heroku - used for deploying the project
    TablePlus - for managing the database entries
    GIMP  - GNU Image Manipulation Program
    Cloudinary - for storing static data
    Bootstrap5 - for styling and responsiveness
    PEP8 Validator - used for validating the python code
    HTML - W3C HTML Validator - used for validating the HTML
    Firefox Dev Tools - For Debugging
    Chromium - Lighthouse testing
    ElephantSQL - For database hosting


## Python Packages
# Testing
# Deployment

    Deploy on Heroku

    Create Pipfile

    In the terminal enter the command  pip3 freeze --local > requirements.txt, and a file with all requirements will be created.

    Deployment on Heroku
        Create a database in ElephantSQL (https://www.elephantsql.com/)
        Go to the Heroku website (https://www.heroku.com/)
        Login to Heroku and choose Create App
        Click New and Create a new app
        Choose a name and select your location
        Go to the Settings tab
        Reveal Config Vars and add your Cloudinary, Database URL, Secret key and PORT.
        Navigate to the Deploy tab
        Click on Connect to Github and search for your repository
        Go to the Deploy tab.
        Deploy :)


## Deploy on Heroku
# Credits
# Acknowledgements



