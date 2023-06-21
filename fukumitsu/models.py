from django.db import models

#宿泊顧客テーブル
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, null=True)
    phone_num = models.IntegerField(null=True)
    birth = models.DateField(null=True)

#家族顧客情報テーブル
class Family(models.Model):
    family_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    relationship = models.CharField(max_length=100, null=True)
    birth = models.DateField(null=True)

#宿泊部屋情報テーブル
class Room(models.Model):
    room_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    people = models.IntegerField()
    price = models.IntegerField()
    filename = models.CharField(max_length=100)
    contents = models.TextField()

#予約情報テーブル
class Reserve(models.Model):
    reserve_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    stay_people = models.IntegerField()
    check_in = models.DateField()
    chack_out = models.DateField()

#旅館からのお知らせ情報テーブル
class Information(models.Model):
    information_id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=100)
    contents = models.TextField()
    time = models.DateField()

#お問い合わせ内容テーブル
class Contact_us(models.Model):
    contact_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contents = models.TextField()

#観光地テーブル
class Sightseeing(models.Model):
    sightseeing_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    contents = models.TextField()
    filename = models.CharField(max_length=100)
