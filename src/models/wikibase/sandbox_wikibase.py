import config
from src.models.wikibase import Wikibase


class SandboxWikibase(Wikibase):
    """This models the properties and items on sandbox.wiki"""

    user_name = config.sandbox_user
    botpassword = config.sandbox_pwd

    query_service_url = "https://query.sandbox.wiki"
    wikibase_url = "https://sandbox.wiki"

    ACCESS_DATE = "P10"  # datatype: WikibaseDatatype.TIME description: date of access of the resource
    ARCHIVE = "P23"  # datatype: WikibaseDatatype.ITEM description: None
    ARCHIVE_DATE = "P18"  # datatype: WikibaseDatatype.TIME description: None
    AUTHOR = "P44"  # datatype: WikibaseDatatype.ITEM description: None
    FULL_NAME_STRING = "P45"  # datatype: WikibaseDatatype.STRING description: None
    DOI = "P46"  # datatype: WikibaseDatatype.EXTERNALID description: None
    EDITOR = "P47"  # datatype: WikibaseDatatype.ITEM description: None
    EDITOR_NAME_STRING = "P48"  # datatype: WikibaseDatatype.STRING description: None
    FAMILY_NAME = "P49"  # datatype: WikibaseDatatype.STRING description: None
    GIVEN_NAME = "P50"  # datatype: WikibaseDatatype.STRING description: None
    CITATIONS = "P51"  # datatype: WikibaseDatatype.ITEM description: None
    FIRST_LEVEL_DOMAIN_STRING = (
        "P52"  # datatype: WikibaseDatatype.STRING description: None
    )
    FULL_WORK_AVAILABLE_AT_URL = (
        "P53"  # datatype: WikibaseDatatype.URL description: None
    )
    HASH = "P54"  # datatype: WikibaseDatatype.STRING description: None
    HOST_STRING = "P55"  # datatype: WikibaseDatatype.STRING description: None
    INSTANCE_OF = "P56"  # datatype: WikibaseDatatype.ITEM description: None
    INTERVIEWER_STRING = "P57"  # datatype: WikibaseDatatype.STRING description: None
    ISBN_10 = "P58"  # datatype: WikibaseDatatype.EXTERNALID description: None
    ISBN_13 = "P59"  # datatype: WikibaseDatatype.EXTERNALID description: None
    ISSUE = "P60"  # datatype: WikibaseDatatype.STRING description: None
    LAST_UPDATE = "P61"  # datatype: WikibaseDatatype.TIME description: date of last update of this item?
    LOCATION_STRING = "P62"  # datatype: WikibaseDatatype.STRING description: None
    LUMPED_AUTHORS = "P63"  # datatype: WikibaseDatatype.STRING description: None
    MEDIAWIKI_PAGE_ID = "P64"  # datatype: WikibaseDatatype.EXTERNALID description: None
    NAME_MASK = "P65"  # datatype: WikibaseDatatype.STRING description: None
    ORCID = "P66"  # datatype: WikibaseDatatype.EXTERNALID description: None
    PAGES = "P67"  # datatype: WikibaseDatatype.STRING description: None
    PMID = "P68"  # datatype: WikibaseDatatype.EXTERNALID description: None
    PUBLICATION_DATE = "P69"  # datatype: WikibaseDatatype.TIME description: date of publication of the resource
    PUBLISHED_IN = "P211"  # datatype: WikibaseDatatype.ITEM description:
    PUBLISHER_STRING = "P71"  # datatype: WikibaseDatatype.STRING description: None
    RETRIEVED_DATE = "P72"  # datatype: WikibaseDatatype.TIME description: date of retrieval of the resource
    PAGE_REVISION_ID = "P73"  # datatype: WikibaseDatatype.STRING description: None
    SERIES_ORDINAL = "P74"  # datatype: WikibaseDatatype.QUANTITY description: None
    SOURCE_WIKIPEDIA = "P75"  # datatype: WikibaseDatatype.ITEM description: None
    STRING_CITATIONS = "P76"  # datatype: WikibaseDatatype.STRING description: None
    TEMPLATE_NAME = "P77"  # datatype: WikibaseDatatype.STRING description: None
    TITLE = "P78"  # datatype: WikibaseDatatype.STRING description: None
    TRANSLATOR_NAME_STRING = (
        "P79"  # datatype: WikibaseDatatype.STRING description: None
    )
    VOLUME = "P80"  # datatype: WikibaseDatatype.STRING description: None
    WEBSITE = "P81"  # datatype: WikibaseDatatype.ITEM description: None
    WEBSITE_STRING = "P82"  # datatype: WikibaseDatatype.STRING description: None
    WIKIDATA_QID = "P83"  # datatype: WikibaseDatatype.EXTERNALID description: None
    ARCHIVE_URL = "P127"  # datatype: WikibaseDatatype.URL description: None
    CHAPTER_URL = "P128"  # datatype: WikibaseDatatype.URL description: None
    CONFERENCE_URL = "P129"  # datatype: WikibaseDatatype.URL description: None
    LAY_URL = "P130"  # datatype: WikibaseDatatype.URL description: None
    TRANSCRIPT_URL = "P131"  # datatype: WikibaseDatatype.URL description: None
    URL = "P132"  # datatype: WikibaseDatatype.URL description: None

    ENGLISH_WIKIPEDIA = (
        "Q2"  # label: English Wikipedia description: language version of Wikipedia
    )
    WEBSITE_ITEM = "Q32"  # label: Website description: first level domain website found in Wikipedia
    WIKIPEDIA_PAGE = "Q33"  # label: Wikipedia page description: page in a language version of Wikipedia
    WIKIPEDIA_REFERENCE = "Q34"  # label: Wikipedia reference description: reference on a page in Wikipedia
    ARCHIVE_ITEM = "Q6"  # label: Archive description: web archive
    ARCHIVE_IS = "Q27"  # label: Archive.is description: web archive
    ARCHIVE_ORG = "Q37"  # label: Archive.org description: web archive
    ARCHIVE_TODAY = "Q38"  # label: Archive.today description: web archive
    WEBCITATION_ORG = "Q39"  # label: Webcitation.org description: web archive

    # This must come last to avoid errors
    wcdqid_language_edition_of_wikipedia_to_work_on = ENGLISH_WIKIPEDIA
