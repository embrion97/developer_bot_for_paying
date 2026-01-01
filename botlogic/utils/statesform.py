from aiogram.fsm.state import StatesGroup, State


class SendFileSteps(StatesGroup):
    mainmenu = State()
    contactmenu = State()
    offer = State()
    pays = State()