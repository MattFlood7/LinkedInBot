#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, random, sys, time, urlparse
from selenium import webdriver
from bs4 import BeautifulSoup
from random import shuffle

def Launch():

    """
    Launch the LinkedIn bot.
    """

    # Check if the file 'config' exists, otherwise quit
    if os.path.isfile('config') == False:
        print 'Error! No configuration file.'
        sys.exit()

    # Check if the file 'visitedUsers.txt' exists, otherwise create it
    if os.path.isfile('visitedUsers.txt') == False:
        visitedUsersFile = open('visitedUsers.txt', 'wb')
        visitedUsersFile.close()

    # Browser choice
    print 'Choose your browser:'
    print '[1] Chrome'
    print '[2] Firefox/Iceweasel'
    print '[3] PhantomJS'

    while True:
        try:
            browserChoice = int(raw_input('Choice? '))
        except ValueError:
            print 'Invalid choice.',
        else:
            if browserChoice not in [1,2,3]:
                print 'Invalid choice.',
            else:
                break

    StartBrowser(browserChoice)

def StartBrowser(browserChoice):

    """
    Launch broswer based on the user's selected choice.
    browserChoice: the browser selected by the user.
    """

    if browserChoice == 1:
        print '\nLaunching Chrome'
        browser = webdriver.Chrome()

    if browserChoice == 2:
        print '\nLaunching Firefox/Iceweasel'
        browser = webdriver.Firefox()

    if browserChoice == 3:
        print '\nLaunching PhantomJS'
        browser = webdriver.PhantomJS()

    # Open, load and close the 'config' file
    with open('config', 'r') as configFile:
        config = [line.strip() for line in configFile]
    configFile.close()

    # Sign in
    browser.get('https://linkedin.com/uas/login')
    emailElement = browser.find_element_by_id('session_key-login')
    emailElement.send_keys(config[0])
    passElement = browser.find_element_by_id('session_password-login')
    passElement.send_keys(config[1])
    passElement.submit()

    print 'Signing in...'
    time.sleep(3)

    soup = BeautifulSoup(browser.page_source)
    if soup.find('div', {'class':'alert error'}):
        print 'Error! Please verify your username and password.'
        browser.quit()
    elif browser.title == '403: Forbidden':
        print 'LinkedIn is momentarily unavailable. Please wait a moment, then try again.'
        browser.quit()
    else:
        print 'Success!\n'
        LinkedInBot(browser)


def LinkedInBot(browser):

    """
    Run the LinkedIn Bot.
    browser: the selenium driver to run the bot with.
    """

    T = 0
    V = 0
    profilesQueued = []
    error403Count = 0
    timer = time.time()

    print 'At the my network page to scrape user urls..\n'

    # Infinite loop
    while True:

        # Generate random IDs
        while True:

            profileID = str(random.randint(10000000, 99999999))
            browser.get('https://www.linkedin.com/mynetwork/')
            T += 1

            # Add the random ID to the visitedUsersFile
            with open('visitedUsers.txt', 'ab') as visitedUsersFile:
                visitedUsersFile.write(str(profileID)+'\r\n')
            visitedUsersFile.close()

            if GetNewProfileURLS(BeautifulSoup(browser.page_source), profilesQueued):
                break
            else:
                print '|',
                time.sleep(random.uniform(5, 7))

        soup = BeautifulSoup(browser.page_source)
        profilesQueued = list(set(GetNewProfileURLS(soup, profilesQueued)))

        V += 1
        print '\n\nGot our users to start viewing with!\n'
        print browser.title.replace(' | LinkedIn', ''), ' visited. T:', T, '| V:', V, '| Q:', len(profilesQueued)

        while profilesQueued:

            # Sleep a random time between profile views to throw off LinkedIn's security tracking.
            time.sleep(random.randrange(25, 300))

            shuffle(profilesQueued)
            profileID = profilesQueued.pop()
            browser.get('https://www.linkedin.com'+profileID)

            # Add the ID to the visitedUsersFile
            with open('visitedUsers.txt', 'ab') as visitedUsersFile:
                visitedUsersFile.write(str(profileID)+'\r\n')
            visitedUsersFile.close()

            # Get new profiles ID
            time.sleep(10)
            soup = BeautifulSoup(browser.page_source)
            profilesQueued.extend(GetNewProfileURLS(soup, profilesQueued))
            profilesQueued = list(set(profilesQueued))

            browserTitle = (browser.title).encode('ascii', 'ignore').replace('  ',' ')

            # 403 error
            if browserTitle == '403: Forbidden':
                error403Count += 1
                print '\nLinkedIn is momentarily unavailable - Paused for', str(error403Count), 'hour(s)\n'
                time.sleep(3600*error403Count+(random.randrange(0, 10))*60)
                timer = time.time() # Reset the timer

            # User out of network
            elif browserTitle == 'Profile | LinkedIn':
                T += 1
                error403Count = 0
                print 'User not in your network. T:', T, '| V:', V, '| Q:', len(profilesQueued)

            # User in network
            else:
                T += 1
                V += 1
                error403Count = 0
                print browserTitle.replace(' | LinkedIn', ''), 'visited. T:', T, '| V:', V, '| Q:', len(profilesQueued)

            # Pause
            if (T%1000==0) or time.time()-timer > 3600:
                print '\nPaused for 1 hour\n'
                time.sleep(3600+(random.randrange(0, 10))*60)
                timer = time.time() # Reset the timer
            else:
                time.sleep(random.uniform(5, 7)) # Otherwise, sleep to make sure everything loads

        print '\nNo more profiles to visit. Everything restarts with the network page...\n'


def GetNewProfileURLS(soup, profilesQueued):

    """
    Get new profile urls to add to the navigate queue.
    soup: beautiful soup instance of page's source code.
    profileQueued: current list of profile queues.
    """

    # Open, load and close
    with open('visitedUsers.txt', 'r') as visitedUsersFile:
        visitedUsers = [line.strip() for line in visitedUsersFile]
    visitedUsersFile.close()

    # Get profiles from the "People Also Viewed" section
    profileURLS = []

    # TODO: This is pretty bad looking. Fix this up at some point to look cleaner.
    try:
        for a in soup.find_all('a', class_='mn-person-info__picture'):
            if a['href'] not in profileURLS and a['href'] not in profilesQueued and "/in/" in a['href'] and "connections" not in a['href'] and "skills" not in a['href']:
                print a['href']
                profileURLS.append(a['href'])

    except:
        pass

    try:
        for a in soup.find_all('a', class_='pv-browsemap-section__member'):
            if a['href'] not in profileURLS and a['href'] not in profilesQueued and "/in/" in a['href'] and "connections" not in a['href'] and "skills" not in a['href']:
                print a['href']
                profileURLS.append(a['href'])

    except:
        pass

    try:
        for ul in soup.find_all('ul', class_='pv-profile-section__section-info'):
            for li in ul.find_all('li'):
                a = li.find('a')
                if a['href'] not in profileURLS and a['href'] not in profilesQueued and "/in/" in a['href'] and "connections" not in a['href'] and "skills" not in a['href']:
                    print a['href']
                    profileURLS.append(a['href'])
    except:
        pass

    profileURLS = list(set(profileURLS))
    return profileURLS


if __name__ == '__main__':
    Launch()
