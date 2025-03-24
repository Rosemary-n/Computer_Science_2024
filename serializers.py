from rest_framework import serializers
from .models import User, Issue, Notification, Comment, Attachment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    
class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'
        
class NotificaticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        
class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = '__all__'
               
#custom register serializer for all models        
class RegisterSerializer(serializers.Serializer):
    user = UserSerializer()
    issues = IssueSerializer(many=True)
    notifications = NotificaticationSerializer(many=True)
    comments =CommentSerializer(many=True)
    attachments = AttachmentSerializer(many=True)  
    
    def create(self, validate_data):
        user_data = validate_data.pop('user')
        user = User.objects.create(**user_data)
        
        issues_data = validate_data.pop('issues', [])
        notifications_data = validate_data.pop('notifications', [])
        comments_data = validate_data.pop('comments', [])
        attachments_data = validate_data.pop('attachments', [])
        
        
        for issue_data in issues_data:
            Issue.objects.create(user=user, **issues_data)
            
        for notification_data in notifications_data:
            Notification.objects.create(user=user, **notifications_data)
        
        for comment_data in comments_data:
            Comment.objects.create(user=user, **comment_data)
        
        for attachment_data in attachments_data:
            Attachment.objects.create(user=user, **attachment_data)        
            
        return user
           
    
    # #check if passwords match
    # def validate(self,data):
    #     if data['password'] != data.pop('confirm_password', None):
    #         raise serializers.ValidationError({"password": "Passwords do not Match"})
     
    #  #defining specific feild requirements   
    #     role_requirements ={
    #         "student": ["student_number", "course_name", "college"],
    #         "lecturer": ["lecturer_number", "subject_taught", "department"],
    #         "academic_registrar": ["college"],
    #         "admin": ["college"]
    #     }   
        
    #     required_fields = role_requirements.get(data.get('role'), [])
    #     missing_fields = [field for field in required_fields if not data.get(field)]
        
    #     if missing_fields:
    #         raise serializers.ValidationError({data["role"]: f"Missing required fields: {', '.join(missing_fields)} "})
    #     return data()