import asyncio
from crawl4ai import AsyncWebCrawler, BFSDeepCrawlStrategy
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
from crawl4ai.markdown_generation_strategy import DefaultMarkdownGenerator
from crawl4ai.content_filter_strategy import PruningContentFilter

START_URL = "https://www.itnb.ch/en"
OUTPUT_FILE = "itnb_content.md" 

async def scrape_itnb_website():

    print(f"Initiating crawl of: {START_URL}...")

    browser_config = BrowserConfig(
        headless=True,
        verbose=False 
    )

    content_filter = PruningContentFilter(
        threshold=0.5,           
        threshold_type="fixed",
        min_word_threshold=10    
    )
    
    markdown_generator = DefaultMarkdownGenerator(
        content_filter=content_filter,
    )
    
    run_config = CrawlerRunConfig(
        markdown_generator=markdown_generator,
        deep_crawl_strategy=BFSDeepCrawlStrategy(
            max_depth=3,  
            include_external=False     
        ))

    async with AsyncWebCrawler(config=browser_config) as crawler:
        results_list = await crawler.arun(
            url=START_URL,
            config=run_config
        )

    full_markdown_content = ""

    for result in results_list:

        if result.success and result.markdown:
            full_markdown_content += result.markdown.raw_markdown + "\n\n---\n\n"


        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            f.write(full_markdown_content)
        
        print(f"Crawl completed. Content saved to {OUTPUT_FILE}.")


if __name__ == "__main__":
    asyncio.run(scrape_itnb_website())
