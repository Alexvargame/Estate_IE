from .db import BotDBClass
from pathlib import Path


BotDB = BotDBClass(Path(__file__).resolve().parent.parent/'estate_agency/db_base.sqlite3')
print('BotDB', BotDB)
print('BotDBFILRE', BotDB.file)
# print('PATH', Path(__file__).resolve())
# print('PATH', Path(__file__).resolve().parent.parent.parent/'db_base.sqlite3')
#
# print('PATH', Path(__file__).resolve().parent.parent/'db_base.sqlite3')
# print('PATH', Path(__file__).resolve().parent/'db_base.sqlite3')
# print('PATH', Path(__file__).resolve().parent.parent/'estate_agency/estate_agency_apps/db_base.sqlite3')