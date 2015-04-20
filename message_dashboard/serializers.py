from rest_framework import serializers
from message_dashboard.models import DashBoard_Messages

class DashBoard_MessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model=DashBoard_Messages
        fields=('sender_name','sender_organization','sender_email','sender_phone','message_subject','message_body','is_read','create_time')



