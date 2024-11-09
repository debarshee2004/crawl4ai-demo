import asyncio
import os
from crawl4ai import AsyncWebCrawler  # type: ignore
from urllib.parse import urlparse


# Define a helper function to print in green
def print_green(text):
    print(f"\033[92m{text}\033[0m")


async def crawl_single(url: str, filename: str):
    async with AsyncWebCrawler(verbose=True) as crawler:
        result = await crawler.arun(url=url)
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(result.markdown))
    print_green(f"Results saved to {filename}")


async def crawl_multiple(urls_file: str):
    os.makedirs("output", exist_ok=True)
    async with AsyncWebCrawler(verbose=True) as crawler:
        with open(urls_file, "r") as file:
            urls = file.read().splitlines()
        for url in urls:
            parsed_url = urlparse(url)
            file_name = f"{parsed_url.netloc.replace('.', '-')}{parsed_url.path.replace('/', '-')}"
            if file_name.endswith("-"):
                file_name = file_name[:-1]  # Remove trailing hyphen
            file_path = os.path.join("output", file_name + ".md")
            result = await crawler.arun(url=url)
            with open(file_path, "w", encoding="utf-8") as output_file:
                output_file.write(str(result.markdown))
            print_green(f"Results for {url} saved to {file_path}")


async def main():
    choice = input(
        "Do you want to scrape one website or multiple? (1 for one, 2 for multiple): "
    )

    if choice == "1":
        url_input = input("Enter the URL to crawl: ")
        filename = input(
            "Enter the filename to save the result (default: demo-output): "
        )
        if filename == "":
            filename = "demo-output"  # Default file name
        file_path = os.path.join("output", filename + ".md")
        os.makedirs("output", exist_ok=True)
        await crawl_single(url_input, file_path)

    elif choice == "2":
        urls_file = input("Enter the .txt file containing URLs (default: urls): ")
        if urls_file == "":
            urls_file = "urls"  # Default file name
        await crawl_multiple(urls_file + ".txt")
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    asyncio.run(main())
