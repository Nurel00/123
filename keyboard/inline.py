from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton,ReplyKeyboardMarkup, KeyboardButton


def about_us_inline_keyboard():
    keyboard = InlineKeyboardBuilder()

    # Instagram
    keyboard.add(
        InlineKeyboardButton(
            text="📸 Instagram", 
            url="https://www.instagram.com/okurmen_kids"
        )
    )

    # WhatsApp (иконка менен)
    keyboard.add(
        InlineKeyboardButton(
            text="💬 WhatsApp",  # же 🟢 WhatsApp / 📲 WhatsApp
            url="https://api.whatsapp.com/send/?phone=996709677723&text&type=phone_number&app_absent=0"
        )
    )

    # Вебсайт
    keyboard.add(
        InlineKeyboardButton(
            text="🌐 WebSite", 
            url="http://okurmen.kids.tilda.ws/"
        )
    )

    # Консультация алуу
    keyboard.add(
        InlineKeyboardButton(
            text="📞 Получить консультацию", 
            callback_data="kk"
        )
    )
    
    keyboard.add(
        InlineKeyboardButton(
            text=" Назад", 
            callback_data="start"
        )
    )
    
    return keyboard.adjust(2,2).as_markup()

def start_inline_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(text="ℹ️ About Us", callback_data="about_us"),
        InlineKeyboardButton(text="🌐 Choose Language", callback_data="choose_language"),
        InlineKeyboardButton(text="👥 Группалар", callback_data="courses"),
        InlineKeyboardButton(text="📚 Okurmen_kids", callback_data="Okurmen_kids")
    )
    return keyboard.adjust(1).as_markup()



def return_main_keyboard():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(
        InlineKeyboardButton(
            text=" Назад", 
            callback_data="start"
        )
    )
    
    
    
    return keyboard.as_markup()