
from pathlib import Path
from environs import Env

BASE_DIR = Path(__name__).resolve().parent

# config env file
ENV_FILE = BASE_DIR / '.env'

# logging config file
LOGGING_CONF_FILE = BASE_DIR / 'logging.conf.json'

# config env file
ENV_FILE = BASE_DIR / '.env'

_env = Env()
_env.read_env(str(ENV_FILE))

ADMIN_ID = _env.list('ADMIN_ID')
TOKEN = _env.list('TOKEN')
partner_url = _env.str('PARTNER_URL', default='https://reg.eda.yandex.ru/?advertisement_campaign=forms_for_agents&user_invite_code=6aac4646df6a42eb88fba73bfecea581&utm_content=tgbot')
PARSE_MODE = 'html'