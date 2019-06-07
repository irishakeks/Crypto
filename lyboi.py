import model
db.connect()
a = Category(letter = 'a', vkhozhdenie = 4, freq = 0.2, freq_teory = 0.25)
a.save()