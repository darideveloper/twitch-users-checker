<div><a href='https://github.com/darideveloper/twitch-users-checker/blob/master/LICENSE' target='_blank'>
            <img src='https://img.shields.io/github/license/darideveloper/twitch-users-checker.svg?style=for-the-badge' alt='MIT License' height='30px'/>
        </a><a href='https://www.linkedin.com/in/francisco-dari-hernandez-6456b6181/' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=LinkedIn&color=0A66C2&logo=LinkedIn&logoColor=FFFFFF&label=' alt='Linkedin' height='30px'/>
            </a><a href='https://t.me/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Telegram&color=26A5E4&logo=Telegram&logoColor=FFFFFF&label=' alt='Telegram' height='30px'/>
            </a><a href='https://github.com/darideveloper' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=GitHub&color=181717&logo=GitHub&logoColor=FFFFFF&label=' alt='Github' height='30px'/>
            </a><a href='https://www.fiverr.com/darideveloper?up_rollout=true' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Fiverr&color=222222&logo=Fiverr&logoColor=1DBF73&label=' alt='Fiverr' height='30px'/>
            </a><a href='https://discord.com/users/992019836811083826' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Discord&color=5865F2&logo=Discord&logoColor=FFFFFF&label=' alt='Discord' height='30px'/>
            </a><a href='mailto:darideveloper@gmail.com?subject=Hello Dari Developer' target='_blank'>
                <img src='https://img.shields.io/static/v1?style=for-the-badge&message=Gmail&color=EA4335&logo=Gmail&logoColor=FFFFFF&label=' alt='Gmail' height='30px'/>
            </a></div><div align='center'><br><br><img src='https://raw.githubusercontent.com/darideveloper/twitch-users-checker/master/logo.webp' alt='Twitch Users Checker' height='80px'/>

# Twitch Users Checker

Check if a group of twitch accounts are active

Project type: **client**

</div><br><details>
            <summary>Table of Contents</summary>
            <ol>
<li><a href='#buildwith'>Build With</a></li>
<li><a href='#relatedprojects'>Related Projects</a></li>
<li><a href='#media'>Media</a></li>
<li><a href='#details'>Details</a></li>
<li><a href='#install'>Install</a></li>
<li><a href='#settings'>Settings</a></li>
<li><a href='#roadmap'>Roadmap</a></li></ol>
        </details><br>

# Build with

<div align='center'><a href='https://www.python.org/' target='_blank'> <img src='https://cdn.svgporn.com/logos/python.svg' alt='Python' title='Python' height='50px'/> </a><a href='https://www.selenium.dev/' target='_blank'> <img src='https://cdn.svgporn.com/logos/selenium.svg' alt='Selenium' title='Selenium' height='50px'/> </a></div>

# Related projects

<div align='center'><a href='https://github.com/darideveloper/twitch-cookies-getter' target='_blank'> <img src='https://github.com/darideveloper/twitch-cookies-getter/blob/master/logo.png?raw=true' alt='Twitch Cookies Getter' title='Twitch Cookies Getter' height='50px'/> </a><a href='https://github.com/darideveloper/twitch-viwer-bot' target='_blank'> <img src='https://github.com/darideveloper/twitch-viwer-bot/blob/master/logo.png?raw=true' alt='Twitch Viwer Bot' title='Twitch Viwer Bot' height='50px'/> </a><a href='https://github.com/darideveloper/twitch-cheer-bot' target='_blank'> <img src='https://github.com/darideveloper/twitch-cheer-bot/blob/master/logo.png?raw=true' alt='Twitch Cheer Bot' title='Twitch Cheer Bot' height='50px'/> </a></div>

# Media

![running](https://github.com/darideveloper/twitch-users-checker/blob/master/screenshots/running.png?raw=true)

# Details

The script get as input a csv file with a list of twitch account. 
Using selenium, it check account by account in order to detect if the accounts are are active or not. 
The final result its saved in separated files

## Sample output data

### users_active.csv
| User | Status |
| ----------- | ----------- |
|lawlietjustice1|active|
|metarc92|active|
|kathysk7|active|


### users_inactive.csv
| User | Status | Details |
| ----------- | ----------- | ----------- |
|pedrtioasj|active|This channel is currently unavailable due to a violation of Twitch's Community Guidelines or Terms of Service.|
|darideveloper|active|This channel is currently unavailable due to a violation of Twitch's Community Guidelines or Terms of Service.|

# Install

## Third party modules

Install all modules from pip: 

``` bash
$ pip install -r requirements.txt
```

## Programs

To run the project, the following software must be installed:: 

* [Google Chrome](https://www.google.com/intl/es/chrome) last version
* Python >= 3.10

# Settings

## Enviroment variables

In this file (*.env*), are the main options and settings of the project.

1. Create a **.env** file, and place the following content

```bash
WAIT_SEC = 120
HEADLESS = True
```

### WAIT_SEC

Number of seconds between each check

### HEADLESS

Hide (True) or show (False) the google chrome window.

*Note: you can see as reference the **sample.env** file*

## Users

You should create a **users.csv** with the twitch users to check.

Sample:
```
pedrtioasj
lawlietjustice1
metarc92
kathysk7
darideveloper
```

*Note: you can see as reference the **sample.users.csv** file*

# Roadmap

* [X] Get users from csv file
* [X] Check users accounts
* [X] Save output in separated files
* [X] Skip duplicates

