import json
from flask import request
from flask import Response
from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin
import random
import string
from src.helpers.sms import send_sms_to


def create_app():
    app = Flask(__name__)
    cors = CORS(app)

    # dictionary to temporarily store session_d and photos
    session_photo_map = {
        "test": ["dummy_photo", '1234']
    }

    # desktop client gets a session id by calling this API
    @app.route('/session/<to_phone_number>', methods = ['GET'])
    def generateSessionId(to_phone_number):
        app.logger.info("reached generate sessionId api")
        session_id = _get_random_string(8)
        send_sms_to(
            # to_phone_number="+18313468659",
            to_phone_number=to_phone_number,
            message="[Yelp-hackathon-test] https://ericucsc.github.io/photo-cross-platform-mobile-client/{}".format(
                session_id
            ),
        )

        try:
            res = {
                'status': 200,
                'session_id': session_id,
            }
            # send sesssion_id to mobile (notification)
            return jsonify(res)
        except Exception as e:
            response = {
                'status': 500,
                'message': str(e),
            }
            return jsonify(response), 500

    def _get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str

    # after receiving photos from mobile, desktop client deletes the session id
    @app.route('/session/<session_id>', methods = ['DELETE'])
    def deleteSessionId(session_id):
        app.logger.info("reached delete sessionId api")
        try:
            del session_photo_map[session_id]
            response = {
                'status': 200,
                'message': f'{session_id} is removed',
            }
            return jsonify(response)
        except Exception as e:
            response = {
                'status': 500,
                'message': f"{session_id} doesn't exist",
            }
            return jsonify(response), 500



    # desktop client provides session id and gets photos if available
    @app.route('/photos/<session_id>', methods = ['GET'])
    def getPhotos(session_id):
        app.logger.info("reached get photos api")
        print('session_id:', session_id)

        try:
            photos = session_photo_map.get(session_id)
            if photos is not None:
                photos = list(photos)
                del session_photo_map[session_id]

            response = {
                'status': 200,
                'message': photos,
            }
            return jsonify(response)
        except Exception as e:
            response = {
                'status': 500,
                'message': f"session_id doesn't exist",
            }
            return jsonify(response), 500


    # mobile client provides session id and selected photos to upload to desktop
    @app.route('/photos/<session_id>', methods = ['POST'])
    def postPhotos(session_id):
        app.logger.info("reached post photos api")

        try:
            photos = set(request.json)

            if session_id in session_photo_map.keys():
                session_photo_map[session_id].update(photos)
            else:
                session_photo_map[session_id] = photos

            response = {
                'status': 200,
                'message': 'OK',
            }
            return jsonify(response)
        except Exception as e:
            print(str(e))
            response = {
                'status': 500,
                'message': str(e),
            }
            return jsonify(response), 500

    return app

if __name__=="__main__":
    app = create_app()
    app.run()
