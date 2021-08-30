from new_backend import db
from sqlalchemy import ForeignKey
from datetime import datetime


class Challenge(db.Model):
    __tablename__ = 'challenges'

    id = db.Column(db.Integer(), primary_key= True)
    internal_id = db.Column(db.String(), unique = True, nullable = False)
    imageUrl = db.Column(db.String())
    language = db.Column(db.String())
    topic = db.Column(db.String())
    created = db.Column(db.DateTime())
    updated = db.Column(db.DateTime())
    srtUrl = db.Column(db.String())
    metadataString = db.Column(db.String())
    referenceAudioUrl = db.Column(db.String())
    
    category_id = db.Column(db.String(), ForeignKey('categories.internal_id'))

    def __init__(self,internal_id,imageUrl,language,topic,metadataString):

        # CHANGE THIS WHEN MOVING THE CHALLENGE FILES
        baseFetchUrlSrt = '/challenges/'
        baseFetchAudio = '/download/'

        self.internal_id = internal_id
        self.imageUrl = imageUrl
        self.language = language
        self.topic = topic
        self.srtUrl = baseFetchUrlSrt + self.internal_id + '/srt'
        self.referenceAudioUrl = baseFetchAudio + self.internal_id + '.wav'
        self.metadataString = metadataString
        self.created = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        self.updated = self.created