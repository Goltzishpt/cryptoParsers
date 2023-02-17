from scrapy.responsetypes import Response
from crawler.parsers.base import CryptoCurrencyParseBase
from .contractParser import ContractParse
from .tagParser import TagParse


class CryptoCurrencyCoinGeckoParse(CryptoCurrencyParseBase):

    def __init__(self, response: Response):
        super().__init__(response=response)
        self.response = response

    @property
    def _get_url(self):
        return self.response.url

    @property
    def _get_name(self):
        return self.response.xpath('//div[@data-controller="coins-information"]//h1/span[1]//text()').get().strip()

    @property
    def _get_image(self):
        return self.response.xpath('//div[@data-controller="coins-information"]//img[@height="28"]/@src').get()

    @property
    def _get_symbol(self):
        return self.response.xpath('//div[@data-controller="coins-information"]//h1/span[2]//text()').get().strip()

    @property
    def _get_rank(self):
        xpath = '//div[@data-controller="coins-information"]//div[contains(text(), "Rank")]//text()'
        return self.response.xpath(xpath).get().replace('Rank #', '').strip()

    @property
    def _get_website(self):
        return self.response.xpath('//div[@data-target="coins-information.mobileOptionalInfo"]'
                                   '//span[contains(text(), "Website")]/following-sibling::*//a/@href').getall()

    @property
    def _get_explorers(self):
        return self.response.xpath('//div[@data-target="coins-information.mobileOptionalInfo"]'
                                   '//span[contains(text(), "Explorers")]/following-sibling::*//a/@href').getall()

    @property
    def _get_wallets(self):
        return self.response.xpath('//div[@data-target="coins-information.mobileOptionalInfo"]'
                                   '//span[contains(text(), "Wallets")]/following-sibling::*//a/@href').getall()

    @property
    def _get_community(self):
        return self.response.xpath('//div[@data-target="coins-information.mobileOptionalInfo"]'
                                   '//span[contains(text(), "Community")]/following-sibling::*//a/@href').getall()

    @property
    def _get_api_id(self):
        return self.response.xpath('//div[@data-target="coins-information.mobileOptionalInfo"]'
                                   '//span[contains(text(), "API")]//following-sibling::*/text()').get().strip()

    @property
    def _get_contracts(self):
        xpath = '//div[@data-controller="coin-contract-address"]/span[contains(text(), "Contract")]' \
                '[1]/following-sibling::*//div[contains(@class, "tw-items-center") and not(@id="dropdownMenuButton")]'
        return [ContractParse(response=i).get_item() for i in self.response.xpath(xpath)]

    @property
    def _get_tags(self):
        xpath = '//div[contains(@class, "coin-link-row")]/span[contains(text(), "Tags")]/following-sibling::*//a'
        return [TagParse(response=i).get_item() for i in self.response.xpath(xpath)]
