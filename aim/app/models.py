from app import db


class AssayJCData(db.Model):
    id = db.Column(db.String(128), index = True, primary_key = True)
    assay_id = db.Column(db.String(64), index = True)
    assay_number = db.Column(db.SmallInteger, index = True)
    assay_date = db.Column(db.DateTime)
    jc_id = db.Column(db.String(64), index = True)
    
    def __repr__(self):
        return str(assay_id)+"_"+str(assay_number)+"_"+str(assay_date)+"_"+str(jc_id)
      
      
class JCResults(db.Model):
    id = db.Column(db.String(128), index = True, primary_key = True)
    jc_id = db.Column(db.String(64), index = True)
    assay_date = db.Column(db.DateTime)
    assay_number1 = db.Column(db.SmallInteger, index = True)
    assay_number2 = db.Column(db.SmallInteger, index = True)
    
    N1 = db.Column(db.Float,index = True)
    L1 = db.Column(db.Float,index = True)
    M1 = db.Column(db.Float,index = True)
    E1 = db.Column(db.Float,index = True)
    B1 = db.Column(db.Float,index = True)
    WBC1 = db.Column(db.Float,index = True)
    
    N2 = db.Column(db.Float,index = True)
    L2 = db.Column(db.Float,index = True)
    M2 = db.Column(db.Float,index = True)
    E2 = db.Column(db.Float,index = True)
    B2 = db.Column(db.Float,index = True)
    WBC2 = db.Column(db.Float,index = True)
    
    def __repr__(self):
        return str(self.jc_id)
      
      