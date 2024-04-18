import asyncio

from aiogram import types, Bot, Dispatcher, F
from inline.keyboards import inline, kb, inline_like_dislike, create_kb_with_languages, inline_bot_skill, inline_languages
from aiogram.filters import Command, CommandStart
from config import TOKEN_BOT_WITH_KEYBOARD

bot = Bot(TOKEN_BOT_WITH_KEYBOARD)
disp = Dispatcher()



async def start_app(_):
    print("Бот был успешно запущен!")

@disp.message(CommandStart())
async def start_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет это бот по заданию по inline клавиатурам", reply_markup=kb)

@disp.message(Command('help'))
async def help_command(message: types.Message):
    await bot.send_message(message.from_user.id, "/start - начало бота\n/help - список команд\n/links - классные urls\n/vote - голосование картинки")

@disp.message(Command('links'))
async def links_command(message: types.Message):
    await bot.send_message(message.chat.id, "YouTube и Stepik", reply_markup=inline)

@disp.message(Command('vote'))
async def vote_command(message: types.Message):
    await bot.send_photo(message.from_user.id, "https://overclockers.ru/st/legacy/blog/395361/197455_O.jpg", reply_markup=inline_like_dislike)

@disp.callback_query(F.data == 'like')
async def callback_inline_like(callback: types.CallbackQuery):
    await callback.answer("Тебе понравилась это картинка", show_alert=True)

@disp.callback_query(F.data == 'dislike')
async def callback_inline_dislike(callback: types.CallbackQuery):
    await callback.answer("Тебе не понравилась это фотка...", show_alert=True)

@disp.message(F.text == "Все возможности бота")
async def bot_skills(message: types.Message):
    await bot.send_message(message.from_user.id, "Пока у бота есть это", reply_markup=inline_bot_skill)

@disp.callback_query(F.data == "languages")
async def callback_inline_languages(callback: types.CallbackQuery):
    await callback.answer("Ты выбрал языки программирования", show_alert=True)
    await callback.message.edit_text("Выбери какой нибудь из них и я расскажу тебе про него", reply_markup=await create_kb_with_languages())

@disp.callback_query()
async def callback_language(callback: types.CallbackQuery):
    keys = [key for key in inline_languages.keys()]
    if callback.data in keys:
        await callback.answer(inline_languages[callback.data],show_alert=True)

@disp.message(F.sticker)
async def send_sticker_id(message: types.Message):
    await message.reply(message.sticker.file_id)
async def main():
    await disp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())