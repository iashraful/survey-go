'''
Anything we add as router we need put the router here.
'''

# V1
import api.survey.routers.v1.survey as survey_v1_routes
import api.survey.routers.v1.survey_response as survey_response_v1_routes


v1_routes = [
    survey_v1_routes.router,
    survey_response_v1_routes.router,
]

v2_routes = [
]
