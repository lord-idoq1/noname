from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 14730975
    API_HASH = "f342c8ec119f37dd8b4dffc8dfc0ad55"
    # the name to display in your alive message
    ALIVE_NAME = "vcky"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "mongodb+srv://userammnadia:redminote8.@cluster0.jthtk.mongodb.net/userammnadia?retryWrites=true&w=majority"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOIIBuyl7IBEoIqSsN2VdyGgt6IjzgRL51B4KfWkXBMEAv5_CO_98OpdeHUqpHrWgLLT65JVgL4FBbrSzoU2GitiJkH0mqXivaRw3nQzL3wZxUYY_rfNFBG6aKscrf-2ccJqJ1yE_uv6vv3ZuIBxGB8EVVnqCSJDDDJIcZd2mrfS7iBE5UzYsoiq2phQRZtPjw6dhPSiimN88jglHEK1pKf2SohuQVhOi3eivcFT8p8SoknOXphB1Xa0sbE1H4FlF_-tJ89vm4m7vbZOTYwAYWbKXEmbZwI8VoSEeyEY_WiejMuDg6QnBjUGe14t2NKIgRQzOgitiE6nYqJ9C8pxek03gTj8="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5904398932:AAFsqOGgm8BY857mDCsyi5l0Es3Or0ZWfTM"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001732208760
    # command handler
    COMMAND_HAND_LER = "-"
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "-"
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"
