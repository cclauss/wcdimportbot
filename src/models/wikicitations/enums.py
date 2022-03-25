from enum import Enum

# WCD = WikiCitations Database


class WCDItem(Enum):
    WIKIPEDIA_REFERENCE = "Q4"
    WIKIPEDIA_PAGE = "Q6"


class WCDProperty(Enum):
    """Mapping for WikiCitations Wikibase"""

    AUTHOR = "P7"
    AUTHOR_NAME_STRING = "P15"
    DOI = "P33"
    EDITOR = "P6"
    FAMILY_NAME = "P5"
    GIVEN_NAME = "P4"
    CITATIONS = "P19"
    FULL_WORK_AVAILABLE_AT_URL = "P23"
    HASH = "P30"
    INSTANCE_OF = "P10"
    ISBN_10 = "P28"
    ISBN_13 = "P32"
    ISSUE = "P24"
    MEDIAWIKI_PAGE_ID = "P18"
    ORCID = "P31"
    PAGES = "P25"
    PMID = "P34"
    PUBLICATION_DATE = "P12"
    PUBLISHED_IN = "P17"
    RETRIEVED_DATE = "P29"
    SERIES_ORDINAL = "P14"  # aka author position
    SOURCE_WIKIPEDIA = "P9"
    TEMPLATE_NAME = "P8"
    TITLE = "P20"
    URL = "P2"
    VOLUME = "P27"
    WEBSITE_STRING = "P35"
    WIKIDATA_QID = "P1"
