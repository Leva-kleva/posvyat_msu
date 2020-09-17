from django.db.models import Sum
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import *
from django.shortcuts import render, redirect
from django.http import Http404

from .scripts import score_update
from ..team.forms import TeamForm
from ..team.models import Team
from django.db import connection
from datetime import datetime

# в запросе первый конкрус не тронут
# остальные считаются также
# в кверисет суем флаг времени
# от него выводим плюсы или баллы
# или делаем имеем два запроса в зависимости от времени
# в первом когда плюсы вместо т3.балл пишем 1

class TableView(View):

    def get(self, request):
            if datetime.now() < datetime(2020, 9, 27, 12, 0):
                q = """
                    SELECT t3.name,
                        coalesce(SUM(CASE WHEN t3.conc_id = '1' then t3.ball end), -1) AS c1 ,
                        coalesce(SUM(CASE WHEN t3.conc_id = '2' then t3.ball end), -1) AS c2, 
                        coalesce(SUM(CASE WHEN t3.conc_id = '3' then t3.ball end), -1) AS c3,
                        coalesce(SUM(CASE WHEN t3.conc_id = '4' then t3.ball end), -1) AS c4,
                        coalesce(SUM(CASE WHEN t3.conc_id = '7' then t3.ball end), -1) AS c5,
                        coalesce(SUM(t3.ball)*SUM(t3.time)*0.1, 0*0.1) as score 
                    FROM (
                        SELECT t1.id as id, t1.name, t2.conc_id, t2.ball, t2.time
                        FROM team_team AS t1
                        LEFT JOIN table_ball AS t2 
                        ON t1.id = t2.team_id ) AS t3
                    GROUP BY t3.name
                    ORDER BY score DESC
                """
            else:
                q = """
                    SELECT t3.name,
                        coalesce(SUM(CASE WHEN t3.conc_id = '1' then t3.ball end), -1) AS c1 ,
                        coalesce(SUM(CASE WHEN t3.conc_id = '2' then -2 end), -3) AS c2, 
                        coalesce(SUM(CASE WHEN t3.conc_id = '3' then -2 end), -3) AS c3,
                        coalesce(SUM(CASE WHEN t3.conc_id = '4' then -2 end), -3) AS c4,
                        coalesce(SUM(CASE WHEN t3.conc_id = '7' then -2 end), -3) AS c5,
                        coalesce(SUM((t3.ball+1)/(t3.ball+1)), 0) as score 
                    FROM (
                        SELECT t1.id as id, t1.name, t2.conc_id, t2.ball, t2.time
                        FROM team_team AS t1
                        LEFT JOIN table_ball AS t2 
                        ON t1.id = t2.team_id ) AS t3
                    GROUP BY t3.name
                    ORDER BY score DESC
            """
            curs = connection.cursor()
            curs.execute(q)
            queryset = curs.fetchall()
            return render(request, "table/base.html", {"table": queryset})


class UpdateScore(View):

    def get(self, request):
        score_update()
        return redirect("/")
