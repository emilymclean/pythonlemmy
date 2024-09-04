from typing import Optional

from .objects import *
from .utils import call_with_filtered_kwarg
from .types import ParsableObjects

class LocalUserView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/LocalUserView.html"""

    local_user: LocalUser = None
    local_user_vote_display_mode: LocalUserVoteDisplayMode = None
    person: Person = None
    counts: PersonAggregates = None

    def parse(self) -> None:
        if "local_user" in self._view.keys():
            self.local_user = LocalUser(self._view["local_user"])
        else:
            self.local_user = None
        if "local_user_vote_display_mode" in self._view.keys():
            self.local_user_vote_display_mode = LocalUserVoteDisplayMode(self._view["local_user_vote_display_mode"])
        else:
            self.local_user_vote_display_mode = None
        if "person" in self._view.keys():
            self.person = Person(self._view["person"])
        else:
            self.person = None
        if "counts" in self._view.keys():
            self.counts = PersonAggregates(self._view["counts"])
        else:
            self.counts = None


class CommentReplyView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CommentReplyView.html"""

    comment_reply: CommentReply = None
    comment: Comment = None
    creator: Person = None
    post: Post = None
    community: Community = None
    recipient: Person = None
    counts: CommentAggregates = None
    creator_banned_from_community: bool = None
    banned_from_community: bool = None
    creator_is_moderator: bool = None
    creator_is_admin: bool = None
    subscribed: str = None
    saved: bool = None
    creator_blocked: bool = None
    my_vote: Optional[int] = None

    def parse(self) -> None:
        if "comment_reply" in self._view.keys():
            self.comment_reply = CommentReply(self._view["comment_reply"])
        else:
            self.comment_reply = None
        if "comment" in self._view.keys():
            self.comment = Comment(self._view["comment"])
        else:
            self.comment = None
        if "creator" in self._view.keys():
            self.creator = Person(self._view["creator"])
        else:
            self.creator = None
        if "post" in self._view.keys():
            self.post = Post(self._view["post"])
        else:
            self.post = None
        if "community" in self._view.keys():
            self.community = Community(self._view["community"])
        else:
            self.community = None
        if "recipient" in self._view.keys():
            self.recipient = Person(self._view["recipient"])
        else:
            self.recipient = None
        if "counts" in self._view.keys():
            self.counts = CommentAggregates(self._view["counts"])
        else:
            self.counts = None
        if "creator_banned_from_community" in self._view.keys():
            self.creator_banned_from_community = self._view["creator_banned_from_community"]
        else:
            self.creator_banned_from_community = None
        if "banned_from_community" in self._view.keys():
            self.banned_from_community = self._view["banned_from_community"]
        else:
            self.banned_from_community = None
        if "creator_is_moderator" in self._view.keys():
            self.creator_is_moderator = self._view["creator_is_moderator"]
        else:
            self.creator_is_moderator = None
        if "creator_is_admin" in self._view.keys():
            self.creator_is_admin = self._view["creator_is_admin"]
        else:
            self.creator_is_admin = None
        if "subscribed" in self._view.keys():
            self.subscribed = self._view["subscribed"]
        else:
            self.subscribed = None
        if "saved" in self._view.keys():
            self.saved = self._view["saved"]
        else:
            self.saved = None
        if "creator_blocked" in self._view.keys():
            self.creator_blocked = self._view["creator_blocked"]
        else:
            self.creator_blocked = None
        if "my_vote" in self._view.keys():
            self.my_vote = self._view["my_vote"]
        else:
            self.my_vote = None


class CommunityFollowerView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CommunityFollowerView.html"""

    community: Community = None
    follower: Person = None

    def parse(self) -> None:
        if "community" in self._view.keys():
            self.community = Community(self._view["community"])
        else:
            self.community = None
        if "follower" in self._view.keys():
            self.follower = Person(self._view["follower"])
        else:
            self.follower = None


class VoteView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/VoteView.html"""

    creator: Person = None
    creator_banned_from_community: bool = None
    score: int = None

    def parse(self) -> None:
        if "creator" in self._view.keys():
            self.creator = Person(self._view["creator"])
        else:
            self.creator = None
        if "creator_banned_from_community" in self._view.keys():
            self.creator_banned_from_community = self._view["creator_banned_from_community"]
        else:
            self.creator_banned_from_community = None
        if "score" in self._view.keys():
            self.score = self._view["score"]
        else:
            self.score = None


class PrivateMessageReportView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PrivateMessageReportView.html"""

    private_message_report: PrivateMessageReport = None
    private_message: PrivateMessage = None
    private_message_creator: Person = None
    creator: Person = None
    resolver: Optional[Person] = None

    def parse(self) -> None:
        if "private_message_report" in self._view.keys():
            self.private_message_report = PrivateMessageReport(self._view["private_message_report"])
        else:
            self.private_message_report = None
        if "private_message" in self._view.keys():
            self.private_message = PrivateMessage(self._view["private_message"])
        else:
            self.private_message = None
        if "private_message_creator" in self._view.keys():
            self.private_message_creator = Person(self._view["private_message_creator"])
        else:
            self.private_message_creator = None
        if "creator" in self._view.keys():
            self.creator = Person(self._view["creator"])
        else:
            self.creator = None
        if "resolver" in self._view.keys():
            self.resolver = Person(self._view["resolver"])
        else:
            self.resolver = None


class ModAddView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModAddView.html"""

    mod_add: ModAdd = None
    moderator: Optional[Person] = None
    modded_person: Person = None

    def parse(self) -> None:
        if "mod_add" in self._view.keys():
            self.mod_add = ModAdd(self._view["mod_add"])
        else:
            self.mod_add = None
        if "moderator" in self._view.keys():
            self.moderator = Person(self._view["moderator"])
        else:
            self.moderator = None
        if "modded_person" in self._view.keys():
            self.modded_person = Person(self._view["modded_person"])
        else:
            self.modded_person = None


class PersonView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PersonView.html"""

    person: Person = None
    counts: PersonAggregates = None
    is_admin: bool = None

    def parse(self) -> None:
        if "person" in self._view.keys():
            self.person = Person(self._view["person"])
        else:
            self.person = None
        if "counts" in self._view.keys():
            self.counts = PersonAggregates(self._view["counts"])
        else:
            self.counts = None
        if "is_admin" in self._view.keys():
            self.is_admin = self._view["is_admin"]
        else:
            self.is_admin = None


class ModBanView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModBanView.html"""

    mod_ban: ModBan = None
    moderator: Optional[Person] = None
    banned_person: Person = None

    def parse(self) -> None:
        if "mod_ban" in self._view.keys():
            self.mod_ban = ModBan(self._view["mod_ban"])
        else:
            self.mod_ban = None
        if "moderator" in self._view.keys():
            self.moderator = Person(self._view["moderator"])
        else:
            self.moderator = None
        if "banned_person" in self._view.keys():
            self.banned_person = Person(self._view["banned_person"])
        else:
            self.banned_person = None


class RegistrationApplicationView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/RegistrationApplicationView.html"""

    registration_application: RegistrationApplication = None
    creator_local_user: LocalUser = None
    creator: Person = None
    admin: Optional[Person] = None

    def parse(self) -> None:
        if "registration_application" in self._view.keys():
            self.registration_application = RegistrationApplication(self._view["registration_application"])
        else:
            self.registration_application = None
        if "creator_local_user" in self._view.keys():
            self.creator_local_user = LocalUser(self._view["creator_local_user"])
        else:
            self.creator_local_user = None
        if "creator" in self._view.keys():
            self.creator = Person(self._view["creator"])
        else:
            self.creator = None
        if "admin" in self._view.keys():
            self.admin = Person(self._view["admin"])
        else:
            self.admin = None


class CommunityBlockView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CommunityBlockView.html"""

    person: Person = None
    community: Community = None

    def parse(self) -> None:
        if "person" in self._view.keys():
            self.person = Person(self._view["person"])
        else:
            self.person = None
        if "community" in self._view.keys():
            self.community = Community(self._view["community"])
        else:
            self.community = None


class ModBanFromCommunityView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModBanFromCommunityView.html"""

    mod_ban_from_community: ModBanFromCommunity = None
    moderator: Optional[Person] = None
    community: Community = None
    banned_person: Person = None

    def parse(self) -> None:
        if "mod_ban_from_community" in self._view.keys():
            self.mod_ban_from_community = ModBanFromCommunity(self._view["mod_ban_from_community"])
        else:
            self.mod_ban_from_community = None
        if "moderator" in self._view.keys():
            self.moderator = Person(self._view["moderator"])
        else:
            self.moderator = None
        if "community" in self._view.keys():
            self.community = Community(self._view["community"])
        else:
            self.community = None
        if "banned_person" in self._view.keys():
            self.banned_person = Person(self._view["banned_person"])
        else:
            self.banned_person = None


class PostView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PostView.html"""

    post: Post = None
    creator: Person = None
    community: Community = None
    image_details: Optional[ImageDetails] = None
    creator_banned_from_community: bool = None
    banned_from_community: bool = None
    creator_is_moderator: bool = None
    creator_is_admin: bool = None
    counts: PostAggregates = None
    subscribed: str = None
    saved: bool = None
    read: bool = None
    hidden: bool = None
    creator_blocked: bool = None
    my_vote: Optional[int] = None
    unread_comments: int = None

    def parse(self) -> None:
        if "post" in self._view.keys():
            self.post = Post(self._view["post"])
        else:
            self.post = None
        if "creator" in self._view.keys():
            self.creator = Person(self._view["creator"])
        else:
            self.creator = None
        if "community" in self._view.keys():
            self.community = Community(self._view["community"])
        else:
            self.community = None
        if "image_details" in self._view.keys():
            self.image_details = ImageDetails(self._view["image_details"])
        else:
            self.image_details = None
        if "creator_banned_from_community" in self._view.keys():
            self.creator_banned_from_community = self._view["creator_banned_from_community"]
        else:
            self.creator_banned_from_community = None
        if "banned_from_community" in self._view.keys():
            self.banned_from_community = self._view["banned_from_community"]
        else:
            self.banned_from_community = None
        if "creator_is_moderator" in self._view.keys():
            self.creator_is_moderator = self._view["creator_is_moderator"]
        else:
            self.creator_is_moderator = None
        if "creator_is_admin" in self._view.keys():
            self.creator_is_admin = self._view["creator_is_admin"]
        else:
            self.creator_is_admin = None
        if "counts" in self._view.keys():
            self.counts = PostAggregates(self._view["counts"])
        else:
            self.counts = None
        if "subscribed" in self._view.keys():
            self.subscribed = self._view["subscribed"]
        else:
            self.subscribed = None
        if "saved" in self._view.keys():
            self.saved = self._view["saved"]
        else:
            self.saved = None
        if "read" in self._view.keys():
            self.read = self._view["read"]
        else:
            self.read = None
        if "hidden" in self._view.keys():
            self.hidden = self._view["hidden"]
        else:
            self.hidden = None
        if "creator_blocked" in self._view.keys():
            self.creator_blocked = self._view["creator_blocked"]
        else:
            self.creator_blocked = None
        if "my_vote" in self._view.keys():
            self.my_vote = self._view["my_vote"]
        else:
            self.my_vote = None
        if "unread_comments" in self._view.keys():
            self.unread_comments = self._view["unread_comments"]
        else:
            self.unread_comments = None


class InstanceBlockView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/InstanceBlockView.html"""

    person: Person = None
    instance: Instance = None
    site: Optional[Site] = None

    def parse(self) -> None:
        if "person" in self._view.keys():
            self.person = Person(self._view["person"])
        else:
            self.person = None
        if "instance" in self._view.keys():
            self.instance = Instance(self._view["instance"])
        else:
            self.instance = None
        if "site" in self._view.keys():
            self.site = Site(self._view["site"])
        else:
            self.site = None


class ModRemoveCommunityView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModRemoveCommunityView.html"""

    mod_remove_community: ModRemoveCommunity = None
    moderator: Optional[Person] = None
    community: Community = None

    def parse(self) -> None:
        if "mod_remove_community" in self._view.keys():
            self.mod_remove_community = ModRemoveCommunity(self._view["mod_remove_community"])
        else:
            self.mod_remove_community = None
        if "moderator" in self._view.keys():
            self.moderator = Person(self._view["moderator"])
        else:
            self.moderator = None
        if "community" in self._view.keys():
            self.community = Community(self._view["community"])
        else:
            self.community = None


class ModHideCommunityView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModHideCommunityView.html"""

    mod_hide_community: ModHideCommunity = None
    admin: Optional[Person] = None
    community: Community = None

    def parse(self) -> None:
        if "mod_hide_community" in self._view.keys():
            self.mod_hide_community = ModHideCommunity(self._view["mod_hide_community"])
        else:
            self.mod_hide_community = None
        if "admin" in self._view.keys():
            self.admin = Person(self._view["admin"])
        else:
            self.admin = None
        if "community" in self._view.keys():
            self.community = Community(self._view["community"])
        else:
            self.community = None


class ModRemoveCommentView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModRemoveCommentView.html"""

    mod_remove_comment: ModRemoveComment = None
    moderator: Optional[Person] = None
    comment: Comment = None
    commenter: Person = None
    post: Post = None
    community: Community = None

    def parse(self) -> None:
        if "mod_remove_comment" in self._view.keys():
            self.mod_remove_comment = ModRemoveComment(self._view["mod_remove_comment"])
        else:
            self.mod_remove_comment = None
        if "moderator" in self._view.keys():
            self.moderator = Person(self._view["moderator"])
        else:
            self.moderator = None
        if "comment" in self._view.keys():
            self.comment = Comment(self._view["comment"])
        else:
            self.comment = None
        if "commenter" in self._view.keys():
            self.commenter = Person(self._view["commenter"])
        else:
            self.commenter = None
        if "post" in self._view.keys():
            self.post = Post(self._view["post"])
        else:
            self.post = None
        if "community" in self._view.keys():
            self.community = Community(self._view["community"])
        else:
            self.community = None


class AdminPurgeCommentView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/AdminPurgeCommentView.html"""

    admin_purge_comment: AdminPurgeComment = None
    admin: Optional[Person] = None
    post: Post = None

    def parse(self) -> None:
        if "admin_purge_comment" in self._view.keys():
            self.admin_purge_comment = AdminPurgeComment(self._view["admin_purge_comment"])
        else:
            self.admin_purge_comment = None
        if "admin" in self._view.keys():
            self.admin = Person(self._view["admin"])
        else:
            self.admin = None
        if "post" in self._view.keys():
            self.post = Post(self._view["post"])
        else:
            self.post = None


class ModAddCommunityView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModAddCommunityView.html"""

    mod_add_community: ModAddCommunity = None
    moderator: Optional[Person] = None
    community: Community = None
    modded_person: Person = None

    def parse(self) -> None:
        if "mod_add_community" in self._view.keys():
            self.mod_add_community = ModAddCommunity(self._view["mod_add_community"])
        else:
            self.mod_add_community = None
        if "moderator" in self._view.keys():
            self.moderator = Person(self._view["moderator"])
        else:
            self.moderator = None
        if "community" in self._view.keys():
            self.community = Community(self._view["community"])
        else:
            self.community = None
        if "modded_person" in self._view.keys():
            self.modded_person = Person(self._view["modded_person"])
        else:
            self.modded_person = None


class PersonBlockView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PersonBlockView.html"""

    person: Person = None
    target: Person = None

    def parse(self) -> None:
        if "person" in self._view.keys():
            self.person = Person(self._view["person"])
        else:
            self.person = None
        if "target" in self._view.keys():
            self.target = Person(self._view["target"])
        else:
            self.target = None


class CommunityModeratorView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CommunityModeratorView.html"""

    community: Community = None
    moderator: Person = None

    def parse(self) -> None:
        if "community" in self._view.keys():
            self.community = Community(self._view["community"])
        else:
            self.community = None
        if "moderator" in self._view.keys():
            self.moderator = Person(self._view["moderator"])
        else:
            self.moderator = None


class ModFeaturePostView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModFeaturePostView.html"""

    mod_feature_post: ModFeaturePost = None
    moderator: Optional[Person] = None
    post: Post = None
    community: Community = None

    def parse(self) -> None:
        if "mod_feature_post" in self._view.keys():
            self.mod_feature_post = ModFeaturePost(self._view["mod_feature_post"])
        else:
            self.mod_feature_post = None
        if "moderator" in self._view.keys():
            self.moderator = Person(self._view["moderator"])
        else:
            self.moderator = None
        if "post" in self._view.keys():
            self.post = Post(self._view["post"])
        else:
            self.post = None
        if "community" in self._view.keys():
            self.community = Community(self._view["community"])
        else:
            self.community = None


class PrivateMessageView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PrivateMessageView.html"""

    private_message: PrivateMessage = None
    creator: Person = None
    recipient: Person = None

    def parse(self) -> None:
        if "private_message" in self._view.keys():
            self.private_message = PrivateMessage(self._view["private_message"])
        else:
            self.private_message = None
        if "creator" in self._view.keys():
            self.creator = Person(self._view["creator"])
        else:
            self.creator = None
        if "recipient" in self._view.keys():
            self.recipient = Person(self._view["recipient"])
        else:
            self.recipient = None


class SiteView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/SiteView.html"""

    site: Site = None
    local_site: LocalSite = None
    local_site_rate_limit: LocalSiteRateLimit = None
    counts: SiteAggregates = None

    def parse(self) -> None:
        if "site" in self._view.keys():
            self.site = Site(self._view["site"])
        else:
            self.site = None
        if "local_site" in self._view.keys():
            self.local_site = LocalSite(self._view["local_site"])
        else:
            self.local_site = None
        if "local_site_rate_limit" in self._view.keys():
            self.local_site_rate_limit = LocalSiteRateLimit(self._view["local_site_rate_limit"])
        else:
            self.local_site_rate_limit = None
        if "counts" in self._view.keys():
            self.counts = SiteAggregates(self._view["counts"])
        else:
            self.counts = None


class ModLockPostView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModLockPostView.html"""

    mod_lock_post: ModLockPost = None
    moderator: Optional[Person] = None
    post: Post = None
    community: Community = None

    def parse(self) -> None:
        if "mod_lock_post" in self._view.keys():
            self.mod_lock_post = ModLockPost(self._view["mod_lock_post"])
        else:
            self.mod_lock_post = None
        if "moderator" in self._view.keys():
            self.moderator = Person(self._view["moderator"])
        else:
            self.moderator = None
        if "post" in self._view.keys():
            self.post = Post(self._view["post"])
        else:
            self.post = None
        if "community" in self._view.keys():
            self.community = Community(self._view["community"])
        else:
            self.community = None


class MyUserInfo(ParsableObject):
    """https://join-lemmy.org/api/interfaces/MyUserInfo.html"""

    local_user_view: LocalUserView = None
    follows: list[CommunityFollowerView] = None
    moderates: list[CommunityModeratorView] = None
    community_blocks: list[CommunityBlockView] = None
    instance_blocks: list[InstanceBlockView] = None
    person_blocks: list[PersonBlockView] = None
    discussion_languages: list[int] = None

    def parse(self) -> None:
        if "local_user_view" in self._view.keys():
            self.local_user_view = LocalUserView(self._view["local_user_view"])
        else:
            self.local_user_view = None
        if "follows" in self._view.keys():
            self.follows = [CommunityFollowerView(e) for e in self._view["follows"]]
        else:
            self.follows = None
        if "moderates" in self._view.keys():
            self.moderates = [CommunityModeratorView(e) for e in self._view["moderates"]]
        else:
            self.moderates = None
        if "community_blocks" in self._view.keys():
            self.community_blocks = [CommunityBlockView(e) for e in self._view["community_blocks"]]
        else:
            self.community_blocks = None
        if "instance_blocks" in self._view.keys():
            self.instance_blocks = [InstanceBlockView(e) for e in self._view["instance_blocks"]]
        else:
            self.instance_blocks = None
        if "person_blocks" in self._view.keys():
            self.person_blocks = [PersonBlockView(e) for e in self._view["person_blocks"]]
        else:
            self.person_blocks = None
        if "discussion_languages" in self._view.keys():
            self.discussion_languages = [int(e) for e in self._view["discussion_languages"]]
        else:
            self.discussion_languages = None


class AdminPurgePersonView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/AdminPurgePersonView.html"""

    admin_purge_person: AdminPurgePerson = None
    admin: Optional[Person] = None

    def parse(self) -> None:
        if "admin_purge_person" in self._view.keys():
            self.admin_purge_person = AdminPurgePerson(self._view["admin_purge_person"])
        else:
            self.admin_purge_person = None
        if "admin" in self._view.keys():
            self.admin = Person(self._view["admin"])
        else:
            self.admin = None


class CommentReportView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CommentReportView.html"""

    comment_report: CommentReport = None
    comment: Comment = None
    post: Post = None
    community: Community = None
    creator: Person = None
    comment_creator: Person = None
    counts: CommentAggregates = None
    creator_banned_from_community: bool = None
    creator_is_moderator: bool = None
    creator_is_admin: bool = None
    creator_blocked: bool = None
    subscribed: str = None
    saved: bool = None
    my_vote: Optional[int] = None
    resolver: Optional[Person] = None

    def parse(self) -> None:
        if "comment_report" in self._view.keys():
            self.comment_report = CommentReport(self._view["comment_report"])
        else:
            self.comment_report = None
        if "comment" in self._view.keys():
            self.comment = Comment(self._view["comment"])
        else:
            self.comment = None
        if "post" in self._view.keys():
            self.post = Post(self._view["post"])
        else:
            self.post = None
        if "community" in self._view.keys():
            self.community = Community(self._view["community"])
        else:
            self.community = None
        if "creator" in self._view.keys():
            self.creator = Person(self._view["creator"])
        else:
            self.creator = None
        if "comment_creator" in self._view.keys():
            self.comment_creator = Person(self._view["comment_creator"])
        else:
            self.comment_creator = None
        if "counts" in self._view.keys():
            self.counts = CommentAggregates(self._view["counts"])
        else:
            self.counts = None
        if "creator_banned_from_community" in self._view.keys():
            self.creator_banned_from_community = self._view["creator_banned_from_community"]
        else:
            self.creator_banned_from_community = None
        if "creator_is_moderator" in self._view.keys():
            self.creator_is_moderator = self._view["creator_is_moderator"]
        else:
            self.creator_is_moderator = None
        if "creator_is_admin" in self._view.keys():
            self.creator_is_admin = self._view["creator_is_admin"]
        else:
            self.creator_is_admin = None
        if "creator_blocked" in self._view.keys():
            self.creator_blocked = self._view["creator_blocked"]
        else:
            self.creator_blocked = None
        if "subscribed" in self._view.keys():
            self.subscribed = self._view["subscribed"]
        else:
            self.subscribed = None
        if "saved" in self._view.keys():
            self.saved = self._view["saved"]
        else:
            self.saved = None
        if "my_vote" in self._view.keys():
            self.my_vote = self._view["my_vote"]
        else:
            self.my_vote = None
        if "resolver" in self._view.keys():
            self.resolver = Person(self._view["resolver"])
        else:
            self.resolver = None


class ModRemovePostView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModRemovePostView.html"""

    mod_remove_post: ModRemovePost = None
    moderator: Optional[Person] = None
    post: Post = None
    community: Community = None

    def parse(self) -> None:
        if "mod_remove_post" in self._view.keys():
            self.mod_remove_post = ModRemovePost(self._view["mod_remove_post"])
        else:
            self.mod_remove_post = None
        if "moderator" in self._view.keys():
            self.moderator = Person(self._view["moderator"])
        else:
            self.moderator = None
        if "post" in self._view.keys():
            self.post = Post(self._view["post"])
        else:
            self.post = None
        if "community" in self._view.keys():
            self.community = Community(self._view["community"])
        else:
            self.community = None


class CommunityView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CommunityView.html"""

    community: Community = None
    subscribed: str = None
    blocked: bool = None
    counts: CommunityAggregates = None
    banned_from_community: bool = None

    def parse(self) -> None:
        if "community" in self._view.keys():
            self.community = Community(self._view["community"])
        else:
            self.community = None
        if "subscribed" in self._view.keys():
            self.subscribed = self._view["subscribed"]
        else:
            self.subscribed = None
        if "blocked" in self._view.keys():
            self.blocked = self._view["blocked"]
        else:
            self.blocked = None
        if "counts" in self._view.keys():
            self.counts = CommunityAggregates(self._view["counts"])
        else:
            self.counts = None
        if "banned_from_community" in self._view.keys():
            self.banned_from_community = self._view["banned_from_community"]
        else:
            self.banned_from_community = None


class AdminPurgeCommunityView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/AdminPurgeCommunityView.html"""

    admin_purge_community: AdminPurgeCommunity = None
    admin: Optional[Person] = None

    def parse(self) -> None:
        if "admin_purge_community" in self._view.keys():
            self.admin_purge_community = AdminPurgeCommunity(self._view["admin_purge_community"])
        else:
            self.admin_purge_community = None
        if "admin" in self._view.keys():
            self.admin = Person(self._view["admin"])
        else:
            self.admin = None


class AdminPurgePostView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/AdminPurgePostView.html"""

    admin_purge_post: AdminPurgePost = None
    admin: Optional[Person] = None
    community: Community = None

    def parse(self) -> None:
        if "admin_purge_post" in self._view.keys():
            self.admin_purge_post = AdminPurgePost(self._view["admin_purge_post"])
        else:
            self.admin_purge_post = None
        if "admin" in self._view.keys():
            self.admin = Person(self._view["admin"])
        else:
            self.admin = None
        if "community" in self._view.keys():
            self.community = Community(self._view["community"])
        else:
            self.community = None


class ModTransferCommunityView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ModTransferCommunityView.html"""

    mod_transfer_community: ModTransferCommunity = None
    moderator: Optional[Person] = None
    community: Community = None
    modded_person: Person = None

    def parse(self) -> None:
        if "mod_transfer_community" in self._view.keys():
            self.mod_transfer_community = ModTransferCommunity(self._view["mod_transfer_community"])
        else:
            self.mod_transfer_community = None
        if "moderator" in self._view.keys():
            self.moderator = Person(self._view["moderator"])
        else:
            self.moderator = None
        if "community" in self._view.keys():
            self.community = Community(self._view["community"])
        else:
            self.community = None
        if "modded_person" in self._view.keys():
            self.modded_person = Person(self._view["modded_person"])
        else:
            self.modded_person = None


class LocalImageView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/LocalImageView.html"""

    local_image: LocalImage = None
    person: Person = None

    def parse(self) -> None:
        if "local_image" in self._view.keys():
            self.local_image = LocalImage(self._view["local_image"])
        else:
            self.local_image = None
        if "person" in self._view.keys():
            self.person = Person(self._view["person"])
        else:
            self.person = None


class PersonMentionView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PersonMentionView.html"""

    person_mention: PersonMention = None
    comment: Comment = None
    creator: Person = None
    post: Post = None
    community: Community = None
    recipient: Person = None
    counts: CommentAggregates = None
    creator_banned_from_community: bool = None
    banned_from_community: bool = None
    creator_is_moderator: bool = None
    creator_is_admin: bool = None
    subscribed: str = None
    saved: bool = None
    creator_blocked: bool = None
    my_vote: Optional[int] = None

    def parse(self) -> None:
        if "person_mention" in self._view.keys():
            self.person_mention = PersonMention(self._view["person_mention"])
        else:
            self.person_mention = None
        if "comment" in self._view.keys():
            self.comment = Comment(self._view["comment"])
        else:
            self.comment = None
        if "creator" in self._view.keys():
            self.creator = Person(self._view["creator"])
        else:
            self.creator = None
        if "post" in self._view.keys():
            self.post = Post(self._view["post"])
        else:
            self.post = None
        if "community" in self._view.keys():
            self.community = Community(self._view["community"])
        else:
            self.community = None
        if "recipient" in self._view.keys():
            self.recipient = Person(self._view["recipient"])
        else:
            self.recipient = None
        if "counts" in self._view.keys():
            self.counts = CommentAggregates(self._view["counts"])
        else:
            self.counts = None
        if "creator_banned_from_community" in self._view.keys():
            self.creator_banned_from_community = self._view["creator_banned_from_community"]
        else:
            self.creator_banned_from_community = None
        if "banned_from_community" in self._view.keys():
            self.banned_from_community = self._view["banned_from_community"]
        else:
            self.banned_from_community = None
        if "creator_is_moderator" in self._view.keys():
            self.creator_is_moderator = self._view["creator_is_moderator"]
        else:
            self.creator_is_moderator = None
        if "creator_is_admin" in self._view.keys():
            self.creator_is_admin = self._view["creator_is_admin"]
        else:
            self.creator_is_admin = None
        if "subscribed" in self._view.keys():
            self.subscribed = self._view["subscribed"]
        else:
            self.subscribed = None
        if "saved" in self._view.keys():
            self.saved = self._view["saved"]
        else:
            self.saved = None
        if "creator_blocked" in self._view.keys():
            self.creator_blocked = self._view["creator_blocked"]
        else:
            self.creator_blocked = None
        if "my_vote" in self._view.keys():
            self.my_vote = self._view["my_vote"]
        else:
            self.my_vote = None


class CustomEmojiView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CustomEmojiView.html"""

    custom_emoji: CustomEmoji = None
    keywords: list[CustomEmojiKeyword] = None

    def parse(self) -> None:
        if "custom_emoji" in self._view.keys():
            self.custom_emoji = CustomEmoji(self._view["custom_emoji"])
        else:
            self.custom_emoji = None
        if "keywords" in self._view.keys():
            self.keywords = [CustomEmojiKeyword(e) for e in self._view["keywords"]]
        else:
            self.keywords = None


class CommentView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CommentView.html"""

    comment: Comment = None
    creator: Person = None
    post: Post = None
    community: Community = None
    counts: CommentAggregates = None
    creator_banned_from_community: bool = None
    banned_from_community: bool = None
    creator_is_moderator: bool = None
    creator_is_admin: bool = None
    subscribed: str = None
    saved: bool = None
    creator_blocked: bool = None
    my_vote: Optional[int] = None

    def parse(self) -> None:
        if "comment" in self._view.keys():
            self.comment = Comment(self._view["comment"])
        else:
            self.comment = None
        if "creator" in self._view.keys():
            self.creator = Person(self._view["creator"])
        else:
            self.creator = None
        if "post" in self._view.keys():
            self.post = Post(self._view["post"])
        else:
            self.post = None
        if "community" in self._view.keys():
            self.community = Community(self._view["community"])
        else:
            self.community = None
        if "counts" in self._view.keys():
            self.counts = CommentAggregates(self._view["counts"])
        else:
            self.counts = None
        if "creator_banned_from_community" in self._view.keys():
            self.creator_banned_from_community = self._view["creator_banned_from_community"]
        else:
            self.creator_banned_from_community = None
        if "banned_from_community" in self._view.keys():
            self.banned_from_community = self._view["banned_from_community"]
        else:
            self.banned_from_community = None
        if "creator_is_moderator" in self._view.keys():
            self.creator_is_moderator = self._view["creator_is_moderator"]
        else:
            self.creator_is_moderator = None
        if "creator_is_admin" in self._view.keys():
            self.creator_is_admin = self._view["creator_is_admin"]
        else:
            self.creator_is_admin = None
        if "subscribed" in self._view.keys():
            self.subscribed = self._view["subscribed"]
        else:
            self.subscribed = None
        if "saved" in self._view.keys():
            self.saved = self._view["saved"]
        else:
            self.saved = None
        if "creator_blocked" in self._view.keys():
            self.creator_blocked = self._view["creator_blocked"]
        else:
            self.creator_blocked = None
        if "my_vote" in self._view.keys():
            self.my_vote = self._view["my_vote"]
        else:
            self.my_vote = None


class PostReportView(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PostReportView.html"""

    post_report: PostReport = None
    post: Post = None
    community: Community = None
    creator: Person = None
    post_creator: Person = None
    creator_banned_from_community: bool = None
    creator_is_moderator: bool = None
    creator_is_admin: bool = None
    subscribed: str = None
    saved: bool = None
    read: bool = None
    hidden: bool = None
    creator_blocked: bool = None
    my_vote: Optional[int] = None
    unread_comments: int = None
    counts: PostAggregates = None
    resolver: Optional[Person] = None

    def parse(self) -> None:
        if "post_report" in self._view.keys():
            self.post_report = PostReport(self._view["post_report"])
        else:
            self.post_report = None
        if "post" in self._view.keys():
            self.post = Post(self._view["post"])
        else:
            self.post = None
        if "community" in self._view.keys():
            self.community = Community(self._view["community"])
        else:
            self.community = None
        if "creator" in self._view.keys():
            self.creator = Person(self._view["creator"])
        else:
            self.creator = None
        if "post_creator" in self._view.keys():
            self.post_creator = Person(self._view["post_creator"])
        else:
            self.post_creator = None
        if "creator_banned_from_community" in self._view.keys():
            self.creator_banned_from_community = self._view["creator_banned_from_community"]
        else:
            self.creator_banned_from_community = None
        if "creator_is_moderator" in self._view.keys():
            self.creator_is_moderator = self._view["creator_is_moderator"]
        else:
            self.creator_is_moderator = None
        if "creator_is_admin" in self._view.keys():
            self.creator_is_admin = self._view["creator_is_admin"]
        else:
            self.creator_is_admin = None
        if "subscribed" in self._view.keys():
            self.subscribed = self._view["subscribed"]
        else:
            self.subscribed = None
        if "saved" in self._view.keys():
            self.saved = self._view["saved"]
        else:
            self.saved = None
        if "read" in self._view.keys():
            self.read = self._view["read"]
        else:
            self.read = None
        if "hidden" in self._view.keys():
            self.hidden = self._view["hidden"]
        else:
            self.hidden = None
        if "creator_blocked" in self._view.keys():
            self.creator_blocked = self._view["creator_blocked"]
        else:
            self.creator_blocked = None
        if "my_vote" in self._view.keys():
            self.my_vote = self._view["my_vote"]
        else:
            self.my_vote = None
        if "unread_comments" in self._view.keys():
            self.unread_comments = self._view["unread_comments"]
        else:
            self.unread_comments = None
        if "counts" in self._view.keys():
            self.counts = PostAggregates(self._view["counts"])
        else:
            self.counts = None
        if "resolver" in self._view.keys():
            self.resolver = Person(self._view["resolver"])
        else:
            self.resolver = None
