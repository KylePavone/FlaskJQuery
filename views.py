from flask import render_template, request, redirect

from app import app
from models import db, Data
from forms import DataForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = DataForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_data = Data(jsonb_data=form.name.data)
            db.session.add(new_data)
            db.session.commit()
            return redirect('/')
    return render_template('index.html', form=form)


@app.route('/datalist')
def datalist():
    output = Data.query.all()
    return render_template('datalist.html', output=output)
