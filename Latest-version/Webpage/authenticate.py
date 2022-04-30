from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend       #authenticate backend provide a extend system
import face_recognition
from django.db.models import Q

from Webpage.models import UserFaceImage

class FaceIdAuthBackend(ModelBackend):
    def authenticate(self, username=None, password=None, face_id=None, **kwargs):
        try:
            
            user = User.objects.get(username=username)
            if  self.check_face_id(face_id=user.userfaceimage.image, uploaded_face_id=face_id):
                return user
        except User.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a non-existing user (#20760).
            User().set_password(password)


    def check_face_id(self, face_id=None, uploaded_face_id=None):
        confirmed_image = face_recognition.load_image_file(face_id)     #Load image file of the registed face image (numpy array)
        uploaded_image = face_recognition.load_image_file(uploaded_face_id) #Load the image file of face image during the face login (numpy array)

        face_locations = face_recognition.face_locations(uploaded_image) #Find out Face position, Returns an array of face boundings in the image(top,right,bottom,left)
        if len(face_locations) == 0:    #Can't find out any face in the image then return false
            return False

        confirmed_encoding = face_recognition.face_encodings(confirmed_image)[0]    #face_recognition.face_encodings() basically returns a list of all the faces found in the photo. Using the index [0] to get the first found face
        unknown_encoding = face_recognition.face_encodings(uploaded_image)[0]

        results = face_recognition.compare_faces([confirmed_encoding], unknown_encoding)

        if results[0] == True:
            return True

        return False


