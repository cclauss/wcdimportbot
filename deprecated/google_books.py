# """Template data example: {{google books |plainurl=y |id=CDJpAAAAMAAJ |page=313}}"""
# import logging
# from enum import Enum
# from typing import Optional, Union
#
# from marshmallow import Schema, post_load
# from marshmallow.fields import String
# from pydantic import ConstrainedStr, ValidationError
#
# from src.wcd_base_model import WcdBaseModel
#
# logger = logging.getLogger(__name__)
#
#
# class YesNo(Enum):
#     YES = "yes"
#     NO = "no"
#
#
# class YesNoShort(Enum):
#     YES = "y"
#     NO = "n"
#
#
# class TwelveCharString(ConstrainedStr):
#     max_length = 12
#     min_length = 12
#
#
# class GoogleBooks(WcdBaseModel):
#     """See https://en.wikipedia.org/wiki/Template:Google_books"""
#
#     first_parameter_id: Optional[TwelveCharString]
#     id: Optional[TwelveCharString]
#     keywords: Optional[str]
#     md5hash: Optional[str]
#     page: Optional[str]
#     plainurl: Optional[Union[YesNo, YesNoShort]]
#     text: Optional[str]
#     title: Optional[str]
#     # wikibase: Optional[Wikibase]
#
#     @property
#     def url(self):
#         return f"https://books.google.com/books?id={self.id}"
#
#     # def __generate_hash__(self):
#     #     if not self.wikibase:
#     #         raise MissingInformationError("self.wikibase was None")
#     #     if self.id is not None:
#     #         str2hash = self.id
#     #         self.md5hash = hashlib.md5(
#     #             f'{self.wikibase.title}{str2hash.replace(" ", "").lower()}'.encode()
#     #         ).hexdigest()
#
#     def finish_parsing(self):
#         if self.first_parameter_id:
#             if self.id:
#                 raise ValueError("Both self.id and self.first_parameter_id specified.")
#             else:
#                 self.id = self.first_parameter_id
#         # self.__generate_hash__()
#
#
# class GoogleBooksSchema(Schema):
#     """Marshmallow schema to load the attributes using aliases
#
#     We don't validate with marshmallow because it does not seem to work correctly."""
#
#     first_parameter_id = String(data_key="1")  # id
#     title = String(data_key="2")  # title
#
#     class Meta:
#         additional = ("id", "keywords", "page", "plainurl", "text")
#
#     # noinspection PyUnusedLocal
#     @post_load
#     # **kwargs is needed here despite what the validator claims
#     def return_object(self, data, **kwargs) -> Optional[GoogleBooks]:
#         result = None
#         try:
#             result = GoogleBooks(**data)
#         except ValidationError as e:
#             #  log to logfile instead
#             logger.warning(f"Encountered error during parsing: {e} for the data {data}")
#         return result
