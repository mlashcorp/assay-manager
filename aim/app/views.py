from app import app, db, models
from flask import render_template, request, flash, redirect, url_for, jsonify, json
from forms import RegistrationForm
from datetime import datetime
import sys,traceback, os
from werkzeug.utils import secure_filename
from get_jc_results import *

ALLOWED_EXTENSIONS = set(['csv'])
API_KEY = "AIzaSyCuf4WGy_cr9ldApn5oVy4FKfz7iCixWbg"

@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for('register'))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

    

@app.route('/get_jc_result/<string:serial>', methods=['GET'])
def get_jc_result(serial):
    print "Got a request for: "+str(serial)
    result = models.JCResults.query.all()
    
    outbound = []
    outbound2 = []
    for entry in result:
      if entry.jc_id == serial:
        outbound.append(entry)
        
    for data in outbound:
        data_map = vars(data)
        data_map['_sa_instance_state'] = ""
        data_map['assay_date'] = "{:%d%m%Y}".format(data_map['assay_date'])
        outbound2.append(data_map)
        
    return json.dumps(outbound2),200
  
@app.route('/upload_jc_results', methods=['GET','POST'])
def upload_jc_results():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            jc_results = get_results(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            inserted_data = []
            
            for result in jc_results:
                try:
                    print str(result.jc_id)+"_"+str(result.date)
                    serial = str(result.jc_id)+"_"+"{:%d%m%Y}".format(result.date)+"_"+str(result.assay_number1)+"_"+str(result.assay_number2)
                    data = models.JCResults(id=serial,jc_id=result.jc_id,assay_date=result.date,\
                                   assay_number1=int(result.assay_number1),assay_number2=int(result.assay_number2),\
                                   N1=result.results1[0],L1=result.results1[1],M1=result.results1[2],E1=result.results1[3],B1=result.results1[4],WBC1=result.results1[5],\
                                   N2=result.results2[0],L2=result.results2[1],M2=result.results2[2],E2=result.results2[3],B2=result.results2[4],WBC2=result.results2[5])
                                   
                    db.session.add(data)
                    db.session.commit()
                    inserted_data.append(serial)
                    print "inserted "+str(serial)
                except:
                    print "Error inserting in Database: " + str(serial)
          
            
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''
  
  
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        assay_id = form.assay_id.data
        assay_number = form.assay_number.data
        date = form.assay_date.data
        jc_id = form.jc_sample.data
        serial_number = str(assay_id)+"_"+str(assay_number)+"_"+str(date.day).zfill(2)+"-"+str(date.month).zfill(2)+"-"+str(date.year).zfill(4)+"_"+str(jc_id)
        
        #Add to DB
        try:
            data = models.AssayJCData(id=serial_number,assay_id=assay_id,\
                                   assay_number=int(assay_number),\
                                   assay_date=date,jc_id=jc_id)
            db.session.add(data)
            db.session.commit()
        except:
            print "Exception in user code:"
            print '-'*60
            traceback.print_exc(file=sys.stdout)
            print '-'*60
            return "Error inserting in Database. What are you doing man??\n",409
    
    
        flash('Assay data logged as: '+str(serial_number))
        return redirect(url_for('register'))
    return render_template('register.html',form = form)
