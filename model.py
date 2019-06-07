import peewee

db = peewee.SqliteDatabase('test.db')

class Data(peewee.Model):
    id = peewee.PrimaryKeyField(null=False)
    letter = peewee.CharField(max_length=1)
    vkhozhdenie = peewee.IntegerField()
    freq = peewee.FloatField()
    freq_teory = peewee.FloatField()

    class Meta:

        database = db
        db_table = 'data'


dat = Data.create(letter='q',vkhozhdenie=1, freq=2.1, freq_teory=4.2)
Data.select()