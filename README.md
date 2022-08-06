This is a fork of https://github.com/zacc/ssi-bot, finetuned with data scraped from the subreddit r/dreamwastaken2. The repository contains a pretrained model. For an example of this repository in action, see this post: https://www.reddit.com/r/DreamWasTaken2/comments/wgvs2w/hi_im_a_robot_trained_using_gpt2_and_data_scraped/. The reposity contains a finetuned model, so user only need to run run.py (and install the required packages and set up the bot account) to post on Reddit. To just generate text, run test_model.py.

-----------------------------

Minimum Python requirement: Python 3.7

Full support/developed on Ubuntu-flavor Linux.

Works on Windows with Python 3.8+ (support for SQLite3's JSON field type is required)

### Glossary / PyPI packages used
`simpletransformers` An open source Python package made by Thilina Rajapakse. It wraps pytorch and enables fine tuning and text generation of huggingface transformer models and others.

Documentation: https://simpletransformers.ai/docs/installation/

`peewee` A database ORM that creates Python access to the database. SQL functions and queries can be completed using Python functions. It's like SQLAlchemy but much much easier to use!

Documentation: http://docs.peewee-orm.com/en/latest/index.html

`praw` A Python package to interface with Reddit's API. It streamlines a lot of the hard work of interacting with the API.

Documentation: https://praw.readthedocs.io/en/latest/

`detoxify` A python package wrapper around a Bert model that can classify the toxicity of comments.

Documentation: https://pypi.org/project/detoxify/

## RUNNING THE BOT ON REDDIT

Although the bot is finetuned on a GPU, a CPU is sufficient for using the model to generate text.

Any modern CPU can be used; having around 4Gb of RAM or more is the main requirement.

In order to run on SubSimGPT2Interactive, we require the bot to be running 24/7.
This means putting it on a VPS/server, or an old laptop in your house could suffice too.


### Setup your Python environment
1. Install packages with `pip install -Ur requirements.txt` (Advised: Use virtualenv)
To keep a terminal window open on Ubuntu Server, use an application
called `tmux`

ssi-bot Config file
1. Copy and rename ssi-bot_template.ini to ssi-bot.ini
1. Where you have section [bot_1_username], change the section to your bot's username.
1. Populate bot's section with filepath to model and negative keywords you want to use. The program already includes some basic negative keywords but we suggest you add more.

Create the bot account, setup reddit app and associated PRAW Config file
1. Create the bot account on reddit
1. Logged in as the bot, navigate to https://www.reddit.com/prefs/apps
1. Click "are you a developer? Create an app.." and complete the flow
1. Copy praw_template.ini to praw.ini
1. Just as you did with ssi-bot.ini, rename the [bot_1_username] section to your bot's username. The sections should match, between ssi-bot.ini and praw.ini.
1. Set all the data in praw.ini as from step 3 above

Running the bot
1. The bot is run by typing `python run.py`
