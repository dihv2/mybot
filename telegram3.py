
import telebot

bot = telebot.TeleBot('')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
  user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
  user_markup.row('ТИ КТО?', '/help', 'Надо', 'Когда выйдет 2.2?')
  user_markup.row('Привет', 'На чём сделан этот бот?', 'Как дела?')
  user_markup.row('Что делаешь?', 'Отправь контакты создателя', 'Зачем создан этот бот?', 'Напомни мне об этом')
  
  if message.text == "ТИ КТО?":
      bot.send_message(message.from_user.id, "Я, Я, Кто мы? МЫ СМЕШАРИКИ!")
  elif message.text == "/help":
      bot.send_message(message.from_user.id, "Все команды бота: \nТИ КТО?\n/help\nПривет\nНа чём сделан этот бот?\nНадо\nКак дела?\nКогда выйдет 2.2?\nЧто делаешь?\nОтправь контакты создателя\nЗачем создан этот бот?\nНапомни мне об этом ")
  elif message.text == "Привет":
      bot.send_message(message.from_user.id, "Привет")
  elif message.text == "На чём сделан этот бот?":
      bot.send_message(message.from_user.id, "А тие зачем?")
  elif message.text == "Надо":
      bot.send_message(message.from_user.id, "Аааа ок на python")
  elif message.text == "Как дела?":
      bot.send_message(message.from_user.id, "Нормально, нормально нереально")
  elif message.text == "/start":
      bot.send_message(message.from_user.id, "Не добро пожаловать!", reply_markup=user_markup)
  elif message.text == "Когда выйдет 2.2?":
      bot.send_message(message.from_user.id, "НИ-КО-ГДА")
  elif message.text == "Отправь контакты создателя":
      bot.send_message(message.from_user.id, "НЕненет ладно на: \nYouTube: https://www.youtube.com/channel/UCqUTBnlmoDcB4Wfdz7nkPDA\nVK: https://vk.com/dih228")
  elif message.text == "Зачем создан этот бот?":
      bot.send_message(message.from_user.id, "Дань! Даань! Зачем я создан? Незнаю!")
  elif message.text == "Что делаешь?":
      bot.send_message(message.from_user.id, "С ТОБОЙ РАЗГОВАРИВАЮ")
  elif message.text == "Напомни мне об этом":
      bot.send_message(message.from_user.id, "Ок. Скажи Okay Google! И скажи создай напоминание. А дальше следуй инструкции.")
  else:
      bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
     
bot.polling(none_stop=True, interval=0)   