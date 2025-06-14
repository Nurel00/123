from aiogram import F, types,Router
from aiogram.filters import Command
from keyboard.inline import about_us_inline_keyboard,start_inline_keyboard,return_main_keyboard

start_functions_router = Router()

welcome_message = (
    """
    🌟 САЛАМСАТСЫЗБЫ, УРМАТТУУ АТА-ЭНЕ! 👨‍👩‍👧‍👦

Кош келиңиздер "📚 Окурмэн Кидс" Telegram ботубузга — бул бот сиздин балаңыз үчүн коопсуз, билимдүү жана кызыктуу ааламга эшик ачат! 🚪✨

👶 Бул жерде балдар:
🎉 Кызыктуу жомокторду угушат
🎲 Интерактивдүү оюн-зоокторду ойношот
🧠 Акыл-эс өнүктүрүүчү тапшырмалар менен машыгышат
📖 Окуу сүйүүсүн арттырышат

🔐 Биз үчүн коопсуздук — биринчи орунда!
🛡️ Бул бот:

Жарнама көрсөтпөйт ❌

Жеке маалымат чогултпайт 📵

Жөнөкөй жана коопсуз колдонула тургандай иштелип чыккан 👌

❤️ Сиздин балаңыздын өнүгүүсү — биздин башкы максат!
Эгерде суроолоруңуз, сунуштарыңыз болсо — биз дайыма байланыштабыз:

📬 Байланыш үчүн: @your_admin_username

🦋 "Окурмэн Кидс" — билим дүйнөсүнө болгон сүйүүнү бала кезден баштайт! 🌈
    
    """
    
)
@start_functions_router.message(Command("start"))
async def start(message: types.Message):
    await message.answer_photo(photo=types.FSInputFile("media/image.png"), caption=welcome_message, parse_mode="Markdown",
                               reply_markup=start_inline_keyboard())
   
@start_functions_router.callback_query(F.data == "start")
async def start_callback(query: types.CallbackQuery):
    await query.message.edit_caption(
                               caption=about_us_text,
                               parse_mode="Markdown",
                               reply_markup=start_inline_keyboard()) 
    
about_us_text = (
    """🚀 OKURMEN KIDS — жаңы муундагы IT-академия! 🌟

Биз жөн гана үйрөтпөстөн, балдарды технологияны сүйүүгө шыктандырабыз! 💡✨

💻 Бизде үйрөнөсүз:

• Frontend & Backend — сайттар жана колдонмолор
• IT үчүн англис тили — заманбап сөздөрдү өздөштүрүү
• AEM методикасы — логика, чыгармачылык жана ишеним

🎮 Сабактар жандуу жана кызыктуу:
✅ Kahoot менен темаларды бекемдөө
✅ Monkeytype менен ылдамдыкты арттыруу
✅ UNO жана башка оюндар менен эс алуу

🎓 Онлайн жана оффлайн форматта, индивидуалдуу мамиле менен.

👇 Толук маалымат алуу же пробный сабакка жазылуу үчүн төмөнкү баскычтарды басыңыз! 
"""
)

@start_functions_router.message(Command("about_us"))
async def about_us(message: types.Message):
    await message.answer_photo(photo=types.FSInputFile("media/image.png"),
                               caption=about_us_text,
                               parse_mode="Markdown",
                               reply_markup=about_us_inline_keyboard())
    
@start_functions_router.callback_query(F.data == "about_us")
async def about_us_callback(query: types.CallbackQuery):
    await query.message.edit_caption(
                               caption=about_us_text,
                               parse_mode="Markdown",
                               reply_markup=about_us_inline_keyboard())
groups = (
    """📅 OKURMEN KIDS — ЖАКЫНКЫ САБАКТАРДЫН ГРАФИГИ

📍 Оффлайн жана онлайн форматтарда
📍 Бардык сабактар алдын ала каттоо менен гана

👶 6–9 жаштагы балдар үчүн:

🗓️ Дүйшөмбү – Шаршемби – Жума
🕒 Саат 15:00 – 16:30
📚 “ITге тааныштыруу” жана “Логикалык ой жүгүртүү”

🧒 10–13 жаштагы балдар үчүн:

🗓️ Шейшемби – Бейшемби
🕒 Саат 16:30 – 18:00
💻 “Frontend негиздери” жана “Англис тили (IT үчүн)”

🧑‍💻 14–17 жаштагы өспүрүмдөр үчүн:

🗓️ Ишемби – Жекшемби
🕒 Саат 13:00 – 15:00
🌐 “Backend негиздери”, “AEM логикасы” жана “Практикалык долбоорлор”

🎓 Кошумча:

🧩 Kahoot викториналары — ар жума сайын, жума күнү саат 18:30
🎲 UNO жана оюн-зоок убактысы — ишемби күндөрү, саат 15:30дан кийин

📌 Так дарек, сабак форматы жана орун боюнча маалымат алуу үчүн админ менен байланышкыла:
📲 @your_admin_username"""
)


@start_functions_router.callback_query(F.data == "courses")
async def courses_callback(query: types.CallbackQuery):
    await query.message.edit_caption(caption=groups,
                                     parse_mode="html",
                                     reply_markup=return_main_keyboard())
    
Okurmen_kids  = (
    """<b>🎓 Окурмен Kids — будущее начинается с детства!</b>

<b>Окурмен Kids</b> — IT-академия в Бишкеке для детей 9–15 лет. Обучаем программированию, цифровой грамотности, логике и английскому языку.

<b>Что мы даём детям:</b>
💻 Современные IT-курсы  
🧠 Soft skills и развитие личности  
🌐 Английский для цифрового мира  
📜 Сертификаты после каждого курса  
📚 Обучение на кыргызском по методике <b>Гапыра Мадаминова (AEM)</b>

<b>Филиалы в Бишкеке:</b>  
🏫 Табышалиева — <b>Окурмен Kids</b>  
🏫 Турусбекова — <b>Окурмэн</b>

⏰ Занятия с 09:00 до 19:00  
🎉 Уютная атмосфера и забота о каждом ребёнке  
📸 Instagram — фото, отзывы, вдохновение

<b>✨ Запишитесь сегодня и подарите ребёнку уверенное будущее!</b>

"""
)


@start_functions_router.callback_query(F.data == "Okurmen_kids")
async def Okurmen_kids_callback(query: types.CallbackQuery):
    await query.message.edit_caption(caption=Okurmen_kids ,
                                     parse_mode="html",
                                     reply_markup=return_main_keyboard())
    
    
