from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import requests as rq


def valyuta_info(text):
    link = "https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
    data  = rq.get(link).json()
    text, amout = text.lower().split()
    for i in data:
        if i['Ccy'].lower() == text or i['CcyNm_RU'].lower() == text or i['CcyNm_UZ'].lower() == text or i['CcyNm_EN'].lower() == text:
            qiymat = int(amout) * float(i['Rate'])
            javob = f"1 {i['CcyNm_UZ']} hozirda {i['Rate']} so'mga teng."
            javob += f"\n{amout} {i['CcyNm_UZ']} {qiymat} so'mga teng bo'ladi."
            return javob
    return "Valyuta topilmadi"




async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Salom {update.effective_user.first_name}, Sizga qanday yordam bera olaman?')


async def func(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user.first_name
    message = update.message.text
    print(f"{user}dan [{message}] xabari keldi...")
    javob = valyuta_info(update.message.text)
    await update.message.reply_text(javob)



token = "8827661928:AAE10hpJuAibxmpliZyawRx-HbCzLWVu7V0"
app = ApplicationBuilder().token(token).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(filters.Text(), func))

print('Bot ishga tushdi...')

app.run_polling()