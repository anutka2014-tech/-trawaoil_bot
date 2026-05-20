"""
TRAWA Telegram Bot · content.py
Весь контент бота: тексты, описания, изображения, ссылки.
Чтобы обновить карточку — меняй только этот файл.
"""

# UTM-метка добавляется ко всем ссылкам
UTM = "?utm_source=telegram&utm_medium=bot&utm_campaign=trawa_bot"

# ─── Изображения продуктов (взяты с trawaoil.ru) ─────────────────────────────

IMG_LINSEED         = "https://s3.trawaoil.ru/pub/inside/angry/still/18b089b6-5277-48b7-bd40-a4944febd6e0.png"
IMG_HEMP            = "https://s3.trawaoil.ru/pub/makewinston/night/being/b9609a5a-c9fa-4f4e-9bd8-5ea4ce7ffcc9.png"
IMG_BLACKSEED       = "https://s3.trawaoil.ru/pub/members/there/women/ebf54ea4-b766-4d45-999b-a554b4cfd3c0.png"
IMG_PUMPKIN         = "https://s3.trawaoil.ru/pub/country/would/behind/3f213621-67ca-478e-8cc2-29d5b30eeabe.png"
IMG_GHI             = "https://s3.trawaoil.ru/pub/again/slowly/never/64434e5e-8dfd-4a24-9a2e-25079253332f.jpg"
IMG_MUSTARD_OIL     = "https://s3.trawaoil.ru/pub/richer/themhow/middlesized/dab9cb5e-e385-4ce6-bcbf-553930f51c44.png"
IMG_HAZELNUT        = "https://s3.trawaoil.ru/pub/nearly/tired/piece/82b24f16-968a-455c-84b3-165b766e8e7c.png"
IMG_WALNUT          = "https://s3.trawaoil.ru/pub/thirty/anything/dowinston/795a32dc-99b5-4cbe-9044-8614f4f1125f.png"
IMG_PESTO           = "https://s3.trawaoil.ru/pub/hidden/obrien/round/29edf5aa-ef2d-40a0-b734-83bf50d5228c.png"
IMG_MUSTARD         = "https://s3.trawaoil.ru/pub/poems/interesting/became/9ac869fa-ed79-40ad-871f-bf0f36c5c4fd.png"
# Новые изображения — найдены на страницах товаров trawaoil.ru
IMG_ALMOND          = "https://s3.trawaoil.ru/pub/changes/changed/peoples/330dd3bd-0a48-4aff-a640-e987eb8e4df0.png"
IMG_CEDAR           = "https://s3.trawaoil.ru/pub/thought/understand/hours/4d051113-9248-4694-b4cd-cb273bc10947.png"
IMG_GLOW            = "https://s3.trawaoil.ru/pub/arrived/other/faces/69b961a8-bae4-4aa4-892f-f58e9a57b07f.png"
IMG_SESAME          = "https://s3.trawaoil.ru/pub/whether/angry/taken/90e228f5-0b4b-48fb-bc76-c8c9efd20e26.png"
IMG_PEANUT          = "https://s3.trawaoil.ru/pub/brotherdown/copies/colour/daf76fca-d364-4d55-9d9e-0c5888dcd283.png"
IMG_SUNFLOWER       = "https://s3.trawaoil.ru/pub/alone/continued/elsefor/e3e330f5-e9a0-4478-a7fd-eb0e4080b170.png"
IMG_FIBER_MIX       = "https://s3.trawaoil.ru/pub/increased/offices/smaller/50109285-9fc8-46b4-9c6f-6f2ebe1db46a.png"
IMG_FIBER_HEDGEHOG  = "https://s3.trawaoil.ru/pub/enough/anything/watched/f8da969e-7cce-4934-b298-7b9de8ae0e86.png"
IMG_CEDAR_FLOUR     = "https://s3.trawaoil.ru/pub/before/think/lettersfreedom/e83f2b39-4fc5-435c-9ceb-97e08064cd41.png"
IMG_ALMOND_FLOUR    = "https://s3.trawaoil.ru/pub/elsefor/smell/there/19d686d5-f039-4592-91b1-108bab86f494.png"
IMG_WALNUT_FLOUR    = ""  # URL повреждён при сборке — нужно обновить вручную
IMG_SUNFLOWER_FLOUR = "https://s3.trawaoil.ru/pub/herhe/yourself/could/9835aad8-1a21-4afa-ae54-fb2de1c85736.png"
IMG_LINSEED_FLOUR   = "https://s3.trawaoil.ru/pub/destroying/could/doanything/66179d6d-19ab-4a82-b9c3-f7684318ed66.png"
IMG_PUMPKIN_FLOUR   = "https://s3.trawaoil.ru/pub/opened/inventing/eleven/079cda8f-d016-43bc-b5f0-ea81f9315bf8.png"
IMG_APRICOT_FLOUR   = "https://s3.trawaoil.ru/pub/fairhaired/party/south/c0b466d6-9558-49e7-9dc9-cb6c499e1f94.png"
IMG_DRY_SKIN        = "https://s3.trawaoil.ru/pub/disobeyed/needed/little/39062fb1-2264-434b-95b6-aaaded5fb70a.png"
IMG_ROLLER          = "https://s3.trawaoil.ru/pub/places/window/round/ef1cfeff-3a45-4df0-a9c1-2f422ec04c23.png"
IMG_HIDROLAT        = "https://s3.trawaoil.ru/pub/shouted/believed/sixty/5240560b-fdef-4ae7-8a34-01415ff4a6c0.png"
IMG_KANTUCHCHI      = "https://s3.trawaoil.ru/pub/always/probably/vaporized/8f3e1f76-0db1-4e22-b52c-3eca621b785a.png"
IMG_DESSERTS_PARTNER = "https://s3.trawaoil.ru/pub/something/touched/young/f4d5122c-7059-47fd-a405-afa48f48be29.png"

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
# Структура каждого продукта:
# name        — название
# photo_url   — ссылка на фото с сайта (пустая строка = карточка без фото)
# benefits    — список из 3 пунктов пользы (для детей: вкус, способ, объём)
# emotion     — эмоциональная фраза
# url         — ссылка с UTM на страницу товара
# is_partner  — True только для продуктов партнёров в разделе «Десерты»

PRODUCTS: dict[str, list[dict]] = {

    # ── 👩 Масла для женщин ────────────────────────────────────────────────────
    "women_oils": [
        {
            "name": "Льняное масло",
            "photo_url": IMG_LINSEED,
            "benefits": [
                "Содержит омега-3 жирные кислоты и антиоксиданты",
                "Свежий травянисто-ореховый вкус, солнечно-жёлтый цвет",
                "Добавляют в супы-пюре, салаты, каши — используется в сыром виде",
            ],
            "emotion": "Традиционное русское масло — бережный метод, натуральный вкус",
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
            "emotion": "Природный баланс жирных кислот — в каждой капле",
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
            "emotion": "Масло с историей из Древнего Египта — для ваших блюд",
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
            "emotion": "Сибирский кедр — кормилец тайги — на вашем столе",
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
            "emotion": "Четыре цели — четыре микса — одна упаковка",
            "url": f"https://trawaoil.ru/p/mini-set-funkcionalnyh-masel-TRAWA--Vegetarian-660d328824dd6523315ca1b1{UTM}",
        },
    ],

    # ── 👨 Масла для мужчин ────────────────────────────────────────────────────
    "men_oils": [
        {
            "name": "Масло чёрного тмина",
            "photo_url": IMG_BLACKSEED,
            "benefits": [
                "Редкое масло с пикантным пряным вкусом и перечной остринкой",
                "Происхождение сырья: Индия; 99,9 г жира на 100 г",
                "Добавляют в горячие супы и овощные блюда или принимают в чистом виде",
            ],
            "emotion": "Редкое масло с характером — для тех, кто ценит особенное",
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
            "emotion": "Кедр питает там, где нужна сила",
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
            "emotion": "Природный баланс — в каждой ложке",
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
            "emotion": "Насыщенный вкус тыквы — в каждой капле",
            "url": f"https://trawaoil.ru/p/maslo-tykvennoe-syrodavlennoe-61fbbd8b794ca429609210a7{UTM}",
        },
    ],

    # ── 👶 Масла для детей (ТОЛЬКО вкус, способ применения, объём) ─────────────
    "children_oils": [
        {
            "name": "Конопляное масло",
            "photo_url": IMG_HEMP,
            "benefits": [
                "Яркий травянисто-ореховый вкус",
                "Для заправки каш, рагу, соусов и салатов",
                "Объём: 250 мл",
            ],
            "emotion": "Вкусно и привычно — без лишних слов",
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
            "emotion": "Знакомый вкус в каждом блюде",
            "url": f"https://trawaoil.ru/p/maslo-podsolnechnoe-syrodavlennoe-61fbbd89794ca42960920f65{UTM}",
        },
    ],

    # ── 🍳 Масла для жарки ─────────────────────────────────────────────────────
    "frying": [
        {
            "name": "Масло ГХИ",
            "photo_url": IMG_GHI,
            "benefits": [
                "Без лактозы и казеина — очищено от молочных примесей в процессе топления",
                "Высокая точка дымления — подходит для приготовления пищи",
                "Натуральное топлёное сливочное масло из Адыгеи — 99,8% жира",
            ],
            "emotion": "Жидкое золото аюрведы — на вашей кухне",
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
            "emotion": "Одно из древнейших масел мира — в вашей кулинарии",
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
            "emotion": "Любимое масло Екатерины Великой — у вас на столе",
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
            "emotion": "Арахис — не орех, а бобовое. И очень вкусное масло",
            "url": f"https://trawaoil.ru/p/maslo-arahisovoe-syrodavlennoe--61fbbd87794ca42960920d40{UTM}",
        },
    ],

    # ── 🌿 Пищеварение ─────────────────────────────────────────────────────────
    "digestion": [
        {
            "name": "Клетчатка — сбалансированный микс",
            "photo_url": IMG_FIBER_MIX,
            "benefits": [
                "36 г пищевых волокон на 100 г продукта",
                "Состав: обезжиренные семена льна, подсолнечника и миндаль",
                "Добавляют в каши, смузи, соки или разводят с водой",
            ],
            "emotion": "Суточная норма клетчатки — просто и вкусно",
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
            "emotion": "Клетчатка нового поколения — каждая ложка содержит 1 г ежовика",
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
            "emotion": "Лёгкость изнутри — каждый день",
            "url": f"https://trawaoil.ru/p/muka-iz-kedrovogo-oreha-bez-glyutena-61fbbd8a794ca42960920fa8{UTM}",
        },
    ],

    # ── 🧁 Для выпечки ─────────────────────────────────────────────────────────
    "baking": [
        {
            "name": "Мука из миндального ореха",
            "photo_url": IMG_ALMOND_FLOUR,
            "benefits": [
                "Содержит витамины А, E и группы B; богата растительным белком",
                "Низкий гликемический индекс — 25 единиц; без глютена",
                "Нежная текстура для кексов, печенья, макарун и кляра",
            ],
            "emotion": "Выпечка без глютена — нежная и вкусная",
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
            "emotion": "Тайга в каждом пироге",
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
            "emotion": "Польза незаметно, вкус — отлично",
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
            "emotion": "Тыквенный пирог, как у бабушки — только лучше",
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
            "emotion": "Выпечка с насыщенным ореховым вкусом",
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
            "emotion": "Простая замена — большая польза",
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
            "emotion": "Вкус лета в зимней выпечке",
            "url": f"https://trawaoil.ru/p/muka-iz-abrikosovoy-kostochki-bez-glyutena-677fc72fcabf41675918ea8b{UTM}",
        },
    ],

    # ── 🌸 Косметика ───────────────────────────────────────────────────────────
    "cosmetics": [
        {
            "name": "Масло для сухой кожи",
            "photo_url": IMG_DRY_SKIN,
            "benefits": [
                "Состав: кунжутное масло, эфирное масло лаванды, мяты перечной, витамин E",
                "Содержит витамин Е — природный антиоксидант",
                "Для лица (1–2 капли), волос (маска 15–20 мин) и тела (после душа)",
            ],
            "emotion": "Натуральный уход — без синтетических добавок",
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
            "emotion": "Красота в твоих руках — буквально",
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
            "emotion": "Природная свежесть — каждое утро",
            "url": f"https://trawaoil.ru/p/gidrolat-zizifora-63500d3ec40257388ce8fa65{UTM}",
        },
    ],

    # ── 🍫 Десерты без сахара ──────────────────────────────────────────────────
    # Правило: сначала продукты TRAWA (is_partner=False), потом партнёры
    "desserts": [
        {
            "name": "Сладости TRAWA",
            "photo_url": IMG_KANTUCHCHI,
            "benefits": [
                "Кантуччи без сахара из безглютеновой муки — собственное производство",
                "Состав: рисовая, амарантовая, льняная мука, сироп цикория, миндаль",
                "Хрустящая текстура — идеально к чаю, кофе и десертным винам",
            ],
            "emotion": "Десерт без сожалений — такое бывает",
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
            "emotion": "Сладкая жизнь без сахара — реально",
            "url": f"https://trawaoil.ru/c/deserty{UTM}",
            "is_partner": True,
        },
    ],

    # ── 🧄 Деликатесы и соусы (подраздел «Деликатесы и суперфуды») ──────────────
    "delicacies": [
        {
            "name": "Соус Песто веганский",
            "photo_url": IMG_PESTO,
            "benefits": [
                "Состав: масло подсолнечное TRAWA, свежий базилик, грецкий орех, лимон, чеснок, соль",
                "Без консервантов, красителей и усилителей вкуса — без термической обработки",
                "Для пасты, брускетты, салатов и горячих блюд",
            ],
            "emotion": "Живой вкус в каждой ложке — достаточно открыть крышку",
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
            "emotion": "Деталь, которая меняет всё блюдо",
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
            "emotion": "Капля вкуса — и блюдо становится другим",
            "url": f"https://trawaoil.ru/c/masla{UTM}",
        },
    ],

    # ── 🌾 Клетчатка и мука (подраздел «Деликатесы и суперфуды») ────────────────
    "fiber": [
        {
            "name": "Клетчатка — сбалансированный микс",
            "photo_url": IMG_FIBER_MIX,
            "benefits": [
                "36 г пищевых волокон на 100 г — натуральный источник клетчатки",
                "Состав: обезжиренные семена льна, подсолнечника и миндаль",
                "Добавляют в йогурт, смузи, каши или разводят с водой",
            ],
            "emotion": "Начни день правильно — с заботы о микробиоме",
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
            "emotion": "Природный интеллект — для умного желудка",
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
            "emotion": "Лёгкость изнутри — каждый день",
            "url": f"https://trawaoil.ru/p/muka-iz-kedrovogo-oreha-bez-glyutena-61fbbd8a794ca42960920fa8{UTM}",
        },
    ],

    # ── 🌟 Хиты продаж ────────────────────────────────────────────────────────
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

# Словарь: ключ категории → читаемое название темы (для аналитики)
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
