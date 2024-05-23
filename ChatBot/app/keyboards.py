from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Help')],
                                     [KeyboardButton(text='Contacts'),
                                     KeyboardButton(text='About me')]],
                           resize_keyboard=True,
                           input_field_placeholder='Choose an option')


helping = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='What should I write?',
                          callback_data='question')],
    [InlineKeyboardButton(text='I have found a mistake',
                          callback_data='mistake')]])