from flask import render_template, flash, redirect, request
from manager import app, db, models
import datetime
import traceback, sys , re

@app.route('/')
@app.route('/index')
def index():
  data = models.assay_metadata.query.all()
  return render_template("list.html",
        assay_data = data)


  
@app.route('/upload_data', methods = ['POST'])
def upload_data():
    
    expected_parameters= ["host","versions","id"]
    #Validate parameters
    for parameter in expected_parameters:
      if not parameter in request.form:
        return "Wrong parameters\n",400
    input_host = request.form.get("host")
    input_versions = request.form.get("versions")
    input_id = request.form.get("id")
    
    #Validate that, at most, there are two ID's in DB
    sub_id = input_id.split('_')[0]
    sub_alpha_id = re.findall("[A-Z]+",input_id)
    
    #Getting the entire DB! Such efficiency!
    stored_data = models.assay_metadata.query.all()
    match_count = 0
    
    #Count how many entries in the DB have the same id ALPHA start
    stored_ids_from_same_person = []
    for entry in stored_data:
      entry_alpha_id = re.findall("[A-Z]+",entry.assay_id)
      if entry_alpha_id == sub_alpha_id:
        stored_ids_from_same_person.append(str(entry.assay_id))
        
    #Count how many entries in the DB hace the same id ALPHANUM start
    for entry in stored_data:
      entry_sub_id = entry.assay_id.split('_')[0]
      if sub_id == entry_sub_id:
        match_count += 1
    
    print "match_count is: "+str(match_count)
    if match_count >= 2:
      return_str = "Already have two entries with that id!\n List of saved ids: "
      for entry in stored_ids_from_same_person:
        return_str += str(entry) + "\n"
      return return_str,409
        
    #Add to DB
    try:
      data = models.assay_metadata(host=input_host,\
                                   date=datetime.datetime.utcnow(),\
                                   versions=input_versions,assay_id=input_id)
      db.session.add(data)
      db.session.commit()
    except:
      return "Error inserting in Database. What are you doing man??\n",409
    
    return "OK", 201