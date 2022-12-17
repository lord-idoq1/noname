from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 
    API_HASH = ""
    # the name to display in your alive message
    ALIVE_NAME = "vcky"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgresql://wysyuysj:VvaFHwihd0jBbSpq66bRE0cOuHXICczy@tiny.db.elephantsql.com/wysyuysj"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = ""
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = ""
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = 
    # command handler
    COMMAND_HAND_LER = "-"
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "-"
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"
