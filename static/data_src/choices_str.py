# FROM DATABASE
color_choices = [
    ('белый', 'белый'),
    ('золотистый', 'золотистый'),
    ('красный', 'красный'),
    ('розовый', 'розовый'),
    ('серебристый', 'серебристый'),
    ('синий', 'синий'),
    ('чёрный', 'чёрный'),
    ('серый', 'серый')
]

illumination_choices = [
    ('ARGB', 'ARGB'),
    ('RGB', 'RGB'),
    ('белая', 'белая'),
    ('голубая', 'голубая'),
    ('зелёная', 'зелёная'),
    ('красная', 'красная'),
    ('многоцветная', 'многоцветная'),
    ('нет', 'нет'),
    ('оранжевая', 'оранжевая'),
    ('синяя', 'синяя')
]

fans_set_choices = [
    ('1 x 40', '1 x 40'),
    ('1 x 80', '1 x 80'),
    ('2 x 92', '2 x 92'),
    ('2 x 120', '2 x 120'),
    ('3 x 120', '3 x 120'),
    ('3 x 140', '3 x 140'),
    ('4 x 120', '4 x 120'),
    ('4 x 140', '4 x 140'),
    ('5 x 120', '5 x 120'),
    ('5 x 140', '5 x 140'),
    ('нет', 'нет')
]

psu_choices = [
    ('верхнее', 'верхнее'),
    ('нижнее', 'нижнее'),
    ('заднее', 'заднее'),
    ('переднее', 'переднее'),
    ('внешнее', 'внешнее')
]

motherboard_form_choices = [
    ('E-ATX', 'E-ATX'),
    ('Flex-ATX', 'Flex-ATX'),
    ('Micro-ATX', 'Micro-ATX'),
    ('Mini-ATX', 'Mini-ATX'),
    ('Mini-DTX', 'Mini-DTX'),
    ('Mini-ITX', 'Mini-ITX'),
    ('SSI-CEB', 'SSI-CEB'),
    ('SSI-EEB', 'SSI-EEB'),
    ('Standard-ATX', 'Standard-ATX'),
    ('Thin mini-ITX', 'Thin mini-ITX'),
    ('UCCF', 'UCCF'),
    ('XL-ATX', 'XL-ATX'),
]

type_size_choices = [
    ('Cube/Desktop', 'Cube/Desktop'),
    ('Desktop', 'Desktop'),
    ('Dual Tower', 'Dual Tower'),
    ('Full-Tower', 'Full-Tower'),
    ('Micro-Tower', 'Micro-Tower'),
    ('Mid-Tower', 'Mid-Tower'),
    ('Mini-Tower', 'Mini-Tower'),
    ('NUC', 'NUC'),
    ('Slim-Desktop', 'Slim-Desktop'),
    ('Slim-Tower', 'Slim-Tower'),
    ('Super-Tower', 'Super-Tower'),
    ('Ultra-Tower', 'Ultra-Tower'),
    ('Pedestal', 'Pedestal')
]

manufacturer_choises = [
    ('1STPLAYER', '1STPLAYER'),
    ('ABCONCORE', 'ABCONCORE'),
    ('AeroCool', 'AeroCool'),
    ('Akasa', 'Akasa'),
    ('ASUS', 'ASUS'),
    ('AZZA', 'AZZA'),
    ('be quiet!', 'be quiet!'),
    ('CaseCom', 'CaseCom'),
    ('ChiefTec', 'ChiefTec'),
    ('CoolerMaster', 'CoolerMaster'),
    ('Zalman', 'Zalman'),
    ('Thermaltake', 'Thermaltake'),
    ('SilverStone', 'SilverStone'),
    ('GAMDIAS', 'GAMDIAS'),
    ('DEXP', 'DEXP')
]

# FROM FORMS

PRICE_CHOICES = [
    ('', 'Все цены'),
    ('1099-3000', 'Менее 3000'),
    ('3001-4500', '3001-4500'),
    ('4501-6000', '4501-6000'),
    ('6001-10000', '6001-10000'),
    ('10001-15000', '10001-15000'),
    ('15001-29999', '15001 и более'),
]

MANUFACTURER_CHOICES = [
    ('', 'Все производители'),
    ('1STPLAYER', '1STPLAYER'),
    ('ABCONCORE', 'ABCONCORE'),
    ('AeroCool', 'AeroCool'),
    ('Akasa', 'Akasa'),
    ('ASUS', 'ASUS'),
    ('AZZA', 'AZZA'),
    ('be quiet!', 'be quiet!'),
    ('CaseCom', 'CaseCom'),
    ('ChiefTec', 'ChiefTec'),
    ('CoolerMaster', 'CoolerMaster'),
    ('Zalman', 'Zalman'),
    ('Thermaltake', 'Thermaltake'),
    ('SilverStone', 'SilverStone'),
    ('GAMDIAS', 'GAMDIAS'),
    ('DEXP', 'DEXP')
]

GARANTY_CHOICES = [
    ('12', '1 год'),
    ('15', '1 год, 3 мес.'),
    ('24', '2 года'),
    ('36', '3 года'),
    ('60', '5 лет'),
]

TYPE_SIZE_CHOICES = [
    ('', 'Все'),
    ('Cube/Desktop', 'Cube/Desktop'),
    ('Desktop', 'Desktop'),
    ('Dual Tower', 'Dual Tower'),
    ('Full-Tower', 'Full-Tower'),
    ('Micro-Tower', 'Micro-Tower'),
    ('Mid-Tower', 'Mid-Tower'),
    ('Mini-Tower', 'Mini-Tower'),
    ('NUC', 'NUC'),
    ('Slim-Desktop', 'Slim-Desktop'),
    ('Slim-Tower', 'Slim-Tower'),
    ('Super-Tower', 'Super-Tower'),
    ('Ultra-Tower', 'Ultra-Tower'),
    ('Pedestal', 'Pedestal')
]

MOTHERBOARD_FORM_CHOICES = [
    ('', 'Все'),
    ('E-ATX', 'E-ATX'),
    ('Flex-ATX', 'Flex-ATX'),
    ('Micro-ATX', 'Micro-ATX'),
    ('Mini-ATX', 'Mini-ATX'),
    ('Mini-DTX', 'Mini-DTX'),
    ('Mini-ITX', 'Mini-ITX'),
    ('SSI-CEB', 'SSI-CEB'),
    ('SSI-EEB', 'SSI-EEB'),
    ('Standard-ATX', 'Standard-ATX'),
    ('Thin mini-ITX', 'Thin mini-ITX'),
    ('UCCF', 'UCCF'),
    ('XL-ATX', 'XL-ATX'),
]

PSU_CHOICES = [
    ('', 'Все'),
    ('верхнее', 'верхнее'),
    ('нижнее', 'нижнее'),
    ('заднее', 'заднее'),
    ('переднее', 'переднее'),
    ('внешнее', 'внешнее')
]

FANS_SET_CHOICES = [
    ('', 'Все'),
    ('no', 'Нет'),
    ('1 x 40', '1 x 40'),
    ('1 x 80', '1 x 80'),
    ('2 x 92', '2 x 92'),
    ('2 x 120', '2 x 120'),
    ('3 x 120', '3 x 120'),
    ('3 x 140', '3 x 140'),
    ('4 x 120', '4 x 120'),
    ('4 x 140', '4 x 140'),
    ('5 x 120', '5 x 120'),
    ('5 x 140', '5 x 140'),
]

ILLUMINATION_CHOICES = [
    ('', 'Все'),
    ('no', 'Нет'),
    ('ARGB', 'ARGB'),
    ('RGB', 'RGB'),
    ('белая', 'белая'),
    ('голубая', 'голубая'),
    ('зелёная', 'зелёная'),
    ('красная', 'красная'),
    ('многоцветная', 'многоцветная'),
    ('оранжевая', 'оранжевая'),
    ('синяя', 'синяя')
]

COLOR_CHOICES = [
    ('', 'Все'),
    ('белый', 'белый'),
    ('золотистый', 'золотистый'),
    ('красный', 'красный'),
    ('розовый', 'розовый'),
    ('серебристый', 'серебристый'),
    ('синий', 'синий'),
    ('чёрный', 'чёрный'),
    ('серый', 'серый')
]

GAMERS_CHOICES = [
    (True, 'Да'),
    (False, 'Нет')
]