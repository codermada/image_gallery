from . import db

inclusions = db.Table('inclusions',
                        db.Column('image_id', db.Integer, db.ForeignKey('images.id')),
                        db.Column('description_id', db.Integer, db.ForeignKey('descriptions.id'))
                    )

class Image(db.Model):
    __tablename__ = 'images'
    id = db.Column(db.Integer, primary_key=True)
    def __repr__(self):
        return f'<image {self.id}>'


class Description(db.Model):
    __tablename__ = 'descriptions'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500))
    images = db.relationship('Image',
                             secondary=inclusions,
                             backref=db.backref('descriptions', lazy='dynamic'),
                             lazy='dynamic')
    def __repr__(self):
        return f'<description {self.id}>'