"""
TRAWA Telegram Bot · content.py
Весь контент бота: тексты, описания, изображения, ссылки.
Чтобы обновить карточку — меняй только этот файл.
"""

# UTM-метка добавляется ко всем ссылкам
UTM = "?utm_source=telegram&utm_medium=bot&utm_campaign=trawa_bot"

# ─── Изображения продуктов ────────────────────────────────────────────────────

IMG_LINSEED         = "https://files.catbox.moe/8uz2c0.png"
IMG_HEMP            = "https://files.catbox.moe/8y96xu.png"
IMG_BLACKSEED       = "https://files.catbox.moe/nhbi8l.png"
IMG_PUMPKIN         = "https://files.catbox.moe/d1e7nx.png"
IMG_GHI             = "https://files.catbox.moe/riump4.jpg"
IMG_MUSTARD_OIL     = "https://files.catbox.moe/hppjli.png"
IMG_HAZELNUT        = "https://files.catbox.moe/h4dddh.png"
IMG_WALNUT          = "https://files.catbox.moe/96j3lx.png"
IMG_PESTO           = "https://files.catbox.moe/dwffoo.png"
IMG_MUSTARD         = "https://files.catbox.moe/eq0vgg.png"
IMG_ALMOND          = "https://files.catbox.moe/d5fie3.png"
IMG_CEDAR           = "https://files.catbox.moe/8vczq0.png"
IMG_GLOW            = "https://files.catbox.moe/hjwwmj.png"
IMG_SESAME          = "https://files.catbox.moe/1wohej.png"
IMG_PEANUT          = "https://files.catbox.moe/7oqp61.png"
IMG_SUNFLOWER       = "https://files.catbox.moe/puq4lh.png"
IMG_FIBER_MIX       = "https://files.catbox.moe/0l1oxx.jpg"
IMG_FIBER_HEDGEHOG  = "https://files.catbox.moe/4nx47d.png"
IMG_CEDAR_FLOUR     = "https://files.catbox.moe/2h7ghd.png"
IMG_ALMOND_FLOUR    = "https://files.catbox.moe/aickmq.jpg"
IMG_WALNUT_FLOUR    = ""
IMG_SUNFLOWER_FLOUR = "https://files.catbox.moe/qfdr2x.png"
IMG_LINSEED_FLOUR   = "https://files.catbox.moe/avquj8.png"
IMG_PUMPKIN_FLOUR   = "https://files.catbox.moe/qek19x.png"
IMG_APRICOT_FLOUR   = "https://files.catbox.moe/nv9e5f.png"
IMG_DRY_SKIN        = "https://files.catbox.moe/z5q9wi.png"
IMG_ROLLER          = "https://files.catbox.moe/x4tsb1.png"
IMG_HIDROLAT        = "https://files.catbox.moe/3dg51k.png"
IMG_KANTUCHCHI      = "https://files.catbox.moe/nktrum.png"
IMG_DESSERTS_PARTNER = "https://files.catbox.moe/4o447t.png"

# ─── Статические тексты ───────────────────────────────────────────────────────

WELCOME_TEXT = (
    "Приветствуем всей командой TRAWA! 🌿\n\n"
    "Мы создали этого ботика, чтобы помогать вам быстро находить "
    "нужные продукты под вашу цель.\n\n"
    "Но если вдруг в нём чего-то не хватает или он не справляется — "
    "мы всегда на связи с 10:00 до 19:00 вот в этом аккаунте: @trawa_support\n\n"
    "Итак, с чего начнём? 💚"
)

FRYING_WARNING = (
    "🍳 <b>Масла для жарки</b>\n\n"
    "Эти масла выдерживают нагрев выше 200°С.\n"
    "Тем не менее мы рекомендуем избегать сильной обжарки."
)

DACHA_TEXT = (
    "🌻 <b>Дачный сезон</b>\n\n"
    "Натуральные масла и продукты TRAWA — для вашего стола "
    "и огорода этим летом.\n\n"
    "Полная подборка — на сайте."
)

DACHA_URL = f"https://trawaoil.ru/c/dacha{UTM}"

NO_PROMOTIONS_TEXT = "🔥 Акций пока нет — следите за обновлениями!\n\nВсе актуальные предложения появятся здесь первыми."

# ─── Контент-матрица продуктов ────────────────────────────────────────────────

PRODUCTS: dict[str, list[dict]] = {

    "women_oils": [
        {
            "name": "Льняное масло",
            "photo_url": IMG_LINSEED,
            "benefits": [
                "Содержит омега-3 жирные кислоты и антиоксиданты",
                "Свежий травянисто-ореховый вкус, солнечно-жёлтый цвет",
                "Добавляют в супы-пюре, салаты, каши — используется в сыром виде",
            ],
            "url": f"https://trawaoil.ru/p/maslo-lnyanoe-syrodavlennoe--61fbbd89794ca42960920f52{UTM}",
        },
        {
            "name": "Конопляное масло",
            "photo_url": IMG_HEMP,
            "benefits": [
                "Содержит омега-3 и омега-6 в соотношении 3:1",
                "Богато антиоксидантами и альфа-линоленовой кислотой",
                "Яркий травянисто-ореховый вкус — для салатов, соусов, каш",
            ],
            "url": f"https://trawaoil.ru/p/maslo-konoplyanoe-syrodavlennoe-61fbbd87794ca42960920d99{UTM}",
        },
        {
            "name": "Миндальное масло",
            "photo_url": IMG_ALMOND,
            "benefits": [
                "Содержит витамин Е — природный антиоксидант",
                "Деликатный ореховый вкус, светлый почти прозрачный цвет",
                "Для ризотто, пасты, салатов и десертов — используется в сыром виде",
            ],
            "url": f"https://trawaoil.ru/p/maslo-mindalnoe-syrodavlennoe--61fbbd89794ca42960920f59{UTM}",
        },
        {
            "name": "Кедровое масло",
            "photo_url": IMG_CEDAR,
            "benefits": [
                "Содержит витамин Е и пиноленовую кислоту",
                "Слабо-ореховый вкус с лёгким сливочным послевкусием",
                "Для рыбы, морепродуктов, овощей и каш — используется в сыром виде",
            ],
            "url": f"https://trawaoil.ru/p/maslo-kedrovoe-syrodavlennoe-61fbbd88794ca42960920ddb{UTM}",
        },
        {
            "name": "Мини-сет «Сияние» (миндаль + кунжут + кедр)",
            "photo_url": IMG_GLOW,
            "benefits": [
                "Женский микс «Сияние»: миндальное, кунжутное и кедровое масла",
                "Часть мини-сета из 4 функциональных миксов по 100 мл",
                "Разработан совместно с VEGETARIAN.RU",
            ],
            "url": f"https://trawaoil.ru/p/mini-set-funkcionalnyh-masel-TRAWA--Vegetarian-660d328824dd6523315ca1b1{UTM}",
        },
    ],

    "men_oils": [
        {
            "name": "Масло чёрного тмина",
            "photo_url": IMG_BLACKSEED,
            "benefits": [
                "Редкое масло с пикантным пряным вкусом и перечной остринкой",
                "Происхождение сырья: Индия; 99,9 г жира на 100 г",
                "Добавляют в горячие супы и овощные блюда или принимают в чистом виде",
            ],
            "url": f"https://trawaoil.ru/p/maslo-chernogo-tmina-syrodavlennoe-623d019f25adee0d7df9355f{UTM}",
        },
        {
            "name": "Кедровое масло",
            "photo_url": IMG_CEDAR,
            "benefits": [
                "Содержит витамин Е и пиноленовую кислоту",
                "Слабо-ореховый вкус с лёгким сливочным послевкусием",
                "Для рыбы, морепродуктов, гарниров, каш — в сыром виде",
            ],
            "url": f"https://trawaoil.ru/p/maslo-kedrovoe-syrodavlennoe-61fbbd88794ca42960920ddb{UTM}",
        },
        {
            "name": "Конопляное масло",
            "photo_url": IMG_HEMP,
            "benefits": [
                "Содержит омега-3 и омега-6 в соотношении 3:1",
                "Богато антиоксидантами и альфа-линоленовой кислотой",
                "Яркий травянисто-ореховый вкус — для салатов, рагу, соусов",
            ],
            "url": f"https://trawaoil.ru/p/maslo-konoplyanoe-syrodavlennoe-61fbbd87794ca42960920d99{UTM}",
        },
        {
            "name": "Тыквенное масло",
            "photo_url": IMG_PUMPKIN,
            "benefits": [
                "Содержит каротиноиды и витамин А (381 мкг на столовую ложку)",
                "В составе кукурбитин и жирорастворимые витамины",
                "Нежный аромат тыквы — для салатов, супов-пюре, соусов к мясу",
            ],
            "url": f"https://trawaoil.ru/p/maslo-tykvennoe-syrodavlennoe-61fbbd8b794ca429609210a7{UTM}",
        },
    ],

    "children_oils": [
        {
            "name": "Конопляное масло",
            "photo_url": IMG_HEMP,
            "benefits": [
                "Яркий травянисто-ореховый вкус",
                "Для заправки каш, рагу, соусов и салатов",
                "Объём: 250 мл",
            ],
            "url": f"https://trawaoil.ru/p/maslo-konoplyanoe-syrodavlennoe-61fbbd87794ca42960920d99{UTM}",
        },
        {
            "name": "Подсолнечное масло",
            "photo_url": IMG_SUNFLOWER,
            "benefits": [
                "Деликатный натуральный вкус подсолнечной семечки",
                "Для заправки салатов, квашеной капусты, соусов и консервации",
                "Объём: 250 мл. Сыродавленное — не нагревать",
            ],
            "url": f"https://trawaoil.ru/p/maslo-podsolnechnoe-syrodavlennoe-61fbbd89794ca42960920f65{UTM}",
        },
    ],

    "frying": [
        {
            "name": "Масло ГХИ",
            "photo_url": IMG_GHI,
            "benefits": [
                "Без лактозы и казеина — очищено от молочных примесей в процессе топления",
                "Высокая точка дымления — подходит для приготовления пищи",
                "Натуральное топлёное сливочное масло из Адыгеи — 99,8% жира",
            ],
            "url": f"https://trawaoil.ru/c/maslo-ghi{UTM}",
        },
        {
            "name": "Кунжутное масло",
            "photo_url": IMG_SESAME,
            "benefits": [
                "Содержит антиоксиданты сезамол и сезаминол",
                "Освежающий аромат с нотками молочного ореха",
                "Для блюд восточной кухни, маринадов, заправок и соусов",
            ],
            "url": f"https://trawaoil.ru/p/maslo-kunzhutnoe-syrodavlennoe-61fbbd8a794ca42960920fad{UTM}",
        },
        {
            "name": "Горчичное масло",
            "photo_url": IMG_MUSTARD_OIL,
            "benefits": [
                "Содержит витамины А, D, E — богатый жирорастворимый состав",
                "Пряный пикантный вкус без горечи, медово-золотистый цвет",
                "Имеет высокую точку дымления; для салатов, рыбы, овощей и консервов",
            ],
            "url": f"https://trawaoil.ru/p/maslo-syrodavlennoe-gorchichnoe-61fbbd88794ca42960920e31{UTM}",
        },
        {
            "name": "Арахисовое масло",
            "photo_url": IMG_PEANUT,
            "benefits": [
                "Лёгкий ореховый вкус, светлый почти прозрачный цвет",
                "99,9% жира — чистый продукт без примесей",
                "Для блюд из бобовых, птицы, азиатской кухни и выпечки",
            ],
            "url": f"https://trawaoil.ru/p/maslo-arahisovoe-syrodavlennoe--61fbbd87794ca42960920d40{UTM}",
        },
    ],

    "digestion": [
        {
            "name": "Клетчатка — сбалансированный микс",
            "photo_url": IMG_FIBER_MIX,
            "benefits": [
                "36 г пищевых волокон на 100 г продукта",
                "Состав: обезжиренные семена льна, подсолнечника и миндаль",
                "Добавляют в каши, смузи, соки или разводят с водой",
            ],
            "url": f"https://trawaoil.ru/p/kletchatka-sbalansirovannyy-miks-semyan-i-orehov--6684ec2b2e27112210dfc130{UTM}",
        },
        {
            "name": "Клетчатка с ежовиком гребенчатым",
            "photo_url": IMG_FIBER_HEDGEHOG,
            "benefits": [
                "Содержит 36 г пищевых волокон на 100 г и ежовик гребенчатый с собственных ферм",
                "Разработан совместно с Юлией Бордовских — упаковка на 30 дней",
                "Добавляют в смузи, каши, йогурты или разводят с водой утром",
            ],
            "url": f"https://trawaoil.ru/p/kletchatka-s-ezhovikom-grebenchatym--679c8e73ba21fcdd727d199d{UTM}",
        },
        {
            "name": "Мука из кедрового ореха",
            "photo_url": IMG_CEDAR_FLOUR,
            "benefits": [
                "Источник витаминов E, группы B и K; содержит пищевые волокна",
                "Содержит растительный белок — 27,9 г на 100 г",
                "Без глютена — для выпечки, сырников, запеканок и каш",
            ],
            "url": f"https://trawaoil.ru/p/muka-iz-kedrovogo-oreha-bez-glyutena-61fbbd8a794ca42960920fa8{UTM}",
        },
    ],

    "baking": [
        {
            "name": "Мука из миндального ореха",
            "photo_url": IMG_ALMOND_FLOUR,
            "benefits": [
                "Содержит витамины А, E и группы B; богата растительным белком",
                "Низкий гликемический индекс — 25 единиц; без глютена",
                "Нежная текстура для кексов, печенья, макарун и кляра",
            ],
            "url": f"https://trawaoil.ru/p/muka-iz-mindalnogo-oreha-bez-glyutena-61fbbd89794ca42960920eab{UTM}",
        },
        {
            "name": "Мука из кедрового ореха",
            "photo_url": IMG_CEDAR_FLOUR,
            "benefits": [
                "Источник витаминов E, группы B и K",
                "Без глютена; воздушная текстура с кедровым ароматом",
                "Для пирогов, блинов, сырников и запеканок",
            ],
            "url": f"https://trawaoil.ru/p/muka-iz-kedrovogo-oreha-bez-glyutena-61fbbd8a794ca42960920fa8{UTM}",
        },
        {
            "name": "Мука из семян льна",
            "photo_url": IMG_LINSEED_FLOUR,
            "benefits": [
                "Источник омега-3, витаминов А, E, K и группы B",
                "Содержит растительный белок — 33,1 г на 100 г; без глютена",
                "Для выпечки, каш, киселей; может заменять яйцо в рецептах",
            ],
            "url": f"https://trawaoil.ru/p/muka-iz-semyan-lna-lnyanaya-kasha-bez-glyutena-61fbbd88794ca42960920e6e{UTM}",
        },
        {
            "name": "Мука из штирийской тыквы",
            "photo_url": IMG_PUMPKIN_FLOUR,
            "benefits": [
                "Источник витаминов А, E и цинка",
                "Высокое содержание растительного белка — 46,3 г на 100 г; без глютена",
                "Воздушная текстура с тонким ореховым вкусом — для выпечки и панировки",
            ],
            "url": f"https://trawaoil.ru/p/muka-iz-semyan-shtiriyskoy-tykvy--bez-glyutena-61fbbd88794ca42960920e25{UTM}",
        },
        {
            "name": "Мука из грецкого ореха",
            "photo_url": IMG_WALNUT_FLOUR,
            "benefits": [
                "Источник витаминов А, E и группы B; содержит цинк",
                "Содержит растительный белок — 33,1 г на 100 г; без глютена",
                "Интенсивный ореховый вкус — для пхали, блинов, соусов и дипов",
            ],
            "url": f"https://trawaoil.ru/p/muka-iz-greckogo-oreha-bez-glyutena-61fbbd82794ca42960920c1c{UTM}",
        },
        {
            "name": "Мука из подсолнечной семечки",
            "photo_url": IMG_SUNFLOWER_FLOUR,
            "benefits": [
                "Высокое содержание растительного белка — 39,1 г на 100 г",
                "Без глютена; светлая мука с нежным вкусом семечки",
                "Для выпечки, сырников, запеканок, панировки и RAW-десертов",
            ],
            "url": f"https://trawaoil.ru/p/muka-iz-podsolnechnoy-semechki-bez-glyutena-61fbbd87794ca42960920d47{UTM}",
        },
        {
            "name": "Мука из абрикосовой косточки",
            "photo_url": IMG_APRICOT_FLOUR,
            "benefits": [
                "Источник витаминов E, C, А и группы B",
                "Содержит растительный белок — 30,1 г на 100 г; без глютена",
                "Тонкий ореховый аромат — для выпечки, йогуртов и каш",
            ],
            "url": f"https://trawaoil.ru/p/muka-iz-abrikosovoy-kostochki-bez-glyutena-677fc72fcabf41675918ea8b{UTM}",
        },
    ],

    "cosmetics": [
        {
            "name": "Масло для сухой кожи",
            "photo_url": IMG_DRY_SKIN,
            "benefits": [
                "Состав: кунжутное масло, эфирное масло лаванды, мяты перечной, витамин E",
                "Содержит витамин Е — природный антиоксидант",
                "Для лица (1–2 капли), волос (маска 15–20 мин) и тела (после душа)",
            ],
            "url": f"https://trawaoil.ru/p/maslo-dlya-suhoy-kozhi-623d030925adee0d7df940e6{UTM}",
        },
        {
            "name": "Роллер регенерирующий",
            "photo_url": IMG_ROLLER,
            "benefits": [
                "Состав: конопляное масло, эфирное масло герани, розмарина, витамин E",
                "Универсальный формат 5 в 1: губы, кутикула, ногти, лицо, волосы",
                "10 мл — удобно для сумочки и поездок",
            ],
            "url": f"https://trawaoil.ru/p/maslo-regeneriruyushchee-v-rollere-10-ml-644467d66a05219bbf149995{UTM}",
        },
        {
            "name": "Гидролат зизифора",
            "photo_url": IMG_HIDROLAT,
            "benefits": [
                "100% гидролат зизифоры пахучковидной с Алтая — без добавок и консервантов",
                "Обладает антибактериальными свойствами; подходит для всех типов кожи",
                "Освежающий травянисто-ментоловый аромат — для лица, шеи и волос",
            ],
            "url": f"https://trawaoil.ru/p/gidrolat-zizifora-63500d3ec40257388ce8fa65{UTM}",
        },
    ],

    "desserts": [
        {
            "name": "Сладости TRAWA",
            "photo_url": IMG_KANTUCHCHI,
            "benefits": [
                "Кантуччи без сахара из безглютеновой муки — собственное производство",
                "Состав: рисовая, амарантовая, льняная мука, сироп цикория, миндаль",
                "Хрустящая текстура — идеально к чаю, кофе и десертным винам",
            ],
            "url": f"https://trawaoil.ru/c/kantuchchi{UTM}",
            "is_partner": False,
        },
        {
            "name": "Сладости от партнёров",
            "photo_url": IMG_DESSERTS_PARTNER,
            "benefits": [
                "Тщательно отобранные партнёры — только проверенные рецептуры",
                "Широкий выбор десертов без сахара и глютена",
                "Новинки появляются регулярно",
            ],
            "url": f"https://trawaoil.ru/c/deserty{UTM}",
            "is_partner": True,
        },
    ],

    "delicacies": [
        {
            "name": "Соус Песто веганский",
            "photo_url": IMG_PESTO,
            "benefits": [
                "Состав: масло подсолнечное TRAWA, свежий базилик, грецкий орех, лимон, чеснок, соль",
                "Без консервантов, красителей и усилителей вкуса — без термической обработки",
                "Для пасты, брускетты, салатов и горячих блюд",
            ],
            "url": f"https://trawaoil.ru/p/sous-pesto-veganskiy-62d7d402f6fb2f27cd4d4512{UTM}",
        },
        {
            "name": "Горчица зернистая",
            "photo_url": IMG_MUSTARD,
            "benefits": [
                "Состав: обезжиренные семена горчицы, яблочный уксус, яблочный сок, мёд, соль",
                "Без консервантов — характерный пряный вкус без остроты, с упругими зёрнышками",
                "Для салатов, мяса, рыбы, сыров и брускетт",
            ],
            "url": f"https://trawaoil.ru/p/gorchica-zernistaya--62e7e89182c1ee261413666d{UTM}",
        },
        {
            "name": "Масло грецкого ореха",
            "photo_url": IMG_WALNUT,
            "benefits": [
                "Источник витаминов А, E и группы B; содержит цинк",
                "Насыщенный ореховый аромат — для холодных блюд и заправок",
                "Используется в сыром виде — не нагревать",
            ],
            "url": f"https://trawaoil.ru/c/masla{UTM}",
        },
    ],

    "fiber": [
        {
            "name": "Клетчатка — сбалансированный микс",
            "photo_url": IMG_FIBER_MIX,
            "benefits": [
                "36 г пищевых волокон на 100 г — натуральный источник клетчатки",
                "Состав: обезжиренные семена льна, подсолнечника и миндаль",
                "Добавляют в йогурт, смузи, каши или разводят с водой",
            ],
            "url": f"https://trawaoil.ru/p/kletchatka-sbalansirovannyy-miks-semyan-i-orehov--6684ec2b2e27112210dfc130{UTM}",
        },
        {
            "name": "Клетчатка с ежовиком гребенчатым",
            "photo_url": IMG_FIBER_HEDGEHOG,
            "benefits": [
                "Содержит 36 г пищевых волокон на 100 г и ежовик гребенчатый с собственных ферм",
                "Разработан с Юлией Бордовских — 1 г ежовика в каждой ложке",
                "Добавляют в смузи, каши, йогурты или разводят с водой утром",
            ],
            "url": f"https://trawaoil.ru/p/kletchatka-s-ezhovikom-grebenchatym--679c8e73ba21fcdd727d199d{UTM}",
        },
        {
            "name": "Мука из кедрового ореха",
            "photo_url": IMG_CEDAR_FLOUR,
            "benefits": [
                "Источник витаминов E, группы B и K; содержит пищевые волокна",
                "Без глютена — подходит при чувствительном пищеварении",
                "Легко добавить в выпечку, сырники или использовать как добавку к блюдам",
            ],
            "url": f"https://trawaoil.ru/p/muka-iz-kedrovogo-oreha-bez-glyutena-61fbbd8a794ca42960920fa8{UTM}",
        },
    ],

    "hits": [
        {
            "name": "Льняное масло",
            "photo_url": IMG_LINSEED,
            "benefits": [
                "Содержит омега-3 жирные кислоты и антиоксиданты",
                "Свежий травянисто-ореховый вкус, солнечно-жёлтый цвет",
                "Добавляют в супы-пюре, салаты, каши — используется в сыром виде",
            ],
            "url": f"https://trawaoil.ru/p/maslo-lnyanoe-syrodavlennoe--61fbbd89794ca42960920f52{UTM}",
        },
        {
            "name": "Масло ГХИ",
            "photo_url": IMG_GHI,
            "benefits": [
                "Без лактозы и казеина — очищено от молочных примесей в процессе топления",
                "Высокая точка дымления — подходит для приготовления пищи",
                "Натуральное топлёное сливочное масло из Адыгеи — 99,8% жира",
            ],
            "url": f"https://trawaoil.ru/c/maslo-ghi{UTM}",
        },
        {
            "name": "Соус Песто веганский",
            "photo_url": IMG_PESTO,
            "benefits": [
                "Состав: масло подсолнечное TRAWA, свежий базилик, грецкий орех, лимон, чеснок, соль",
                "Без консервантов, красителей и усилителей вкуса — без термической обработки",
                "Для пасты, брускетты, салатов и горячих блюд",
            ],
            "url": f"https://trawaoil.ru/p/sous-pesto-veganskiy-62d7d402f6fb2f27cd4d4512{UTM}",
        },
        {
            "name": "Клетчатка — сбалансированный микс",
            "photo_url": IMG_FIBER_MIX,
            "benefits": [
                "36 г пищевых волокон на 100 г продукта",
                "Состав: обезжиренные семена льна, подсолнечника и миндаль",
                "Добавляют в каши, смузи, соки или разводят с водой",
            ],
            "url": f"https://trawaoil.ru/p/kletchatka-sbalansirovannyy-miks-semyan-i-orehov--6684ec2b2e27112210dfc130{UTM}",
        },
        {
            "name": "Подсолнечное масло",
            "photo_url": IMG_SUNFLOWER,
            "benefits": [
                "Деликатный натуральный вкус подсолнечной семечки",
                "Для заправки салатов, квашеной капусты, соусов и консервации",
                "Содержит витамин Е и лецитин — сыродавленное, без нагрева",
            ],
            "url": f"https://trawaoil.ru/p/maslo-podsolnechnoe-syrodavlennoe-61fbbd89794ca42960920f65{UTM}",
        },
    ],
}

CATEGORY_THEME: dict[str, str] = {
    "women_oils":   "Масла",
    "men_oils":     "Масла",
    "children_oils":"Масла",
    "frying":       "Масла",
    "digestion":    "Пищеварение",
    "baking":       "Для выпечки",
    "cosmetics":    "Косметика",
    "desserts":     "Десерты без сахара",
    "delicacies":   "Деликатесы и суперфуды",
    "fiber":        "Деликатесы и суперфуды",
    "hits":         "Хиты продаж",
    "promotions":   "Акции",
    "dacha":        "Дачный сезон",
}
