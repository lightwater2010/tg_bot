from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

kb = ReplyKeyboardMarkup(keyboard=[[
    KeyboardButton(text="/links"),KeyboardButton(text="/vote")
], [KeyboardButton(text="Все возможности бота")]], resize_keyboard=True)

inline = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="YouTube", url="https://www.youtube.com/"),
    InlineKeyboardButton(text="Stepik", url="https://stepik.org/learn")
]])

inline_like_dislike = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="👍🏿", callback_data="like"),
    InlineKeyboardButton(text="👎🏿", callback_data="dislike")
]])

inline_bot_skill = InlineKeyboardMarkup(inline_keyboard=[[
    InlineKeyboardButton(text="Языки программирования", callback_data="languages")
]])

inline_languages = {
    "Python":"Хорош в бэкенде, вебе и в data science", "JavaScript":"Хорош в вебе",
    "Rust":"Хорош в backend", "Go":"Новый язык, хорош в бэкенде веба", "C++":"Хорош в приложениях и бэкенде",
    "PHP":"Более 75% сайтов всего мира сделаны на нём, вот теперь и думайте"
}

async def create_kb_with_languages():
    inline_kb = InlineKeyboardBuilder()
    for language in inline_languages.keys():
        inline_kb.add(InlineKeyboardButton(text=f'{language}', callback_data=language))
    return inline_kb.adjust(2).as_markup()