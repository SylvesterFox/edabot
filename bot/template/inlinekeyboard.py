from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from settings import config

keyboard_start = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📑 Перейти к анкете", url=config.partner_url),  
        ],
        [
             InlineKeyboardButton(text="❓ Часто задаваемые вопросы", callback_data="faq")
        ]
    ]
)

keyboatd_faq = InlineKeyboardMarkup(
    inline_keyboard=[
         [
            InlineKeyboardButton(text="Какие документы нужны для оформления?", callback_data="faq_7")
        ],
        [
            InlineKeyboardButton(text="Можно мне стать курьером-партнером, если мне ещё нет 18 лет?", callback_data="faq_1")
        ],
        [
            InlineKeyboardButton(text="Можно доставлять заказы на велосипеде, самокате или только пешком?", callback_data="faq_2")
        ],
        [
            InlineKeyboardButton(text="Можно ли выполнять заказы по выходным?", callback_data="faq_3")
        ],
        [
            InlineKeyboardButton(text="Сколько заказов выполняет курьер за час?", callback_data="faq_4")
        ],
        [
            InlineKeyboardButton(text="У меня есть основная работа, могу ли я выполнять заказы в свободное время?", callback_data="faq_5")
        ],
        [
            InlineKeyboardButton(text="Оплачивается ли курьерам проезд на общественном транспорте?", callback_data="faq_14")
        ],
        [
            InlineKeyboardButton(text="Если с первого раза не вышло стать курьером, когда можно снова подать заявку?", callback_data="faq_13")
        ],
         [
            InlineKeyboardButton(text="Выдают ли одежду с логотипом?", callback_data="faq_6")
        ],
         [
            InlineKeyboardButton(text="Из каких ресторанов будет доставка?", callback_data="faq_8")
        ],
         [
            InlineKeyboardButton(text="Можно ли получать оплату ежедневно?", callback_data="faq_9")
        ],
         [
            InlineKeyboardButton(text="Есть ли страхование во время заказов?", callback_data="faq_10")
        ],
         [
            InlineKeyboardButton(text="Можно выполнять доставки с телефоном на iOS? Или только со смартфоном на Android?", callback_data="faq_11")
        ],
         [
            InlineKeyboardButton(text="Что такое статус самозанятый?", callback_data="faq_12")
        ],
        [
            InlineKeyboardButton(text="◀ Назад", callback_data="back_to_start")
        ]
    ]
)
keyboard_faq_view = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📑 Перейти к анкете", url=config.partner_url),  
        ],
        [
             InlineKeyboardButton(text="❓ Часто задаваемые вопросы", callback_data="faq")
        ],
        [
            InlineKeyboardButton(text="◀ Назад", callback_data="back_to_start")
        ]
    ]
)