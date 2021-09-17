# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 08:59:35 2018

@author: Administrateur
"""

from flask import Flask, render_template, url_for, request, redirect
from datetime import date, datetime, timedelta
#from flask_sqlalchemy import SQLAlchemy
#from sqlalchemy import text
#
#import werkzeug.exceptions

urldb = "postgresql://xxx:xxx@host:5432/dbname"

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = urldb
#db = SQLAlchemy(app)

# Fake db
liste_movies = [ ('Kate', 2021), ('Shang-Chi',2021),
                    ('Dune', 1984), ('Dune', 2021)]

@app.route("/")
def welcome():
    return render_template('movies.html', liste_movies=liste_movies)

#@app.route("/pittags_without_marker/<int:startdate>")
@app.route("/movies_range_year",  methods=['GET','POST'])
def movies_range_year():
    if request.method == 'GET':
        date_ref = date.today()
        return render_template('formulaire_movies.html',
               start_default = date_ref.year - 10,
               end_default = date_ref.year)
    else:  # POST
        date_debut = request.form.get('start')
        date_fin = request.form.get('end')
        start_date = int(date_debut)
        end_date = int(date_fin)
        # recuper les pittags de la base
        # sql_all = text("""select * 
        #     from movies
        #     where year between :start_date and :end_date""")
        # sql_param = {
        #         'start_date': start_date,
        #         'end_date': end_date}
        # result = db.engine.execute(sql_all, #sql_param)
        #             start_date = start_date,
        #             end_date = end_date)
        # liste_movies_filter = list(result)
        # app.logger.debug("Result from DB : {} / {}".format(
        #         result.rowcount,
        #         result.keys()))
        liste_movies_filter = [ m for m in liste_movies 
                               if start_date <= m[1] <= end_date]
        return render_template('movies_selection.html',
                               liste_movies = liste_movies_filter,
                               date_debut=date_debut,
                               date_fin=date_fin)
    


















