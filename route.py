from flask import render_template, flash, redirect, url_for, request
from marksheet import app, db
from marksheet.forms import Marksheetform, Updatemarksheetform
from marksheet.models import Marksheet


@app.route('/home', methods=['GET', 'POST'])
def home():
    form = Marksheetform()
    if request.method == "POST":
        if form.validate_on_submit():
            user = Marksheet.query.filter_by(rollno=form.rollno.data).first()
            if user:
                flash('That rollno is marks already submited!', 'danger')
                return redirect(url_for('home'))
            sheet = Marksheet(name= form.name.data, rollno = form.rollno.data, maths= form.maths.data, science= form.science.data, english= form.english.data)
            db.session.add(sheet)
            db.session.commit()
            flash('Your sheet has been created!', 'success')
            return redirect(url_for('home'))
    sheets = Marksheet.query.all()
    return render_template('collect_mark.html', form=form, sheets= sheets)

@app.route('/sheet/<int:sheet_id>/detele', methods=['POST'])
def delete_sheet(sheet_id):
    sheet = Marksheet.query.get_or_404(sheet_id)
    db.session.delete(sheet)
    db.session.commit()
    flash("Sheet has been successfully deleted!",'success')
    return redirect(url_for('home'))

@app.route('/sheet/<int:sheet_id>/update', methods=['GET','POST'])
def update_sheet(sheet_id):
    sheet = Marksheet.query.get_or_404(sheet_id)
    form = Updatemarksheetform()
    if form.validate_on_submit():
        sheet.name = form.name.data
        sheet.content = form.rollno.data
        sheet.maths = form.maths.data
        sheet.science = form.science.data
        sheet.english = form.english.data
        db.session.commit()
        flash("Sheet has been successfully updated!",'success')
        return redirect(url_for('home'))
    elif request.method == "GET":
        user = Marksheet.query.filter_by(id = sheet_id).first()
        form.name.data = user.name
        form.rollno.data = user.rollno
        form.maths.data = user.maths
        form.science.data = user.science
        form.english.data = user.english
        
    return render_template('update_sheet.html', form=form)






























# CREATE TABLE example ( id smallint unsigned not null auto_increment, name varchar(20) not null, constraint pk_example primary key (id) );
# INSERT INTO marksheet ( name, rollno, maths, science, english ) VALUES ('prince', 15566, 12,34,100 );




# CREATE TABLE marksheet(
#    mid INT AUTO_INCREMENT PRIMARY KEY,
#    name VARCHAR(40),
#    rollno INT UNIQUE KEY,
#    maths INT,
#    science INT,
#    english INT
# );