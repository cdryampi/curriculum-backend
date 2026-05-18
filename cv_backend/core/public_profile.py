from django.conf import settings

from base_user.models import UserProfile


def get_public_profile():
    username = getattr(settings, "PUBLIC_PROFILE_USERNAME", "").strip()
    queryset = UserProfile.objects.select_related("user").order_by("id")
    if username:
        return queryset.filter(user__username=username).first()
    return queryset.first()


def public_profile_queryset(model, relation_field="user_profile"):
    profile = get_public_profile()
    if profile is None:
        return model.objects.none()
    return model.objects.filter(**{relation_field: profile})
