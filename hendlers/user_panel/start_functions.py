from aiogram import F, types,Router
from aiogram.filters import Command
start_functions_router = Router()

welcome_message = (
    """
    кош келиниз
    """
    
)
@start_functions_router.message(Command("start"))
async def start(message: types.Message):
    await message.answer_photo(photo=types.FSInputFile("media/image.png"), caption=welcome_message)