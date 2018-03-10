# from PIL import Image
# from PIL import ImageFont
# from PIL import ImageDraw
# import datetime
# import time
# img = Image.open("im.jpg")
# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype("arial.ttf", 32)
# small_font = ImageFont.truetype("arial.ttf", 22)
# data = dict()
# with open('data.txt', 'r') as file:
#     data = eval(file.read())
#
# while True:
#     print("Введите фамилию и имя: ")
#     p_f, p_n = input().split()
#     found = False
#     for key in data:
#         if data[key][0] == p_f and data[key][3] == p_n:
#             p_key = key
#             found = True
#             break
#     if not found:
#         print("Не найдено")
#         continue
#     p_class = data[p_key][1]
#     p_sn = data[p_key][4]
#     p_age = data[p_key][5]
#     p_manta = data[p_key][6]
#     p_adc = data[p_key][7]
#     p_opv = data[p_key][8]
#     p_measles = data[p_key][9]
#     p_fluorography = data[p_key][10]
#     p_polis = data[p_key][11]
#     p_passport = data[p_key][12]
#     p_parents = data[p_key][13]
#     p_address = data[p_key][14]
#     p_ospa = data[p_key][15]
#     p_chronic = data[p_key][16]
#     p_allergy = data[p_key][17]
#     p_group_health = data[p_key][18]
#     p_group_fiz = data[p_key][19]
#     p_gendor = data[p_key][20]
#     p_kr = data[p_key][21]
#     today = datetime.datetime.now()
#     draw.text((620, 698), p_f, (5, 5, 5), font=font)
#     draw.text((870, 698), p_n, (5, 5, 5), font=font)
#     draw.text((1120, 698), p_sn, (5, 5, 5), font=font)
#     if p_gendor == 'м':
#         draw.text((550, 771), 'X', (5, 5, 5), font=font)
#     else:
#         draw.text((830, 771), 'X', (5, 5, 5), font=font)
#     a = p_age.isoformat()
#     draw.text((1200, 771), a[8:9], (5, 5, 5), font=font)
#     draw.text((1230, 771), a[9:10], (5, 5, 5), font=font)
#     draw.text((1297, 771), a[5:6], (5, 5, 5), font=font)
#     draw.text((1334, 771), a[6:7], (5, 5, 5), font=font)
#     draw.text((1403, 771), a[0:1], (5, 5, 5), font=font)
#     draw.text((1437, 771), a[1:2], (5, 5, 5), font=font)
#     draw.text((1477, 771), a[2:3], (5, 5, 5), font=font)
#     draw.text((1510, 771), a[3:4], (5, 5, 5), font=font)
#     draw.text((1270, 975), p_parents, (5, 5, 5), font=font)
#     draw.text((1060, 1069), p_class, (5, 5, 5), font=font)
#     draw.text((1200, 1143), p_ospa, (5, 5, 5), font=font)
#     draw.text((600, 1213), p_kr, (5, 5, 5), font=font)
#     if type(p_adc) is datetime.datetime:
#         draw.text((919, 1296), p_adc.strftime("%d.%m.%y"), (5, 5, 5), font=font)
#     if type(p_opv) is datetime.datetime:
#         draw.text((1160, 1296), p_opv.strftime("%d.%m.%y"), (5, 5, 5), font=font)
#     if type(p_measles) is datetime.datetime:
#         draw.text((1400, 1296), p_measles.strftime("%d.%m.%y"), (5, 5, 5), font=font)
#     draw.text((433, 1342), p_manta[p_manta.rfind(';') + 1:], (5, 5, 5), font=small_font)
#     if type(p_fluorography) is datetime.datetime:
#         draw.text((840, 1337), p_fluorography.strftime("%d.%m.%y"), (5, 5, 5), font=font)
#     draw.text((540, 1717), p_group_fiz, (5, 5, 5), font=font)
#     draw.text((1093, 2183), str(today)[8:10], (5, 5, 5), font=font)
#     draw.text((1293, 2183), str(today)[5:7], (5, 5, 5), font=font)
#     draw.text((1408, 2183), str(today)[2:4], (5, 5, 5), font=font)
#     if p_gendor == 'м':
#         draw.text((308, 1450), "здоров", (5, 5, 5), font=font)
#     else:
#         draw.text((308, 1450), "здорова", (5, 5, 5), font=font)
#     img.save("C:\\Users\\Руслан\\PycharmProjects\\doctor\\" + p_f + " " + p_n + '.jpg')
#     print("Сделано!")
#     img.show()
#     time.sleep(5)
#     exit()
import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello Dreamforce'
hello()