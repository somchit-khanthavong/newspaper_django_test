from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# ແບບຟອມທີ່ໃຊ້ໃນການສ້າງບັນຊີຜູ້ໃຊ້ (Sign up)
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age', 'phone', 'address', 'date_of_birth',)

# ແບບຟອມທີ່ໃຊ້ໃນການແກ້ໄຂຂໍ້ມູນຜູ້ໃຊ້ (Update profile ໃນໜ້າ admin)
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields