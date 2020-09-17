from django.contrib.auth.models import User
from .models import Team
from random import randint
from datetime import datetime


symb = [
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
    "A", "a", "B", "b", "C", "c", "D", "d", "E", "e",
    "F", "f", "G", "g", "H", "h", "!", "$", "%",
    "N", "n", "J", "j"
    ]


def generate_password():
    pw = ""
    for i in range(randint(10, 15)):
        pw += symb[randint(0, len(symb)-1)]
    return pw


def create_users():
    team = Team.objects.all()
    f = open("log_pass_"+str(datetime.now()), 'w')
    for t in team:
        if t.account:
            pass
        else:
            try:
                p = generate_password()
                user = User.objects.create_user(username=str(t.cap.mail),
                                                email=t.cap.mail,
                                                password=p)
                t.account = user
                t.save()
                f.write(t.name + " " + str(t.cap.mail) + " " + str(p) + "\n")
                print(t.cap.mail, p)
                #send_mess
            except:
                f.write(t.name + '\n')
    f.close()
