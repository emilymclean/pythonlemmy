from dataclasses import dataclass
from typing import Optional, Any
import requests

from .views import *
from .objects import *


class CaptchaResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CaptchaResponse.html"""

    png: str = None
    wav: str = None
    uuid: str = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                png=data["png"],
                wav=data["wav"],
                uuid=data["uuid"]
        )


class BannedPersonsResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/BannedPersonsResponse.html"""

    banned: list[PersonView] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                banned=[PersonView.parse(e0) for e0 in data["banned"]]
        )


class ListMediaResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ListMediaResponse.html"""

    images: list[LocalImageView] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                images=[LocalImageView.parse(e0) for e0 in data["images"]]
        )


class UpdateTotpResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/UpdateTotpResponse.html"""

    enabled: bool = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                enabled=data["enabled"]
        )


class CommentReportResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CommentReportResponse.html"""

    comment_report_view: CommentReportView = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                comment_report_view=CommentReportView.parse(data["comment_report_view"])
        )


class GetCommunityResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetCommunityResponse.html"""

    community_view: CommunityView = None
    site: Optional[Site] = None
    moderators: list[CommunityModeratorView] = None
    discussion_languages: list[int] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                community_view=CommunityView.parse(data["community_view"]),
                site=Site.parse(data["site"]) if "site" in data else None,
                moderators=[CommunityModeratorView.parse(e0) for e0 in data["moderators"]],
                discussion_languages=[e0 for e0 in data["discussion_languages"]]
        )


class GetPostsResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetPostsResponse.html"""

    posts: list[PostView] = None
    next_page: Optional[str] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                posts=[PostView.parse(e0) for e0 in data["posts"]],
                next_page=data["next_page"] if "next_page" in data else None
        )


class CommunityResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CommunityResponse.html"""

    community_view: CommunityView = None
    discussion_languages: list[int] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                community_view=CommunityView.parse(data["community_view"]),
                discussion_languages=[e0 for e0 in data["discussion_languages"]]
        )


class GetCommentsResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetCommentsResponse.html"""

    comments: list[CommentView] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                comments=[CommentView.parse(e0) for e0 in data["comments"]]
        )


class SearchResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/SearchResponse.html"""

    type_: str = None
    comments: list[CommentView] = None
    posts: list[PostView] = None
    communities: list[CommunityView] = None
    users: list[PersonView] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                type_=data["type_"],
                comments=[CommentView.parse(e0) for e0 in data["comments"]],
                posts=[PostView.parse(e0) for e0 in data["posts"]],
                communities=[CommunityView.parse(e0) for e0 in data["communities"]],
                users=[PersonView.parse(e0) for e0 in data["users"]]
        )


class PrivateMessageResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PrivateMessageResponse.html"""

    private_message_view: PrivateMessageView = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                private_message_view=PrivateMessageView.parse(data["private_message_view"])
        )


class AddModToCommunityResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/AddModToCommunityResponse.html"""

    moderators: list[CommunityModeratorView] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                moderators=[CommunityModeratorView.parse(e0) for e0 in data["moderators"]]
        )


class GetReportCountResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetReportCountResponse.html"""

    community_id: Optional[int] = None
    comment_reports: int = None
    post_reports: int = None
    private_message_reports: Optional[int] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                community_id=data["community_id"] if "community_id" in data else None,
                comment_reports=data["comment_reports"],
                post_reports=data["post_reports"],
                private_message_reports=data["private_message_reports"] if "private_message_reports" in data else None
        )


class PostReportResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PostReportResponse.html"""

    post_report_view: PostReportView = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                post_report_view=PostReportView.parse(data["post_report_view"])
        )


class RegistrationApplicationResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/RegistrationApplicationResponse.html"""

    registration_application: RegistrationApplicationView = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                registration_application=RegistrationApplicationView.parse(data["registration_application"])
        )


class GetSiteResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetSiteResponse.html"""

    site_view: SiteView = None
    admins: list[PersonView] = None
    version: str = None
    my_user: Optional[MyUserInfo] = None
    all_languages: list[Language] = None
    discussion_languages: list[int] = None
    taglines: list[Tagline] = None
    custom_emojis: list[CustomEmojiView] = None
    blocked_urls: list[LocalSiteUrlBlocklist] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                site_view=SiteView.parse(data["site_view"]),
                admins=[PersonView.parse(e0) for e0 in data["admins"]],
                version=data["version"],
                my_user=MyUserInfo.parse(data["my_user"]) if "my_user" in data else None,
                all_languages=[Language.parse(e0) for e0 in data["all_languages"]],
                discussion_languages=[e0 for e0 in data["discussion_languages"]],
                taglines=[Tagline.parse(e0) for e0 in data["taglines"]],
                custom_emojis=[CustomEmojiView.parse(e0) for e0 in data["custom_emojis"]],
                blocked_urls=[LocalSiteUrlBlocklist.parse(e0) for e0 in data["blocked_urls"]]
        )


class GetCaptchaResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetCaptchaResponse.html"""

    ok: Optional[CaptchaResponse] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                ok=CaptchaResponse.parse(data["ok"]) if "ok" in data else None
        )


class PersonMentionResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PersonMentionResponse.html"""

    person_mention_view: PersonMentionView = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                person_mention_view=PersonMentionView.parse(data["person_mention_view"])
        )


class GetModlogResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetModlogResponse.html"""

    removed_posts: list[ModRemovePostView] = None
    locked_posts: list[ModLockPostView] = None
    featured_posts: list[ModFeaturePostView] = None
    removed_comments: list[ModRemoveCommentView] = None
    removed_communities: list[ModRemoveCommunityView] = None
    banned_from_community: list[ModBanFromCommunityView] = None
    banned: list[ModBanView] = None
    added_to_community: list[ModAddCommunityView] = None
    transferred_to_community: list[ModTransferCommunityView] = None
    added: list[ModAddView] = None
    admin_purged_persons: list[AdminPurgePersonView] = None
    admin_purged_communities: list[AdminPurgeCommunityView] = None
    admin_purged_posts: list[AdminPurgePostView] = None
    admin_purged_comments: list[AdminPurgeCommentView] = None
    hidden_communities: list[ModHideCommunityView] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                removed_posts=[ModRemovePostView.parse(e0) for e0 in data["removed_posts"]],
                locked_posts=[ModLockPostView.parse(e0) for e0 in data["locked_posts"]],
                featured_posts=[ModFeaturePostView.parse(e0) for e0 in data["featured_posts"]],
                removed_comments=[ModRemoveCommentView.parse(e0) for e0 in data["removed_comments"]],
                removed_communities=[ModRemoveCommunityView.parse(e0) for e0 in data["removed_communities"]],
                banned_from_community=[ModBanFromCommunityView.parse(e0) for e0 in data["banned_from_community"]],
                banned=[ModBanView.parse(e0) for e0 in data["banned"]],
                added_to_community=[ModAddCommunityView.parse(e0) for e0 in data["added_to_community"]],
                transferred_to_community=[ModTransferCommunityView.parse(e0) for e0 in data["transferred_to_community"]],
                added=[ModAddView.parse(e0) for e0 in data["added"]],
                admin_purged_persons=[AdminPurgePersonView.parse(e0) for e0 in data["admin_purged_persons"]],
                admin_purged_communities=[AdminPurgeCommunityView.parse(e0) for e0 in data["admin_purged_communities"]],
                admin_purged_posts=[AdminPurgePostView.parse(e0) for e0 in data["admin_purged_posts"]],
                admin_purged_comments=[AdminPurgeCommentView.parse(e0) for e0 in data["admin_purged_comments"]],
                hidden_communities=[ModHideCommunityView.parse(e0) for e0 in data["hidden_communities"]]
        )


class SuccessResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/SuccessResponse.html"""

    success: bool = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                success=data["success"]
        )


class ListRegistrationApplicationsResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ListRegistrationApplicationsResponse.html"""

    registration_applications: list[RegistrationApplicationView] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                registration_applications=[RegistrationApplicationView.parse(e0) for e0 in data["registration_applications"]]
        )


class BlockInstanceResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/BlockInstanceResponse.html"""

    blocked: bool = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                blocked=data["blocked"]
        )


class ResolveObjectResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ResolveObjectResponse.html"""

    comment: Optional[CommentView] = None
    post: Optional[PostView] = None
    community: Optional[CommunityView] = None
    person: Optional[PersonView] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                comment=CommentView.parse(data["comment"]) if "comment" in data else None,
                post=PostView.parse(data["post"]) if "post" in data else None,
                community=CommunityView.parse(data["community"]) if "community" in data else None,
                person=PersonView.parse(data["person"]) if "person" in data else None
        )


class PrivateMessageReportResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PrivateMessageReportResponse.html"""

    private_message_report_view: PrivateMessageReportView = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                private_message_report_view=PrivateMessageReportView.parse(data["private_message_report_view"])
        )


class SiteResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/SiteResponse.html"""

    site_view: SiteView = None
    taglines: list[Tagline] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                site_view=SiteView.parse(data["site_view"]),
                taglines=[Tagline.parse(e0) for e0 in data["taglines"]]
        )


class ListPostReportsResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ListPostReportsResponse.html"""

    post_reports: list[PostReportView] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                post_reports=[PostReportView.parse(e0) for e0 in data["post_reports"]]
        )


class BlockCommunityResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/BlockCommunityResponse.html"""

    community_view: CommunityView = None
    blocked: bool = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                community_view=CommunityView.parse(data["community_view"]),
                blocked=data["blocked"]
        )


class PrivateMessagesResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PrivateMessagesResponse.html"""

    private_messages: list[PrivateMessageView] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                private_messages=[PrivateMessageView.parse(e0) for e0 in data["private_messages"]]
        )


class LoginResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/LoginResponse.html"""

    jwt: Optional[str] = None
    registration_created: bool = None
    verify_email_sent: bool = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                jwt=data["jwt"] if "jwt" in data else None,
                registration_created=data["registration_created"],
                verify_email_sent=data["verify_email_sent"]
        )


class GetUnreadCountResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetUnreadCountResponse.html"""

    replies: int = None
    mentions: int = None
    private_messages: int = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                replies=data["replies"],
                mentions=data["mentions"],
                private_messages=data["private_messages"]
        )


class BanFromCommunityResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/BanFromCommunityResponse.html"""

    person_view: PersonView = None
    banned: bool = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                person_view=PersonView.parse(data["person_view"]),
                banned=data["banned"]
        )


class CommentReplyResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CommentReplyResponse.html"""

    comment_reply_view: CommentReplyView = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                comment_reply_view=CommentReplyView.parse(data["comment_reply_view"])
        )


class ListPostLikesResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ListPostLikesResponse.html"""

    post_likes: list[VoteView] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                post_likes=[VoteView.parse(e0) for e0 in data["post_likes"]]
        )


class ListCommentReportsResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ListCommentReportsResponse.html"""

    comment_reports: list[CommentReportView] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                comment_reports=[CommentReportView.parse(e0) for e0 in data["comment_reports"]]
        )


class GetSiteMetadataResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetSiteMetadataResponse.html"""

    metadata: LinkMetadata = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                metadata=LinkMetadata.parse(data["metadata"])
        )


class BanPersonResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/BanPersonResponse.html"""

    person_view: PersonView = None
    banned: bool = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                person_view=PersonView.parse(data["person_view"]),
                banned=data["banned"]
        )


class CommentResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CommentResponse.html"""

    comment_view: CommentView = None
    recipient_ids: list[int] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                comment_view=CommentView.parse(data["comment_view"]),
                recipient_ids=[e0 for e0 in data["recipient_ids"]]
        )


class GetRepliesResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetRepliesResponse.html"""

    replies: list[CommentReplyView] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                replies=[CommentReplyView.parse(e0) for e0 in data["replies"]]
        )


class GetUnreadRegistrationApplicationCountResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetUnreadRegistrationApplicationCountResponse.html"""

    registration_applications: int = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                registration_applications=data["registration_applications"]
        )


class CustomEmojiResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/CustomEmojiResponse.html"""

    custom_emoji: CustomEmojiView = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                custom_emoji=CustomEmojiView.parse(data["custom_emoji"])
        )


class GetPersonDetailsResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetPersonDetailsResponse.html"""

    person_view: PersonView = None
    site: Optional[Site] = None
    comments: list[CommentView] = None
    posts: list[PostView] = None
    moderates: list[CommunityModeratorView] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                person_view=PersonView.parse(data["person_view"]),
                site=Site.parse(data["site"]) if "site" in data else None,
                comments=[CommentView.parse(e0) for e0 in data["comments"]],
                posts=[PostView.parse(e0) for e0 in data["posts"]],
                moderates=[CommunityModeratorView.parse(e0) for e0 in data["moderates"]]
        )


class ListCommunitiesResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ListCommunitiesResponse.html"""

    communities: list[CommunityView] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                communities=[CommunityView.parse(e0) for e0 in data["communities"]]
        )


class GetPersonMentionsResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetPersonMentionsResponse.html"""

    mentions: list[PersonMentionView] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                mentions=[PersonMentionView.parse(e0) for e0 in data["mentions"]]
        )


class AddAdminResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/AddAdminResponse.html"""

    admins: list[PersonView] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                admins=[PersonView.parse(e0) for e0 in data["admins"]]
        )


class GetFederatedInstancesResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetFederatedInstancesResponse.html"""

    federated_instances: Optional[FederatedInstances] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                federated_instances=FederatedInstances.parse(data["federated_instances"]) if "federated_instances" in data else None
        )


class PostResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/PostResponse.html"""

    post_view: PostView = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                post_view=PostView.parse(data["post_view"])
        )


class GenerateTotpSecretResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GenerateTotpSecretResponse.html"""

    totp_secret_url: str = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                totp_secret_url=data["totp_secret_url"]
        )


class ListPrivateMessageReportsResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ListPrivateMessageReportsResponse.html"""

    private_message_reports: list[PrivateMessageReportView] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                private_message_reports=[PrivateMessageReportView.parse(e0) for e0 in data["private_message_reports"]]
        )


class BlockPersonResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/BlockPersonResponse.html"""

    person_view: PersonView = None
    blocked: bool = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                person_view=PersonView.parse(data["person_view"]),
                blocked=data["blocked"]
        )


class GetPostResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/GetPostResponse.html"""

    post_view: PostView = None
    community_view: CommunityView = None
    moderators: list[CommunityModeratorView] = None
    cross_posts: list[PostView] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                post_view=PostView.parse(data["post_view"]),
                community_view=CommunityView.parse(data["community_view"]),
                moderators=[CommunityModeratorView.parse(e0) for e0 in data["moderators"]],
                cross_posts=[PostView.parse(e0) for e0 in data["cross_posts"]]
        )


class ListCommentLikesResponse(ParsableObject):
    """https://join-lemmy.org/api/interfaces/ListCommentLikesResponse.html"""

    comment_likes: list[VoteView] = None
    
    @classmethod
    def parse(cls, data: dict[str, Any]):
        return cls(
                comment_likes=[VoteView.parse(e0) for e0 in data["comment_likes"]]
        )
