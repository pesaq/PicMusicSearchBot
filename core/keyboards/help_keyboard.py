from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

help_board = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(
            text='Помощь',
            callback_data='help_callback'
        )
    ]
])