# Life in Blog
[View live project Here](https://the-club-77a7b1e1e156.herokuapp.com/)
***

The Club is the online home of The Seans GAA Club Threemilehouse. The club allows users, players and members of the community to purchase club gear, pay player subs, catch up on club and community news and view upcoming fixtures. The admin views also allow the managers and board of the club to manage and view sub payments, list games, news etc. 

![Mock Up](media/doc-images/mockup.png)

- [Blog Website](#blog-website)
- [User Experience UX](#user-experience-ux)
  - [UX-strategy](#ux-strategy)
  - [UX-scope](#ux-scope)
  - [UX-structure](#ux-structure)
  - [UX-skeleton](#ux-skeleton)
  - [UX-surface](#ux-surface)
- [Technologies-used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

# User Experience UX

## UX-strategy

The goal of the project is to provide a one stop shop for the local community to interact with their club. In an increasingly cashless society paying for club subs and gear has become a chore. The Club allows users to pay subs online and administrators still have the ability to add subs manually. As a not for profit community orgainsation the additional revenue generated from sales of club merchandise are used to further enhance the club for the community. Social Media has in recent years become the primary platform to communicate club news and fixtures. The Club brings that communication back to a central point which is owned and operated by the club but also provides the oportunity for additional revenue generation. 

**Developer Goals**

- Build portfolio.
- Develop my technical skills.
- Deliver a real world project which I will be able to give to my community club. 

**User Stories**

[Full User Stories](https://docs.google.com/spreadsheets/d/1QvcKgmC9WbiC6ZFg4j-qCKpRea_9rqwP6MOy0nx6mpA/edit?usp=sharing)

_As a FIRST TIME user of the site I want to be able to:_
- Intuitively and easily navigate the site
- Browse club items for sale
- Purchase club gear
- Read news
- Find upcoming fixture
- Register as a user
- Logout of the site

_As a RETURNING user of the site I want to be able to:_
- Log in and out of the site
- Pay subs
- Browse club items for sale
- Purchase club gear
- Review most recent news easily
- See updated fixtures
- Search for specific fixtures

**Admins**

I considered that due to the nature of the Club there may be two types of admin for a site such as this. Community volenteers, coaches etc and then admin of the overall site. I wanted to create an easy UI for more casual administrators making it easy for them to administer everyday tasks on the site without utilising the built in Django admin. 

_As an admin of the site I want to be able to:_
- Manage Product Categories (add, edit, delete)
- Manage Products (add, edit, delete)
- Manage News (add, edit, delete)
- Manage Fixtures (add, edit, delete)
- Manage Players (add, edit, delete)
- Manage Subs (view and add)

## UX-scope

**Existing Features**

**Home Page**

![homepage LoggedOut]()

**Nav Bar**

Links available within the navbar vary dependent on access. 

_Logged Out_

![Nav LoggedOut]()

_Logged In_

![Nav LoggedIn]()

_Admin_

![Nav Admin]()

**Logo**

![Logo]()

**Search Shop Feature**

![Search]()

**Club News**

![Club News]()

**Footer**

![Footer]()

**Register Page**

![registration form]()

**Login Page**

![Login]()

**Profile Page**

![profile]()

**Logout**

![Logout]()

- **Contact page**

![Contact]()

**Administrator Features**
- Add Club News

![club news]()

- Add Shop Items

![new shop item]()

_**404/500 Error Pages:**_

- A 404 error page will display if a user tries to navigate to a page that doesn't exist. 
- A 500 error page will display if there is an internal server error.
- Both error pages contain the familiar navigation but will also redirect back to the homepage after 5 seconds. 

**Future Improvements**

- User commenting on News

## UX-structure

- _Navigation_: Logo, search function, shop, fixtures, account and basket to facilitate browsing the site. On mobile devices the navigation collapses to a familiar hamburger icon which the user will find familiar. 

- _Search Feature_: searches the club kit items for sale with placeholder text of 'shop club kit' for user clarity. 

- _Menu Items_: Navigation menu items allwo the user to navigate intuitively through the site. 

- _News Section_: The news section of the home page displays the 10 most recent news articles (with most recent first). The Club News heading is a clickable link with eye catching hover css to ensure clear user understanding. 

- _Bag Page_: This is broken up to display subs section and products seperately. with appropriate details and buttons for both. The products quantity can be updated or deleted while the individual subs lines can be removed from the bag. 

- 


**Data Structure**

![Data Structure](media/doc-images/data-model/seansdb.png)

**Security**


## UX-skeleton

**Design Choices**
 


**Wireframes**

To follow best practice wireframes were developed for Mobile followed by tablet and desktop. I used [Balsamiq](https://balsamiq.com/) to design my wireframes. 

[View Wireframes](wireframes.md)

## UX-surface

**Colour Palette**

https://color.adobe.com/create/image

https://mycolor.space/
background-image: linear-gradient(to bottom, #266b73, #157877, #0d8476, #218f70, #3d9a66, #42955a, #47904e, #4c8b42, #3a7735, #286429, #16521d, #014011);

**Fonts**

I used [Google Fonts](https://fonts.google.com/) to choose 


**Responsiveness**




# Technologies-used
- **Libraries:** jQuery, Materialize 
- **Python Framework:** Flask
- **Languages:** HTML, CSS, JavaScript, Python
- **Database Management:** MongoDB
- **Version Control:** Git
- **Gitpod:** used as a cloud code editor.
- **GitHub:** used as a cloud based code repository.
- **Heroku:** was used to deploy the app. 

# Testing 
[View Testing Documentation](testing.md)

# Deployment
The Website has been deployed using Heroku [Here]() using the method below:



### Heroku Deployment

- I logged into my Heroku Account. 
- I clicked on New and choose 'Create New App'
- I choose a unique name for my app and set the region to Europe. 
- I then chose Github as the deployment method and searched for my repo name. 
- I then clicked on settings and updated the config variables. 
- I navigated back to the deploy and enabled automatic deployment. 

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's **requirements** (where applicable) using:
- `pip3 install -r requirements.txt`

You can update your requirements.txt file using:
- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:
- `echo web: python app.py > Procfile`

This project can be cloned or forked in order to make a local copy on your own system.

For either method, you will need to install any applicable packages found within the *requirements.txt* file.
- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level which contains your own environment variables. 

```
os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("MONGO_DBNAME", "user's own value")
os.environ.setdefault("MONGO_URI", "user's own value")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "user's own value")`
```

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://github.com/janebmckenna/MilestoneProject3/tree/main) 
2. Locate the Code button above the list of files and click it 
3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
4. Open Git shell or Terminal
5. Change the current working directory to the one where you want the cloned directory
6. In your IDE Terminal, type the following command to clone my repository:
  
   `git clone https://github.com/janebmckenna/MilestoneProject3.git`
7. Press Enter to create your local clone.

#### Forking

By forking the GitHub Repository, we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository.
You can fork this repository by using the following steps:

1. Login to GitHub and locate the [GitHub Repository](https://github.com/janebmckenna/MilestoneProject3/tree/main)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!


# Credits
**Content**



**Code**
- I ran into a bug with the date field and i found the solution code [here](https://stackoverflow.com/questions/61077802/how-to-use-a-datepicker-in-a-modelform-in-django)

One of the comments suggested 

`target_Date = forms.DateField(widget=forms.TextInput(attrs={'min': today, 'value': today, 'type': 'date'}), required=True)`

As I had already set the min date to today in the model I ended up using 

`date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}), required=True)`

- I tried many different ways of implimenting the subs into the exisiting payment/order/product models I had built. I saw MVP as not requiring the subs model but it was a feature I wanted to impliment as I felt it was needed for the club. I googled/read/followed many ways of implimenting each of which ran into more issues. 

Some of the articles

1. [saaspegasus.com](https://www.saaspegasus.com/guides/django-stripe-integrate/)
2. [stripe docs](https://docs.stripe.com/billing/subscriptions/build-subscriptions?ui=stripe-hosted#create-session)
3. I also searched slack 
4. Asked AI both [perplexity.ai](www.perplexity.ai) and [chatgpt](chat.openai.com) (Which I found frustrating and unhelpful due to the narrow answers)

In truth none of it worked and I reversed back and started from scratch breaking the code and fixing it as I went step by step. Truthfully I have probably subconciously taken inspiration from code I learnt as I researched and havent documented but I implimented the final fixes by breaking and fixing the code as I worked through it step by step. 


https://docs.djangoproject.com/en/5.0/ref/templates/builtins/#

**Images**

I would like to thank my brother in law Ashley Maguire who is treasurer of the club who inspired this project for providing all the images. 

**Advice**

