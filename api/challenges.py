from flask import request, jsonify, send_file

from .models.challenge import Challenge
from .models.category import Category
from . import api
from .. import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from dotenv import load_dotenv
import os
import requests


@api.route('/challenges/<speechChallengeId>', methods=['GET'])
def getChallenges(speechChallengeId):

    try:
        challenge = Challenge.query.filter_by(
            internal_id=speechChallengeId).first()
    except:

        return 'Speech Challenge requested does not exist', 404

    response = {
        'id': challenge.internal_id,
        'imageUrl': challenge.imageUrl,
        'topic': challenge.topic,
        'srtUrl': challenge.srtUrl,
        'metadata': challenge.metadataString,
        'referenceAudioUrl': challenge.referenceAudioUrl,
        'created': challenge.created.__str__(),
        'updated': challenge.updated.__str__()
    }

    return response


@api.route('/create_challenge', methods=['POST'])
def createChallenge():

    internal_id = request.json.get('id')
    imageUrl = request.json.get('imageUrl')
    language = request.json.get('language')
    topic = request.json.get('topic')
    metadata = request.json.get('metadata')
    category_id = request.json.get('category_id')

    challenge = Challenge(internal_id, imageUrl, language, topic, metadata)

    in_db = Challenge.query.filter_by(internal_id=internal_id).first()
    if in_db:
        return {'message': 'Already in db!'}

    target_category = Category.query.filter_by(
        internal_id=category_id).first()
    target_category.speechChallenges.append(challenge)

    db.session.add(challenge)
    db.session.commit()

    return {'message': 'Successfully created challenge, id: {internal_id} topic: {topic}'.format(internal_id=internal_id, topic=topic)}


@api.route('/challenges/<speechChallengeId>/srt', methods=['GET'])
def getSrt(speechChallengeId):
    eos = request.args.get('eos')

    if eos == 'True':
        path = 'new_backend/api/downloads/challenges/{speechChallengeId}.srt.eos'.format(
            speechChallengeId=speechChallengeId)
        with open(path, 'r') as srt:
            return jsonify(srt.read())
    else:
        path = 'new_backend/api/downloads/challenges/{speechChallengeId}.srt'.format(
            speechChallengeId=speechChallengeId)
        with open(path, 'r') as srt:
            return jsonify(srt.read())


@api.route('/download/<file_name>', methods=['GET'])
def download(file_name):

    path = "api/downloads/challenges/{file_name}".format(
        file_name=file_name)
    return send_file(path, attachment_filename='{file_name}'.format(file_name=file_name))


@api.route('/recordings/<speechChallengeId>', methods=['GET'])
def getRecording(speechChallengeId):

    recordings = []
    return jsonify(recordings)


@api.route('/wstoken', methods=['GET'])
def getWSTOKEN():

    load_dotenv()
    token = os.environ.get('BEARER_TOKEN_ITSTUTO')
    jsonHeader = {'Authorization': f'Bearer {token}'}
    r = requests.get(
        'https://staging.amazing.itsapi.com/wstoken', headers=jsonHeader)

    return r.json()
