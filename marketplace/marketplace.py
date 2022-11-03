# see the requirements.txt for all packages from this app
# for create package dump file type command: pip freeze > requirements.txt
# for expand all packages for this app type command: pip install -r requirements.txt 


# for run
# set FLASK_APP=test_app.py
# python -m flask run
# for run over special ip (view in network) --host=[ip adress]
# python -m flask run --host=192.168.100.5
# for debugging use:set FLASK_DEBUG=1
# for deactivate debug mode use: set FLASK_DEBUG=0



import os

from flask import Flask, render_template
import grpc


from recommendations_pb2 import BookCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub


app = Flask(__name__)

recommendations_host = os.getenv("RECOMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(
	f"{recommendations_host}:50051"
)

recommendations_client = RecommendationsStub(recommendations_channel)


@app.route("/")
def renfer_homepage():
	recommendations_request = RecommendationRequest(
		user_id = 1,
		category = BookCategory.MYSTERY,
		max_results = 3
	)

	recommendations_response = recommendations_client.Recommend(
		recommendations_request
	)

	return render_template(
		"homepage.html",
		recommendations = recommendations_response.recommendations,
	)


# import os

# from flask import Flask, render_template
# import grpc


# from recommendations_pb2 import BookCategory, RecommendationRequest
# from recommendations_pb2_grpc import RecommendationsStub


# app = Flask(__name__)

# recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
# recommendations_channel = grpc.insecure_channel(
#     f"{recommendations_host}:50051"
# )
# recommendations_client = RecommendationsStub(recommendations_channel)


# @app.route("/")
# def render_homepage():
#     recommendations_request = RecommendationRequest(
#         user_id=1, category=BookCategory.MYSTERY, max_results=3
#     )
#     recommendations_response = recommendations_client.Recommend(
#         recommendations_request
#     )
#     return render_template(
#         "homepage.html",
#         recommendations=recommendations_response.recommendations,
#     )