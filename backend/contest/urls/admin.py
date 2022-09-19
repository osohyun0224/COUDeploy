from django.conf.urls import url

from ..views.admin import ContestAnnouncementAPI, ContestAPI, ACMContestHelper, DownloadContestSubmissions, ContestImageUploadAPI

urlpatterns = [
    url(r"^contest/?$", ContestAPI.as_view(), name="contest_admin_api"),
    url(r"^contest/announcement/?$", ContestAnnouncementAPI.as_view(), name="contest_announcement_admin_api"),
    url(r"^contest/acm_helper/?$", ACMContestHelper.as_view(), name="acm_contest_helper"),
    url(r"^download_submissions/?$", DownloadContestSubmissions.as_view(), name="acm_contest_helper"),
    url(r"^upload_contest_img/?$", ContestImageUploadAPI.as_view(), name="upload_contest_img_api"),
]
