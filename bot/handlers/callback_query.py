from aiogram import Router, Dispatcher, F
from aiogram.types import CallbackQuery, FSInputFile

from bot.template import inlinekeyboard, message_template

router = Router()

@router.callback_query(F.data.in_(["faq"]))
async def faq_callback(callback_query: CallbackQuery):
    await callback_query.answer("Часто задаваемые вопросы")
    await callback_query.message.answer(
        "Выберите вопрос, на который вы хотите получить ответ:",
        reply_markup=inlinekeyboard.keyboatd_faq
    )

@router.callback_query(F.data.in_(["back_to_start"]))
async def back_to_start_callback(callback_query: CallbackQuery):
    await callback_query.answer("")
    await callback_query.message.delete()
    photo_path = FSInputFile('public/1080x1080-1.jpg')
    await callback_query.message.answer_photo(photo=photo_path)
    await callback_query.message.answer(
        message_template.start_message,
        parse_mode='html',
        reply_markup=inlinekeyboard.keyboard_start
    )

@router.callback_query(F.data.in_(["faq_1", "faq_2", "faq_3", "faq_4", "faq_5", "faq_6", "faq_7", "faq_8", "faq_9", "faq_10", "faq_11", "faq_12", "faq_13", "faq_14"]))
async def faq_answer_callback(callback_query: CallbackQuery):
    faq_answers = {
        "faq_1": "Стать курьером-партнером Яндекс Еды можно, если вам есть 18 лет.",
        "faq_2": "Вы можете выполнять заказы не только пешком. Если вы хорошо управляетесь с велосипедом, самокатом, роликами и другими средствами передвижения — используйте их. Так выполнять доставки можно быстрее, а значит, и доход будет выше. Главное, будьте аккуратны и помните о правилах дорожного движения. На покупку и ремонт велосипедов и самокатов можно будет получить скидки до 20% у партнёров.",
        "faq_3": "Да, вы сами выбираете доступное время и районы. Если вы сотрудничаете с курьерской службой, в выборе могут быть небольшие ограничения.",
        "faq_4": "По данным сервиса, в обычный день за час в среднем может быть до двух заказов от пользователей.",
        "faq_5": "Да, обычно курьеры могут совмещать основную работу с подработкой у партнёра сервиса Яндекс.Еда",
        "faq_6": "Курьерская служба предоставит вам жёлтую одежду с логотипом сервиса после начала сотрудничества. Не забывайте надевать её на заказы.",
        "faq_7": message_template.docks_message,
        "faq_8": "На заказах могут встречаться самые разные рестораны, доступные в выбранном вами районе.",
        "faq_9": "Да, можно. Для прямых курьеров-партнёров в статусе самозанятых предусмотрены ежедневные выплаты.**",
        "faq_10": "Да — страховое возмещение можно получить в случае серьёзных травм, которые случились с вами во время слота. За информацией нужно будет обратиться в службу поддержки.",
        "faq_11": "Теперь можно! Чтобы стать курьером-партнёром Яндекс Еды и доставлять со смартфоном на iOS, нужно скачать приложение Яндекс Про из App Store и следовать инструкции.",
        "faq_12": "Это статус физического лица который платит специальный налог на профессиональный доход (НПД). При этом не нужно дополнительно отчислять подоходный налог или налог на прибыль. Статус открывается онлайн в приложении Мой Налог. Прекратить деятельность cамозанятого можно в любой момент, через приложение. За открытие и закрытие статуса не взымаются никакие налоги и комиссии",
        "faq_13": "Подать заявку и пройти тестирование ещё раз можно сразу, если же вам отказали в офисе партнера, то новую заявку можно будет подать через месяц.",
        "faq_14": "Обычно определённая сумма на проезд входит в фиксированную сумму дохода."
    }
    
    answer = faq_answers.get(callback_query.data)
    if answer:
        await callback_query.message.delete()
        await callback_query.answer("")
        await callback_query.message.answer(answer, parse_mode='html', reply_markup=inlinekeyboard.keyboard_faq_view)
    else:
        await callback_query.answer("Ответ на этот вопрос не найден.", show_alert=True)

def setup(*, dispatcher: Dispatcher):
    dispatcher.include_router(router)