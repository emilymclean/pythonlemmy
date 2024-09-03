import logging

import requests
from typing import List, Optional

from .types import File
from .utils import create_session, post_handler, put_handler, get_handler, \
    create_form, file_handler

API_VERSION = "v3"


class LemmyHttp(object):

    def __init__(self, base_url: str, headers: dict = None,
                 jwt: str = None):
        """ LemmyHttp object: handles all POST, PUT, and GET operations from
        the LemmyHttp API (https://join-lemmy.org/api/classes/LemmyHttp.html)

        Args:
            base_url (str): Lemmy instance to connect to (e.g.,
                "https://lemmy.world")
            headers (dict, optional): optional headers
            jwt (str, optional): login token if not immediately using
                `LemmyHttp.login`
        """

        if not base_url.startswith("http://") and not base_url.startswith("https://"):
            base_url = "https://" + base_url

        self._base_url = base_url
        self._api_url = base_url + f"/api/{API_VERSION}"
        self._headers = headers
        self._session = create_session(self._headers, jwt)
        self.logger = logging.getLogger(__name__)

    def get_site(
        self
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/site", form)

        return result

    def create_site(
        self,
        name: str,
        sidebar: Optional[str] = None,
        description: Optional[str] = None,
        icon: Optional[str] = None,
        banner: Optional[str] = None,
        enable_downvotes: Optional[bool] = None,
        enable_nsfw: Optional[bool] = None,
        community_creation_admin_only: Optional[bool] = None,
        require_email_verification: Optional[bool] = None,
        application_question: Optional[str] = None,
        private_instance: Optional[bool] = None,
        default_theme: Optional[str] = None,
        default_post_listing_type: Optional[str] = None,
        default_sort_type: Optional[str] = None,
        legal_information: Optional[str] = None,
        application_email_admins: Optional[bool] = None,
        hide_modlog_mod_names: Optional[bool] = None,
        discussion_languages: Optional[list[int]] = None,
        slur_filter_regex: Optional[str] = None,
        actor_name_max_length: Optional[int] = None,
        rate_limit_message: Optional[int] = None,
        rate_limit_message_per_second: Optional[int] = None,
        rate_limit_post: Optional[int] = None,
        rate_limit_post_per_second: Optional[int] = None,
        rate_limit_register: Optional[int] = None,
        rate_limit_register_per_second: Optional[int] = None,
        rate_limit_image: Optional[int] = None,
        rate_limit_image_per_second: Optional[int] = None,
        rate_limit_comment: Optional[int] = None,
        rate_limit_comment_per_second: Optional[int] = None,
        rate_limit_search: Optional[int] = None,
        rate_limit_search_per_second: Optional[int] = None,
        federation_enabled: Optional[bool] = None,
        federation_debug: Optional[bool] = None,
        captcha_enabled: Optional[bool] = None,
        captcha_difficulty: Optional[str] = None,
        allowed_instances: Optional[list[str]] = None,
        blocked_instances: Optional[list[str]] = None,
        taglines: Optional[list[str]] = None,
        registration_mode: Optional[str] = None,
        content_warning: Optional[str] = None,
        default_post_listing_mode: Optional[str] = None
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/site", form)

        return result

    def edit_site(
        self,
        name: Optional[str] = None,
        sidebar: Optional[str] = None,
        description: Optional[str] = None,
        icon: Optional[str] = None,
        banner: Optional[str] = None,
        enable_downvotes: Optional[bool] = None,
        enable_nsfw: Optional[bool] = None,
        community_creation_admin_only: Optional[bool] = None,
        require_email_verification: Optional[bool] = None,
        application_question: Optional[str] = None,
        private_instance: Optional[bool] = None,
        default_theme: Optional[str] = None,
        default_post_listing_type: Optional[str] = None,
        default_sort_type: Optional[str] = None,
        legal_information: Optional[str] = None,
        application_email_admins: Optional[bool] = None,
        hide_modlog_mod_names: Optional[bool] = None,
        discussion_languages: Optional[list[int]] = None,
        slur_filter_regex: Optional[str] = None,
        actor_name_max_length: Optional[int] = None,
        rate_limit_message: Optional[int] = None,
        rate_limit_message_per_second: Optional[int] = None,
        rate_limit_post: Optional[int] = None,
        rate_limit_post_per_second: Optional[int] = None,
        rate_limit_register: Optional[int] = None,
        rate_limit_register_per_second: Optional[int] = None,
        rate_limit_image: Optional[int] = None,
        rate_limit_image_per_second: Optional[int] = None,
        rate_limit_comment: Optional[int] = None,
        rate_limit_comment_per_second: Optional[int] = None,
        rate_limit_search: Optional[int] = None,
        rate_limit_search_per_second: Optional[int] = None,
        federation_enabled: Optional[bool] = None,
        federation_debug: Optional[bool] = None,
        captcha_enabled: Optional[bool] = None,
        captcha_difficulty: Optional[str] = None,
        allowed_instances: Optional[list[str]] = None,
        blocked_instances: Optional[list[str]] = None,
        blocked_urls: Optional[list[str]] = None,
        taglines: Optional[list[str]] = None,
        registration_mode: Optional[str] = None,
        reports_email_admins: Optional[bool] = None,
        content_warning: Optional[str] = None,
        default_post_listing_mode: Optional[str] = None
    ):
        form = create_form(locals())
        result = put_handler(self._session, f"{self._api_url}/site", form)

        return result

    def leave_admin(
        self
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/user/leave_admin", form)

        return result

    def generate_totp_secret(
        self
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/user/totp/generate", form)

        return result

    def export_settings(
        self
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/user/export_settings", form)

        return result

    def import_settings(
        self
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/user/import_settings", form)

        return result

    def list_logins(
        self
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/user/list_logins", form)

        return result

    def validate_auth(
        self
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/user/validate_auth", form)

        return result

    def list_media(
        self,
        page: Optional[int] = None,
        limit: Optional[int] = None
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/account/list_media", form)

        return result

    def list_all_media(
        self,
        page: Optional[int] = None,
        limit: Optional[int] = None
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/admin/list_all_media", form)

        return result

    def update_totp(
        self,
        totp_token: str,
        enabled: bool
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/user/totp/update", form)

        return result

    def get_modlog(
        self,
        mod_person_id: Optional[int] = None,
        community_id: Optional[int] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
        type_: Optional[str] = None,
        other_person_id: Optional[int] = None,
        post_id: Optional[int] = None,
        comment_id: Optional[int] = None
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/modlog", form)

        return result

    def search(
        self,
        q: str,
        community_id: Optional[int] = None,
        community_name: Optional[str] = None,
        creator_id: Optional[int] = None,
        type_: Optional[str] = None,
        sort: Optional[str] = None,
        listing_type: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/search", form)

        return result

    def resolve_object(
        self,
        q: str
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/resolve_object", form)

        return result

    def create_community(
        self,
        name: str,
        title: str,
        description: Optional[str] = None,
        icon: Optional[str] = None,
        banner: Optional[str] = None,
        nsfw: Optional[bool] = None,
        posting_restricted_to_mods: Optional[bool] = None,
        discussion_languages: Optional[list[int]] = None,
        visibility: Optional[str] = None
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/community", form)

        return result

    def get_community(
        self,
        id: Optional[int] = None,
        name: Optional[str] = None
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/community", form)

        return result

    def edit_community(
        self,
        community_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None,
        icon: Optional[str] = None,
        banner: Optional[str] = None,
        nsfw: Optional[bool] = None,
        posting_restricted_to_mods: Optional[bool] = None,
        discussion_languages: Optional[list[int]] = None,
        visibility: Optional[str] = None
    ):
        form = create_form(locals())
        result = put_handler(self._session, f"{self._api_url}/community", form)

        return result

    def list_communities(
        self,
        type_: Optional[str] = None,
        sort: Optional[str] = None,
        show_nsfw: Optional[bool] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/community/list", form)

        return result

    def follow_community(
        self,
        community_id: int,
        follow: bool
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/community/follow", form)

        return result

    def block_community(
        self,
        community_id: int,
        block: bool
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/community/block", form)

        return result

    def delete_community(
        self,
        community_id: int,
        deleted: bool
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/community/delete", form)

        return result

    def hide_community(
        self,
        community_id: int,
        hidden: bool,
        reason: Optional[str] = None
    ):
        form = create_form(locals())
        result = put_handler(self._session, f"{self._api_url}/community/hide", form)

        return result

    def remove_community(
        self,
        community_id: int,
        removed: bool,
        reason: Optional[str] = None
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/community/remove", form)

        return result

    def transfer_community(
        self,
        community_id: int,
        person_id: int
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/community/transfer", form)

        return result

    def ban_from_community(
        self,
        community_id: int,
        person_id: int,
        ban: bool,
        remove_data: Optional[bool] = None,
        reason: Optional[str] = None,
        expires: Optional[int] = None
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/community/ban_user", form)

        return result

    def add_mod_to_community(
        self,
        community_id: int,
        person_id: int,
        added: bool
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/community/mod", form)

        return result

    def create_post(
        self,
        name: str,
        community_id: int,
        url: Optional[str] = None,
        body: Optional[str] = None,
        alt_text: Optional[str] = None,
        honeypot: Optional[str] = None,
        nsfw: Optional[bool] = None,
        language_id: Optional[int] = None,
        custom_thumbnail: Optional[str] = None
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/post", form)

        return result

    def get_post(
        self,
        id: Optional[int] = None,
        comment_id: Optional[int] = None
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/post", form)

        return result

    def edit_post(
        self,
        post_id: int,
        name: Optional[str] = None,
        url: Optional[str] = None,
        body: Optional[str] = None,
        alt_text: Optional[str] = None,
        nsfw: Optional[bool] = None,
        language_id: Optional[int] = None,
        custom_thumbnail: Optional[str] = None
    ):
        form = create_form(locals())
        result = put_handler(self._session, f"{self._api_url}/post", form)

        return result

    def delete_post(
        self,
        post_id: int,
        deleted: bool
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/post/delete", form)

        return result

    def remove_post(
        self,
        post_id: int,
        removed: bool,
        reason: Optional[str] = None
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/post/remove", form)

        return result

    def mark_post_as_read(
        self,
        post_ids: list[int],
        read: bool
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/post/mark_as_read", form)

        return result

    def hide_post(
        self,
        post_ids: list[int],
        hide: bool
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/post/hide", form)

        return result

    def lock_post(
        self,
        post_id: int,
        locked: bool
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/post/lock", form)

        return result

    def feature_post(
        self,
        post_id: int,
        featured: bool,
        feature_type: str
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/post/feature", form)

        return result

    def get_posts(
        self,
        type_: Optional[str] = None,
        sort: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
        community_id: Optional[int] = None,
        community_name: Optional[str] = None,
        saved_only: Optional[bool] = None,
        liked_only: Optional[bool] = None,
        disliked_only: Optional[bool] = None,
        show_hidden: Optional[bool] = None,
        show_read: Optional[bool] = None,
        show_nsfw: Optional[bool] = None,
        page_cursor: Optional[str] = None
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/post/list", form)

        return result

    def like_post(
        self,
        post_id: int,
        score: int
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/post/like", form)

        return result

    def list_post_likes(
        self,
        post_id: int,
        page: Optional[int] = None,
        limit: Optional[int] = None
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/post/like/list", form)

        return result

    def save_post(
        self,
        post_id: int,
        save: bool
    ):
        form = create_form(locals())
        result = put_handler(self._session, f"{self._api_url}/post/save", form)

        return result

    def create_post_report(
        self,
        post_id: int,
        reason: str
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/post/report", form)

        return result

    def resolve_post_report(
        self,
        report_id: int,
        resolved: bool
    ):
        form = create_form(locals())
        result = put_handler(self._session, f"{self._api_url}/post/report/resolve", form)

        return result

    def list_post_reports(
        self,
        page: Optional[int] = None,
        limit: Optional[int] = None,
        unresolved_only: Optional[bool] = None,
        community_id: Optional[int] = None,
        post_id: Optional[int] = None
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/post/report/list", form)

        return result

    def get_site_metadata(
        self,
        url: str
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/post/site_metadata", form)

        return result

    def create_comment(
        self,
        content: str,
        post_id: int,
        parent_id: Optional[int] = None,
        language_id: Optional[int] = None
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/comment", form)

        return result

    def edit_comment(
        self,
        comment_id: int,
        content: Optional[str] = None,
        language_id: Optional[int] = None
    ):
        form = create_form(locals())
        result = put_handler(self._session, f"{self._api_url}/comment", form)

        return result

    def delete_comment(
        self,
        comment_id: int,
        deleted: bool
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/comment/delete", form)

        return result

    def remove_comment(
        self,
        comment_id: int,
        removed: bool,
        reason: Optional[str] = None
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/comment/remove", form)

        return result

    def mark_comment_reply_as_read(
        self,
        comment_reply_id: int,
        read: bool
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/comment/mark_as_read", form)

        return result

    def like_comment(
        self,
        comment_id: int,
        score: int
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/comment/like", form)

        return result

    def list_comment_likes(
        self,
        comment_id: int,
        page: Optional[int] = None,
        limit: Optional[int] = None
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/comment/like/list", form)

        return result

    def save_comment(
        self,
        comment_id: int,
        save: bool
    ):
        form = create_form(locals())
        result = put_handler(self._session, f"{self._api_url}/comment/save", form)

        return result

    def distinguish_comment(
        self,
        comment_id: int,
        distinguished: bool
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/comment/distinguish", form)

        return result

    def get_comments(
        self,
        type_: Optional[str] = None,
        sort: Optional[str] = None,
        max_depth: Optional[int] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
        community_id: Optional[int] = None,
        community_name: Optional[str] = None,
        post_id: Optional[int] = None,
        parent_id: Optional[int] = None,
        saved_only: Optional[bool] = None,
        liked_only: Optional[bool] = None,
        disliked_only: Optional[bool] = None
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/comment/list", form)

        return result

    def get_comment(
        self,
        id: int
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/comment", form)

        return result

    def create_comment_report(
        self,
        comment_id: int,
        reason: str
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/comment/report", form)

        return result

    def resolve_comment_report(
        self,
        report_id: int,
        resolved: bool
    ):
        form = create_form(locals())
        result = put_handler(self._session, f"{self._api_url}/comment/report/resolve", form)

        return result

    def list_comment_reports(
        self,
        comment_id: Optional[int] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
        unresolved_only: Optional[bool] = None,
        community_id: Optional[int] = None
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/comment/report/list", form)

        return result

    def get_private_messages(
        self,
        unread_only: Optional[bool] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
        creator_id: Optional[int] = None
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/private_message/list", form)

        return result

    def create_private_message(
        self,
        content: str,
        recipient_id: int
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/private_message", form)

        return result

    def edit_private_message(
        self,
        private_message_id: int,
        content: str
    ):
        form = create_form(locals())
        result = put_handler(self._session, f"{self._api_url}/private_message", form)

        return result

    def delete_private_message(
        self,
        private_message_id: int,
        deleted: bool
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/private_message/delete", form)

        return result

    def mark_private_message_as_read(
        self,
        private_message_id: int,
        read: bool
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/private_message/mark_as_read", form)

        return result

    def create_private_message_report(
        self,
        private_message_id: int,
        reason: str
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/private_message/report", form)

        return result

    def resolve_private_message_report(
        self,
        report_id: int,
        resolved: bool
    ):
        form = create_form(locals())
        result = put_handler(self._session, f"{self._api_url}/private_message/report/resolve", form)

        return result

    def list_private_message_reports(
        self,
        page: Optional[int] = None,
        limit: Optional[int] = None,
        unresolved_only: Optional[bool] = None
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/private_message/report/list", form)

        return result

    def register(
        self,
        username: str,
        password: str,
        password_verify: str,
        show_nsfw: Optional[bool] = None,
        email: Optional[str] = None,
        captcha_uuid: Optional[str] = None,
        captcha_answer: Optional[str] = None,
        honeypot: Optional[str] = None,
        answer: Optional[str] = None
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/user/register", form)

        return result

    def login(
        self,
        username_or_email: str,
        password: str,
        totp_2fa_token: Optional[str] = None
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/user/login", form)
        if result.status_code == 200:
            self._session = create_session(self._headers, result.json()["jwt"])
        else:
            raise Exception("Login failed with status code: " + str(result.status_code))
        return result

    def logout(
        self
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/user/logout", form)
        if result.status_code == 200:
            self._session = create_session(self._headers, None)
        return result

    def get_person_details(
        self,
        person_id: Optional[int] = None,
        username: Optional[str] = None,
        sort: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
        community_id: Optional[int] = None,
        saved_only: Optional[bool] = None
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/user", form)

        return result

    def get_person_mentions(
        self,
        sort: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
        unread_only: Optional[bool] = None
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/user/mention", form)

        return result

    def mark_person_mention_as_read(
        self,
        person_mention_id: int,
        read: bool
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/user/mention/mark_as_read", form)

        return result

    def get_replies(
        self,
        sort: Optional[str] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None,
        unread_only: Optional[bool] = None
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/user/replies", form)

        return result

    def ban_person(
        self,
        person_id: int,
        ban: bool,
        remove_data: Optional[bool] = None,
        reason: Optional[str] = None,
        expires: Optional[int] = None
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/user/ban", form)

        return result

    def get_banned_persons(
        self
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/user/banned", form)

        return result

    def block_person(
        self,
        person_id: int,
        block: bool
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/user/block", form)

        return result

    def get_captcha(
        self
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/user/get_captcha", form)

        return result

    def delete_account(
        self,
        password: str,
        delete_content: bool
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/user/delete_account", form)

        return result

    def password_reset(
        self,
        email: str
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/user/password_reset", form)

        return result

    def password_change_after_reset(
        self,
        token: str,
        password: str,
        password_verify: str
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/user/password_change", form)

        return result

    def mark_all_as_read(
        self
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/user/mark_all_as_read", form)

        return result

    def save_user_settings(
        self,
        show_nsfw: Optional[bool] = None,
        blur_nsfw: Optional[bool] = None,
        auto_expand: Optional[bool] = None,
        theme: Optional[str] = None,
        default_sort_type: Optional[str] = None,
        default_listing_type: Optional[str] = None,
        interface_language: Optional[str] = None,
        avatar: Optional[str] = None,
        banner: Optional[str] = None,
        display_name: Optional[str] = None,
        email: Optional[str] = None,
        bio: Optional[str] = None,
        matrix_user_id: Optional[str] = None,
        show_avatars: Optional[bool] = None,
        send_notifications_to_email: Optional[bool] = None,
        bot_account: Optional[bool] = None,
        show_bot_accounts: Optional[bool] = None,
        show_read_posts: Optional[bool] = None,
        discussion_languages: Optional[list[int]] = None,
        open_links_in_new_tab: Optional[bool] = None,
        infinite_scroll_enabled: Optional[bool] = None,
        post_listing_mode: Optional[str] = None,
        enable_keyboard_navigation: Optional[bool] = None,
        enable_animated_images: Optional[bool] = None,
        collapse_bot_comments: Optional[bool] = None,
        show_scores: Optional[bool] = None,
        show_upvotes: Optional[bool] = None,
        show_downvotes: Optional[bool] = None,
        show_upvote_percentage: Optional[bool] = None
    ):
        form = create_form(locals())
        result = put_handler(self._session, f"{self._api_url}/user/save_user_settings", form)

        return result

    def change_password(
        self,
        new_password: str,
        new_password_verify: str,
        old_password: str
    ):
        form = create_form(locals())
        result = put_handler(self._session, f"{self._api_url}/user/change_password", form)

        return result

    def get_report_count(
        self,
        community_id: Optional[int] = None
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/user/report_count", form)

        return result

    def get_unread_count(
        self
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/user/unread_count", form)

        return result

    def verify_email(
        self,
        token: str
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/user/verify_email", form)

        return result

    def add_admin(
        self,
        person_id: int,
        added: bool
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/admin/add", form)

        return result

    def get_unread_registration_application_count(
        self
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/admin/registration_application/count", form)

        return result

    def list_registration_applications(
        self,
        unread_only: Optional[bool] = None,
        page: Optional[int] = None,
        limit: Optional[int] = None
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/admin/registration_application/list", form)

        return result

    def approve_registration_application(
        self,
        id: int,
        approve: bool,
        deny_reason: Optional[str] = None
    ):
        form = create_form(locals())
        result = put_handler(self._session, f"{self._api_url}/admin/registration_application/approve", form)

        return result

    def get_registration_application(
        self,
        person_id: int
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/admin/registration_application", form)

        return result

    def purge_person(
        self,
        person_id: int,
        reason: Optional[str] = None
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/admin/purge/person", form)

        return result

    def purge_community(
        self,
        community_id: int,
        reason: Optional[str] = None
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/admin/purge/community", form)

        return result

    def purge_post(
        self,
        post_id: int,
        reason: Optional[str] = None
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/admin/purge/post", form)

        return result

    def purge_comment(
        self,
        comment_id: int,
        reason: Optional[str] = None
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/admin/purge/comment", form)

        return result

    def create_custom_emoji(
        self,
        category: str,
        shortcode: str,
        image_url: str,
        alt_text: str,
        keywords: list[str]
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/custom_emoji", form)

        return result

    def edit_custom_emoji(
        self,
        id: int,
        category: str,
        image_url: str,
        alt_text: str,
        keywords: list[str]
    ):
        form = create_form(locals())
        result = put_handler(self._session, f"{self._api_url}/custom_emoji", form)

        return result

    def delete_custom_emoji(
        self,
        id: int
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/custom_emoji/delete", form)

        return result

    def get_federated_instances(
        self
    ):
        form = create_form(locals())
        result = get_handler(self._session, f"{self._api_url}/federated_instances", form)

        return result

    def block_instance(
        self,
        instance_id: int,
        block: bool
    ):
        form = create_form(locals())
        result = post_handler(self._session, f"{self._api_url}/site/block", form)

        return result
