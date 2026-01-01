from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from botlogic import views
from botlogic.utils import kb
from botlogic.utils.statesform import SendFileSteps
from aiogram.types import InputFile, FSInputFile


async def start_menu(message: Message, state: FSMContext):
    await message.answer(views.start_text(), reply_markup=kb.start_kb, parse_mode="HTML")
    await state.set_state(SendFileSteps.mainmenu)


async def contact_menu(message: Message, state: FSMContext):
    await state.set_state(SendFileSteps.contactmenu)
    await message.answer(views.contacts(), reply_markup=kb.contact_keyboard.as_markup())



async def next_menu(message: Message, state: FSMContext):
    await message.answer(views.pay(), reply_markup=kb.back_kb)
    await state.set_state(SendFileSteps.pays)

async def send_fail(x: CallbackQuery, state: FSMContext):
    await state.set_state(SendFileSteps.offer)
    doc = FSInputFile(path="oferta.docx")
    await x.message.answer_document(doc)
    await x.message.answer(views.file_text(), reply_markup=kb.back_kb)
