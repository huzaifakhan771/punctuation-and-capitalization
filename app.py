from flask import Flask, request, jsonify
from flask import make_response
import nemo
import nemo.collections.nlp as nemo_nlp
import os
from ast import literal_eval
from nltk.tokenize import TweetTokenizer


app = Flask(__name__)
model = nemo_nlp.models.PunctuationCapitalizationModel.restore_from(restore_path="punctuation_en_bert.nemo")


@app.route('/', methods=['GET'])
def index():  # put application's code here
    return jsonify({'usage examples': {
        'restorePunct': "http://localhost:8080/restorePunct?text=hello how are you",
        'capitalizeAndPunctuate': "http://localhost:8080/capitalizePunct?text=hello how are you"
        }
        }),200


@app.route('/restorePunct', methods=['GET'])
def restore_punct():  # put application's code here
    try:
        text = request.args.get('text')
        tokenized_sents = TweetTokenizer().tokenize(text)
        punctuated_list = model.add_punctuation_capitalization([text])
        punctuated = ''.join(punctuated_list)
        output = []
        lookup_idx = 0
        
        print("PUNCTUATED", punctuated)
        print("text", text)
        for i, token in enumerate(tokenized_sents):
            lookup_idx += len(token)
            if punctuated[lookup_idx] != ' ':
                output.append(
                        {'index':i,
                        'word': token,
                        'label':punctuated[lookup_idx]
                        }
                        )
                lookup_idx += 1
            lookup_idx += 1

        return jsonify({'output': output}), 200
    except Exception as e:
        print("ERROR", e)
        return jsonify({'error': 'Invalid Request',
        'usage example': "http://localhost:8080/restorePunct?text=hello how are you"}), 400


@app.route('/capitalizePunct', methods=['GET'])
def capitalize_punctuate():  # put application's code here
    try:
        text = request.args.get('text')
        print('text', text)
        punctuated_list = model.add_punctuation_capitalization([text])
        print('punc', punctuated_list)
        punctuated = ''.join(punctuated_list)

        return jsonify({'output': punctuated}), 200
    except Exception as e:
        print("ERROR", e)
        return jsonify({'error': 'Invalid Request',
        'usage example': "http://localhost:8080/capitalizePunct?text=hello how are you"}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
