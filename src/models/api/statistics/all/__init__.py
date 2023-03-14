"""This code was partly generated by chatGPT using the following prompt:
please write me some code in python that can fetch asynchronously a reference_id from the following endpoint based on a list like this ids=["id1", "id2"]:
http://18.217.22.248/v2/statistics/reference/{reference_id}
"""
import asyncio
from typing import Any, Dict, List, Set

import aiohttp
import requests

from src import WcdBaseModel
from src.models.api.job.article_job import ArticleJob


class AllHandler(WcdBaseModel):
    compilation: Dict[str, Any] = {}
    data: Dict[str, Any] = {}
    # We use a set to avoid duplicates
    dois: Set[str] = set()
    doi_details: List[Dict[str, Any]] = []
    job: ArticleJob
    references: List[Dict[str, Any]] = []
    url_details: List[Dict[str, Any]] = []
    error: bool = False
    extract_dois_done = False

    @property
    def number_of_references(self) -> int:
        return len(self.data["references"])

    @property
    def number_of_dois(self) -> int:
        self.__extract_dois__()
        return len(self.dois)

    @staticmethod
    async def fetch_data(session, url):
        async with session.get(url) as response:
            return await response.json()

    async def get_reference_ids(self, ids: List[str]):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for reference_id in ids:
                url = f"http://18.217.22.248/v2/statistics/reference/{reference_id}"
                tasks.append(asyncio.ensure_future(self.fetch_data(session, url)))

            results = await asyncio.gather(*tasks)
            return results

    async def check_urls(self, urls: Set[str]):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for url in urls:
                url = f"http://18.217.22.248/v2/check-url?url={url}"
                tasks.append(asyncio.ensure_future(self.fetch_data(session, url)))

            results = await asyncio.gather(*tasks)
            return results

    async def check_dois(self, dois: Set[str]):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for doi in dois:
                url = f"http://18.217.22.248/v2/check-doi?doi={doi}"
                tasks.append(asyncio.ensure_future(self.fetch_data(session, url)))

            results = await asyncio.gather(*tasks)
            return results

    def fetch_and_compile(self):
        from src.models.api import app

        self.__fetch_article__()
        self.__fetch_references__()
        self.__extract_dois__()
        app.logger.info(f"Found {self.number_of_dois} DOIs")
        self.__fetch_url_details__()
        self.__fetch_doi_details__()
        self.__compile_everything__()

    def __fetch_references__(self):
        from src.models.api import app

        if not self.error and not self.references:
            app.logger.debug("__fetch_references__: running")
            # this code from chatgpt does not work via flask
            # loop = asyncio.get_event_loop()
            # solution from https://techoverflow.net/2020/10/01/how-to-fix-python-asyncio-runtimeerror-there-is-no-current-event-loop-in-thread/
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            self.references = loop.run_until_complete(
                self.get_reference_ids(self.data["references"])
            )

    def __fetch_url_details__(self):
        from src.models.api import app

        if not self.error:
            app.logger.debug("__fetch_url_details__: running")
            # this code from chatgpt does not work via flask
            # loop = asyncio.get_event_loop()
            # solution from https://techoverflow.net/2020/10/01/how-to-fix-python-asyncio-runtimeerror-there-is-no-current-event-loop-in-thread/
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            # we use a set here to avoid duplicates
            urls = set(self.data["urls"])
            app.logger.info(f"Checking {len(urls)} URLs")
            self.url_details = loop.run_until_complete(self.check_urls(urls))

    def __fetch_doi_details__(self):
        from src.models.api import app

        if not self.error:
            app.logger.debug("__fetch_doi_details__: running")
            # this code from chatgpt does not work via flask
            # loop = asyncio.get_event_loop()
            # solution from https://techoverflow.net/2020/10/01/how-to-fix-python-asyncio-runtimeerror-there-is-no-current-event-loop-in-thread/
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            self.__extract_dois__()
            if self.dois:
                app.logger.info(f"Checking {len(self.dois)} DOIs")
                self.doi_details = loop.run_until_complete(self.check_dois(self.dois))
            else:
                app.logger.info(f"Not checking DOIs because none were found")

    def __fetch_article__(self):
        from src.models.api import app

        app.logger.debug("__fetch_article__: running")
        # response = requests.get(f"http://18.217.22.248/v2/statistics/article?url={}")
        response = requests.get(
            f"http://18.217.22.248/v2/statistics/article?lang=en&site=wikipedia&title={self.job.title}"
        )
        if response.status_code == 200:
            self.data = response.json()
            app.logger.info(
                f"got article data with {self.number_of_references} " f"references"
            )
        else:
            app.logger.error(
                f"Got status code {response.status_code} when "
                f"fetching from the article endpoint"
            )
            self.error = True

    def __compile_everything__(self):
        """Here we put the big json object together"""
        if not self.error:
            self.compilation = self.data
            self.compilation["doi_details"] = self.doi_details
            self.compilation["reference_details"] = self.references
            self.compilation["url_details"] = self.url_details

    def __extract_dois__(self):
        """Extract the DOIs which are hiding in the templates"""

        if self.references and not self.extract_dois_done:
            for reference in self.references:
                # app.logger.debug(f"working on this reference: {reference}")
                for template in reference["templates"]:
                    # app.logger.debug(f"working on this template: {template}")
                    if "doi" in template["parameters"]:
                        self.dois.add(template["parameters"]["doi"])
        self.extract_dois_done = True