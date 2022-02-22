from likelion10th.settings.base import *
from decouple import config

DEBUG = False
# 추후 ip 추가
ALLOWED_HOSTS = [ config("ALLOWED_HOST") ]
