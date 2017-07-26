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

LinkedInBot was developed under [Pyhton 2.7](https://www.python.org/downloads).

Before you can run the bot, you will need to install a few Python dependencies.

Note: Python 2.7.9 and later (on the python2 series), and Python 3.4 and later include pip by default, so you may have pip already. Otherwise, you can install [easy_install](https://pythonhosted.org/setuptools/easy_install.html) `sudo apt-get install python-setuptools` to install [pip](https://pypi.python.org/pypi/pip) `sudo easy_install pip`.

- [BeautifulSoup4](https://pypi.python.org/pypi/beautifulsoup4), for parsing html: `pip install BeautifulSoup4`
- [Selenium](http://www.seleniumhq.org/), for browser automation: `pip install Selenium`

If you plan to use Firefox (or Iceweasel) you don't need anything more.

For Chrome, first get the [webdriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) then put it in the same folder than the bot if you are on Windows, or in the `/usr/bin` folder if you are on OS X.

PhantomJS:
- On Windows, download the binary from the [official website](http://phantomjs.org) and put it in the same folder than the bot.
- On OS X Yosemite, the binary provided by the PhantomJS crew doesn't work (*selenium.common.exceptions.WebDriverException: Message: 'Can not connect to GhostDriver'*). You can either compile it by yourself or download the binary provided by the awesome [eugene1g](https://github.com/eugene1g/phantomjs/releases). Then put it in the `/usr/bin` folder.
- It's the same for Raspbian : compile it and put it in the `/usr/bin` folder or download the binary provided by the awesome [fg2it](https://github.com/fg2it/phantomjs-on-raspberry/tree/master/rpi-2-3/wheezy-jessie/v2.1.1).

If you want to built your own binaries, here is the [build instructions](http://phantomjs.org/build.html) for PhantomJS.

## Configuration
Before you run the bot, edit the configuration portion of the script. This will include your account login information (email, password, etc.) and other logical values to make the bot more of your own. It's that simple!

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
Once you have installed the required dependencies and edited the `config` file, you can run the bot.

Make sure you are in the correct folder and run the following command: `python LinkedInBot.py`

Then, after choosing your favorite browser the bot will start visiting profiles.

## Output

![LinkedInBot Demo Gif](http://g.recordit.co/xPh4gK70lz.gif)

T: Number of profiles the bot tried to access;

V: Number of profiles the bot actually visited (profiles you can access: rank 3 or less);

Q: Number of profiles in queue.

## Enhancements
Please feel free to message me or open an issue if you have an idea for an enhancement! Seems like people are starting to use this and I would like to improve it.
