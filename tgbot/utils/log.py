import logging
from pathlib import Path

path = Path(__file__).resolve().parent.parent.parent.joinpath('logs')


def aiogram_logging(level=logging.INFO):
    log = logging.getLogger('aiogram')
    log.setLevel(level)
    FH = logging.FileHandler(path.joinpath('aiogram.log'), mode='a+', encoding='utf-8')
    logtype = logging.Formatter(u'%(asctime)-2s [%(levelname)s]  -  %(message)s')
    FH.setFormatter(logtype)
    log.addHandler(FH)


def configure_logs():
    aiogram_logging()
