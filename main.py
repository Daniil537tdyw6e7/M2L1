import telebot
    
    # Замени 'TOKEN' на токен твоего бота
    # Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши /help!")
    
@bot.message_handler(commands=['hello']) 
def send_bye(message):
    bot.reply_to(message, "Привет! Как дела?")
   
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
    
@bot.message_handler(commands=['help'])
def send_hello(message):
    bot.reply_to(message, "/hello-приветствие /bye-прощание    /help-все команды /channels-мои каналы /mems - мемы /eco - экология")

@bot.message_handler(commands=['mems'])
def send_hello(message):
    bot.reply_to(message, "какой какой темы мем вы хотите? маркейтинг /marketing котики(не те которые в траве лежат) /cat програмирование /programming без темы /mem")

@bot.message_handler(commands=['marketing'])
def send_hello(message):
    bot.reply_to(message, " может добавлю еще, а может и нет) пока этим пользуйтесь /mem8 /mem12  ")   

@bot.message_handler(commands=['cat'])
def send_hello(message):
    bot.reply_to(message, "пушистые комочки шерсти /mem9 /mem13")     

@bot.message_handler(commands=['programming'])
def send_hello(message):
    bot.reply_to(message, "ты вроде не прграмист, ну ладно /mem1 /mem2 /mem3 /mem10 /mem11")    

@bot.message_handler(commands=['mem'])
def send_hello(message):
    bot.reply_to(message, "просто мемы /mem14 /mem15")        
        
@bot.message_handler(commands=['mem1'])
def send_hello(message):
    with open("images/mem1.jpg", "rb") as f:
        bot.send_photo(message.chat.id, telebot.types.InputFile(f))

@bot.message_handler(commands=['mem3'])
def send_hello(message):
    with open("images/mem3.jpg", "rb") as f:
        bot.send_photo(message.chat.id, telebot.types.InputFile(f))

@bot.message_handler(commands=['mem2'])
def send_hello(message):
    with open("images/mem2.jpg", "rb") as f:
        bot.send_photo(message.chat.id, telebot.types.InputFile(f))   

@bot.message_handler(commands=['mem8'])
def send_hello(message):
    with open("images/mem8.jpg", "rb") as f:
        bot.send_photo(message.chat.id, telebot.types.InputFile(f))   

@bot.message_handler(commands=['mem9'])
def send_hello(message):
    with open("images/mem9.jpg", "rb") as f:
        bot.send_photo(message.chat.id, telebot.types.InputFile(f))     

@bot.message_handler(commands=['mem10'])
def send_hello(message):
    with open("images/mem10.jpg", "rb") as f:
        bot.send_photo(message.chat.id, telebot.types.InputFile(f)) 

@bot.message_handler(commands=['mem11'])
def send_hello(message):
    with open("images/mem11.jpg", "rb") as f:
        bot.send_photo(message.chat.id, telebot.types.InputFile(f))         

@bot.message_handler(commands=['mem12'])
def send_hello(message):
    with open("images/mem12.jpg", "rb") as f:
        bot.send_photo(message.chat.id, telebot.types.InputFile(f))  

@bot.message_handler(commands=['mem13'])
def send_hello(message):
    with open("images/mem13.jpg", "rb") as f:
        bot.send_photo(message.chat.id, telebot.types.InputFile(f))    

@bot.message_handler(commands=['mem14'])
def send_hello(message):
    with open("images/mem14.jpg", "rb") as f:
        bot.send_photo(message.chat.id, telebot.types.InputFile(f))  

@bot.message_handler(commands=['mem15'])
def send_hello(message):
    with open("images/mem15.jpg", "rb") as f:
        bot.send_photo(message.chat.id, telebot.types.InputFile(f))  

@bot.message_handler(commands=['mem7'])
def send_hello(message):
    with open("images/mem7.jpg", "rb") as f:
        bot.send_photo(message.chat.id, telebot.types.InputFile(f))

@bot.message_handler(commands=['eco'])
def send_hello(message):
    bot.reply_to(message, "В чем именно твоя пробмена загрязнения. \
\nЗагрязнение почвы /soil, \
\nзагрязнение рек /river, \
\nзагрязнение воздуха /air"
        )    

@bot.message_handler(commands=['soil'])
def send_hello(message):
    with open("images/mem5.jpg", "rb") as f:
        bot.send_photo( 
            message.chat.id,
            telebot.types.InputFile(f),
            caption= "Загрязнение почв — вид антропогенной деградации почв, при которой содержание химических веществ в почвах, \
подверженных антропогенному воздействию, превышает природный региональный фоновый уровень их содержания в почвах. \
\n\nРешение проблемы загрязнения почвы. Утилизация отходов. Промышленные и бытовые отходы должны подвергаться правильной утилизации, \
чтобы предотвратить их накопление в почве. Мониторинг качества почвы. Регулярное наблюдение и мониторинг за состоянием почвы позволит выявлять и  \
предотвращать загрязнение на ранней стадии."
        )

@bot.message_handler(commands=['river'])
def send_hello(message):
    with open("images/mem6.jpg","rb") as f:
        bot.send_photo(
            message.chat.id, 
            telebot.types.InputFile(f),
            caption= "Загрязне́ние во́дных ресу́рсов — сброс или поступление иным способом загрязняющих веществ в водные объекты,\
а также образование в них вредных веществ, ухудшающих качество поверхностных и подземных вод, что негативно влияет на\
состояние дна и берегов водных объектов и ограничивает их использование.\
\n\nКак решать проблемы водных ресурсов? снижение выбросов предприятий путем использования современных безотходных технологий;обеспечение слаженной работы предприятия,\
исключение аварий на производствах;очистка выбрасываемых сточных вод и переработка отходов;сключение выброса отходов на бытовом уровне."
        )

@bot.message_handler(commands=['air'])
def send_hello(message):
    with open("images/mem4.jpg", "rb") as f:
        bot.send_photo(
            message.chat.id,
            telebot.types.InputFile(f),
            caption="Загрязнение воздуха ‒ это заражение окружающей среды внутри и вне помещений любым химическим, \
физическим веществом или биологическим агентом, которые изменяют природные характеристики атмосферы. \
\n\nУменьшить воздействие основных источников загрязнения атмосферного воздуха можно за счет мер политики \
и инвестиций, стимулирующих развитие более экологически чистых видов транспорта, повышение энергоэффективности зданий,\
электроэнергетики и промышленного производства, а также совершенствование систем удаления"
        )     

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()
