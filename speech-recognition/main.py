import os
import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_watson.websocket import RecognizeCallback, AudioSource
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from secrets import WATSON_API_KEY, WATSON_URL

authenticator = IAMAuthenticator(WATSON_API_KEY)
speech_to_text = SpeechToTextV1(authenticator=authenticator)
speech_to_text.set_service_url(WATSON_URL)
file_name = 'test00'


class MyRecognizeCallback(RecognizeCallback):
    def __init__(self):
        RecognizeCallback.__init__(self)

    def on_data(self, data):
        # print(json.dumps(data, indent=2))
        with open(f'{file_name}.json', 'w') as outfile:
            json.dump(data, outfile, indent=2, ensure_ascii=False)

    def on_error(self, error):
        print(f'Error received: {error}')

    def on_inactivity_timeout(self, error):
        print(f'Inactivity timeout: {error}')


my_recognize_callback = MyRecognizeCallback()

with open(os.path.join('audio-files', f'{file_name}.wav'), 'rb') as audio_file:
    audio_source = AudioSource(audio_file)
    speech_to_text.recognize_using_websocket(
        audio=audio_source,
        content_type='audio/wav',
        recognize_callback=my_recognize_callback,
        model='pt-BR_BroadbandModel',
        max_alternatives=1,
        timestamps=True
    )
