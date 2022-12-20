from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = "22617384"
    API_HASH = "1e73a59e5b4efa2c79ba97d0ebaff5ba"
    # the name to display in your alive message
    ALIVE_NAME = "ido"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://aofqbhhz:xFi8v8oyZ2Yq2uFwiJC4eISojh-t0hFh@mel.db.elephantsql.com/aofqbhhz"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1BVtsOKABu1eJDVdGv8cF4NKiXpPm75y3uU670cGCPlvGIrSpUrlD404ZhGYAEds6Y7_D9y7WGdBYA7eVrGDe0zSFpBQormAiBVL8BI-E2sSEz7urDFumEGxO-gUHu2jzrQsfmvPkHObcReHQEQ8sFmW1JbHPkK1O7TFAcwX79oaGrHWcLkUA6CbttbzjOOu6m5UE2_f2DvjXC8wnldh7Ww0CC9ZSiufE1JZhlFJyXqzUp3baCA0yw67OuFzcr0BGTJY1Bxxyyr7Uph6IXaCLNC6COzOsM7FH3j4CNlzmk7rHFEl0fdIeTrs68eAnlYEe6cKTQP9bMURBvwMxtrCDsGyfL2oD9DE="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5916472641:AAEzWGA22X-xjXQ0KB34jgqRfo6jbBq2K0M"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = "-1001891076909"
    # command handler
    COMMAND_HAND_LER = "-"
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "-"
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"
