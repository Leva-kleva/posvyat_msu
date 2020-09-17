from .models import Ball
from ..team.models import Team


def score_update():
    a = Team.objects.all()
    for team in a:
        b, t = 0, 0
        ball = Ball.objects.filter(team=team)
        for obj in ball:
            b += obj.ball
            t += obj.time
        print(b, t, team.name)
        c = Team.objects.get(name=team.name)
        c.score = b*t*0.1
        c.save()
