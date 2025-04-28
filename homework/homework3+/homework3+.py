import decimal
import logging
from pywebio.input import slider, FLOAT, NUMBER
from pywebio.input import input as pw_input
from pywebio.output import put_html, put_success

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("shop.log"), logging.StreamHandler()],
)
logging.info("info")
logging.debug("debug")
put_html("<h1>Welcome to our Fruit Shop</h1>")

price_apple = decimal.Decimal("52.75")
price_banana = decimal.Decimal("81.40")

apple_weight = slider(
    "Вага яблук", type=FLOAT, min_value=0, max_value=5, value=0.15, required=True
)
banana_weight = pw_input(
    "Вага бананів", type=NUMBER, required=True, min=0, max=10, value=3
)
apple_weight = decimal.Decimal(apple_weight).quantize(
    decimal.Decimal("0.000"), rounding=decimal.ROUND_HALF_UP
)

banana_weight = decimal.Decimal(banana_weight).quantize(
    decimal.Decimal("0.000"), rounding=decimal.ROUND_HALF_UP
)
total_price_apple = (price_apple * apple_weight).quantize(
    decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP
)

total_price_banana = (price_banana * banana_weight).quantize(
    decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP
)

all_price = total_price_apple + total_price_banana

put_success(
    f"Cумма до сплати: {all_price} грн \nВартість яблук {total_price_apple} грн \nВартість бананів {total_price_banana} грн"
)
pass
