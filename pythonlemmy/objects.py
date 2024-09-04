from typing import Optional

from .types import ParsableObject


class ListCommunities(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ListCommunities.html"""

    type_: Optional[str] = None
    sort: Optional[str] = None
    show_nsfw: Optional[bool] = None
    page: Optional[int] = None
    limit: Optional[int] = None

    def parse(self) -> None:
        if "type_" in self._view.keys():
            self.type_ = self._view["type_"]
        else:
            self.type_ = None
        if "sort" in self._view.keys():
            self.sort = self._view["sort"]
        else:
            self.sort = None
        if "show_nsfw" in self._view.keys():
            self.show_nsfw = self._view["show_nsfw"]
        else:
            self.show_nsfw = None
        if "page" in self._view.keys():
            self.page = self._view["page"]
        else:
            self.page = None
        if "limit" in self._view.keys():
            self.limit = self._view["limit"]
        else:
            self.limit = None


class RegistrationApplication(ParsableObject):
    """https://join-lemmy.org/api/interfaces/RegistrationApplication.html"""

    id: int = None
    local_user_id: int = None
    answer: str = None
    admin_id: Optional[int] = None
    deny_reason: Optional[str] = None
    published: str = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.local_user_id = self._view["local_user_id"]
        self.answer = self._view["answer"]
        if "admin_id" in self._view.keys():
            self.admin_id = self._view["admin_id"]
        else:
            self.admin_id = None
        if "deny_reason" in self._view.keys():
            self.deny_reason = self._view["deny_reason"]
        else:
            self.deny_reason = None
        self.published = self._view["published"]


class AdminPurgeComment(ParsableObject):
    """https://join-lemmy.org/api/interfaces/AdminPurgeComment.html"""

    id: int = None
    admin_person_id: int = None
    post_id: int = None
    reason: Optional[str] = None
    when_: str = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.admin_person_id = self._view["admin_person_id"]
        self.post_id = self._view["post_id"]
        if "reason" in self._view.keys():
            self.reason = self._view["reason"]
        else:
            self.reason = None
        self.when_ = self._view["when_"]


class CreateSite(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CreateSite.html"""

    name: str = None
    sidebar: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None
    banner: Optional[str] = None
    enable_downvotes: Optional[bool] = None
    enable_nsfw: Optional[bool] = None
    community_creation_admin_only: Optional[bool] = None
    require_email_verification: Optional[bool] = None
    application_question: Optional[str] = None
    private_instance: Optional[bool] = None
    default_theme: Optional[str] = None
    default_post_listing_type: Optional[str] = None
    default_sort_type: Optional[str] = None
    legal_information: Optional[str] = None
    application_email_admins: Optional[bool] = None
    hide_modlog_mod_names: Optional[bool] = None
    discussion_languages: Optional[list[int]] = None
    slur_filter_regex: Optional[str] = None
    actor_name_max_length: Optional[int] = None
    rate_limit_message: Optional[int] = None
    rate_limit_message_per_second: Optional[int] = None
    rate_limit_post: Optional[int] = None
    rate_limit_post_per_second: Optional[int] = None
    rate_limit_register: Optional[int] = None
    rate_limit_register_per_second: Optional[int] = None
    rate_limit_image: Optional[int] = None
    rate_limit_image_per_second: Optional[int] = None
    rate_limit_comment: Optional[int] = None
    rate_limit_comment_per_second: Optional[int] = None
    rate_limit_search: Optional[int] = None
    rate_limit_search_per_second: Optional[int] = None
    federation_enabled: Optional[bool] = None
    federation_debug: Optional[bool] = None
    captcha_enabled: Optional[bool] = None
    captcha_difficulty: Optional[str] = None
    allowed_instances: Optional[list[str]] = None
    blocked_instances: Optional[list[str]] = None
    taglines: Optional[list[str]] = None
    registration_mode: Optional[str] = None
    content_warning: Optional[str] = None
    default_post_listing_mode: Optional[str] = None

    def parse(self) -> None:
        self.name = self._view["name"]
        if "sidebar" in self._view.keys():
            self.sidebar = self._view["sidebar"]
        else:
            self.sidebar = None
        if "description" in self._view.keys():
            self.description = self._view["description"]
        else:
            self.description = None
        if "icon" in self._view.keys():
            self.icon = self._view["icon"]
        else:
            self.icon = None
        if "banner" in self._view.keys():
            self.banner = self._view["banner"]
        else:
            self.banner = None
        if "enable_downvotes" in self._view.keys():
            self.enable_downvotes = self._view["enable_downvotes"]
        else:
            self.enable_downvotes = None
        if "enable_nsfw" in self._view.keys():
            self.enable_nsfw = self._view["enable_nsfw"]
        else:
            self.enable_nsfw = None
        if "community_creation_admin_only" in self._view.keys():
            self.community_creation_admin_only = self._view["community_creation_admin_only"]
        else:
            self.community_creation_admin_only = None
        if "require_email_verification" in self._view.keys():
            self.require_email_verification = self._view["require_email_verification"]
        else:
            self.require_email_verification = None
        if "application_question" in self._view.keys():
            self.application_question = self._view["application_question"]
        else:
            self.application_question = None
        if "private_instance" in self._view.keys():
            self.private_instance = self._view["private_instance"]
        else:
            self.private_instance = None
        if "default_theme" in self._view.keys():
            self.default_theme = self._view["default_theme"]
        else:
            self.default_theme = None
        if "default_post_listing_type" in self._view.keys():
            self.default_post_listing_type = self._view["default_post_listing_type"]
        else:
            self.default_post_listing_type = None
        if "default_sort_type" in self._view.keys():
            self.default_sort_type = self._view["default_sort_type"]
        else:
            self.default_sort_type = None
        if "legal_information" in self._view.keys():
            self.legal_information = self._view["legal_information"]
        else:
            self.legal_information = None
        if "application_email_admins" in self._view.keys():
            self.application_email_admins = self._view["application_email_admins"]
        else:
            self.application_email_admins = None
        if "hide_modlog_mod_names" in self._view.keys():
            self.hide_modlog_mod_names = self._view["hide_modlog_mod_names"]
        else:
            self.hide_modlog_mod_names = None
        if "discussion_languages" in self._view.keys():
            self.discussion_languages = [int(e) for e in self._view["discussion_languages"]]
        else:
            self.discussion_languages = None
        if "slur_filter_regex" in self._view.keys():
            self.slur_filter_regex = self._view["slur_filter_regex"]
        else:
            self.slur_filter_regex = None
        if "actor_name_max_length" in self._view.keys():
            self.actor_name_max_length = self._view["actor_name_max_length"]
        else:
            self.actor_name_max_length = None
        if "rate_limit_message" in self._view.keys():
            self.rate_limit_message = self._view["rate_limit_message"]
        else:
            self.rate_limit_message = None
        if "rate_limit_message_per_second" in self._view.keys():
            self.rate_limit_message_per_second = self._view["rate_limit_message_per_second"]
        else:
            self.rate_limit_message_per_second = None
        if "rate_limit_post" in self._view.keys():
            self.rate_limit_post = self._view["rate_limit_post"]
        else:
            self.rate_limit_post = None
        if "rate_limit_post_per_second" in self._view.keys():
            self.rate_limit_post_per_second = self._view["rate_limit_post_per_second"]
        else:
            self.rate_limit_post_per_second = None
        if "rate_limit_register" in self._view.keys():
            self.rate_limit_register = self._view["rate_limit_register"]
        else:
            self.rate_limit_register = None
        if "rate_limit_register_per_second" in self._view.keys():
            self.rate_limit_register_per_second = self._view["rate_limit_register_per_second"]
        else:
            self.rate_limit_register_per_second = None
        if "rate_limit_image" in self._view.keys():
            self.rate_limit_image = self._view["rate_limit_image"]
        else:
            self.rate_limit_image = None
        if "rate_limit_image_per_second" in self._view.keys():
            self.rate_limit_image_per_second = self._view["rate_limit_image_per_second"]
        else:
            self.rate_limit_image_per_second = None
        if "rate_limit_comment" in self._view.keys():
            self.rate_limit_comment = self._view["rate_limit_comment"]
        else:
            self.rate_limit_comment = None
        if "rate_limit_comment_per_second" in self._view.keys():
            self.rate_limit_comment_per_second = self._view["rate_limit_comment_per_second"]
        else:
            self.rate_limit_comment_per_second = None
        if "rate_limit_search" in self._view.keys():
            self.rate_limit_search = self._view["rate_limit_search"]
        else:
            self.rate_limit_search = None
        if "rate_limit_search_per_second" in self._view.keys():
            self.rate_limit_search_per_second = self._view["rate_limit_search_per_second"]
        else:
            self.rate_limit_search_per_second = None
        if "federation_enabled" in self._view.keys():
            self.federation_enabled = self._view["federation_enabled"]
        else:
            self.federation_enabled = None
        if "federation_debug" in self._view.keys():
            self.federation_debug = self._view["federation_debug"]
        else:
            self.federation_debug = None
        if "captcha_enabled" in self._view.keys():
            self.captcha_enabled = self._view["captcha_enabled"]
        else:
            self.captcha_enabled = None
        if "captcha_difficulty" in self._view.keys():
            self.captcha_difficulty = self._view["captcha_difficulty"]
        else:
            self.captcha_difficulty = None
        if "allowed_instances" in self._view.keys():
            self.allowed_instances = [str(e) for e in self._view["allowed_instances"]]
        else:
            self.allowed_instances = None
        if "blocked_instances" in self._view.keys():
            self.blocked_instances = [str(e) for e in self._view["blocked_instances"]]
        else:
            self.blocked_instances = None
        if "taglines" in self._view.keys():
            self.taglines = [str(e) for e in self._view["taglines"]]
        else:
            self.taglines = None
        if "registration_mode" in self._view.keys():
            self.registration_mode = self._view["registration_mode"]
        else:
            self.registration_mode = None
        if "content_warning" in self._view.keys():
            self.content_warning = self._view["content_warning"]
        else:
            self.content_warning = None
        if "default_post_listing_mode" in self._view.keys():
            self.default_post_listing_mode = self._view["default_post_listing_mode"]
        else:
            self.default_post_listing_mode = None


class DeleteComment(ParsableObject):
    """https://join-lemmy.org/api/interfaces/DeleteComment.html"""

    comment_id: int = None
    deleted: bool = None

    def parse(self) -> None:
        self.comment_id = self._view["comment_id"]
        self.deleted = self._view["deleted"]


class CreateCommunity(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CreateCommunity.html"""

    name: str = None
    title: str = None
    description: Optional[str] = None
    icon: Optional[str] = None
    banner: Optional[str] = None
    nsfw: Optional[bool] = None
    posting_restricted_to_mods: Optional[bool] = None
    discussion_languages: Optional[list[int]] = None
    visibility: Optional[str] = None

    def parse(self) -> None:
        self.name = self._view["name"]
        self.title = self._view["title"]
        if "description" in self._view.keys():
            self.description = self._view["description"]
        else:
            self.description = None
        if "icon" in self._view.keys():
            self.icon = self._view["icon"]
        else:
            self.icon = None
        if "banner" in self._view.keys():
            self.banner = self._view["banner"]
        else:
            self.banner = None
        if "nsfw" in self._view.keys():
            self.nsfw = self._view["nsfw"]
        else:
            self.nsfw = None
        if "posting_restricted_to_mods" in self._view.keys():
            self.posting_restricted_to_mods = self._view["posting_restricted_to_mods"]
        else:
            self.posting_restricted_to_mods = None
        if "discussion_languages" in self._view.keys():
            self.discussion_languages = [int(e) for e in self._view["discussion_languages"]]
        else:
            self.discussion_languages = None
        if "visibility" in self._view.keys():
            self.visibility = self._view["visibility"]
        else:
            self.visibility = None


class AdminPurgeCommunity(ParsableObject):
    """https://join-lemmy.org/api/interfaces/AdminPurgeCommunity.html"""

    id: int = None
    admin_person_id: int = None
    reason: Optional[str] = None
    when_: str = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.admin_person_id = self._view["admin_person_id"]
        if "reason" in self._view.keys():
            self.reason = self._view["reason"]
        else:
            self.reason = None
        self.when_ = self._view["when_"]


class ModRemoveCommunity(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModRemoveCommunity.html"""

    id: int = None
    mod_person_id: int = None
    community_id: int = None
    reason: Optional[str] = None
    removed: bool = None
    when_: str = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.mod_person_id = self._view["mod_person_id"]
        self.community_id = self._view["community_id"]
        if "reason" in self._view.keys():
            self.reason = self._view["reason"]
        else:
            self.reason = None
        self.removed = self._view["removed"]
        self.when_ = self._view["when_"]


class LocalSiteUrlBlocklist(ParsableObject):
    """https://join-lemmy.org/api/interfaces/LocalSiteUrlBlocklist.html"""

    id: int = None
    url: str = None
    published: str = None
    updated: Optional[str] = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.url = self._view["url"]
        self.published = self._view["published"]
        if "updated" in self._view.keys():
            self.updated = self._view["updated"]
        else:
            self.updated = None


class PostReport(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PostReport.html"""

    id: int = None
    creator_id: int = None
    post_id: int = None
    original_post_name: str = None
    original_post_url: Optional[str] = None
    original_post_body: Optional[str] = None
    reason: str = None
    resolved: bool = None
    resolver_id: Optional[int] = None
    published: str = None
    updated: Optional[str] = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.creator_id = self._view["creator_id"]
        self.post_id = self._view["post_id"]
        self.original_post_name = self._view["original_post_name"]
        if "original_post_url" in self._view.keys():
            self.original_post_url = self._view["original_post_url"]
        else:
            self.original_post_url = None
        if "original_post_body" in self._view.keys():
            self.original_post_body = self._view["original_post_body"]
        else:
            self.original_post_body = None
        self.reason = self._view["reason"]
        self.resolved = self._view["resolved"]
        if "resolver_id" in self._view.keys():
            self.resolver_id = self._view["resolver_id"]
        else:
            self.resolver_id = None
        self.published = self._view["published"]
        if "updated" in self._view.keys():
            self.updated = self._view["updated"]
        else:
            self.updated = None


class CommentAggregates(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CommentAggregates.html"""

    comment_id: int = None
    score: int = None
    upvotes: int = None
    downvotes: int = None
    published: str = None
    child_count: int = None

    def parse(self) -> None:
        self.comment_id = self._view["comment_id"]
        self.score = self._view["score"]
        self.upvotes = self._view["upvotes"]
        self.downvotes = self._view["downvotes"]
        self.published = self._view["published"]
        self.child_count = self._view["child_count"]


class FeaturePost(ParsableObject):
    """https://join-lemmy.org/api/interfaces/FeaturePost.html"""

    post_id: int = None
    featured: bool = None
    feature_type: str = None

    def parse(self) -> None:
        self.post_id = self._view["post_id"]
        self.featured = self._view["featured"]
        self.feature_type = self._view["feature_type"]


class GetSiteMetadata(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetSiteMetadata.html"""

    url: str = None

    def parse(self) -> None:
        self.url = self._view["url"]


class ModLockPost(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModLockPost.html"""

    id: int = None
    mod_person_id: int = None
    post_id: int = None
    locked: bool = None
    when_: str = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.mod_person_id = self._view["mod_person_id"]
        self.post_id = self._view["post_id"]
        self.locked = self._view["locked"]
        self.when_ = self._view["when_"]


class ResolveCommentReport(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ResolveCommentReport.html"""

    report_id: int = None
    resolved: bool = None

    def parse(self) -> None:
        self.report_id = self._view["report_id"]
        self.resolved = self._view["resolved"]


class DeleteCommunity(ParsableObject):
    """https://join-lemmy.org/api/interfaces/DeleteCommunity.html"""

    community_id: int = None
    deleted: bool = None

    def parse(self) -> None:
        self.community_id = self._view["community_id"]
        self.deleted = self._view["deleted"]


class GetPersonMentions(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetPersonMentions.html"""

    sort: Optional[str] = None
    page: Optional[int] = None
    limit: Optional[int] = None
    unread_only: Optional[bool] = None

    def parse(self) -> None:
        if "sort" in self._view.keys():
            self.sort = self._view["sort"]
        else:
            self.sort = None
        if "page" in self._view.keys():
            self.page = self._view["page"]
        else:
            self.page = None
        if "limit" in self._view.keys():
            self.limit = self._view["limit"]
        else:
            self.limit = None
        if "unread_only" in self._view.keys():
            self.unread_only = self._view["unread_only"]
        else:
            self.unread_only = None


class ModHideCommunity(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModHideCommunity.html"""

    id: int = None
    community_id: int = None
    mod_person_id: int = None
    when_: str = None
    reason: Optional[str] = None
    hidden: bool = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.community_id = self._view["community_id"]
        self.mod_person_id = self._view["mod_person_id"]
        self.when_ = self._view["when_"]
        if "reason" in self._view.keys():
            self.reason = self._view["reason"]
        else:
            self.reason = None
        self.hidden = self._view["hidden"]


class HideCommunity(ParsableObject):
    """https://join-lemmy.org/api/interfaces/HideCommunity.html"""

    community_id: int = None
    hidden: bool = None
    reason: Optional[str] = None

    def parse(self) -> None:
        self.community_id = self._view["community_id"]
        self.hidden = self._view["hidden"]
        if "reason" in self._view.keys():
            self.reason = self._view["reason"]
        else:
            self.reason = None


class RemoveCommunity(ParsableObject):
    """https://join-lemmy.org/api/interfaces/RemoveCommunity.html"""

    community_id: int = None
    removed: bool = None
    reason: Optional[str] = None

    def parse(self) -> None:
        self.community_id = self._view["community_id"]
        self.removed = self._view["removed"]
        if "reason" in self._view.keys():
            self.reason = self._view["reason"]
        else:
            self.reason = None


class EditComment(ParsableObject):
    """https://join-lemmy.org/api/interfaces/EditComment.html"""

    comment_id: int = None
    content: Optional[str] = None
    language_id: Optional[int] = None

    def parse(self) -> None:
        self.comment_id = self._view["comment_id"]
        if "content" in self._view.keys():
            self.content = self._view["content"]
        else:
            self.content = None
        if "language_id" in self._view.keys():
            self.language_id = self._view["language_id"]
        else:
            self.language_id = None


class EditCustomEmoji(ParsableObject):
    """https://join-lemmy.org/api/interfaces/EditCustomEmoji.html"""

    id: int = None
    category: str = None
    image_url: str = None
    alt_text: str = None
    keywords: list[str] = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.category = self._view["category"]
        self.image_url = self._view["image_url"]
        self.alt_text = self._view["alt_text"]
        self.keywords = [str(e) for e in self._view["keywords"]]


class PersonMention(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PersonMention.html"""

    id: int = None
    recipient_id: int = None
    comment_id: int = None
    read: bool = None
    published: str = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.recipient_id = self._view["recipient_id"]
        self.comment_id = self._view["comment_id"]
        self.read = self._view["read"]
        self.published = self._view["published"]


class HidePost(ParsableObject):
    """https://join-lemmy.org/api/interfaces/HidePost.html"""

    post_ids: list[int] = None
    hide: bool = None

    def parse(self) -> None:
        self.post_ids = [int(e) for e in self._view["post_ids"]]
        self.hide = self._view["hide"]


class CreatePrivateMessageReport(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CreatePrivateMessageReport.html"""

    private_message_id: int = None
    reason: str = None

    def parse(self) -> None:
        self.private_message_id = self._view["private_message_id"]
        self.reason = self._view["reason"]


class ReadableFederationState(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ReadableFederationState.html"""

    instance_id: int = None
    last_successful_id: Optional[int] = None
    last_successful_published_time: Optional[str] = None
    fail_count: int = None
    last_retry: Optional[str] = None
    next_retry: Optional[str] = None

    def parse(self) -> None:
        self.instance_id = self._view["instance_id"]
        if "last_successful_id" in self._view.keys():
            self.last_successful_id = self._view["last_successful_id"]
        else:
            self.last_successful_id = None
        if "last_successful_published_time" in self._view.keys():
            self.last_successful_published_time = self._view["last_successful_published_time"]
        else:
            self.last_successful_published_time = None
        self.fail_count = self._view["fail_count"]
        if "last_retry" in self._view.keys():
            self.last_retry = self._view["last_retry"]
        else:
            self.last_retry = None
        if "next_retry" in self._view.keys():
            self.next_retry = self._view["next_retry"]
        else:
            self.next_retry = None


class Login(ParsableObject):
    """https://join-lemmy.org/api/interfaces/Login.html"""

    username_or_email: str = None
    password: str = None
    totp_2fa_token: Optional[str] = None

    def parse(self) -> None:
        self.username_or_email = self._view["username_or_email"]
        self.password = self._view["password"]
        if "totp_2fa_token" in self._view.keys():
            self.totp_2fa_token = self._view["totp_2fa_token"]
        else:
            self.totp_2fa_token = None


class BlockInstance(ParsableObject):
    """https://join-lemmy.org/api/interfaces/BlockInstance.html"""

    instance_id: int = None
    block: bool = None

    def parse(self) -> None:
        self.instance_id = self._view["instance_id"]
        self.block = self._view["block"]


class LoginToken(ParsableObject):
    """https://join-lemmy.org/api/interfaces/LoginToken.html"""

    user_id: int = None
    published: str = None
    ip: Optional[str] = None
    user_agent: Optional[str] = None

    def parse(self) -> None:
        self.user_id = self._view["user_id"]
        self.published = self._view["published"]
        if "ip" in self._view.keys():
            self.ip = self._view["ip"]
        else:
            self.ip = None
        if "user_agent" in self._view.keys():
            self.user_agent = self._view["user_agent"]
        else:
            self.user_agent = None


class PasswordChangeAfterReset(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PasswordChangeAfterReset.html"""

    token: str = None
    password: str = None
    password_verify: str = None

    def parse(self) -> None:
        self.token = self._view["token"]
        self.password = self._view["password"]
        self.password_verify = self._view["password_verify"]


class LocalUser(ParsableObject):
    """https://join-lemmy.org/api/interfaces/LocalUser.html"""

    id: int = None
    person_id: int = None
    email: Optional[str] = None
    show_nsfw: bool = None
    theme: str = None
    default_sort_type: str = None
    default_listing_type: str = None
    interface_language: str = None
    show_avatars: bool = None
    send_notifications_to_email: bool = None
    show_scores: bool = None
    show_bot_accounts: bool = None
    show_read_posts: bool = None
    email_verified: bool = None
    accepted_application: bool = None
    open_links_in_new_tab: bool = None
    blur_nsfw: bool = None
    auto_expand: bool = None
    infinite_scroll_enabled: bool = None
    admin: bool = None
    post_listing_mode: str = None
    totp_2fa_enabled: bool = None
    enable_keyboard_navigation: bool = None
    enable_animated_images: bool = None
    collapse_bot_comments: bool = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.person_id = self._view["person_id"]
        if "email" in self._view.keys():
            self.email = self._view["email"]
        else:
            self.email = None
        self.show_nsfw = self._view["show_nsfw"]
        self.theme = self._view["theme"]
        self.default_sort_type = self._view["default_sort_type"]
        self.default_listing_type = self._view["default_listing_type"]
        self.interface_language = self._view["interface_language"]
        self.show_avatars = self._view["show_avatars"]
        self.send_notifications_to_email = self._view["send_notifications_to_email"]
        self.show_scores = self._view["show_scores"]
        self.show_bot_accounts = self._view["show_bot_accounts"]
        self.show_read_posts = self._view["show_read_posts"]
        self.email_verified = self._view["email_verified"]
        self.accepted_application = self._view["accepted_application"]
        self.open_links_in_new_tab = self._view["open_links_in_new_tab"]
        self.blur_nsfw = self._view["blur_nsfw"]
        self.auto_expand = self._view["auto_expand"]
        self.infinite_scroll_enabled = self._view["infinite_scroll_enabled"]
        self.admin = self._view["admin"]
        self.post_listing_mode = self._view["post_listing_mode"]
        self.totp_2fa_enabled = self._view["totp_2fa_enabled"]
        self.enable_keyboard_navigation = self._view["enable_keyboard_navigation"]
        self.enable_animated_images = self._view["enable_animated_images"]
        self.collapse_bot_comments = self._view["collapse_bot_comments"]


class PersonAggregates(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PersonAggregates.html"""

    person_id: int = None
    post_count: int = None
    comment_count: int = None

    def parse(self) -> None:
        self.person_id = self._view["person_id"]
        self.post_count = self._view["post_count"]
        self.comment_count = self._view["comment_count"]


class MarkCommentReplyAsRead(ParsableObject):
    """https://join-lemmy.org/api/interfaces/MarkCommentReplyAsRead.html"""

    comment_reply_id: int = None
    read: bool = None

    def parse(self) -> None:
        self.comment_reply_id = self._view["comment_reply_id"]
        self.read = self._view["read"]


class Search(ParsableObject):
    """https://join-lemmy.org/api/interfaces/Search.html"""

    q: str = None
    community_id: Optional[int] = None
    community_name: Optional[str] = None
    creator_id: Optional[int] = None
    type_: Optional[str] = None
    sort: Optional[str] = None
    listing_type: Optional[str] = None
    page: Optional[int] = None
    limit: Optional[int] = None

    def parse(self) -> None:
        self.q = self._view["q"]
        if "community_id" in self._view.keys():
            self.community_id = self._view["community_id"]
        else:
            self.community_id = None
        if "community_name" in self._view.keys():
            self.community_name = self._view["community_name"]
        else:
            self.community_name = None
        if "creator_id" in self._view.keys():
            self.creator_id = self._view["creator_id"]
        else:
            self.creator_id = None
        if "type_" in self._view.keys():
            self.type_ = self._view["type_"]
        else:
            self.type_ = None
        if "sort" in self._view.keys():
            self.sort = self._view["sort"]
        else:
            self.sort = None
        if "listing_type" in self._view.keys():
            self.listing_type = self._view["listing_type"]
        else:
            self.listing_type = None
        if "page" in self._view.keys():
            self.page = self._view["page"]
        else:
            self.page = None
        if "limit" in self._view.keys():
            self.limit = self._view["limit"]
        else:
            self.limit = None


class LocalUserVoteDisplayMode(ParsableObject):
    """https://join-lemmy.org/api/interfaces/LocalUserVoteDisplayMode.html"""

    local_user_id: int = None
    score: bool = None
    upvotes: bool = None
    downvotes: bool = None
    upvote_percentage: bool = None

    def parse(self) -> None:
        self.local_user_id = self._view["local_user_id"]
        self.score = self._view["score"]
        self.upvotes = self._view["upvotes"]
        self.downvotes = self._view["downvotes"]
        self.upvote_percentage = self._view["upvote_percentage"]


class LockPost(ParsableObject):
    """https://join-lemmy.org/api/interfaces/LockPost.html"""

    post_id: int = None
    locked: bool = None

    def parse(self) -> None:
        self.post_id = self._view["post_id"]
        self.locked = self._view["locked"]


class ChangePassword(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ChangePassword.html"""

    new_password: str = None
    new_password_verify: str = None
    old_password: str = None

    def parse(self) -> None:
        self.new_password = self._view["new_password"]
        self.new_password_verify = self._view["new_password_verify"]
        self.old_password = self._view["old_password"]


class ResolveObject(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ResolveObject.html"""

    q: str = None

    def parse(self) -> None:
        self.q = self._view["q"]


class VerifyEmail(ParsableObject):
    """https://join-lemmy.org/api/interfaces/VerifyEmail.html"""

    token: str = None

    def parse(self) -> None:
        self.token = self._view["token"]


class ModAddCommunity(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModAddCommunity.html"""

    id: int = None
    mod_person_id: int = None
    other_person_id: int = None
    community_id: int = None
    removed: bool = None
    when_: str = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.mod_person_id = self._view["mod_person_id"]
        self.other_person_id = self._view["other_person_id"]
        self.community_id = self._view["community_id"]
        self.removed = self._view["removed"]
        self.when_ = self._view["when_"]


class BlockPerson(ParsableObject):
    """https://join-lemmy.org/api/interfaces/BlockPerson.html"""

    person_id: int = None
    block: bool = None

    def parse(self) -> None:
        self.person_id = self._view["person_id"]
        self.block = self._view["block"]


class ListPrivateMessageReports(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ListPrivateMessageReports.html"""

    page: Optional[int] = None
    limit: Optional[int] = None
    unresolved_only: Optional[bool] = None

    def parse(self) -> None:
        if "page" in self._view.keys():
            self.page = self._view["page"]
        else:
            self.page = None
        if "limit" in self._view.keys():
            self.limit = self._view["limit"]
        else:
            self.limit = None
        if "unresolved_only" in self._view.keys():
            self.unresolved_only = self._view["unresolved_only"]
        else:
            self.unresolved_only = None


class SiteAggregates(ParsableObject):
    """https://join-lemmy.org/api/interfaces/SiteAggregates.html"""

    site_id: int = None
    users: int = None
    posts: int = None
    comments: int = None
    communities: int = None
    users_active_day: int = None
    users_active_week: int = None
    users_active_month: int = None
    users_active_half_year: int = None

    def parse(self) -> None:
        self.site_id = self._view["site_id"]
        self.users = self._view["users"]
        self.posts = self._view["posts"]
        self.comments = self._view["comments"]
        self.communities = self._view["communities"]
        self.users_active_day = self._view["users_active_day"]
        self.users_active_week = self._view["users_active_week"]
        self.users_active_month = self._view["users_active_month"]
        self.users_active_half_year = self._view["users_active_half_year"]


class CreatePostReport(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CreatePostReport.html"""

    post_id: int = None
    reason: str = None

    def parse(self) -> None:
        self.post_id = self._view["post_id"]
        self.reason = self._view["reason"]


class CustomEmoji(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CustomEmoji.html"""

    id: int = None
    local_site_id: int = None
    shortcode: str = None
    image_url: str = None
    alt_text: str = None
    category: str = None
    published: str = None
    updated: Optional[str] = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.local_site_id = self._view["local_site_id"]
        self.shortcode = self._view["shortcode"]
        self.image_url = self._view["image_url"]
        self.alt_text = self._view["alt_text"]
        self.category = self._view["category"]
        self.published = self._view["published"]
        if "updated" in self._view.keys():
            self.updated = self._view["updated"]
        else:
            self.updated = None


class PurgePost(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PurgePost.html"""

    post_id: int = None
    reason: Optional[str] = None

    def parse(self) -> None:
        self.post_id = self._view["post_id"]
        if "reason" in self._view.keys():
            self.reason = self._view["reason"]
        else:
            self.reason = None


class PostAggregates(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PostAggregates.html"""

    post_id: int = None
    comments: int = None
    score: int = None
    upvotes: int = None
    downvotes: int = None
    published: str = None
    newest_comment_time: str = None

    def parse(self) -> None:
        self.post_id = self._view["post_id"]
        self.comments = self._view["comments"]
        self.score = self._view["score"]
        self.upvotes = self._view["upvotes"]
        self.downvotes = self._view["downvotes"]
        self.published = self._view["published"]
        self.newest_comment_time = self._view["newest_comment_time"]


class Language(ParsableObject):
    """https://join-lemmy.org/api/interfaces/Language.html"""

    id: int = None
    code: str = None
    name: str = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.code = self._view["code"]
        self.name = self._view["name"]


class GetReportCount(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetReportCount.html"""

    community_id: Optional[int] = None

    def parse(self) -> None:
        if "community_id" in self._view.keys():
            self.community_id = self._view["community_id"]
        else:
            self.community_id = None


class DeletePrivateMessage(ParsableObject):
    """https://join-lemmy.org/api/interfaces/DeletePrivateMessage.html"""

    private_message_id: int = None
    deleted: bool = None

    def parse(self) -> None:
        self.private_message_id = self._view["private_message_id"]
        self.deleted = self._view["deleted"]


class Community(ParsableObject):
    """https://join-lemmy.org/api/interfaces/Community.html"""

    id: int = None
    name: str = None
    title: str = None
    description: Optional[str] = None
    removed: bool = None
    published: str = None
    updated: Optional[str] = None
    deleted: bool = None
    nsfw: bool = None
    actor_id: str = None
    local: bool = None
    icon: Optional[str] = None
    banner: Optional[str] = None
    hidden: bool = None
    posting_restricted_to_mods: bool = None
    instance_id: int = None
    visibility: str = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.name = self._view["name"]
        self.title = self._view["title"]
        if "description" in self._view.keys():
            self.description = self._view["description"]
        else:
            self.description = None
        self.removed = self._view["removed"]
        self.published = self._view["published"]
        if "updated" in self._view.keys():
            self.updated = self._view["updated"]
        else:
            self.updated = None
        self.deleted = self._view["deleted"]
        self.nsfw = self._view["nsfw"]
        self.actor_id = self._view["actor_id"]
        self.local = self._view["local"]
        if "icon" in self._view.keys():
            self.icon = self._view["icon"]
        else:
            self.icon = None
        if "banner" in self._view.keys():
            self.banner = self._view["banner"]
        else:
            self.banner = None
        self.hidden = self._view["hidden"]
        self.posting_restricted_to_mods = self._view["posting_restricted_to_mods"]
        self.instance_id = self._view["instance_id"]
        self.visibility = self._view["visibility"]


class ListPostReports(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ListPostReports.html"""

    page: Optional[int] = None
    limit: Optional[int] = None
    unresolved_only: Optional[bool] = None
    community_id: Optional[int] = None
    post_id: Optional[int] = None

    def parse(self) -> None:
        if "page" in self._view.keys():
            self.page = self._view["page"]
        else:
            self.page = None
        if "limit" in self._view.keys():
            self.limit = self._view["limit"]
        else:
            self.limit = None
        if "unresolved_only" in self._view.keys():
            self.unresolved_only = self._view["unresolved_only"]
        else:
            self.unresolved_only = None
        if "community_id" in self._view.keys():
            self.community_id = self._view["community_id"]
        else:
            self.community_id = None
        if "post_id" in self._view.keys():
            self.post_id = self._view["post_id"]
        else:
            self.post_id = None


class ModFeaturePost(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModFeaturePost.html"""

    id: int = None
    mod_person_id: int = None
    post_id: int = None
    featured: bool = None
    when_: str = None
    is_featured_community: bool = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.mod_person_id = self._view["mod_person_id"]
        self.post_id = self._view["post_id"]
        self.featured = self._view["featured"]
        self.when_ = self._view["when_"]
        self.is_featured_community = self._view["is_featured_community"]


class GetPersonDetails(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetPersonDetails.html"""

    person_id: Optional[int] = None
    username: Optional[str] = None
    sort: Optional[str] = None
    page: Optional[int] = None
    limit: Optional[int] = None
    community_id: Optional[int] = None
    saved_only: Optional[bool] = None

    def parse(self) -> None:
        if "person_id" in self._view.keys():
            self.person_id = self._view["person_id"]
        else:
            self.person_id = None
        if "username" in self._view.keys():
            self.username = self._view["username"]
        else:
            self.username = None
        if "sort" in self._view.keys():
            self.sort = self._view["sort"]
        else:
            self.sort = None
        if "page" in self._view.keys():
            self.page = self._view["page"]
        else:
            self.page = None
        if "limit" in self._view.keys():
            self.limit = self._view["limit"]
        else:
            self.limit = None
        if "community_id" in self._view.keys():
            self.community_id = self._view["community_id"]
        else:
            self.community_id = None
        if "saved_only" in self._view.keys():
            self.saved_only = self._view["saved_only"]
        else:
            self.saved_only = None


class AddModToCommunity(ParsableObject):
    """https://join-lemmy.org/api/interfaces/AddModToCommunity.html"""

    community_id: int = None
    person_id: int = None
    added: bool = None

    def parse(self) -> None:
        self.community_id = self._view["community_id"]
        self.person_id = self._view["person_id"]
        self.added = self._view["added"]


class Site(ParsableObject):
    """https://join-lemmy.org/api/interfaces/Site.html"""

    id: int = None
    name: str = None
    sidebar: Optional[str] = None
    published: str = None
    updated: Optional[str] = None
    icon: Optional[str] = None
    banner: Optional[str] = None
    description: Optional[str] = None
    actor_id: str = None
    last_refreshed_at: str = None
    inbox_url: str = None
    public_key: str = None
    instance_id: int = None
    content_warning: Optional[str] = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.name = self._view["name"]
        if "sidebar" in self._view.keys():
            self.sidebar = self._view["sidebar"]
        else:
            self.sidebar = None
        self.published = self._view["published"]
        if "updated" in self._view.keys():
            self.updated = self._view["updated"]
        else:
            self.updated = None
        if "icon" in self._view.keys():
            self.icon = self._view["icon"]
        else:
            self.icon = None
        if "banner" in self._view.keys():
            self.banner = self._view["banner"]
        else:
            self.banner = None
        if "description" in self._view.keys():
            self.description = self._view["description"]
        else:
            self.description = None
        self.actor_id = self._view["actor_id"]
        self.last_refreshed_at = self._view["last_refreshed_at"]
        self.inbox_url = self._view["inbox_url"]
        self.public_key = self._view["public_key"]
        self.instance_id = self._view["instance_id"]
        if "content_warning" in self._view.keys():
            self.content_warning = self._view["content_warning"]
        else:
            self.content_warning = None


class ApproveRegistrationApplication(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ApproveRegistrationApplication.html"""

    id: int = None
    approve: bool = None
    deny_reason: Optional[str] = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.approve = self._view["approve"]
        if "deny_reason" in self._view.keys():
            self.deny_reason = self._view["deny_reason"]
        else:
            self.deny_reason = None


class EditPost(ParsableObject):
    """https://join-lemmy.org/api/interfaces/EditPost.html"""

    post_id: int = None
    name: Optional[str] = None
    url: Optional[str] = None
    body: Optional[str] = None
    alt_text: Optional[str] = None
    nsfw: Optional[bool] = None
    language_id: Optional[int] = None
    custom_thumbnail: Optional[str] = None

    def parse(self) -> None:
        self.post_id = self._view["post_id"]
        if "name" in self._view.keys():
            self.name = self._view["name"]
        else:
            self.name = None
        if "url" in self._view.keys():
            self.url = self._view["url"]
        else:
            self.url = None
        if "body" in self._view.keys():
            self.body = self._view["body"]
        else:
            self.body = None
        if "alt_text" in self._view.keys():
            self.alt_text = self._view["alt_text"]
        else:
            self.alt_text = None
        if "nsfw" in self._view.keys():
            self.nsfw = self._view["nsfw"]
        else:
            self.nsfw = None
        if "language_id" in self._view.keys():
            self.language_id = self._view["language_id"]
        else:
            self.language_id = None
        if "custom_thumbnail" in self._view.keys():
            self.custom_thumbnail = self._view["custom_thumbnail"]
        else:
            self.custom_thumbnail = None


class GetPost(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetPost.html"""

    id: Optional[int] = None
    comment_id: Optional[int] = None

    def parse(self) -> None:
        if "id" in self._view.keys():
            self.id = self._view["id"]
        else:
            self.id = None
        if "comment_id" in self._view.keys():
            self.comment_id = self._view["comment_id"]
        else:
            self.comment_id = None


class FollowCommunity(ParsableObject):
    """https://join-lemmy.org/api/interfaces/FollowCommunity.html"""

    community_id: int = None
    follow: bool = None

    def parse(self) -> None:
        self.community_id = self._view["community_id"]
        self.follow = self._view["follow"]


class GetPrivateMessages(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetPrivateMessages.html"""

    unread_only: Optional[bool] = None
    page: Optional[int] = None
    limit: Optional[int] = None
    creator_id: Optional[int] = None

    def parse(self) -> None:
        if "unread_only" in self._view.keys():
            self.unread_only = self._view["unread_only"]
        else:
            self.unread_only = None
        if "page" in self._view.keys():
            self.page = self._view["page"]
        else:
            self.page = None
        if "limit" in self._view.keys():
            self.limit = self._view["limit"]
        else:
            self.limit = None
        if "creator_id" in self._view.keys():
            self.creator_id = self._view["creator_id"]
        else:
            self.creator_id = None


class ModBan(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModBan.html"""

    id: int = None
    mod_person_id: int = None
    other_person_id: int = None
    reason: Optional[str] = None
    banned: bool = None
    expires: Optional[str] = None
    when_: str = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.mod_person_id = self._view["mod_person_id"]
        self.other_person_id = self._view["other_person_id"]
        if "reason" in self._view.keys():
            self.reason = self._view["reason"]
        else:
            self.reason = None
        self.banned = self._view["banned"]
        if "expires" in self._view.keys():
            self.expires = self._view["expires"]
        else:
            self.expires = None
        self.when_ = self._view["when_"]


class Tagline(ParsableObject):
    """https://join-lemmy.org/api/interfaces/Tagline.html"""

    id: int = None
    local_site_id: int = None
    content: str = None
    published: str = None
    updated: Optional[str] = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.local_site_id = self._view["local_site_id"]
        self.content = self._view["content"]
        self.published = self._view["published"]
        if "updated" in self._view.keys():
            self.updated = self._view["updated"]
        else:
            self.updated = None


class RemoveComment(ParsableObject):
    """https://join-lemmy.org/api/interfaces/RemoveComment.html"""

    comment_id: int = None
    removed: bool = None
    reason: Optional[str] = None

    def parse(self) -> None:
        self.comment_id = self._view["comment_id"]
        self.removed = self._view["removed"]
        if "reason" in self._view.keys():
            self.reason = self._view["reason"]
        else:
            self.reason = None


class UpdateTotp(ParsableObject):
    """https://join-lemmy.org/api/interfaces/UpdateTotp.html"""

    totp_token: str = None
    enabled: bool = None

    def parse(self) -> None:
        self.totp_token = self._view["totp_token"]
        self.enabled = self._view["enabled"]


class MarkPostAsRead(ParsableObject):
    """https://join-lemmy.org/api/interfaces/MarkPostAsRead.html"""

    post_ids: list[int] = None
    read: bool = None

    def parse(self) -> None:
        self.post_ids = [int(e) for e in self._view["post_ids"]]
        self.read = self._view["read"]


class ResolvePrivateMessageReport(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ResolvePrivateMessageReport.html"""

    report_id: int = None
    resolved: bool = None

    def parse(self) -> None:
        self.report_id = self._view["report_id"]
        self.resolved = self._view["resolved"]


class LinkMetadata(ParsableObject):
    """https://join-lemmy.org/api/interfaces/LinkMetadata.html"""

    title: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    embed_video_url: Optional[str] = None
    content_type: Optional[str] = None

    def parse(self) -> None:
        if "title" in self._view.keys():
            self.title = self._view["title"]
        else:
            self.title = None
        if "description" in self._view.keys():
            self.description = self._view["description"]
        else:
            self.description = None
        if "image" in self._view.keys():
            self.image = self._view["image"]
        else:
            self.image = None
        if "embed_video_url" in self._view.keys():
            self.embed_video_url = self._view["embed_video_url"]
        else:
            self.embed_video_url = None
        if "content_type" in self._view.keys():
            self.content_type = self._view["content_type"]
        else:
            self.content_type = None


class PrivateMessage(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PrivateMessage.html"""

    id: int = None
    creator_id: int = None
    recipient_id: int = None
    content: str = None
    deleted: bool = None
    read: bool = None
    published: str = None
    updated: Optional[str] = None
    ap_id: str = None
    local: bool = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.creator_id = self._view["creator_id"]
        self.recipient_id = self._view["recipient_id"]
        self.content = self._view["content"]
        self.deleted = self._view["deleted"]
        self.read = self._view["read"]
        self.published = self._view["published"]
        if "updated" in self._view.keys():
            self.updated = self._view["updated"]
        else:
            self.updated = None
        self.ap_id = self._view["ap_id"]
        self.local = self._view["local"]


class DeletePost(ParsableObject):
    """https://join-lemmy.org/api/interfaces/DeletePost.html"""

    post_id: int = None
    deleted: bool = None

    def parse(self) -> None:
        self.post_id = self._view["post_id"]
        self.deleted = self._view["deleted"]


class PurgeComment(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PurgeComment.html"""

    comment_id: int = None
    reason: Optional[str] = None

    def parse(self) -> None:
        self.comment_id = self._view["comment_id"]
        if "reason" in self._view.keys():
            self.reason = self._view["reason"]
        else:
            self.reason = None


class CreatePost(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CreatePost.html"""

    name: str = None
    community_id: int = None
    url: Optional[str] = None
    body: Optional[str] = None
    alt_text: Optional[str] = None
    honeypot: Optional[str] = None
    nsfw: Optional[bool] = None
    language_id: Optional[int] = None
    custom_thumbnail: Optional[str] = None

    def parse(self) -> None:
        self.name = self._view["name"]
        self.community_id = self._view["community_id"]
        if "url" in self._view.keys():
            self.url = self._view["url"]
        else:
            self.url = None
        if "body" in self._view.keys():
            self.body = self._view["body"]
        else:
            self.body = None
        if "alt_text" in self._view.keys():
            self.alt_text = self._view["alt_text"]
        else:
            self.alt_text = None
        if "honeypot" in self._view.keys():
            self.honeypot = self._view["honeypot"]
        else:
            self.honeypot = None
        if "nsfw" in self._view.keys():
            self.nsfw = self._view["nsfw"]
        else:
            self.nsfw = None
        if "language_id" in self._view.keys():
            self.language_id = self._view["language_id"]
        else:
            self.language_id = None
        if "custom_thumbnail" in self._view.keys():
            self.custom_thumbnail = self._view["custom_thumbnail"]
        else:
            self.custom_thumbnail = None


class CreateCustomEmoji(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CreateCustomEmoji.html"""

    category: str = None
    shortcode: str = None
    image_url: str = None
    alt_text: str = None
    keywords: list[str] = None

    def parse(self) -> None:
        self.category = self._view["category"]
        self.shortcode = self._view["shortcode"]
        self.image_url = self._view["image_url"]
        self.alt_text = self._view["alt_text"]
        self.keywords = [str(e) for e in self._view["keywords"]]


class InstanceWithFederationState(ParsableObject):
    """https://join-lemmy.org/api/interfaces/InstanceWithFederationState.html"""

    id: int = None
    domain: str = None
    published: str = None
    updated: Optional[str] = None
    software: Optional[str] = None
    version: Optional[str] = None
    federation_state: Optional[ReadableFederationState] = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.domain = self._view["domain"]
        self.published = self._view["published"]
        if "updated" in self._view.keys():
            self.updated = self._view["updated"]
        else:
            self.updated = None
        if "software" in self._view.keys():
            self.software = self._view["software"]
        else:
            self.software = None
        if "version" in self._view.keys():
            self.version = self._view["version"]
        else:
            self.version = None
        if "federation_state" in self._view.keys():
            self.federation_state = ReadableFederationState(self._view["federation_state"])
        else:
            self.federation_state = None


class CommunityAggregates(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CommunityAggregates.html"""

    community_id: int = None
    subscribers: int = None
    posts: int = None
    comments: int = None
    published: str = None
    users_active_day: int = None
    users_active_week: int = None
    users_active_month: int = None
    users_active_half_year: int = None
    subscribers_local: int = None

    def parse(self) -> None:
        self.community_id = self._view["community_id"]
        self.subscribers = self._view["subscribers"]
        self.posts = self._view["posts"]
        self.comments = self._view["comments"]
        self.published = self._view["published"]
        self.users_active_day = self._view["users_active_day"]
        self.users_active_week = self._view["users_active_week"]
        self.users_active_month = self._view["users_active_month"]
        self.users_active_half_year = self._view["users_active_half_year"]
        self.subscribers_local = self._view["subscribers_local"]


class LocalImage(ParsableObject):
    """https://join-lemmy.org/api/interfaces/LocalImage.html"""

    local_user_id: Optional[int] = None
    pictrs_alias: str = None
    pictrs_delete_token: str = None
    published: str = None

    def parse(self) -> None:
        if "local_user_id" in self._view.keys():
            self.local_user_id = self._view["local_user_id"]
        else:
            self.local_user_id = None
        self.pictrs_alias = self._view["pictrs_alias"]
        self.pictrs_delete_token = self._view["pictrs_delete_token"]
        self.published = self._view["published"]


class EditCommunity(ParsableObject):
    """https://join-lemmy.org/api/interfaces/EditCommunity.html"""

    community_id: int = None
    title: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None
    banner: Optional[str] = None
    nsfw: Optional[bool] = None
    posting_restricted_to_mods: Optional[bool] = None
    discussion_languages: Optional[list[int]] = None
    visibility: Optional[str] = None

    def parse(self) -> None:
        self.community_id = self._view["community_id"]
        if "title" in self._view.keys():
            self.title = self._view["title"]
        else:
            self.title = None
        if "description" in self._view.keys():
            self.description = self._view["description"]
        else:
            self.description = None
        if "icon" in self._view.keys():
            self.icon = self._view["icon"]
        else:
            self.icon = None
        if "banner" in self._view.keys():
            self.banner = self._view["banner"]
        else:
            self.banner = None
        if "nsfw" in self._view.keys():
            self.nsfw = self._view["nsfw"]
        else:
            self.nsfw = None
        if "posting_restricted_to_mods" in self._view.keys():
            self.posting_restricted_to_mods = self._view["posting_restricted_to_mods"]
        else:
            self.posting_restricted_to_mods = None
        if "discussion_languages" in self._view.keys():
            self.discussion_languages = [int(e) for e in self._view["discussion_languages"]]
        else:
            self.discussion_languages = None
        if "visibility" in self._view.keys():
            self.visibility = self._view["visibility"]
        else:
            self.visibility = None


class ListPostLikes(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ListPostLikes.html"""

    post_id: int = None
    page: Optional[int] = None
    limit: Optional[int] = None

    def parse(self) -> None:
        self.post_id = self._view["post_id"]
        if "page" in self._view.keys():
            self.page = self._view["page"]
        else:
            self.page = None
        if "limit" in self._view.keys():
            self.limit = self._view["limit"]
        else:
            self.limit = None


class CommentReply(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CommentReply.html"""

    id: int = None
    recipient_id: int = None
    comment_id: int = None
    read: bool = None
    published: str = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.recipient_id = self._view["recipient_id"]
        self.comment_id = self._view["comment_id"]
        self.read = self._view["read"]
        self.published = self._view["published"]


class ModRemovePost(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModRemovePost.html"""

    id: int = None
    mod_person_id: int = None
    post_id: int = None
    reason: Optional[str] = None
    removed: bool = None
    when_: str = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.mod_person_id = self._view["mod_person_id"]
        self.post_id = self._view["post_id"]
        if "reason" in self._view.keys():
            self.reason = self._view["reason"]
        else:
            self.reason = None
        self.removed = self._view["removed"]
        self.when_ = self._view["when_"]


class BanFromCommunity(ParsableObject):
    """https://join-lemmy.org/api/interfaces/BanFromCommunity.html"""

    community_id: int = None
    person_id: int = None
    ban: bool = None
    remove_data: Optional[bool] = None
    reason: Optional[str] = None
    expires: Optional[int] = None

    def parse(self) -> None:
        self.community_id = self._view["community_id"]
        self.person_id = self._view["person_id"]
        self.ban = self._view["ban"]
        if "remove_data" in self._view.keys():
            self.remove_data = self._view["remove_data"]
        else:
            self.remove_data = None
        if "reason" in self._view.keys():
            self.reason = self._view["reason"]
        else:
            self.reason = None
        if "expires" in self._view.keys():
            self.expires = self._view["expires"]
        else:
            self.expires = None


class CreatePostLike(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CreatePostLike.html"""

    post_id: int = None
    score: int = None

    def parse(self) -> None:
        self.post_id = self._view["post_id"]
        self.score = self._view["score"]


class RemovePost(ParsableObject):
    """https://join-lemmy.org/api/interfaces/RemovePost.html"""

    post_id: int = None
    removed: bool = None
    reason: Optional[str] = None

    def parse(self) -> None:
        self.post_id = self._view["post_id"]
        self.removed = self._view["removed"]
        if "reason" in self._view.keys():
            self.reason = self._view["reason"]
        else:
            self.reason = None


class EditPrivateMessage(ParsableObject):
    """https://join-lemmy.org/api/interfaces/EditPrivateMessage.html"""

    private_message_id: int = None
    content: str = None

    def parse(self) -> None:
        self.private_message_id = self._view["private_message_id"]
        self.content = self._view["content"]


class ImageDetails(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ImageDetails.html"""

    link: str = None
    width: int = None
    height: int = None
    content_type: str = None

    def parse(self) -> None:
        self.link = self._view["link"]
        self.width = self._view["width"]
        self.height = self._view["height"]
        self.content_type = self._view["content_type"]


class GetModlog(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetModlog.html"""

    mod_person_id: Optional[int] = None
    community_id: Optional[int] = None
    page: Optional[int] = None
    limit: Optional[int] = None
    type_: Optional[str] = None
    other_person_id: Optional[int] = None
    post_id: Optional[int] = None
    comment_id: Optional[int] = None

    def parse(self) -> None:
        if "mod_person_id" in self._view.keys():
            self.mod_person_id = self._view["mod_person_id"]
        else:
            self.mod_person_id = None
        if "community_id" in self._view.keys():
            self.community_id = self._view["community_id"]
        else:
            self.community_id = None
        if "page" in self._view.keys():
            self.page = self._view["page"]
        else:
            self.page = None
        if "limit" in self._view.keys():
            self.limit = self._view["limit"]
        else:
            self.limit = None
        if "type_" in self._view.keys():
            self.type_ = self._view["type_"]
        else:
            self.type_ = None
        if "other_person_id" in self._view.keys():
            self.other_person_id = self._view["other_person_id"]
        else:
            self.other_person_id = None
        if "post_id" in self._view.keys():
            self.post_id = self._view["post_id"]
        else:
            self.post_id = None
        if "comment_id" in self._view.keys():
            self.comment_id = self._view["comment_id"]
        else:
            self.comment_id = None


class SaveUserSettings(ParsableObject):
    """https://join-lemmy.org/api/interfaces/SaveUserSettings.html"""

    show_nsfw: Optional[bool] = None
    blur_nsfw: Optional[bool] = None
    auto_expand: Optional[bool] = None
    theme: Optional[str] = None
    default_sort_type: Optional[str] = None
    default_listing_type: Optional[str] = None
    interface_language: Optional[str] = None
    avatar: Optional[str] = None
    banner: Optional[str] = None
    display_name: Optional[str] = None
    email: Optional[str] = None
    bio: Optional[str] = None
    matrix_user_id: Optional[str] = None
    show_avatars: Optional[bool] = None
    send_notifications_to_email: Optional[bool] = None
    bot_account: Optional[bool] = None
    show_bot_accounts: Optional[bool] = None
    show_read_posts: Optional[bool] = None
    discussion_languages: Optional[list[int]] = None
    open_links_in_new_tab: Optional[bool] = None
    infinite_scroll_enabled: Optional[bool] = None
    post_listing_mode: Optional[str] = None
    enable_keyboard_navigation: Optional[bool] = None
    enable_animated_images: Optional[bool] = None
    collapse_bot_comments: Optional[bool] = None
    show_scores: Optional[bool] = None
    show_upvotes: Optional[bool] = None
    show_downvotes: Optional[bool] = None
    show_upvote_percentage: Optional[bool] = None

    def parse(self) -> None:
        if "show_nsfw" in self._view.keys():
            self.show_nsfw = self._view["show_nsfw"]
        else:
            self.show_nsfw = None
        if "blur_nsfw" in self._view.keys():
            self.blur_nsfw = self._view["blur_nsfw"]
        else:
            self.blur_nsfw = None
        if "auto_expand" in self._view.keys():
            self.auto_expand = self._view["auto_expand"]
        else:
            self.auto_expand = None
        if "theme" in self._view.keys():
            self.theme = self._view["theme"]
        else:
            self.theme = None
        if "default_sort_type" in self._view.keys():
            self.default_sort_type = self._view["default_sort_type"]
        else:
            self.default_sort_type = None
        if "default_listing_type" in self._view.keys():
            self.default_listing_type = self._view["default_listing_type"]
        else:
            self.default_listing_type = None
        if "interface_language" in self._view.keys():
            self.interface_language = self._view["interface_language"]
        else:
            self.interface_language = None
        if "avatar" in self._view.keys():
            self.avatar = self._view["avatar"]
        else:
            self.avatar = None
        if "banner" in self._view.keys():
            self.banner = self._view["banner"]
        else:
            self.banner = None
        if "display_name" in self._view.keys():
            self.display_name = self._view["display_name"]
        else:
            self.display_name = None
        if "email" in self._view.keys():
            self.email = self._view["email"]
        else:
            self.email = None
        if "bio" in self._view.keys():
            self.bio = self._view["bio"]
        else:
            self.bio = None
        if "matrix_user_id" in self._view.keys():
            self.matrix_user_id = self._view["matrix_user_id"]
        else:
            self.matrix_user_id = None
        if "show_avatars" in self._view.keys():
            self.show_avatars = self._view["show_avatars"]
        else:
            self.show_avatars = None
        if "send_notifications_to_email" in self._view.keys():
            self.send_notifications_to_email = self._view["send_notifications_to_email"]
        else:
            self.send_notifications_to_email = None
        if "bot_account" in self._view.keys():
            self.bot_account = self._view["bot_account"]
        else:
            self.bot_account = None
        if "show_bot_accounts" in self._view.keys():
            self.show_bot_accounts = self._view["show_bot_accounts"]
        else:
            self.show_bot_accounts = None
        if "show_read_posts" in self._view.keys():
            self.show_read_posts = self._view["show_read_posts"]
        else:
            self.show_read_posts = None
        if "discussion_languages" in self._view.keys():
            self.discussion_languages = [int(e) for e in self._view["discussion_languages"]]
        else:
            self.discussion_languages = None
        if "open_links_in_new_tab" in self._view.keys():
            self.open_links_in_new_tab = self._view["open_links_in_new_tab"]
        else:
            self.open_links_in_new_tab = None
        if "infinite_scroll_enabled" in self._view.keys():
            self.infinite_scroll_enabled = self._view["infinite_scroll_enabled"]
        else:
            self.infinite_scroll_enabled = None
        if "post_listing_mode" in self._view.keys():
            self.post_listing_mode = self._view["post_listing_mode"]
        else:
            self.post_listing_mode = None
        if "enable_keyboard_navigation" in self._view.keys():
            self.enable_keyboard_navigation = self._view["enable_keyboard_navigation"]
        else:
            self.enable_keyboard_navigation = None
        if "enable_animated_images" in self._view.keys():
            self.enable_animated_images = self._view["enable_animated_images"]
        else:
            self.enable_animated_images = None
        if "collapse_bot_comments" in self._view.keys():
            self.collapse_bot_comments = self._view["collapse_bot_comments"]
        else:
            self.collapse_bot_comments = None
        if "show_scores" in self._view.keys():
            self.show_scores = self._view["show_scores"]
        else:
            self.show_scores = None
        if "show_upvotes" in self._view.keys():
            self.show_upvotes = self._view["show_upvotes"]
        else:
            self.show_upvotes = None
        if "show_downvotes" in self._view.keys():
            self.show_downvotes = self._view["show_downvotes"]
        else:
            self.show_downvotes = None
        if "show_upvote_percentage" in self._view.keys():
            self.show_upvote_percentage = self._view["show_upvote_percentage"]
        else:
            self.show_upvote_percentage = None


class CreatePrivateMessage(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CreatePrivateMessage.html"""

    content: str = None
    recipient_id: int = None

    def parse(self) -> None:
        self.content = self._view["content"]
        self.recipient_id = self._view["recipient_id"]


class LocalSiteRateLimit(ParsableObject):
    """https://join-lemmy.org/api/interfaces/LocalSiteRateLimit.html"""

    local_site_id: int = None
    message: int = None
    message_per_second: int = None
    post: int = None
    post_per_second: int = None
    register: int = None
    register_per_second: int = None
    image: int = None
    image_per_second: int = None
    comment: int = None
    comment_per_second: int = None
    search: int = None
    search_per_second: int = None
    published: str = None
    updated: Optional[str] = None
    import_user_settings: int = None
    import_user_settings_per_second: int = None

    def parse(self) -> None:
        self.local_site_id = self._view["local_site_id"]
        self.message = self._view["message"]
        self.message_per_second = self._view["message_per_second"]
        self.post = self._view["post"]
        self.post_per_second = self._view["post_per_second"]
        self.register = self._view["register"]
        self.register_per_second = self._view["register_per_second"]
        self.image = self._view["image"]
        self.image_per_second = self._view["image_per_second"]
        self.comment = self._view["comment"]
        self.comment_per_second = self._view["comment_per_second"]
        self.search = self._view["search"]
        self.search_per_second = self._view["search_per_second"]
        self.published = self._view["published"]
        if "updated" in self._view.keys():
            self.updated = self._view["updated"]
        else:
            self.updated = None
        self.import_user_settings = self._view["import_user_settings"]
        self.import_user_settings_per_second = self._view["import_user_settings_per_second"]


class ListCommentLikes(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ListCommentLikes.html"""

    comment_id: int = None
    page: Optional[int] = None
    limit: Optional[int] = None

    def parse(self) -> None:
        self.comment_id = self._view["comment_id"]
        if "page" in self._view.keys():
            self.page = self._view["page"]
        else:
            self.page = None
        if "limit" in self._view.keys():
            self.limit = self._view["limit"]
        else:
            self.limit = None


class SaveComment(ParsableObject):
    """https://join-lemmy.org/api/interfaces/SaveComment.html"""

    comment_id: int = None
    save: bool = None

    def parse(self) -> None:
        self.comment_id = self._view["comment_id"]
        self.save = self._view["save"]


class ListMedia(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ListMedia.html"""

    page: Optional[int] = None
    limit: Optional[int] = None

    def parse(self) -> None:
        if "page" in self._view.keys():
            self.page = self._view["page"]
        else:
            self.page = None
        if "limit" in self._view.keys():
            self.limit = self._view["limit"]
        else:
            self.limit = None


class LocalSite(ParsableObject):
    """https://join-lemmy.org/api/interfaces/LocalSite.html"""

    id: int = None
    site_id: int = None
    site_setup: bool = None
    enable_downvotes: bool = None
    enable_nsfw: bool = None
    community_creation_admin_only: bool = None
    require_email_verification: bool = None
    application_question: Optional[str] = None
    private_instance: bool = None
    default_theme: str = None
    default_post_listing_type: str = None
    legal_information: Optional[str] = None
    hide_modlog_mod_names: bool = None
    application_email_admins: bool = None
    slur_filter_regex: Optional[str] = None
    actor_name_max_length: int = None
    federation_enabled: bool = None
    captcha_enabled: bool = None
    captcha_difficulty: str = None
    published: str = None
    updated: Optional[str] = None
    registration_mode: str = None
    reports_email_admins: bool = None
    federation_signed_fetch: bool = None
    default_post_listing_mode: str = None
    default_sort_type: str = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.site_id = self._view["site_id"]
        self.site_setup = self._view["site_setup"]
        self.enable_downvotes = self._view["enable_downvotes"]
        self.enable_nsfw = self._view["enable_nsfw"]
        self.community_creation_admin_only = self._view["community_creation_admin_only"]
        self.require_email_verification = self._view["require_email_verification"]
        if "application_question" in self._view.keys():
            self.application_question = self._view["application_question"]
        else:
            self.application_question = None
        self.private_instance = self._view["private_instance"]
        self.default_theme = self._view["default_theme"]
        self.default_post_listing_type = self._view["default_post_listing_type"]
        if "legal_information" in self._view.keys():
            self.legal_information = self._view["legal_information"]
        else:
            self.legal_information = None
        self.hide_modlog_mod_names = self._view["hide_modlog_mod_names"]
        self.application_email_admins = self._view["application_email_admins"]
        if "slur_filter_regex" in self._view.keys():
            self.slur_filter_regex = self._view["slur_filter_regex"]
        else:
            self.slur_filter_regex = None
        self.actor_name_max_length = self._view["actor_name_max_length"]
        self.federation_enabled = self._view["federation_enabled"]
        self.captcha_enabled = self._view["captcha_enabled"]
        self.captcha_difficulty = self._view["captcha_difficulty"]
        self.published = self._view["published"]
        if "updated" in self._view.keys():
            self.updated = self._view["updated"]
        else:
            self.updated = None
        self.registration_mode = self._view["registration_mode"]
        self.reports_email_admins = self._view["reports_email_admins"]
        self.federation_signed_fetch = self._view["federation_signed_fetch"]
        self.default_post_listing_mode = self._view["default_post_listing_mode"]
        self.default_sort_type = self._view["default_sort_type"]


class CustomEmojiKeyword(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CustomEmojiKeyword.html"""

    custom_emoji_id: int = None
    keyword: str = None

    def parse(self) -> None:
        self.custom_emoji_id = self._view["custom_emoji_id"]
        self.keyword = self._view["keyword"]


class ModlogListParams(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModlogListParams.html"""

    community_id: Optional[int] = None
    mod_person_id: Optional[int] = None
    other_person_id: Optional[int] = None
    post_id: Optional[int] = None
    comment_id: Optional[int] = None
    page: Optional[int] = None
    limit: Optional[int] = None
    hide_modlog_names: bool = None

    def parse(self) -> None:
        if "community_id" in self._view.keys():
            self.community_id = self._view["community_id"]
        else:
            self.community_id = None
        if "mod_person_id" in self._view.keys():
            self.mod_person_id = self._view["mod_person_id"]
        else:
            self.mod_person_id = None
        if "other_person_id" in self._view.keys():
            self.other_person_id = self._view["other_person_id"]
        else:
            self.other_person_id = None
        if "post_id" in self._view.keys():
            self.post_id = self._view["post_id"]
        else:
            self.post_id = None
        if "comment_id" in self._view.keys():
            self.comment_id = self._view["comment_id"]
        else:
            self.comment_id = None
        if "page" in self._view.keys():
            self.page = self._view["page"]
        else:
            self.page = None
        if "limit" in self._view.keys():
            self.limit = self._view["limit"]
        else:
            self.limit = None
        self.hide_modlog_names = self._view["hide_modlog_names"]


class ModRemoveComment(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModRemoveComment.html"""

    id: int = None
    mod_person_id: int = None
    comment_id: int = None
    reason: Optional[str] = None
    removed: bool = None
    when_: str = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.mod_person_id = self._view["mod_person_id"]
        self.comment_id = self._view["comment_id"]
        if "reason" in self._view.keys():
            self.reason = self._view["reason"]
        else:
            self.reason = None
        self.removed = self._view["removed"]
        self.when_ = self._view["when_"]


class GetComments(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetComments.html"""

    type_: Optional[str] = None
    sort: Optional[str] = None
    max_depth: Optional[int] = None
    page: Optional[int] = None
    limit: Optional[int] = None
    community_id: Optional[int] = None
    community_name: Optional[str] = None
    post_id: Optional[int] = None
    parent_id: Optional[int] = None
    saved_only: Optional[bool] = None
    liked_only: Optional[bool] = None
    disliked_only: Optional[bool] = None

    def parse(self) -> None:
        if "type_" in self._view.keys():
            self.type_ = self._view["type_"]
        else:
            self.type_ = None
        if "sort" in self._view.keys():
            self.sort = self._view["sort"]
        else:
            self.sort = None
        if "max_depth" in self._view.keys():
            self.max_depth = self._view["max_depth"]
        else:
            self.max_depth = None
        if "page" in self._view.keys():
            self.page = self._view["page"]
        else:
            self.page = None
        if "limit" in self._view.keys():
            self.limit = self._view["limit"]
        else:
            self.limit = None
        if "community_id" in self._view.keys():
            self.community_id = self._view["community_id"]
        else:
            self.community_id = None
        if "community_name" in self._view.keys():
            self.community_name = self._view["community_name"]
        else:
            self.community_name = None
        if "post_id" in self._view.keys():
            self.post_id = self._view["post_id"]
        else:
            self.post_id = None
        if "parent_id" in self._view.keys():
            self.parent_id = self._view["parent_id"]
        else:
            self.parent_id = None
        if "saved_only" in self._view.keys():
            self.saved_only = self._view["saved_only"]
        else:
            self.saved_only = None
        if "liked_only" in self._view.keys():
            self.liked_only = self._view["liked_only"]
        else:
            self.liked_only = None
        if "disliked_only" in self._view.keys():
            self.disliked_only = self._view["disliked_only"]
        else:
            self.disliked_only = None


class ModBanFromCommunity(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModBanFromCommunity.html"""

    id: int = None
    mod_person_id: int = None
    other_person_id: int = None
    community_id: int = None
    reason: Optional[str] = None
    banned: bool = None
    expires: Optional[str] = None
    when_: str = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.mod_person_id = self._view["mod_person_id"]
        self.other_person_id = self._view["other_person_id"]
        self.community_id = self._view["community_id"]
        if "reason" in self._view.keys():
            self.reason = self._view["reason"]
        else:
            self.reason = None
        self.banned = self._view["banned"]
        if "expires" in self._view.keys():
            self.expires = self._view["expires"]
        else:
            self.expires = None
        self.when_ = self._view["when_"]


class MarkPersonMentionAsRead(ParsableObject):
    """https://join-lemmy.org/api/interfaces/MarkPersonMentionAsRead.html"""

    person_mention_id: int = None
    read: bool = None

    def parse(self) -> None:
        self.person_mention_id = self._view["person_mention_id"]
        self.read = self._view["read"]


class GetCommunity(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetCommunity.html"""

    id: Optional[int] = None
    name: Optional[str] = None

    def parse(self) -> None:
        if "id" in self._view.keys():
            self.id = self._view["id"]
        else:
            self.id = None
        if "name" in self._view.keys():
            self.name = self._view["name"]
        else:
            self.name = None


class PrivateMessageReport(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PrivateMessageReport.html"""

    id: int = None
    creator_id: int = None
    private_message_id: int = None
    original_pm_text: str = None
    reason: str = None
    resolved: bool = None
    resolver_id: Optional[int] = None
    published: str = None
    updated: Optional[str] = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.creator_id = self._view["creator_id"]
        self.private_message_id = self._view["private_message_id"]
        self.original_pm_text = self._view["original_pm_text"]
        self.reason = self._view["reason"]
        self.resolved = self._view["resolved"]
        if "resolver_id" in self._view.keys():
            self.resolver_id = self._view["resolver_id"]
        else:
            self.resolver_id = None
        self.published = self._view["published"]
        if "updated" in self._view.keys():
            self.updated = self._view["updated"]
        else:
            self.updated = None


class SavePost(ParsableObject):
    """https://join-lemmy.org/api/interfaces/SavePost.html"""

    post_id: int = None
    save: bool = None

    def parse(self) -> None:
        self.post_id = self._view["post_id"]
        self.save = self._view["save"]


class PasswordReset(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PasswordReset.html"""

    email: str = None

    def parse(self) -> None:
        self.email = self._view["email"]


class CreateCommentReport(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CreateCommentReport.html"""

    comment_id: int = None
    reason: str = None

    def parse(self) -> None:
        self.comment_id = self._view["comment_id"]
        self.reason = self._view["reason"]


class CreateCommentLike(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CreateCommentLike.html"""

    comment_id: int = None
    score: int = None

    def parse(self) -> None:
        self.comment_id = self._view["comment_id"]
        self.score = self._view["score"]


class Register(ParsableObject):
    """https://join-lemmy.org/api/interfaces/Register.html"""

    username: str = None
    password: str = None
    password_verify: str = None
    show_nsfw: Optional[bool] = None
    email: Optional[str] = None
    captcha_uuid: Optional[str] = None
    captcha_answer: Optional[str] = None
    honeypot: Optional[str] = None
    answer: Optional[str] = None

    def parse(self) -> None:
        self.username = self._view["username"]
        self.password = self._view["password"]
        self.password_verify = self._view["password_verify"]
        if "show_nsfw" in self._view.keys():
            self.show_nsfw = self._view["show_nsfw"]
        else:
            self.show_nsfw = None
        if "email" in self._view.keys():
            self.email = self._view["email"]
        else:
            self.email = None
        if "captcha_uuid" in self._view.keys():
            self.captcha_uuid = self._view["captcha_uuid"]
        else:
            self.captcha_uuid = None
        if "captcha_answer" in self._view.keys():
            self.captcha_answer = self._view["captcha_answer"]
        else:
            self.captcha_answer = None
        if "honeypot" in self._view.keys():
            self.honeypot = self._view["honeypot"]
        else:
            self.honeypot = None
        if "answer" in self._view.keys():
            self.answer = self._view["answer"]
        else:
            self.answer = None


class FederatedInstances(ParsableObject):
    """https://join-lemmy.org/api/interfaces/FederatedInstances.html"""

    linked: list[InstanceWithFederationState] = None
    allowed: list[InstanceWithFederationState] = None
    blocked: list[InstanceWithFederationState] = None

    def parse(self) -> None:
        self.linked = [InstanceWithFederationState(e) for e in self._view["linked"]]
        self.allowed = [InstanceWithFederationState(e) for e in self._view["allowed"]]
        self.blocked = [InstanceWithFederationState(e) for e in self._view["blocked"]]


class DeleteAccount(ParsableObject):
    """https://join-lemmy.org/api/interfaces/DeleteAccount.html"""

    password: str = None
    delete_content: bool = None

    def parse(self) -> None:
        self.password = self._view["password"]
        self.delete_content = self._view["delete_content"]


class MarkPrivateMessageAsRead(ParsableObject):
    """https://join-lemmy.org/api/interfaces/MarkPrivateMessageAsRead.html"""

    private_message_id: int = None
    read: bool = None

    def parse(self) -> None:
        self.private_message_id = self._view["private_message_id"]
        self.read = self._view["read"]


class GetComment(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetComment.html"""

    id: int = None

    def parse(self) -> None:
        self.id = self._view["id"]


class PurgeCommunity(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PurgeCommunity.html"""

    community_id: int = None
    reason: Optional[str] = None

    def parse(self) -> None:
        self.community_id = self._view["community_id"]
        if "reason" in self._view.keys():
            self.reason = self._view["reason"]
        else:
            self.reason = None


class AddAdmin(ParsableObject):
    """https://join-lemmy.org/api/interfaces/AddAdmin.html"""

    person_id: int = None
    added: bool = None

    def parse(self) -> None:
        self.person_id = self._view["person_id"]
        self.added = self._view["added"]


class ModTransferCommunity(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModTransferCommunity.html"""

    id: int = None
    mod_person_id: int = None
    other_person_id: int = None
    community_id: int = None
    when_: str = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.mod_person_id = self._view["mod_person_id"]
        self.other_person_id = self._view["other_person_id"]
        self.community_id = self._view["community_id"]
        self.when_ = self._view["when_"]


class Person(ParsableObject):
    """https://join-lemmy.org/api/interfaces/Person.html"""

    id: int = None
    name: str = None
    display_name: Optional[str] = None
    avatar: Optional[str] = None
    banned: bool = None
    published: str = None
    updated: Optional[str] = None
    actor_id: str = None
    bio: Optional[str] = None
    local: bool = None
    banner: Optional[str] = None
    deleted: bool = None
    matrix_user_id: Optional[str] = None
    bot_account: bool = None
    ban_expires: Optional[str] = None
    instance_id: int = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.name = self._view["name"]
        if "display_name" in self._view.keys():
            self.display_name = self._view["display_name"]
        else:
            self.display_name = None
        if "avatar" in self._view.keys():
            self.avatar = self._view["avatar"]
        else:
            self.avatar = None
        self.banned = self._view["banned"]
        self.published = self._view["published"]
        if "updated" in self._view.keys():
            self.updated = self._view["updated"]
        else:
            self.updated = None
        self.actor_id = self._view["actor_id"]
        if "bio" in self._view.keys():
            self.bio = self._view["bio"]
        else:
            self.bio = None
        self.local = self._view["local"]
        if "banner" in self._view.keys():
            self.banner = self._view["banner"]
        else:
            self.banner = None
        self.deleted = self._view["deleted"]
        if "matrix_user_id" in self._view.keys():
            self.matrix_user_id = self._view["matrix_user_id"]
        else:
            self.matrix_user_id = None
        self.bot_account = self._view["bot_account"]
        if "ban_expires" in self._view.keys():
            self.ban_expires = self._view["ban_expires"]
        else:
            self.ban_expires = None
        self.instance_id = self._view["instance_id"]


class Comment(ParsableObject):
    """https://join-lemmy.org/api/interfaces/Comment.html"""

    id: int = None
    creator_id: int = None
    post_id: int = None
    content: str = None
    removed: bool = None
    published: str = None
    updated: Optional[str] = None
    deleted: bool = None
    ap_id: str = None
    local: bool = None
    path: str = None
    distinguished: bool = None
    language_id: int = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.creator_id = self._view["creator_id"]
        self.post_id = self._view["post_id"]
        self.content = self._view["content"]
        self.removed = self._view["removed"]
        self.published = self._view["published"]
        if "updated" in self._view.keys():
            self.updated = self._view["updated"]
        else:
            self.updated = None
        self.deleted = self._view["deleted"]
        self.ap_id = self._view["ap_id"]
        self.local = self._view["local"]
        self.path = self._view["path"]
        self.distinguished = self._view["distinguished"]
        self.language_id = self._view["language_id"]


class OpenGraphData(ParsableObject):
    """https://join-lemmy.org/api/interfaces/OpenGraphData.html"""

    title: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None
    embed_video_url: Optional[str] = None

    def parse(self) -> None:
        if "title" in self._view.keys():
            self.title = self._view["title"]
        else:
            self.title = None
        if "description" in self._view.keys():
            self.description = self._view["description"]
        else:
            self.description = None
        if "image" in self._view.keys():
            self.image = self._view["image"]
        else:
            self.image = None
        if "embed_video_url" in self._view.keys():
            self.embed_video_url = self._view["embed_video_url"]
        else:
            self.embed_video_url = None


class PurgePerson(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PurgePerson.html"""

    person_id: int = None
    reason: Optional[str] = None

    def parse(self) -> None:
        self.person_id = self._view["person_id"]
        if "reason" in self._view.keys():
            self.reason = self._view["reason"]
        else:
            self.reason = None


class BlockCommunity(ParsableObject):
    """https://join-lemmy.org/api/interfaces/BlockCommunity.html"""

    community_id: int = None
    block: bool = None

    def parse(self) -> None:
        self.community_id = self._view["community_id"]
        self.block = self._view["block"]


class AdminPurgePost(ParsableObject):
    """https://join-lemmy.org/api/interfaces/AdminPurgePost.html"""

    id: int = None
    admin_person_id: int = None
    community_id: int = None
    reason: Optional[str] = None
    when_: str = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.admin_person_id = self._view["admin_person_id"]
        self.community_id = self._view["community_id"]
        if "reason" in self._view.keys():
            self.reason = self._view["reason"]
        else:
            self.reason = None
        self.when_ = self._view["when_"]


class ResolvePostReport(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ResolvePostReport.html"""

    report_id: int = None
    resolved: bool = None

    def parse(self) -> None:
        self.report_id = self._view["report_id"]
        self.resolved = self._view["resolved"]


class CreateComment(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CreateComment.html"""

    content: str = None
    post_id: int = None
    parent_id: Optional[int] = None
    language_id: Optional[int] = None

    def parse(self) -> None:
        self.content = self._view["content"]
        self.post_id = self._view["post_id"]
        if "parent_id" in self._view.keys():
            self.parent_id = self._view["parent_id"]
        else:
            self.parent_id = None
        if "language_id" in self._view.keys():
            self.language_id = self._view["language_id"]
        else:
            self.language_id = None


class ListRegistrationApplications(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ListRegistrationApplications.html"""

    unread_only: Optional[bool] = None
    page: Optional[int] = None
    limit: Optional[int] = None

    def parse(self) -> None:
        if "unread_only" in self._view.keys():
            self.unread_only = self._view["unread_only"]
        else:
            self.unread_only = None
        if "page" in self._view.keys():
            self.page = self._view["page"]
        else:
            self.page = None
        if "limit" in self._view.keys():
            self.limit = self._view["limit"]
        else:
            self.limit = None


class DistinguishComment(ParsableObject):
    """https://join-lemmy.org/api/interfaces/DistinguishComment.html"""

    comment_id: int = None
    distinguished: bool = None

    def parse(self) -> None:
        self.comment_id = self._view["comment_id"]
        self.distinguished = self._view["distinguished"]


class CommentReport(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CommentReport.html"""

    id: int = None
    creator_id: int = None
    comment_id: int = None
    original_comment_text: str = None
    reason: str = None
    resolved: bool = None
    resolver_id: Optional[int] = None
    published: str = None
    updated: Optional[str] = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.creator_id = self._view["creator_id"]
        self.comment_id = self._view["comment_id"]
        self.original_comment_text = self._view["original_comment_text"]
        self.reason = self._view["reason"]
        self.resolved = self._view["resolved"]
        if "resolver_id" in self._view.keys():
            self.resolver_id = self._view["resolver_id"]
        else:
            self.resolver_id = None
        self.published = self._view["published"]
        if "updated" in self._view.keys():
            self.updated = self._view["updated"]
        else:
            self.updated = None


class DeleteCustomEmoji(ParsableObject):
    """https://join-lemmy.org/api/interfaces/DeleteCustomEmoji.html"""

    id: int = None

    def parse(self) -> None:
        self.id = self._view["id"]


class BanPerson(ParsableObject):
    """https://join-lemmy.org/api/interfaces/BanPerson.html"""

    person_id: int = None
    ban: bool = None
    remove_data: Optional[bool] = None
    reason: Optional[str] = None
    expires: Optional[int] = None

    def parse(self) -> None:
        self.person_id = self._view["person_id"]
        self.ban = self._view["ban"]
        if "remove_data" in self._view.keys():
            self.remove_data = self._view["remove_data"]
        else:
            self.remove_data = None
        if "reason" in self._view.keys():
            self.reason = self._view["reason"]
        else:
            self.reason = None
        if "expires" in self._view.keys():
            self.expires = self._view["expires"]
        else:
            self.expires = None


class ListCommentReports(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ListCommentReports.html"""

    comment_id: Optional[int] = None
    page: Optional[int] = None
    limit: Optional[int] = None
    unresolved_only: Optional[bool] = None
    community_id: Optional[int] = None

    def parse(self) -> None:
        if "comment_id" in self._view.keys():
            self.comment_id = self._view["comment_id"]
        else:
            self.comment_id = None
        if "page" in self._view.keys():
            self.page = self._view["page"]
        else:
            self.page = None
        if "limit" in self._view.keys():
            self.limit = self._view["limit"]
        else:
            self.limit = None
        if "unresolved_only" in self._view.keys():
            self.unresolved_only = self._view["unresolved_only"]
        else:
            self.unresolved_only = None
        if "community_id" in self._view.keys():
            self.community_id = self._view["community_id"]
        else:
            self.community_id = None


class ModAdd(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModAdd.html"""

    id: int = None
    mod_person_id: int = None
    other_person_id: int = None
    removed: bool = None
    when_: str = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.mod_person_id = self._view["mod_person_id"]
        self.other_person_id = self._view["other_person_id"]
        self.removed = self._view["removed"]
        self.when_ = self._view["when_"]


class EditSite(ParsableObject):
    """https://join-lemmy.org/api/interfaces/EditSite.html"""

    name: Optional[str] = None
    sidebar: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None
    banner: Optional[str] = None
    enable_downvotes: Optional[bool] = None
    enable_nsfw: Optional[bool] = None
    community_creation_admin_only: Optional[bool] = None
    require_email_verification: Optional[bool] = None
    application_question: Optional[str] = None
    private_instance: Optional[bool] = None
    default_theme: Optional[str] = None
    default_post_listing_type: Optional[str] = None
    default_sort_type: Optional[str] = None
    legal_information: Optional[str] = None
    application_email_admins: Optional[bool] = None
    hide_modlog_mod_names: Optional[bool] = None
    discussion_languages: Optional[list[int]] = None
    slur_filter_regex: Optional[str] = None
    actor_name_max_length: Optional[int] = None
    rate_limit_message: Optional[int] = None
    rate_limit_message_per_second: Optional[int] = None
    rate_limit_post: Optional[int] = None
    rate_limit_post_per_second: Optional[int] = None
    rate_limit_register: Optional[int] = None
    rate_limit_register_per_second: Optional[int] = None
    rate_limit_image: Optional[int] = None
    rate_limit_image_per_second: Optional[int] = None
    rate_limit_comment: Optional[int] = None
    rate_limit_comment_per_second: Optional[int] = None
    rate_limit_search: Optional[int] = None
    rate_limit_search_per_second: Optional[int] = None
    federation_enabled: Optional[bool] = None
    federation_debug: Optional[bool] = None
    captcha_enabled: Optional[bool] = None
    captcha_difficulty: Optional[str] = None
    allowed_instances: Optional[list[str]] = None
    blocked_instances: Optional[list[str]] = None
    blocked_urls: Optional[list[str]] = None
    taglines: Optional[list[str]] = None
    registration_mode: Optional[str] = None
    reports_email_admins: Optional[bool] = None
    content_warning: Optional[str] = None
    default_post_listing_mode: Optional[str] = None

    def parse(self) -> None:
        if "name" in self._view.keys():
            self.name = self._view["name"]
        else:
            self.name = None
        if "sidebar" in self._view.keys():
            self.sidebar = self._view["sidebar"]
        else:
            self.sidebar = None
        if "description" in self._view.keys():
            self.description = self._view["description"]
        else:
            self.description = None
        if "icon" in self._view.keys():
            self.icon = self._view["icon"]
        else:
            self.icon = None
        if "banner" in self._view.keys():
            self.banner = self._view["banner"]
        else:
            self.banner = None
        if "enable_downvotes" in self._view.keys():
            self.enable_downvotes = self._view["enable_downvotes"]
        else:
            self.enable_downvotes = None
        if "enable_nsfw" in self._view.keys():
            self.enable_nsfw = self._view["enable_nsfw"]
        else:
            self.enable_nsfw = None
        if "community_creation_admin_only" in self._view.keys():
            self.community_creation_admin_only = self._view["community_creation_admin_only"]
        else:
            self.community_creation_admin_only = None
        if "require_email_verification" in self._view.keys():
            self.require_email_verification = self._view["require_email_verification"]
        else:
            self.require_email_verification = None
        if "application_question" in self._view.keys():
            self.application_question = self._view["application_question"]
        else:
            self.application_question = None
        if "private_instance" in self._view.keys():
            self.private_instance = self._view["private_instance"]
        else:
            self.private_instance = None
        if "default_theme" in self._view.keys():
            self.default_theme = self._view["default_theme"]
        else:
            self.default_theme = None
        if "default_post_listing_type" in self._view.keys():
            self.default_post_listing_type = self._view["default_post_listing_type"]
        else:
            self.default_post_listing_type = None
        if "default_sort_type" in self._view.keys():
            self.default_sort_type = self._view["default_sort_type"]
        else:
            self.default_sort_type = None
        if "legal_information" in self._view.keys():
            self.legal_information = self._view["legal_information"]
        else:
            self.legal_information = None
        if "application_email_admins" in self._view.keys():
            self.application_email_admins = self._view["application_email_admins"]
        else:
            self.application_email_admins = None
        if "hide_modlog_mod_names" in self._view.keys():
            self.hide_modlog_mod_names = self._view["hide_modlog_mod_names"]
        else:
            self.hide_modlog_mod_names = None
        if "discussion_languages" in self._view.keys():
            self.discussion_languages = [int(e) for e in self._view["discussion_languages"]]
        else:
            self.discussion_languages = None
        if "slur_filter_regex" in self._view.keys():
            self.slur_filter_regex = self._view["slur_filter_regex"]
        else:
            self.slur_filter_regex = None
        if "actor_name_max_length" in self._view.keys():
            self.actor_name_max_length = self._view["actor_name_max_length"]
        else:
            self.actor_name_max_length = None
        if "rate_limit_message" in self._view.keys():
            self.rate_limit_message = self._view["rate_limit_message"]
        else:
            self.rate_limit_message = None
        if "rate_limit_message_per_second" in self._view.keys():
            self.rate_limit_message_per_second = self._view["rate_limit_message_per_second"]
        else:
            self.rate_limit_message_per_second = None
        if "rate_limit_post" in self._view.keys():
            self.rate_limit_post = self._view["rate_limit_post"]
        else:
            self.rate_limit_post = None
        if "rate_limit_post_per_second" in self._view.keys():
            self.rate_limit_post_per_second = self._view["rate_limit_post_per_second"]
        else:
            self.rate_limit_post_per_second = None
        if "rate_limit_register" in self._view.keys():
            self.rate_limit_register = self._view["rate_limit_register"]
        else:
            self.rate_limit_register = None
        if "rate_limit_register_per_second" in self._view.keys():
            self.rate_limit_register_per_second = self._view["rate_limit_register_per_second"]
        else:
            self.rate_limit_register_per_second = None
        if "rate_limit_image" in self._view.keys():
            self.rate_limit_image = self._view["rate_limit_image"]
        else:
            self.rate_limit_image = None
        if "rate_limit_image_per_second" in self._view.keys():
            self.rate_limit_image_per_second = self._view["rate_limit_image_per_second"]
        else:
            self.rate_limit_image_per_second = None
        if "rate_limit_comment" in self._view.keys():
            self.rate_limit_comment = self._view["rate_limit_comment"]
        else:
            self.rate_limit_comment = None
        if "rate_limit_comment_per_second" in self._view.keys():
            self.rate_limit_comment_per_second = self._view["rate_limit_comment_per_second"]
        else:
            self.rate_limit_comment_per_second = None
        if "rate_limit_search" in self._view.keys():
            self.rate_limit_search = self._view["rate_limit_search"]
        else:
            self.rate_limit_search = None
        if "rate_limit_search_per_second" in self._view.keys():
            self.rate_limit_search_per_second = self._view["rate_limit_search_per_second"]
        else:
            self.rate_limit_search_per_second = None
        if "federation_enabled" in self._view.keys():
            self.federation_enabled = self._view["federation_enabled"]
        else:
            self.federation_enabled = None
        if "federation_debug" in self._view.keys():
            self.federation_debug = self._view["federation_debug"]
        else:
            self.federation_debug = None
        if "captcha_enabled" in self._view.keys():
            self.captcha_enabled = self._view["captcha_enabled"]
        else:
            self.captcha_enabled = None
        if "captcha_difficulty" in self._view.keys():
            self.captcha_difficulty = self._view["captcha_difficulty"]
        else:
            self.captcha_difficulty = None
        if "allowed_instances" in self._view.keys():
            self.allowed_instances = [str(e) for e in self._view["allowed_instances"]]
        else:
            self.allowed_instances = None
        if "blocked_instances" in self._view.keys():
            self.blocked_instances = [str(e) for e in self._view["blocked_instances"]]
        else:
            self.blocked_instances = None
        if "blocked_urls" in self._view.keys():
            self.blocked_urls = [str(e) for e in self._view["blocked_urls"]]
        else:
            self.blocked_urls = None
        if "taglines" in self._view.keys():
            self.taglines = [str(e) for e in self._view["taglines"]]
        else:
            self.taglines = None
        if "registration_mode" in self._view.keys():
            self.registration_mode = self._view["registration_mode"]
        else:
            self.registration_mode = None
        if "reports_email_admins" in self._view.keys():
            self.reports_email_admins = self._view["reports_email_admins"]
        else:
            self.reports_email_admins = None
        if "content_warning" in self._view.keys():
            self.content_warning = self._view["content_warning"]
        else:
            self.content_warning = None
        if "default_post_listing_mode" in self._view.keys():
            self.default_post_listing_mode = self._view["default_post_listing_mode"]
        else:
            self.default_post_listing_mode = None


class Instance(ParsableObject):
    """https://join-lemmy.org/api/interfaces/Instance.html"""

    id: int = None
    domain: str = None
    published: str = None
    updated: Optional[str] = None
    software: Optional[str] = None
    version: Optional[str] = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.domain = self._view["domain"]
        self.published = self._view["published"]
        if "updated" in self._view.keys():
            self.updated = self._view["updated"]
        else:
            self.updated = None
        if "software" in self._view.keys():
            self.software = self._view["software"]
        else:
            self.software = None
        if "version" in self._view.keys():
            self.version = self._view["version"]
        else:
            self.version = None


class Post(ParsableObject):
    """https://join-lemmy.org/api/interfaces/Post.html"""

    id: int = None
    name: str = None
    url: Optional[str] = None
    body: Optional[str] = None
    creator_id: int = None
    community_id: int = None
    removed: bool = None
    locked: bool = None
    published: str = None
    updated: Optional[str] = None
    deleted: bool = None
    nsfw: bool = None
    embed_title: Optional[str] = None
    embed_description: Optional[str] = None
    thumbnail_url: Optional[str] = None
    ap_id: str = None
    local: bool = None
    embed_video_url: Optional[str] = None
    language_id: int = None
    featured_community: bool = None
    featured_local: bool = None
    url_content_type: Optional[str] = None
    alt_text: Optional[str] = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.name = self._view["name"]
        if "url" in self._view.keys():
            self.url = self._view["url"]
        else:
            self.url = None
        if "body" in self._view.keys():
            self.body = self._view["body"]
        else:
            self.body = None
        self.creator_id = self._view["creator_id"]
        self.community_id = self._view["community_id"]
        self.removed = self._view["removed"]
        self.locked = self._view["locked"]
        self.published = self._view["published"]
        if "updated" in self._view.keys():
            self.updated = self._view["updated"]
        else:
            self.updated = None
        self.deleted = self._view["deleted"]
        self.nsfw = self._view["nsfw"]
        if "embed_title" in self._view.keys():
            self.embed_title = self._view["embed_title"]
        else:
            self.embed_title = None
        if "embed_description" in self._view.keys():
            self.embed_description = self._view["embed_description"]
        else:
            self.embed_description = None
        if "thumbnail_url" in self._view.keys():
            self.thumbnail_url = self._view["thumbnail_url"]
        else:
            self.thumbnail_url = None
        self.ap_id = self._view["ap_id"]
        self.local = self._view["local"]
        if "embed_video_url" in self._view.keys():
            self.embed_video_url = self._view["embed_video_url"]
        else:
            self.embed_video_url = None
        self.language_id = self._view["language_id"]
        self.featured_community = self._view["featured_community"]
        self.featured_local = self._view["featured_local"]
        if "url_content_type" in self._view.keys():
            self.url_content_type = self._view["url_content_type"]
        else:
            self.url_content_type = None
        if "alt_text" in self._view.keys():
            self.alt_text = self._view["alt_text"]
        else:
            self.alt_text = None


class GetPosts(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetPosts.html"""

    type_: Optional[str] = None
    sort: Optional[str] = None
    page: Optional[int] = None
    limit: Optional[int] = None
    community_id: Optional[int] = None
    community_name: Optional[str] = None
    saved_only: Optional[bool] = None
    liked_only: Optional[bool] = None
    disliked_only: Optional[bool] = None
    show_hidden: Optional[bool] = None
    show_read: Optional[bool] = None
    show_nsfw: Optional[bool] = None
    page_cursor: Optional[str] = None

    def parse(self) -> None:
        if "type_" in self._view.keys():
            self.type_ = self._view["type_"]
        else:
            self.type_ = None
        if "sort" in self._view.keys():
            self.sort = self._view["sort"]
        else:
            self.sort = None
        if "page" in self._view.keys():
            self.page = self._view["page"]
        else:
            self.page = None
        if "limit" in self._view.keys():
            self.limit = self._view["limit"]
        else:
            self.limit = None
        if "community_id" in self._view.keys():
            self.community_id = self._view["community_id"]
        else:
            self.community_id = None
        if "community_name" in self._view.keys():
            self.community_name = self._view["community_name"]
        else:
            self.community_name = None
        if "saved_only" in self._view.keys():
            self.saved_only = self._view["saved_only"]
        else:
            self.saved_only = None
        if "liked_only" in self._view.keys():
            self.liked_only = self._view["liked_only"]
        else:
            self.liked_only = None
        if "disliked_only" in self._view.keys():
            self.disliked_only = self._view["disliked_only"]
        else:
            self.disliked_only = None
        if "show_hidden" in self._view.keys():
            self.show_hidden = self._view["show_hidden"]
        else:
            self.show_hidden = None
        if "show_read" in self._view.keys():
            self.show_read = self._view["show_read"]
        else:
            self.show_read = None
        if "show_nsfw" in self._view.keys():
            self.show_nsfw = self._view["show_nsfw"]
        else:
            self.show_nsfw = None
        if "page_cursor" in self._view.keys():
            self.page_cursor = self._view["page_cursor"]
        else:
            self.page_cursor = None


class GetRegistrationApplication(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetRegistrationApplication.html"""

    person_id: int = None

    def parse(self) -> None:
        self.person_id = self._view["person_id"]


class GetReplies(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetReplies.html"""

    sort: Optional[str] = None
    page: Optional[int] = None
    limit: Optional[int] = None
    unread_only: Optional[bool] = None

    def parse(self) -> None:
        if "sort" in self._view.keys():
            self.sort = self._view["sort"]
        else:
            self.sort = None
        if "page" in self._view.keys():
            self.page = self._view["page"]
        else:
            self.page = None
        if "limit" in self._view.keys():
            self.limit = self._view["limit"]
        else:
            self.limit = None
        if "unread_only" in self._view.keys():
            self.unread_only = self._view["unread_only"]
        else:
            self.unread_only = None


class AdminPurgePerson(ParsableObject):
    """https://join-lemmy.org/api/interfaces/AdminPurgePerson.html"""

    id: int = None
    admin_person_id: int = None
    reason: Optional[str] = None
    when_: str = None

    def parse(self) -> None:
        self.id = self._view["id"]
        self.admin_person_id = self._view["admin_person_id"]
        if "reason" in self._view.keys():
            self.reason = self._view["reason"]
        else:
            self.reason = None
        self.when_ = self._view["when_"]


class TransferCommunity(ParsableObject):
    """https://join-lemmy.org/api/interfaces/TransferCommunity.html"""

    community_id: int = None
    person_id: int = None

    def parse(self) -> None:
        self.community_id = self._view["community_id"]
        self.person_id = self._view["person_id"]
