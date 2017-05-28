from datetime import date, timedelta

import models
from google.appengine.ext import ndb


def get_first_day(dt, d_years=0, d_months=0):
    # d_years, d_months are "deltas" to apply to dt
    y, m = dt.year + d_years, dt.month + d_months
    a, m = divmod(m-1, 12)
    return date(y+a, m+1, 1)

def updatemodel():
    s_query = models.SoldierData.query(models.SoldierData.platoon == 'viking')
    soldier_data = s_query.fetch()

    for x in soldier_data:
        soldier_key = ndb.Key(urlsafe=x.key.urlsafe())
        soldier = soldier_key.get()
        soldier.num_certs = 0
        soldier.num_ribbons = 0
        soldier.num_badges = 0
        soldier.num_medals = 0
        soldier.num_awards = 0
        soldier.put()
