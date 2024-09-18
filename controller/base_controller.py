# from odoo import http
# from odoo.http import request
# from odoo.exceptions import AccessError
# from odoo.addons.web.controllers.session import Session


# class Custom_Session(Session):
#     @http.route('/web/session/authenticate', type='json', auth="none")
#     def authenticate(self, db, login, password, base_location=None):
#         print('my method call')

#         try:
#             # Rotate the session and set the cookie with max_age as None
#             if not request.db:
#                 print('my method call')
#                 http.root.session_store.rotate(request.session, request.env)
#                 request.future_response.set_cookie(
#                     'session_id', request.session.sid,
#                     max_age=None,  # Setting max_age to None
#                     httponly=True
#                 )
#             # Call the original method from the base controller
#             # response = super(Session, self).authenticate(db, login, password, base_location)
#                 response.set_cookie('session_id', session.sid, max_age=None, httponly=True)
#                 response = super().authenticate(db, login, password, base_location)
#         except AccessError as e:
#             return {'uid': None, 'error': str(e)}

#         return response
#         # return  super(Session, self).authenticate(db, login, password, base_location)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# from odoo import http
# from odoo.http import request
# from odoo.exceptions import AccessError
# from odoo.addons.web.controllers.session import Session


# class CustomSession(Session):
#     @http.route('/web/session/authenticate', type='json', auth="none")
#     def authenticate(self, db, login, password, base_location=None):
#         print('Custom authentication method called')

#         try:
#             # Call the original authenticate method from the base controller
#             response = super().authenticate(db, login, password, base_location)

#             # Rotate the session and update the session cookie
#             if not request.db:
#                 http.root.session_store.rotate(request.session, request.env)
#                 request.future_response.set_cookie(
#                     'session_id', request.session.sid,
#                     max_age=None,  # Setting max_age to None for session expiry when browser is closed
#                     httponly=True
#                 )
                
#             return response
#         except AccessError as e:
#             return {'uid': None, 'error': str(e)}


# from odoo import http
# from odoo.http import request
# from odoo.addons.web.controllers.main import Session

# class CustomSession(Session):

#     @http.route('/web/session/authenticate', type='json', auth="none")
#     def authenticate(self, db, login, password, base_location=None):
#         # Call the original authentication method
#         response = super(Session, self).authenticate(db, login, password, base_location)

#         # Set the session timeout to None (no expiration)
#         request.session.timeout = 0

#         # Optionally, you can modify session expiration cookie parameters
#         request.session.modified = True
#         if request.session.sid:
#             ("request.session.sid>>>>>>>>>>>>>>>>>>>>>>>>>>>", request.session.sid)
#             # Set max_age of session cookie to None so it doesn't expire
#             request.set_cookie('session_id', request.session.sid, max_age=None, httponly=True)

#         return response
