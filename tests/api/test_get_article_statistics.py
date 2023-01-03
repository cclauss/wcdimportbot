import json
import unittest

from flask import Flask
from flask_restful import Api  # type: ignore

from src.models.api.article_statistics import ArticleStatistics
from src.models.api.get_article_statistics import GetArticleStatistics


class TestGetArticleStatistics(unittest.TestCase):
    """Generated by ChatGPT using this prompt:
        Create a test for this flask api endpoint
    import logging
    from typing import Optional

    from flask import request
    from flask_restful import Resource, abort  # type: ignore

    from src.helpers.console import console
    from src.models.api.get_statistics_schema import GetStatisticsSchema
    from src.models.api.job import Job
    from src.models.wikimedia.enums import AnalyzerReturn
    from src.models.wikimedia.wikipedia.analyzer import WikipediaAnalyzer

    logger = logging.getLogger(__name__)


    class GetArticleStatistics(Resource):
        schema = GetStatisticsSchema()
        job: Optional[Job]

        def get(self):
            self.__validate_and_get_job__()
            if self.job.lang.lower() == "en" and self.job.title and self.job.site.lower() == "wikipedia":
                logger.info(f"Analyzing {self.job.title}...")
                # TODO use a work queue here like ReFill so
                #  we can easily scale the workload from thousands of users
                wikipedia_analyzer = WikipediaAnalyzer(title=self.job.title,
                                                       lang=self.job.lang,
                                                       wikimedia_site=self.job.site,
                                                       testing=self.job.testing)
                statistics = wikipedia_analyzer.get_statistics()
                if self.job.testing:
                    # what is the purpose of this?
                    return "ok", 200
                else:
                    if isinstance(statistics, dict):
                        # we got a json response
                        # according to https://stackoverflow.com/questions/13081532/return-json-response-from-flask-view
                        # flask calls jsonify automatically
                        return statistics, 200
                    elif statistics == AnalyzerReturn.NOT_FOUND:
                        return statistics.value, 404
                    elif statistics == AnalyzerReturn.IS_REDIRECT:
                        return statistics.value, 400
                    else:
                        raise Exception("this should never be reached.")

            else:
                # Something was not valid, return a meaningful error
                logger.error("did not get what we need")
                if self.job.lang != "en":
                    return "Only en language code is supported", 400
                if self.job.title == "":
                    return "Title was missing", 400
                if self.job.site != "wikipedia":
                    return "Only 'wikipedia' site is supported", 400

        def __validate_and_get_job__(self):
            self.__validate__()
            self.__parse_into_job__()

        def __validate__(self):
            print(request.args)
            errors = self.schema.validate(request.args)
            if errors:
                abort(400, error=str(errors))

        def __parse_into_job__(self):
            console.print(request.args)
            self.job = self.schema.load(request.args)
            console.print(self.job.dict())

    from marshmallow import Schema, fields, post_load

    from src.models.api.job import Job


    class GetStatisticsSchema(Schema):
        lang = fields.Str(required=True)
        site = fields.Str(required=True)
        testing = fields.Bool(required=False)
        title = fields.Str(required=True)

        # noinspection PyUnusedLocal
        @post_load
        # **kwargs is needed here despite what the validator claims
        def return_object(self, data, **kwargs):  # type: ignore
            return Job(**data)
    """

    def setUp(self):
        app = Flask(__name__)
        api = Api(app)

        api.add_resource(GetArticleStatistics, "/get_article_statistics")
        self.app = app.test_client()

    def test_valid_request_test(self):
        response = self.app.get(
            "/get_article_statistics?lang=en&site=wikipedia&title=Test&testing=True"
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ArticleStatistics(**data).dict(), ArticleStatistics().dict())

    def test_valid_request_easter_island(self):
        response = self.app.get(
            "/get_article_statistics?lang=en&site=wikipedia&title=Easter Island&testing=True"
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            ArticleStatistics(**data).dict(),
            {
                "number_of_bare_url_references": 0,
                "number_of_citation_references": 0,
                "number_of_citeq_references": 0,
                "number_of_content_reference_with_at_least_one_template": 2,
                "number_of_content_reference_with_no_templates": 0,
                "number_of_content_references": 2,
                "number_of_cs1_references": 2,
                "number_of_hashed_content_references": 2,
                "number_of_isbn_template_references": 0,
                "number_of_multiple_template_references": 0,
                "number_of_named_references": 1,
                "number_of_references_with_a_supported_template": 2,
                "percent_of_content_references_with_a_hash": 100,
                "references": [
                    {
                        "bare_url_template_found": False,
                        "citation_template_found": False,
                        "citeq_template_found": False,
                        "cs1_template_found": True,
                        "is_named_reference": False,
                        "isbn_template_found": False,
                        "multiple_templates_found": False,
                        "plain_text_in_reference": False,
                        "url_template_found": False,
                        "wikitext": '<ref name="INE">{{cite web | url= '
                        "http://www.ine.cl/canales/chile_estadistico/censos_poblacion_vivienda/censo_pobl_vivi.php "
                        "| title= Censo de Población y Vivienda 2002 | "
                        "work= [[National Statistics Institute "
                        "(Chile)|National Statistics Institute]] | "
                        "access-date= 1 May 2010 | url-status=live | "
                        "archive-url= "
                        "https://web.archive.org/web/20100715195638/http://www.ine.cl/canales/chile_estadistico/censos_poblacion_vivienda/censo_pobl_vivi.php "
                        "| archive-date= 15 July 2010}}</ref>",
                    },
                    {
                        "bare_url_template_found": False,
                        "citation_template_found": False,
                        "citeq_template_found": False,
                        "cs1_template_found": True,
                        "is_named_reference": False,
                        "isbn_template_found": False,
                        "multiple_templates_found": False,
                        "plain_text_in_reference": False,
                        "url_template_found": False,
                        "wikitext": "<ref>{{cite web |language= es |url= "
                        "https://resultados.censo2017.cl/Home/Download "
                        "|title= Censo 2017 |work= [[National Statistics "
                        "Institute (Chile)|National Statistics "
                        "Institute]] |access-date= 11 May 2018 "
                        "|archive-url= "
                        "https://web.archive.org/web/20180511145942/https://resultados.censo2017.cl/Home/Download "
                        "|archive-date= 11 May 2018 |url-status=dead "
                        "}}</ref>",
                    },
                    {
                        "bare_url_template_found": False,
                        "citation_template_found": False,
                        "citeq_template_found": False,
                        "cs1_template_found": False,
                        "is_named_reference": True,
                        "isbn_template_found": False,
                        "multiple_templates_found": False,
                        "plain_text_in_reference": False,
                        "url_template_found": False,
                        "wikitext": '<ref name="INE"/>',
                    },
                ],
            },
        )

    def test_invalid_language(self):
        response = self.app.get(
            "/get_article_statistics?lang=fr&site=wikipedia&title=Test"
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data, b'"Only en language code is supported"\n'
        )  # expected output

    def test_missing_title(self):
        response = self.app.get("/get_article_statistics?lang=en&site=wikipedia")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data,
            b"{\"error\": \"{'title': ['Missing data for required field.']}\"}\n",
        )

    def test_invalid_site(self):
        response = self.app.get(
            "/get_article_statistics?lang=en&site=example.com&title=Test"
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.data, b"\"Only 'wikipedia' site is supported\"\n"
        )  # expected output
