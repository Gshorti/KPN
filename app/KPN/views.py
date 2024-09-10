from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
import telebot
from KPN.models import User
from KPN.serializers import UserSerializer
from currency.models import Currency

user_pass1 = ''
user_pass2 = ' '
def index2(request):
    return render(request, 'index.html')


def register(request):
    username = request.GET['username']
    moneys = request.GET['moneys']
    for i in User.objects.all():
        if i.Telegram_hash == username:
            Usr = User.objects.get(Telegram_hash=username)
            Usr.KPCS = moneys
            Usr.save()
    if not User.objects.filter(Telegram_hash=username).exists():User.objects.create(Telegram_hash=username, KPСS=moneys,Rubles=0)

    return render(request, 'register.html')
class KPNview(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def index(request):
    while True:
        bot = telebot.TeleBot('7462217215:AAG63g7vFWalIIo4I3Wt_0F5qbk_LbFtV6E')

        @bot.message_handler(content_types=['text'])
        def get_text_messages(message):
            if message.text == '/reg':
                bot.send_message(message.chat.id,'Вам необходимо придумать пароль для вашего аккаунта')
                bot.register_next_step_handler(message, parol)
            elif message.text == "/start":
                bot.send_message(message.chat.id, "Вас приветствует интерфейс системы Kringe Production Network. В ней скоро будет можно много чего... Для регистрации в системе напишите /reg Для получения подробной информации напишите /help")
            elif message.text == "/help":
                bot.send_message(message.chat.id, 'Чтобы зарегистрироваться в системе Kringe Production Network напишите /reg \nЧтобы посмотреть баланс напишите /wallet\nЧтобы перевести деньги на другой счёт напишите /transfer\nЧтобы посмотреть список торгуемых активов напишите /quotes\nДля того, чтобы сменить пароль напишите /passwd\nЧтобы обменять одну валюту на другую напишите /exchange\nПо всем вопросам писать @gshorti')
            elif message.text == "/wallet":
                buffer = ''
                buffer += 'Ваш баланс: \n'
                buffer += str(User.objects.get(Telegram_hash=message.from_user.username).Rubles)
                buffer += ' Рубли\n'
                buffer += str(User.objects.get(Telegram_hash=message.from_user.username).KPCS)
                buffer += '  KPC\n'
                bot.send_message(message.chat.id, buffer)
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
                    Usr.KPCS += int(amount)
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
                if int(amount) > 0:
                    if currency == 'RUB':
                        Usr.Rubles += int(amount)
                        Usr2.Rubles -= int(amount)
                        Usr.save()
                        Usr2.save()
                    elif currency == 'KPC':
                        Usr.KPCS += int(amount)
                        Usr2.KPCS -= int(amount)
                        Usr2.save()
                        Usr.save()
                    bot.send_message(Usr.Telegram_ID, f'Пользователь @{Usr2.Telegram_hash} перевёл вам {amount} {currency}')
                    bot.send_message(message.chat.id, 'Перевод выполнен успешно')
                else:
                    bot.send_message(Usr.Telegram_ID, f'Пользователь @{Usr2.Telegram_hash} хотел вас обокрасть')
                    bot.send_message(message.chat.id, 'ТЫ ЧО? В ВОРЫ ЗАДЕЛАЛСЯ? СОВСЕМ УЖЕ? НЕ СТЫДНО?')

            elif message.text == '/quotes':
                quotes = Currency.objects.all()
                buffer = ''
                buffer += "На данный момент в системе торгуются следующие котировки:\n\n"
                for k in quotes:
                   buffer += (f'{k.Name}/RUB {float(k.Amount)}\n')
                bot.send_message(message.chat.id, buffer)

            elif message.text == '/exchange':
                bot.send_message(message.chat.id, 'Напишите /exchange Валюта, которую вы обмениваете(RUB или KPC) сумма(В валюте, которую вы  обменивате) Валюта, на которую вы хотите обменять(RUB или KPC)')

            elif '/exchange' in message.text:
                Usr = User.objects.get(Telegram_hash=message.from_user.username)
                txt = message.text.split(' ')
                cur1 = txt[1]
                amount = int(txt[2])
                cur2 = txt[3]
                if amount > 0:
                    var1 = Currency.objects.get(Name=cur1)
                    var2 = Currency.objects.get(Name=cur2)
                    if var1.Name == 'KPC':
                        Usr.KPCS -= amount
                        Usr.Rubles += (amount*var1.Amount)
                        print(cur1.Amount)
                        Usr.save()
                    else:
                        Usr.Rubles -= amount
                        Usr.KPCS += (1/var1.Amount)
                        Usr.save()
                    bot.send_message(message.chat.id, 'Обмен выполнен успешно')
                else: 
                    bot.send_message(message.chat.id, 'ТЫ МЕНЯ ЗА КОГО ДЕРЖИШЬ??? А?')
            elif '/passwd' in message.text:
                bot.send_message(message.chat.id, 'Введите новый пароль')
                bot.register_next_step_handler(message, parol2)
        def parol(message):
            User.objects.create(Telegram_hash=message.from_user.username, Telegram_ID=message.from_user.id, Rubles=0, KPСS=0, password=message.text)
            bot.send_message(message.chat.id, 'Поздравляю вы зарегистрировались в системе Kringe Production Network!')

        def parol2(message):
            user = User.objects.get(Telegram_hash=message.from_user.username)
            user.password = message.text
            user.save()
            bot.send_message(message. chat.id, 'Пароль был успешно изменён')

        bot.infinity_polling(timeout=10, long_polling_timeout = 5)
    return render(request, 'index.html')
