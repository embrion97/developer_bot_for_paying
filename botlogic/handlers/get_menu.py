from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from botlogic import views
from botlogic.utils import kb
from botlogic.utils.statesform import SendFileSteps
from aiogram.types import InputFile, FSInputFile


async def start_menu(message: Message, state: FSMContext):
    await message.answer(views.start_text(), reply_markup=kb.start_kb, parse_mode="HTML")
    await state.set_state(SendFileSteps.mainmenu)

async def back_inline(x: CallbackQuery, state: FSMContext):
    await x.message.answer(views.vazno(), reply_markup=kb.contact_keyboard, parse_mode="HTML")
    await state.set_state(SendFileSteps.contactmenu)


async def contact_menu(message: Message, state: FSMContext):
    await state.set_state(SendFileSteps.contactmenu)
    await message.answer(views.vazno(), reply_markup=kb.contact_keyboard, parse_mode="HTML")

async def go_to_contacty(message: Message, state: FSMContext):
    await state.set_state(SendFileSteps.contactmenu)
    await message.answer(views.contact(), reply_markup=kb.inline_back.as_markup(), parse_mode="HTML")


async def go_to_refund(message: Message, state: FSMContext):
    await state.set_state(SendFileSteps.contactmenu)
    await message.answer(views.refund(), reply_markup=kb.inline_back.as_markup(), parse_mode="HTML")


async def next_menu(message: Message, state: FSMContext):
    await message.answer(views.pay(), reply_markup=kb.back_kb, parse_mode="HTML")
    await state.set_state(SendFileSteps.pays)

async def send_fail(x: Message, state: FSMContext):
    await state.set_state(SendFileSteps.contactmenu)
    doc = FSInputFile(path="oferta.docx")
    await x.answer_document(doc)
    await x.answer(views.file_text(), reply_markup=kb.inline_back.as_markup(), parse_mode="HTML")
