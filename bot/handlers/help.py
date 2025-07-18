# bot/handlers/help.py
from aiogram import Router, F
from aiogram.types import Message
from bot.keyboards import get_dialog_kb

help_router = Router()

@help_router.message(F.text == "❓ Помощь по функциям")
async def show_function_help(message: Message):
    """Показывает справку по доступным функциям диалога"""
    help_text = """
    Доступные команды в диалоге:
    
    🔄 Новый вопрос - начать новый диалог с нейросетью
    ❌ Завершить диалог - вернуться в главное меню
    ❓ Помощь по функциям - эта справка
    
    В режиме диалога вы можете:
    • Задавать уточняющие вопросы по предыдущему запросу
    • Получать дополнительную информацию
    • Уточнять детали ответа
    
    Для нового поиска информации используйте "🔄 Новый вопрос"
    """
    await message.answer(help_text, reply_markup=get_dialog_kb())