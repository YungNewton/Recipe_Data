# First, we import the scrapy library
import scrapy

# We define a new spider by creating a class that inherits from scrapy.Spider
class ProductSpider(scrapy.Spider):
    # We give our spider a name
    name = "products"

    # Define the start URLs for our spider - this would be the URLs of the pages you want to start scraping from
    start_urls = ['https://www.aliexpress.com/item/1005005368384787.html?spm=a2g0o.productlist.main.15.26fd3324wOtx4Y&algo_pvid=23af3d8e-3b56-43ff-8301-24be281184a7&aem_p4p_detail=2023071809572617375450387514240001245635&algo_exp_id=23af3d8e-3b56-43ff-8301-24be281184a7-7&pdp_npi=3%40dis%21NGN%2117718.79%219214.16%21%21%21162.82%21%21%40211bf2da16896994468987624d0790%2112000032765442840%21sea%21NG%212542925502&curPageLogUid=8bfJfrtGo6Ia&search_p4p_id=2023071809572617375450387514240001245635_8']

    # The parse method is called for each URL in start_urls, and also for each URL followed from the start URLs
    def parse(self, response):
        # Extract product details
        for product in response.css('div.sg-col-inner'):
            yield {
                'title': product.css('span.a-size-medium::text').get(),
                'price': product.css('span.a-offscreen::text').get(),
            }

        # Follow pagination links and repeat
        next_page = response.css('div.s-pagination-item.s-pagination-next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

