# from pydantic import BaseModel
#
#
# class CiteWebReferences(BaseModel):
#     """The purpose of this class is to model the statistics
#     the patron wants from the article endpoint
#
#     We use BaseModel to avoid the cache attribute"""
#
#     all: int
#     has_url: int
#     has_google_books_url: int
#     has_ia_details_url: int
#     has_wm_url: int
#
#     class Config:  # dead: disable
#         extra = "forbid"  # dead: disable
