from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend       #认证后端 提供了一个可扩展的系统
import face_recognition
from django.db.models import Q

from Webpage.models import UserFaceImage

class FaceIdAuthBackend(ModelBackend):
    def authenticate(self, username=None, password=None, face_id=None, **kwargs):
        try:
            
            user = User.objects.get(username=username)
            #  if user.check_password(password) and self.check_face_id(face_id=user.userfaceimage.image, uploaded_face_id=face_id):
            if  self.check_face_id(face_id=user.userfaceimage.image, uploaded_face_id=face_id):
                return user
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            User().set_password(password)

        # Version2
    # def authenticate(self, username=None, password=None, face_id=None, **kwargs):
    #     try:
    #         user = User.objects.get(username=username)
    #         if self.check_face_id(face_id=user.userfaceimage.image, uploaded_face_id=face_id):
    #             return user
    #     except User.DoesNotExist:
    #         return None




    def check_face_id(self, face_id=None, uploaded_face_id=None):
        confirmed_image = face_recognition.load_image_file(face_id)
        uploaded_image = face_recognition.load_image_file(uploaded_face_id)

        face_locations = face_recognition.face_locations(uploaded_image)
        if len(face_locations) == 0:
            return False

        confirmed_encoding = face_recognition.face_encodings(confirmed_image)[0]
        unknown_encoding = face_recognition.face_encodings(uploaded_image)[0]

        results = face_recognition.compare_faces([confirmed_encoding], unknown_encoding)

        if results[0] == True:
            return True

        return False

# def recognize_face(id_image, q_image):
#     """
#     :param image: image of the face in the id
#     :param q_image: image of the face from the cam
#     :return:
#     """
#     q_face_encoding = face_recognition.face_encodings(id_image)[0]

#     face_locations = face_recognition.face_locations(q_image)
#     face_encodings = face_recognition.face_encodings(q_image, face_locations)

#     # Loop through each face in this image
#     for face_encoding in face_encodings:
#         # See if the face is a match for the known face(s)
#         match = face_recognition.compare_faces([q_face_encoding], face_encoding)

#         result = False
#         if match[0]:
#             result = True
#         return result

