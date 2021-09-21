'''
Anything we add as router we need put the router here.
'''

# V1
import api.auth.routers.v1.users as user_v1_routes
import api.auth.routers.v2.users as user_v2_routes


v1_routes = [
    user_v1_routes.router
]

v2_routes = [
    user_v2_routes.router
]
