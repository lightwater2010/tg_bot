from aiogram import types,F, Router
from inline.keyboards import inline, kb, inline_like_dislike, create_kb_with_languages, inline_bot_skill, inline_languages
from aiogram.filters import Command, CommandStart

router = Router()

@router.message(CommandStart())
async def start_command(message: types.Message):
    await message.answer("Привет это бот по заданию по inline клавиатурам", reply_markup=kb)

@router.message(Command('help'))
async def help_command(message: types.Message):
    await message.answer("/start - начало бота\n/help - список команд\n/links - классные urls\n/vote - голосование картинки")

@router.message(Command('links'))
async def links_command(message: types.Message):
    await message.answer("YouTube и Stepik", reply_markup=inline)

@router.message(Command('vote'))
async def vote_command(message: types.Message):
    await message.answer_photo("https://overclockers.ru/st/legacy/blog/395361/197455_O.jpg", reply_markup=inline_like_dislike, caption="Крутое фото")

@router.callback_query(F.data == 'like')
async def callback_inline_like(callback: types.CallbackQuery):
    await callback.answer("Тебе понравилась это картинка", show_alert=True)

@router.callback_query(F.data == 'dislike')
async def callback_inline_dislike(callback: types.CallbackQuery):
    await callback.answer("Тебе не понравилась это фотка...", show_alert=True)

@router.message(F.text == "Все возможности бота")
async def bot_skills(message: types.Message):
    await message.answer("Пока у бота есть это", reply_markup=inline_bot_skill)

@router.callback_query(F.data == "languages")
async def callback_inline_languages(callback: types.CallbackQuery):
    await callback.answer("Ты выбрал языки программирования", show_alert=True)
    await callback.message.edit_text("Выбери какой нибудь из них и я расскажу тебе про него", reply_markup=await create_kb_with_languages())

@router.callback_query()
async def callback_language(callback: types.CallbackQuery):
    keys = [key for key in inline_languages.keys()]
    if callback.data in keys:
        await callback.answer(inline_languages[callback.data],show_alert=True)

@router.message(F.sticker)
async def send_sticker_id(message: types.Message):
    await message.reply(message.sticker.file_id)