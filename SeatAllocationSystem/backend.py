# from django.contrib.auth import get_user_model
from SeatAllocationAuthentication.models import User

from django.contrib.auth.backends import ModelBackend

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        print("Hi")
        # UserModel = get_user_model()
        try:
            print(username)
            user = User.objects.get(EmployeeEmail=username)
            if (User.objects.filter(EmployeeEmail=username)):
                if (User.objects.filter(Code=password)):
                    print("Yes")
                    print("Yot actually where you are meant to be!")
                # if user.check_password(password):
                    return user
            return None
        except User.DoesNotExist:
            return None
        
    def get_user(self, user_id):
        try:
            return User.objects.get(EmployeeName=user_id)
        except User.DoesNotExist:
            return None
        