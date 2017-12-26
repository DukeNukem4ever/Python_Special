#x = input ("Введите слово")
#def countChars(chars, text):
#    n = 0
#    for char in text:
#        if char in chars or char in chars.upper():
#            n += 1
#    return n
#text = u"Текст, в кОТОРом будЕм считатЬ гласные И соГЛАсные"

#CONSTANTS = u"qwrtpsdfghjklzxcvbnm"
#word = input (u"Введите слово")
#while word:
#print (u"".join(_for_in word.decode ('cp1251')if _.lower() not in CONSTANTS))

#print (u"гласных: %i, согласных: %i" % (g, s))


CONSTANTS = u'mйцкнгшщзхъфвпрлджчсмтьб'
 
word = input(u'Введите слово ')
 
while word:
    print(u"".join(_ for _ in word.decode('cp1251') if _.lower() not in CONSTANTS))
    word = input(u'Введите слово ')
