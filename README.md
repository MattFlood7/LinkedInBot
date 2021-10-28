# LinkedInBot
Increase your likelihood to grow your connections and potentially get interview opportunities on LinkedIn by increasing visibility of your profile by viewing others profiles.
## About
When you view user's profile in LinkedIn they get notified that you have looked at their profile. This bot will allow you to view user's profiles thus increasing your visibility in your suggested LinkedIn network.
<p align="center">
  <img src="https://preview.ibb.co/mMDuAk/linked_In_Bot_Profile_View_Results.png" alt="LinkedInBot Result" width="325" height="200">
</p>

## Note
This project is a modified and updated version of the awesome [helloitsim](https://github.com/helloitsim)'s [LInBot](https://github.com/helloitsim/LInBot) project. I found his repository and noticed it was outdated and needed some updating after LinkedIn had modified their site.

## Requirements
**Important:** make sure that you have your [Profile Viewing Setting](https://www.linkedin.com/settings/?trk=nav_account_sub_nav_settings) changed from 'Anonymous' to  'Public' so LinkedIn members can see that you have visited them and can visit your profile in return.
You also must change your language setting to **English**.

LinkedInBot was developed under [Python 3.8](https://www.python.org/downloads).

Before you can run the bot, you will need to install a few Python dependencies. Run `pip3 install -r requirements.txt` to install them.

If you plan to use Firefox (or Iceweasel) you don't need anything more.

For Chrome, first get the [webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) then put it in the same folder than the bot if you are on Windows, or in the `/usr/bin` folder if you are on OS X.

PhantomJS:
- On Windows, download the binary from the [official website](http://phantomjs.org) and put it in the same folder than the bot.
- On OS X Yosemite, the binary provided by the PhantomJS crew doesn't work (*selenium.common.exceptions.WebDriverException: Message: 'Can not connect to GhostDriver'*). You can either compile it by yourself or download the binary provided by the awesome [eugene1g](https://github.com/eugene1g/phantomjs/releases). Then put it in the `/usr/bin` folder.
- It's the same for Raspbian : compile it and put it in the `/usr/bin` folder or download the binary provided by the awesome [fg2it](https://github.com/fg2it/phantomjs-on-raspberry/tree/master/rpi-2-3/wheezy-jessie/v2.1.1).

If you want to built your own binaries, here is the [build instructions](http://phantomjs.org/build.html) for PhantomJS.

## Configuration
Before you run the bot, create a `.env` file with the configuration of the script. This will include your account login information (email, password, etc.) and other logical values to make the bot more of your own. It's that simple!

```python
# Configurable Constants
EMAIL = 'youremail@gmail.com'
PASSWORD = 'password'
VIEW_SPECIFIC_USERS = False
SPECIFIC_USERS_TO_VIEW = ['CEO', 'CTO', 'Developer', 'HR', 'Recruiter']
NUM_LAZY_LOAD_ON_MY_NETWORK_PAGE = 5
CONNECT_WITH_USERS = True
RANDOMIZE_CONNECTING_WITH_USERS = True
JOBS_TO_CONNECT_WITH = ['CEO', 'CTO', 'Developer', 'HR', 'Recruiter']
ENDORSE_CONNECTIONS = False
RANDOMIZE_ENDORSING_CONNECTIONS = True
VERBOSE = True
```

## Run
Once you have installed the required dependencies, created the `.env` file with your data, you can run the bot.

Make sure you are in the correct folder and run the following command: `python LinkedInBot.py`

Then, after choosing your favorite browser the bot will start visiting profiles.

## Output

![LinkedInBot Demo Gif](http://g.recordit.co/xPh4gK70lz.gif)

T: Number of profiles the bot tried to access;

V: Number of profiles the bot actually visited (profiles you can access: rank 3 or less);

Q: Number of profiles in queue.

## POTENTIAL ISSUES

* 2 Factor Authentication
	* Solution: Working on a setting to give more time to get it, if it is enabled you cannot use headless mode
* Stuck on `-> Scraping User URLs on Network tab.`
	* Solution: I have encountered this issue before and restarting the script usually works
* LinkedIn Security Email
	* You were sent a pin to make sure its really you, either enter the pin if you are not in headless mode or restart the bot.
	* At this point it might be best to tread lightly, as your account could be flagged and being monitored. However I am not certain on that.

## DISCLAIMER

The use of bots and scrapers are mentioned [here](https://www.linkedin.com/help/linkedin/answer/56347/prohibited-software-and-extensions?lang=en).
Use this bot at your own risk. 
Just to push more knowledege a judge in California ruled that they cannot prohibit bots([article](https://www.bbc.com/news/technology-40932487)).

## Note

I have sparily modified this project over the past few years. Others have taken upon themselves to leverage this as a base and work off of it from here. As I learn more about other's work using this I will link their projects here:

* [@SethRzeszutek's](https://github.com/SethRzeszutek) https://github.com/SethRzeszutek/LinkedIn-Bot
