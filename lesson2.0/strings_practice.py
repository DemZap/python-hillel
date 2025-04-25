import templates
import constants

name = input(templates.MSG_ENTER_NAME)

# name = "Олександр"
service = "пломбування зуба"
smile = "🦷"
# sms = name + service + address
# sms = (
#     "Шановний"
#     + name
#     + ", ми Вас очікуємо на послугу"
#     + service
#     + "за адресою "
#     + address
# )
sms = f"Шановний {name}, ми Вас очікуємо на послугу {service} за адресою {constants.ADDRESS}{smile}"
sms2 = templates.SMS_TEMPLATE.format(
    name=name, service="шиномонтаж", address=constants.ADDRESS, smile="🏎"
)
print(f"{sms2}")

print(sms)
