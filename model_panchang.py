from peewee import SqliteDatabase, CharField, Model, TextField, DateField, ForeignKeyField
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent

DB = SqliteDatabase(f'{BASE_DIR}/panchag_data.db')


class BaseClass(Model):
    class Meta:
        database = DB


class Date(BaseClass):
    date = DateField(unique=True, primary_key=True)


class SunRiseAndMoonRise(BaseClass):
    date = ForeignKeyField(Date, primary_key=True)
    sunrise = CharField(max_length=200,null=True)
    sunset = CharField(max_length=200,null=True)
    moonrise = CharField(max_length=200,null=True)
    moonset = CharField(max_length=200,null=True)


class Panchang(BaseClass):
    date = ForeignKeyField(Date, primary_key=True)
    tithi = CharField(max_length=200,null=True)
    nakshatra = CharField(max_length=200,null=True)
    yoga = CharField(max_length=200,null=True)
    weekday = CharField(max_length=200,null=True)
    paksha = CharField(max_length=200,null=True)

class LunarMonthAndSamvat(BaseClass):
    date = ForeignKeyField(Date, primary_key=True)
    shaka_samvat = CharField(max_length=200,null=True)
    chandramasa = CharField(max_length=200,null=True)
    vikram_samvat = CharField(max_length=200,null=True)
    gujarati_samvat = CharField(max_length=200,null=True)

class RashiAndNakshatra(BaseClass):
    date = ForeignKeyField(Date, primary_key=True)
    moonsign = CharField(max_length=200,null=True)
    nakshatra_pada = CharField(max_length=500)
    sunsign = CharField(max_length=200,null=True)
    surya_nakshatra = CharField(max_length=200,null=True)
    surya_pada = CharField(max_length=200,null=True)

class RituAndAyana(BaseClass):
    date = ForeignKeyField(Date,primary_key = True)
    drik_ritu = CharField(max_length=200,null=True)
    dinamana = CharField(max_length=200,null=True)
    vedic_ritu = CharField(max_length=200,null=True)
    ratrimana = CharField(max_length=200,null=True)
    drik_ayana = CharField(max_length=200,null=True)
    madhyahna = CharField(max_length=200,null=True)
    vedic_ayana = CharField(max_length=200,null=True)


class AuspiciousTimings(BaseClass):
    date = ForeignKeyField(Date,primary_key=True)
    brahma_muhurta = CharField(max_length=200,null=True)
    pratah_sandhya = CharField(max_length=200,null=True)
    abhijit = CharField(max_length=200,null=True)
    vijaya_muhurta = CharField(max_length=200,null=True)
    godhuli_muhurta = CharField(max_length=200,null=True)
    sayahna_sandhya = CharField(max_length=200,null=True)
    amrit_kalam = CharField(max_length=200,null=True)
    nishita_muhurta = CharField(max_length=200,null=True)

class InauspiciousTimings(BaseClass):
    date = ForeignKeyField(Date,primary_key=True)
    rahu_kalam = CharField(max_length=200,null=True)
    yamaganda = CharField(max_length=200,null=True)
    gulikai_kalam = CharField(max_length=200,null=True)
    vidaal_yoga = CharField(max_length=200,null=True)
    varjyam = CharField(max_length=200,null=True)
    dur_muhurtam = CharField(max_length=200,null=True)
    baana = CharField(max_length=200,null=True)
    bhadra = CharField(max_length=200,null=True)

class AnandadiAndTamilYoga(BaseClass):
    date = ForeignKeyField(Date,primary_key=True)
    anandadi_yoga = CharField(max_length=500)
    tamil_yoga = CharField(max_length=200,null=True)
    jeevanama = CharField(max_length=200,null=True)
    netrama = CharField(max_length=200,null=True)

class NivasAndShool(BaseClass):
    date = ForeignKeyField(Date,primary_key=True)
    homahuti = CharField(max_length=200,null=True)
    disha_shool = CharField(max_length=200,null=True)
    agnivasa = CharField(max_length=200,null=True)
    chandra_vasa = CharField(max_length=200,null=True)
    shivavasa = CharField(max_length=200,null=True)
    rahu_vasa = CharField(max_length=200,null=True)
    kumbha_chakra = CharField(max_length=200,null=True)

class OtherCalendarsAndEpoch(BaseClass):
    date = ForeignKeyField(Date,primary_key=True)
    kaliyuga = CharField(max_length=200,null=True)
    lahiri_ayanamsha =CharField(max_length=200,null=True)
    rata_die = CharField(max_length=200,null=True)
    julian_date = CharField(max_length=200,null=True)
    national_civil_date = CharField(max_length=200,null=True)
    modified_julian_day = CharField(max_length=200,null=True)
    national_nirayana_date = CharField(max_length=200,null=True)





    





