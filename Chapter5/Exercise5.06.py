count = 0
mile1 = 1
kilometer1 = 0
mile2 = 0
kilometer2 = 20
print("Miles        Kilometers | Kilometers      Miles")
while count < 10:
    kilometer1 = mile1 * 1.609
    mile2 = kilometer2 / 1.609
    print(format(mile1, "2.0f"), format(kilometer1, "-18.3f") + '   |  ' + format(kilometer2, "-2.0f") + format(mile2, "18.3f"))
    kilometer2 += 5
    mile1 += 1
    count += 1
