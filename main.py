import asyncio
import os
from crawl4ai import AsyncWebCrawler  # type: ignore


async def main():
    # Get URL and filename from user input
    url_input = input("Enter the URL to crawl: ")
    filename = input("Enter the filename to save the results: ")

    # Ensure the docs directory exists
    os.makedirs("output", exist_ok=True)

    # Save the file in the docs/ folder
    file_path = os.path.join("output", filename)

    # Perform web crawling
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url=url_input)

    # Save the results to a file with UTF-8 encoding
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(str(result.markdown))

    print(f"Results saved to {file_path}")


if __name__ == "__main__":
    asyncio.run(main())
