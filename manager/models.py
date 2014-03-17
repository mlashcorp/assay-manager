from manager import db

class assay_metadata(db.Model):
    host = db.Column(db.String(128), unique = False)
    date = db.Column(db.DateTime)
    versions = db.Column(db.String(512))
    assay_id = db.Column(db.String(64),primary_key = True)

    def __repr__(self):
        return '<Assay %r>' % (self.assay_id)