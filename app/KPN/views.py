from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from KPN.models import User
from KPN.serializers import UserSerializer
from currency.models import Currency


def index2(request):
    return render(request, 'index.html')


def register(request):
    username = request.GET['username']
    moneys = request.GET['moneys']
    for i in User.objects.all():
        if i.Telegram_hash == username:
            Usr = User.objects.get(Telegram_hash=username)
            Usr.KPСS = moneys
            Usr.save()
    if not User.objects.filter(Telegram_hash=username).exists():User.objects.create(Telegram_hash=username, KPСS=moneys,Rubles=0)

    return render(request, 'register.html')
class KPNview(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
def index(request):
    while True:
        import telebot
        import datetime
        from KPN.models import User
        bot = telebot.TeleBot('')
        @bot.message_handler(content_types=['text'])
        def get_text_messages(message):
            if message.text == "/start":
                bot.send_message(message.chat.id, "Вас приветствует интерфейс системы Kringe Production Network. В ней скоро будет можно много чего... Для регистрации в системе напишите /reg Для получения подробной информации напишите /help")
            elif message.text == "/help":
                me = bot.get_me()
                print(me.id)
                bot.send_message(message.chat.id, 'Чтобы зарегистрироваться в системе Kringe Production Network напишите /reg \nЧтобы посмотреть баланс напишите /wallet\nЧтобы перевести деньги на другой счёт напишите /transfer\nЧтобы посмотреть список торгуемых активов напишите /quotes\nПо всем вопросам писать @gshorti')
            elif message.text == "/wallet":
                buffer = ''
                buffer += 'Ваш баланс: \n'
                buffer += str(User.objects.get(Telegram_hash=message.from_user.username).Rubles)
                buffer += ' Рубли\n'
                buffer += str(User.objects.get(Telegram_hash=message.from_user.username).KPСS)
                buffer += '  KPC\n'
                bot.send_message(message.chat.id, buffer)
            elif message.text == "/reg":
                bot.send_message(message.chat.id, 'Поздравляю вы зарегистрировались в системе Kringe Production Network!')
                nowdate = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
                User.objects.create(Telegram_hash=message.from_user.username, Telegram_ID=message.from_user.id, Rubles=0, KPСS=0)
                with open('reg.log', 'a', encoding='utf-8') as f:
                    print('New registration:', nowdate, message.from_user.username, message.from_user.id, file=f)
            elif "пополнить" in message.text and 'qbIHg#kMrjhJw1q22NMp' in message.text:
                txt = message.text
                txt = txt.split(' ')
                user = txt[1]
                currency = txt[2]
                amount = txt[3]
                Usr = User.objects.get(Telegram_hash=user)
                if currency == 'RUB':
                    Usr.Rubles += int(amount)
                    Usr.save()
                elif currency == 'KPC':
                    Usr.KPСS += int(amount)
                    Usr.save()
                bot.send_message(Usr.Telegram_ID, f'Система внесла на ваш счёт {amount} {currency}')
            elif message.text == "/transfer":
                bot.send_message(message.chat.id, 'Напишите /transfer <Имя пользователя в телеграме без @> <RUB или KPC> <сумма>')
            elif '/transfer' in message.text:
                txt = message.text.split(' ')
                user = txt[1]
                currency = txt[2]
                amount = txt[3]
                Usr = User.objects.get(Telegram_hash=user)
                Usr2 = User.objects.get(Telegram_ID=message.from_user.id)
                if currency == 'RUB':
                    Usr.Rubles += int(amount)
                    Usr2.Rubles -= int(amount)
                    Usr.save()
                    Usr2.save()
                elif currency == 'KPC':
                    Usr.KPСS += int(amount)
                    Usr2.KPСS -= int(amount)
                    Usr2.save()
                    Usr.save()
                bot.send_message(Usr.Telegram_ID, f'Пользователь @{Usr2.Telegram_hash} перевёл вам {amount} {currency}')
                bot.send_message(message.chat.id, 'Перевод выполнен успешно')

            elif message.text == '/quotes':
                kpc = Currency.objects.get(Name='KPC')
                buffer = ''
                buffer += "На данный момент в системе торгуются следующие котировки:\n\n"
                buffer += ('KPC/RUB ' + str(kpc.Rubles))
                bot.send_message(message.chat.id, buffer)

            elif message.text == '/exchange':
                bot.send_message(message.chat.id, 'Напишите /exchange Валюта, которую вы обмениваете(RUB или KPC) сумма(В валюте, которую вы  обменивате) Валюта, на которую вы хотите обменять(RUB или KPC)')

            elif '/exchange' in message.text:
                Usr = User.objects.get(Telegram_hash=message.from_user.username)
                foreman = Usr.foreman
                print(dir(foreman))
                txt = message.text.split(' ')
                currency1 = txt[1]
                amount = txt[2]
                currency2 = txt[3]
                kpc = Currency.objects.get(Name='KPC')
                rub = Currency.objects.get(Name='RUB')
                if currency1 == 'RUB' and currency2 == 'KPC':
                    kpc.ratio += 1
                    rub.ratio -= 1
                    rub.save()
                    kpc.save()
                    Usr.Rubles -= int(amount)
                    Usr.KPСS += rub.KPNS * int(amount)
                    Usr.save()
                elif currency1 == 'KPC' and currency2 == 'RUB':
                    kpc.ratio -= 1
                    rub.ratio += 1
                    rub.save()
                    kpc.save()
                    Usr.KPСS -= int(amount)
                    Usr.Rubles += rub.KPNS * int(amount)
                    Usr.save()
                bot.send_message(message.chat.id, 'Обмен выполнен успешно')
                bot.send_message(foreman, f'Пользователь @{message.from_user.username} обменял {amount} {currency1} на {currency2}')



        bot.polling(none_stop=True, interval=0)
    return render(request, 'index.html')
