from django.db import models

# Create your models here.
#1. user_login - id, uname, passwd, u_type
class user_login(models.Model):
    uname = models.CharField(max_length=100)
    passwd = models.CharField(max_length=25)
    u_type = models.CharField(max_length=10)

    def __str__(self):
        return self.uname

#7. user_details - id, user_id, fname, lname, dob, aadhaar_no, gender, addr, pin, email, contact, status
class user_details(models.Model):
    user_id = models.IntegerField()
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=200)
    gender = models.CharField(max_length=25)
    aadhaar_no = models.CharField(max_length=25)
    age = models.CharField(max_length=25)
    addr = models.CharField(max_length=500)
    pin = models.CharField(max_length=25)
    contact = models.CharField(max_length=25)
    email = models.CharField(max_length=25)

    def __str__(self):
        return self.fname


#2. state_master - id, state_name
class state_master(models.Model):
    #id
    state_name = models.CharField(max_length=50)

#3. district_master - id, state_id, district_name
class district_master(models.Model):
    #id
    state_id = models.IntegerField()
    district_name = models.CharField(max_length=50)

#4. place_master - id, district_id, place_name
class place_master(models.Model):
    id
    district_id = models.IntegerField()
    place_name = models.CharField(max_length=50)

#5. police_station_master - id, station_name, station_type, station_descp, saddr, spin, place_id, s_contact1, s_contact2, s_email, status
class police_station_master(models.Model):
    #id
    station_name = models.CharField(max_length=500)
    station_type = models.CharField(max_length=500)
    station_descp = models.CharField(max_length=500)
    saddr = models.CharField(max_length=500)
    spin = models.CharField(max_length=50)
    place_id = models.IntegerField()
    s_contact1 = models.CharField(max_length=20)
    s_contact2 = models.CharField(max_length=20)
    s_email = models.CharField(max_length=500)
    status = models.CharField(max_length=50)

#6. station_user - id, police_station_id, user_id, name, designation, email, contact, dt, tm, status
class station_user(models.Model):
    #id
    police_station_id = models.IntegerField()
    user_id = models.IntegerField()
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    email = models.CharField(max_length=500)
    contact = models.CharField(max_length=20)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

#8. user_report_master - id, user_id, station_id, type_id, descrption, addr, place_id, dt, tm, status
class user_report_master(models.Model):
    #id
    user_id = models.IntegerField()
    station_id = models.IntegerField()
    type_id = models.IntegerField()
    descrption = models.CharField(max_length=500)
    addr = models.CharField(max_length=500)
    place_id = models.IntegerField()
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

#9. report_pics - id, report_id, pic_path, pic_info
class report_pics(models.Model):
    #id
    report_id = models.IntegerField()
    pic_path = models.CharField(max_length=150)
    pic_info = models.CharField(max_length=500)

#10. user_report_followups - id, report_id, user_id, remarks, dt, tm
class user_report_followups(models.Model):
    #id
    report_id = models.IntegerField()
    user_id = models.IntegerField()
    remarks = models.CharField(max_length=500)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)

#11. crime_type - id, type_name
class crime_type(models.Model):
    #id
    type_name = models.CharField(max_length=100)

#12. notice_board_master - id, station_id, title, pic_path, descp, dt, tm, status
class notice_board_master(models.Model):
    #id
    station_id = models.IntegerField()
    title = models.CharField(max_length=150)
    pic_path = models.CharField(max_length=500)
    descp = models.CharField(max_length=500)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

#13. look_out_master - id, station_id, name, remarks, pic, dt, tm, status
class look_out_master(models.Model):
    #id
    station_id = models.IntegerField()
    name = models.CharField(max_length=50)
    remarks = models.CharField(max_length=500)
    pic = models.CharField(max_length=500)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

#14. feedback - id, user_id, msg, dt, tm
class feedback(models.Model):
    #id
    user_id = models.IntegerField()
    msg = models.CharField(max_length=500)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)

#15. message_master - id, user1_id, user2_id, msg, dt, tm, status
class message_master(models.Model):
    #id
    user1_id = models.IntegerField()
    user2_id = models.IntegerField()
    msg = models.CharField(max_length=500)
    dt = models.CharField(max_length=50)
    tm = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
