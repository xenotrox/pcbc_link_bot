class AffiliateLinkConverter:
    def __init__(self, link):
        self.link = link

    def _convert_to_caseking(self, link):
        link_parts = link[6:]
        affiliate_link_parts = ["http://partners.webmasterplan.com/", "click.asp?ref=807387&site=2767&typ",
                                "e=text&tnb=65&diurl=https%3A", "%3FsPartner%3D112"]
        return (affiliate_link_parts[0] + affiliate_link_parts[1]
                + affiliate_link_parts[2] + link_parts
                + affiliate_link_parts[3])

    def _convert_to_idealo(self, link):
        link_parts = link.split("/")
        affiliate_link_parts = ["http://partners.webmasterplan.com/click.asp?ref=807387&site=15168&type",
                                "=text&tnb=8&diurl=https%3A%2F%2F", "%2F", "%2F", "%2F", "%3Fcamp%3Daffilinet"]
        print(len(affiliate_link_parts))
        return (affiliate_link_parts[0] + affiliate_link_parts[1]
                + link_parts[2] + affiliate_link_parts[2]
                + link_parts[3] + affiliate_link_parts[3]
                + link_parts[4] + affiliate_link_parts[4]
                + link_parts[5] + affiliate_link_parts[5])

    def _convert_to_alternate(self, link):
        link_parts = link.split("/")
        link = ""
        affiliate_link_parts = ["https://ad.zanox.com/ppc/?43600950C52555739&ULP=[[https%3A%2F%2Fwww.alternate.de%2F",
                                "%3Fpartner%3Ddezanoxtextlink%26campaign%3DAF%2FDeZanox%2FTextlinks%2FAlternate]]"]
        for i in range(0, 3):
            del link_parts[0]

        for i in range(0, len(link_parts)):
            link = link + link_parts[i] + "%2F"

        return (affiliate_link_parts[0] + link + affiliate_link_parts[1])

    def _convert_to_notebooksbilliger(self, link):
        link_parts = link.replace("+", "%2B")
        affiliate_link_parts = ["https://ad.zanox.com/ppc/?42726803C40044189&ULP=[[", "]]"]
        return affiliate_link_parts[0] + link_parts + affiliate_link_parts[1]

    @property
    def link_to_affilate_link(self):
        link = self.link

        if "caseking.de" in link:
            return self._convert_to_caseking(link), "[Caseking] "
        elif "idealo.de" in link:
            return self._convert_to_idealo(link), "[Idealo] "
        elif "alternate.de" in link:
            return self._convert_to_alternate(link), "[Alternate] "
        elif "notebooksbilliger.de" in link:
            return self._convert_to_notebooksbilliger(link), "[Notebooksbilliger] "
        else:
            return ("no valid partner", "no note")

    def get_affiliate_link(self):
        return self.link_to_affilate_link
