from recommendations_pb2 import BookCategory, RecommendationRequest

request = RecommendationRequest(
	user_id = 1,
	category = BookCategory.SCIENCE_FICTION,
	max_results = 3
)

# request.category

requestResult = request.category
print(requestResult)

# selftesting
testRequest = RecommendationRequest(
	user_id = 0,
	category = BookCategory.MYSTERY,
	max_results = 3
)
testRequestResult = testRequest.category
print(testRequestResult)