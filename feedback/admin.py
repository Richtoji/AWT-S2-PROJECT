from django.contrib import admin
from .models import Feedback, Issue, Suggestion, CampusPhoto, PhotoComment, PendingFeedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('category', 'target', 'rating', 'is_approved', 'created_at')
    list_filter = ('is_approved', 'category', 'rating', 'created_at')
    list_editable = ('is_approved',)
    search_fields = ('target', 'message')

@admin.register(PendingFeedback)
class PendingFeedbackAdmin(admin.ModelAdmin):
    list_display = ('category', 'target', 'rating', 'created_at')
    list_filter = ('category', 'rating')
    search_fields = ('target', 'message')
    actions = ['approve_feedbacks']

    def get_queryset(self, request):
        return super().get_queryset(request).filter(is_approved=False)

    def has_add_permission(self, request, obj=None):
        return False

    @admin.action(description='Approve selected reviews')
    def approve_feedbacks(self, request, queryset):
        queryset.update(is_approved=True)

@admin.register(Issue)
class IssueAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'priority', 'status', 'created_at')
    list_filter = ('status', 'priority', 'category', 'created_at')
    search_fields = ('title', 'description', 'location')
    list_editable = ('status', 'priority')

@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'upvotes', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')
    readonly_fields = ('created_at',)

@admin.register(CampusPhoto)
class CampusPhotoAdmin(admin.ModelAdmin):
    list_display = ('uploader_pseudonym', 'category', 'likes', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('uploader_pseudonym', 'caption')

@admin.register(PhotoComment)
class PhotoCommentAdmin(admin.ModelAdmin):
    list_display = ('commenter_pseudonym', 'photo', 'created_at')
    search_fields = ('commenter_pseudonym', 'text')
