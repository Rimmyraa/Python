import logging

from aiogram.types import KeyboardButton
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import os
from dotenv import load_dotenv

from steps import Search
from utlis import check_query
from parse import get_book
# from parse2 import contemporary_prose
from database import Database

load_dotenv()


TOKEN = os.getenv('TOKEN')


logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())
db = Database()

@dp.message_handler(commands='start')
async def start_process(message: types.Message):
    user = await db.check_user(message.from_id)
    if not user:
        await db.register_user(
            message.from_user.first_name,
            message.from_user.last_name,
            message.from_user.username,
            message.from_id
        )
        # await message.answer('Дякую за реєстрацію!')
        await message.answer('Привіт!🌟\nЯ спробую допомогти знайти тобі якусь книгу для читання!')
    
        topic = '/topic'
        search = '/search'
                                

        await message.answer(f'Щоб зробити пошуковий запит, \nскористуйся командою {search}🔍\n\nЯкщо не знаєш що шукати, команда {topic} допоможе тобі щось знайти.📚')
    else:
        await message.answer('Ви вже зареєстровані')


@dp.message_handler(commands='topic')
async def start(message: types.Message, state:FSMContext):
    kb = [

        [types.KeyboardButton("Сучасна проза")],
        [types.KeyboardButton("Фантастика та фентезі")],
        [types.KeyboardButton("Саморозвиток і мотивація")],
        [types.KeyboardButton("Здоровий спосіб життя")],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, selective=True)
    await message.answer('Яка категорія тобі більш подобається?', reply_markup=keyboard)


@dp.message_handler(text="Сучасна проза")
async def start(message: types.Message):
    await message.answer("Ось книжки з цієї теми (вони з'являться у твоїй клавіатурі )")
    kb_1 = [

        [KeyboardButton(text="Тисяча сяйливих сонць")],
        [KeyboardButton(text="Фабула")],
        [KeyboardButton(text="Шлях до несвободи")],
        [KeyboardButton(text="Ворошиловград")],
        [KeyboardButton(text="Месопотамія")],
        [KeyboardButton(text="Місто")],
        [KeyboardButton(text="Брама Європи")],
        [KeyboardButton(text="Припини це")],
        [KeyboardButton(text="Подолати минуле")],
        [KeyboardButton(text="Задивляюсь у твої зіниці")],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb_1, resize_keyboard=True, selective=True)
    await message.answer('Вибирай, яка тобі до вподоби', reply_markup=keyboard)


@dp.message_handler(text="Фантастика та фентезі")
async def start(message: types.Message):
    await message.answer("Ось книжки з цієї теми (вони з'являться у твоїй клавіатурі )")
    kb_1 = [

        [KeyboardButton(text="Тисяча сяйливих сонць")],
        [KeyboardButton(text="Фабула")],
        [KeyboardButton(text="Шлях до несвободи")],
        [KeyboardButton(text="Ворошиловград")],
        [KeyboardButton(text="Месопотамія")],
        [KeyboardButton(text="Місто")],
        [KeyboardButton(text="Брама Європи")],
        [KeyboardButton(text="Припини це")],
        [KeyboardButton(text="Подолати минуле")],
        [KeyboardButton(text="Задивляюсь у твої зіниці")],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb_1, resize_keyboard=True, selective=True)
    await message.answer('Вибирай, яка тобі до вподоби', reply_markup=keyboard)


@dp.message_handler(text="Саморозвиток і мотивація")
async def start(message: types.Message):
    await message.answer("Ось книжки з цієї теми (вони з'являться у твоїй клавіатурі )")
    kb_1 = [

        [KeyboardButton(text="Тисяча сяйливих сонць")],
        [KeyboardButton(text="Фабула")],
        [KeyboardButton(text="Шлях до несвободи")],
        [KeyboardButton(text="Ворошиловград")],
        [KeyboardButton(text="Месопотамія")],
        [KeyboardButton(text="Місто")],
        [KeyboardButton(text="Брама Європи")],
        [KeyboardButton(text="Припини це")],
        [KeyboardButton(text="Подолати минуле")],
        [KeyboardButton(text="Задивляюсь у твої зіниці")],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb_1, resize_keyboard=True, selective=True)
    await message.answer('Вибирай, яка тобі до вподоби', reply_markup=keyboard)


@dp.message_handler(text="Здоровий спосіб життя")
async def start(message: types.Message):
    await message.answer("Ось книжки з цієї теми (вони з'являться у твоїй клавіатурі )")
    kb_1 = [

        [KeyboardButton(text="Тисяча сяйливих сонць")],
        [KeyboardButton(text="Фабула")],
        [KeyboardButton(text="Шлях до несвободи")],
        [KeyboardButton(text="Ворошиловград")],
        [KeyboardButton(text="Месопотамія")],
        [KeyboardButton(text="Місто")],
        [KeyboardButton(text="Брама Європи")],
        [KeyboardButton(text="Припини це")],
        [KeyboardButton(text="Подолати минуле")],
        [KeyboardButton(text="Задивляюсь у твої зіниці")],

    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb_1, resize_keyboard=True, selective=True)
    await message.answer('Вибирай, яка тобі до вподоби', reply_markup=keyboard)




@dp.message_handler(commands='search')
async def get_books(message:types.Message):
    await message.answer('Тепер введи свій пошуковий запит!')
    await Search.state_on.set()



@dp.message_handler(state=Search.state_on, content_types='text')
async def get_books(message:types.Message, state: FSMContext):
    if not check_query(message.text):
        await message.answer('Будь ласка, введи пошукий запит через пробіли.')
    else:
        query = message.text.lower().strip()
        books = get_book(query)
        for book in books:
            title = book['title']
            author = book['author']
            availability = book['availability']
            url = book['url']
            banner = book['banner']

            msg = (f'<b>Назва: </b>{title}\n<b>Автор: </b>{author}\n\n<b>{availability}</b>\n\n<b>Посилання: </b>{url}')

            await bot.send_photo(message.chat.id, banner)
            await message.answer(text=msg, parse_mode='html', disable_web_page_preview=True)
            await state.finish()
            await message.answer(f'Якщо бажаєш ввести інший пошуковий запит, скористайся коммандою /search знову!🔍')
    


@dp.message_handler(content_types='text')
async def get_book_by_topic(message: types.Message):

    if (message.text == "Тисяча сяйливих сонць"):
        name = 'Тисяча сяйливих сонць'
        author = 'Халед Госсейні'
        cover = 'https://cdn.vogue.ua/i/original/media/image/63c/a40/076/63ca40076862e.jpg.webp'
        description = '"Тисяча сяйливих сонць" зображує історію дорослішання та дружбу двох дівчат, Маріам і Лейли, яких об`єднують спільні драми (обидві дівчатка виходять заміж у 15 за значно старших чоловіків), боротьба (роман зображує прихід талібів до влади в Кабулі) та, звісно, любов, що здатна перемогти всі руйнування.'
        all = f"📕<b>Назва:</b> {name}\n\n📕<b>Автор:</b> {author}\n\n📕<b>Про книгу:</b> {description}\n\n📕<b>Обкладинка:</b> {cover}"
        await bot.send_message(message.from_user.id, all, parse_mode="html")

    if (message.text == "Фабула"):
        name = 'Фабула'
        author = 'French Braid, Енн Тайлер'
        cover = 'https://cdn.vogue.ua/i/original/media/image/63c/a40/1b8/63ca401b87de5.jpg.webp'
        description = 'Події роману відбуваються в Балтиморі, це історія Гарретів: чоловік і дружина Робін і Мерсі, діти Еліс, Лілі й Девід. Ми зустрічаємо їх під час рідкісної відпустки на озері штату Меріленд, і проведемо з ними декілька десятиріч, відстежуючи їхні травми та радощі, дорослішання та старіння. Як завжди, Тайлер написала щемкий, іронічний роман, від якого не відірватись.'
        all = f"📕<b>Назва:</b> {name}\n\n📕<b>Автор:</b> {author}\n\n📕<b>Про книгу:</b> {description}\n\n📕<b>Обкладинка:</b> {cover}"
        await bot.send_message(message.from_user.id, all, parse_mode="html")

    if (message.text == "Шлях до несвободи"):
        name = 'Шлях до несвободи'
        author = 'Тімоті Снайдер'
        cover = 'https://sens.in.ua/content/images/35/520x783l80mc0/shliakh-do-nesvobody.-timoti-snaider-91359348333515.webp'
        description = ' Це книжка про події, політичні фігури та глобальні ідеї, які приховані за цими подіями. Тімоті Снайдер аналізує складні та драматичні трансформації в Росії, Україні, Європі та США від 2011 до 2016 року. Серед головних подій – російські протести на Болотній площі в Москві, Революція Гідності в Україні, анексія Криму та вторгнення Росії на Донбас, криза біженців, Брекзит і перемога Дональда Трампа на президентських виборах у США. Тімоті Снайдер не лише ставить питання про те, чому ж ідея «кінця історії» була помилковою. Він доводить, як закладена в «кінець історії» неуникність, або ж, іншими словами, думка про те, що «ідеї не мають значення», могла докластися до створення сучасного політичного клімату. Тімоті Снайдер – американський історик, письменник, публічний інтелектуал.'
        all = f"📕<b>Назва:</b> {name}\n\n📕<b>Автор:</b> {author}\n\n📕<b>Про книгу:</b> {description}\n\n📕<b>Обкладинка:</b> {cover}"
        await bot.send_message(message.from_user.id, all, parse_mode="html")

    if (message.text == "Ворошиловград"):
        name = 'Ворошиловград'
        author = 'Сергій Жадан'
        cover = 'https://sens.in.ua/content/images/34/520x770l80mc0/voroshylovohrad.-serhii-zhadan-65207799979773.webp'
        description = 'За версією конкурсу "Книга року BBC" роман "Ворошиловград" став кращою книгою десятиліття! Пил доріг, іржаві бензоколонки, втомлені автобуси, старі "хрущовки"... Місто, що залишилось десь поза часом. Дивні люди, які займаються дивними справами. Абсурд - та водночас "справжність" існування... Герман повертається до містечка свого дитинства у степах Донбасу, щоб знайти зниклого брата і врятувати його бізнес. Проте реальність виявляється хиткою, майбутнє - невизначеним, а минуле викликає надто гостру ностальгію... Лірична і жорстка, соціальна і метафізична, меланхолійна і реалістична історія, сповнена безмежних просторів, спогадів, сновидь, мрій, джазу та духу справжньої дружби.'
        all = f"📕<b>Назва:</b> {name}\n\n📕<b>Автор:</b> {author}\n\n📕<b>Про книгу:</b> {description}\n\n📕<b>Обкладинка:</b> {cover}"
        await bot.send_message(message.from_user.id, all, parse_mode="html")

    if (message.text == "Месопотамія"):
        name = 'Месопотамія'
        author = 'Сергій Жадан'
        cover = 'https://sens.in.ua/content/images/35/520x781l80mc0/mesopotamiia.-serhii-zhadan-41985549918985.webp'
        description = 'Філософські відступи, фантастичні образи, вишукані метафори й специфічний гумор – тут є все, що так приваблює у творах Сергія Жадана. Історії Вавилона, переказані для тих, хто цікавиться питаннями любові і смерті. Життя міста, що лежить поміж рік, біографії персонажів, які б’ються за своє право бути почутими й збагнутими, хроніка вуличних сутичок і щоденних пристрастей. Освідчення і зради, втечі і повернення, ніжність і жорстокість.'
        all = f"📕<b>Назва:</b> {name}\n\n📕<b>Автор:</b> {author}\n\n📕<b>Про книгу:</b> {description}\n\n📕<b>Обкладинка:</b> {cover}"
        await bot.send_message(message.from_user.id, all, parse_mode="html")

    if (message.text == "Місто"):
        name = 'Місто'
        author = 'Валер’ян Підмогильний'
        cover = 'https://sens.in.ua/content/images/37/369x504l80mc0/misto.-valerian-pidmohylnyi-73694907820809.webp'
        description = 'У найпростішому прочитанні роман «Місто» Валер’яна Підмогильного — це історія амбітного юнака, який переїжджає із села у Київ і будує там нове життя. Його часто порівнюють з героєм «Любого друга» Мопассана й самовпевненими і неперебірливими в засобах  підкорювачами суспільних вершин із сюжетів Бальзака. Однак для Підмогильного це не лише історія кар’єри. Він уписує життя Степана Радченка в історико-культурний контекст тогочасної України.\nМаргінал і чужинець Радченко протягом роману цілеспрямовано викшталтовує себе, здобуває освіту, прилучається до інтелектуальної  та творчої еліти. Довколишній світ видається йому дедалі складнішим.\nОкрім іншого, роман «Місто», написаний у 1927 році, засвідчував неймовірно важливий здобуток національної революції: повернення урбаністичного простору під українську культурну юрисдикцію. Епоха принизливого самообмеження  в рамках домашньовжиткової рустикальности зосталася позаду, Київ знову ставав осередком потужного мистецького ренесансу.'
        all = f"📕<b>Назва:</b> {name}\n\n📕<b>Автор:</b> {author}\n\n📕<b>Про книгу:</b> {description}\n\n📕<b>Обкладинка:</b> {cover}"
        await bot.send_message(message.from_user.id, all, parse_mode="html")

    if (message.text == "Брама Європи"):
        name = "Брама Європи"
        author = 'Сергій Плохій'
        cover = 'https://sens.in.ua/content/images/1/553x800l80mc0/brama-ievropi-50646877436642.webp'
        description = 'Книга цікаво й доступно розповідає про історію нашої держави від часів Геродота до подій на Сході України сьогодні. Це авторитетне видання допоможе краще зрозуміти події минулого, а через них — і наше сьогодення. Автор фокусує увагу на українцях як найбільшій демографічній групі, а згодом — головній силі, що стояла за створенням сучасної нації. Дізнайтеся, як наші предки «призвали варягів на царювання», як наша країна боролася за право бути незалежною, пройшла крізь часи кріпацтва, комуністичного терору й Голодомору, Другої світової війни та врешті-решт отримала незалежність.'
        all = f"📕<b>Назва:</b> {name}\n\n📕<b>Автор:</b> {author}\n\n📕<b>Про книгу:</b> {description}\n\n📕<b>Обкладинка:</b> {cover}"
        await bot.send_message(message.from_user.id, all, parse_mode="html")

    if (message.text == 'Припини це'):
        name = 'Припини це'
        author = 'Спартак Суббота'
        cover = 'https://sens.in.ua/content/images/11/502x800l80mc0/pripini-tse.-yak-rozpiznati-nasilstvo-ta-protidiyati-yomu-50078109319486.webp'
        description = 'Насильство має багато проявів. Перше, що може спасти на думку, — це фізичний напад, але не тільки він спричиняє непоправні наслідки. Багато людей можуть потерпати від насильства і навіть не підозрювати, що з ними відбувається насправді. Сексуальне, психологічне, економічне насильство, педагогічне нехтування — це різні прояви того самого явища, що впливають на комунікацію з оточенням, на виховання, формування сімейних та особистісних цінностей. Автор цієї книжки, психотерапевт Спартак Суббота переконаний: кожен з нас має вміти розпізнавати насилля та знати алгоритм дій, аби вчасно запобігти йому. Ця книжка допоможе розібратися в природі насильства, ідентифікувати його види, зрозуміти, за якими ознаками можна розпізнати насильство, що робити, щоб мінімізувати його прояви у житті, і до кого звертатися по допомогу, якщо насильство трапилося в минулому. Автор наводить приклади з особистої психотерапевтичної практики, пропонує читачам чеклісти, за якими можна перевірити, чи присутнє насилля у вашому житті або чи є ви його свідками.'
        all = f"📕<b>Назва:</b> {name}\n\n📕<b>Автор:</b> {author}\n\n📕<b>Про книгу:</b> {description}\n\n📕<b>Обкладинка:</b> {cover}"
        await bot.send_message(message.from_user.id, all, parse_mode="html")

    if (message.text == 'Подолати минуле'):
        name = 'Подолати минуле'
        author = 'Ярослав Грицак'
        cover = 'https://sens.in.ua/content/images/5/579x800l80mc0/podolati-minule-globalna-istoriya-ukraini-73374718997007.webp'
        description = 'Ця книжка – результат 15-літньої роботи професора Ярослава Грицака. У ній автор прискіпливо препарує минуле і закликає до співтворення сучасної України. Він намагається зрозуміти сам і дати читачам розуміння, що і чому відбувається з нами тут і тепер, і яким може бути майбутнє країни.'
        all = f"📕<b>Назва:</b> {name}\n\n📕<b>Автор:</b> {author}\n\n📕<b>Про книгу:</b> {description}\n\n📕<b>Обкладинка:</b> {cover}"
        await bot.send_message(message.from_user.id, all, parse_mode="html")

    if (message.text == 'Задивляюсь у твої зіниці'):
        name = 'Задивляюсь у твої зіниці'
        author = 'Василь Симоненко'
        cover = 'https://sens.in.ua/content/images/39/1180x1180l80mc0/zadivlyaus-u-tvoi-zinitsi-56006379021139.webp'
        description = 'Василь Симоненко — поетична легенда «шістдесятництва» як суспільно-мистецького руху. Його вірші не пропускала до друку радянська цензура, тому їх поширювали у самвидавних списках і переписували від руки — вчителі, професори і хлібороби.'
        all = f"📕<b>Назва:</b> {name}\n\n📕<b>Автор:</b> {author}\n\n📕<b>Про книгу:</b> {description}\n\n📕<b>Обкладинка:</b> {cover}"
        await bot.send_message(message.from_user.id, all, parse_mode="html")


    

if __name__ == '__main__':
    executor.start_polling(dp)