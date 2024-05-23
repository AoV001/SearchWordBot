from aiogram import F, Router, types
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery

import spacy
import re

from app.config import client

import app.keyboards as kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hello!', reply_markup=kb.main)
    await message.reply('What do you want to know?')


@router.message(F.text == 'Help')
async def cmd_help(message: Message):
    await message.answer('What is wrong?', reply_markup=kb.helping)


@router.message(F.text == 'Contacts')
async def cmd_contacts(message: Message):
    await message.answer(
        'My Authors name is Antonia Vlasova, you can contact her by the tel.: 017645995926')


@router.message(F.text == 'About me')
async def cmd_help(message: Message):
    await message.answer(
        'Hi! Send me a word or a text, and I will provide definitions of any words I recognize.')


@router.callback_query(F.data == 'question')
async def cmd_quest(callback: CallbackQuery):
    await callback.message.answer(
        'You can write whatever you want, I will find some definitions in your massage and tell you what it means')


@router.callback_query(F.data == 'mistake')
async def cmd_mistake(callback: CallbackQuery):
    await callback.message.answer(
        'Oh noway! We should fix that! Please press the "Contacts" Button and tell my Author about the mistake :) ')


nlp = spacy.load("en_core_web_sm")

# Pattern to check for alphabetic characters only
alpha_pattern = re.compile('[\\W_]+')


@router.message()
async def handle_message(message: types.Message):

    text = message.text
    doc = nlp(text)

    for token in doc:

        # Exclude symbols and convert words to lowercase
        lemma = token.lemma_.lower()

        # Check if the obtained word is not empty and does not contain digits
        if lemma and not alpha_pattern.match(lemma) and not any(char.isdigit() for char in lemma):

            if lemma in ['be', 'are', 'is']:

                await message.answer('The form of "to be" Verb')

            else:

                try:

                    # Fetch the word definition from the API
                    word_definition = await client.fetch_word(lemma)

                    # Get the first meaning
                    first_meaning = word_definition.meanings[0]

                    # Get the definition
                    definition = first_meaning.definitions[0].definition

                    # Send the word and its definition as a message
                    await message.answer(f"{token.text}:\n{definition}")

                except Exception as e:

                    await message.answer(f"Error with the word: '{token.text}': {e}")
