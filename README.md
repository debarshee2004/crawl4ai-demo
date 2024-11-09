# Crawl4AI Web Scraping

Crawl4AI is a web scraping tool that allows you to extract data from websites and save in markdown format.
Original Project at GitHub: [github.com/unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)

## Setting up this project locally

1. Clone the repository to your local machine using the following command:

```
https://github.com/debarshee2004/crawl4ai-demo.git
```

2. Navigate to the project directory using the following command:

```
cd crawl4ai-demo
```

3. Install the required dependencies using the following command:

```
pip install crawl4ai crawl4ai[sync] # or pip3 install crawl4ai crawl4ai[sync]
playwright install # or python -m playwright install chromium
```

4. Run the project using the following command:

```
python main.py
```

## Demo

**Web Scraping only one webpage.**

```log
Code\aiml\crawl4ai> python .\main.py
Do you want to scrape one website or multiple? (1 for one, 2 for multiple): 1
Enter the URL to crawl: https://elevenlabs.io/docs/product/workspace/sso_setup
Enter the filename to save the result (default: demo-output.txt):
[LOG] 🚀 Crawl4AI 0.3.73
[LOG] 🌤️  Warming up the AsyncWebCrawler
[LOG] 🌞 AsyncWebCrawler is ready to crawl
[LOG] 🚀 Content extracted for https://elevenlabs.io/docs/product/workspace/sso_setup, success: True, time taken: 0.44 seconds
[LOG] 🚀 Extraction done for https://elevenlabs.io/docs/product/workspace/sso_setup, time taken: 0.44 seconds.
Results saved to output\demo-output.md
```

**Web Scraping multiple webpages with a `urls.txt` file containing the urls to scrape.**

```log
Code\aiml\crawl4ai> python .\main.py
Do you want to scrape one website or multiple? (1 for one, 2 for multiple): 2
Enter the .txt file containing URLs (default: urls.txt):
[LOG] 🚀 Crawl4AI 0.3.73
[LOG] 🌤️  Warming up the AsyncWebCrawler
[LOG] 🌞 AsyncWebCrawler is ready to crawl
[LOG] 🚀 Content extracted for https://elevenlabs.io/docs/product/voices/default-voices, success: True, time taken: 0.39 seconds
[LOG] 🚀 Extraction done for https://elevenlabs.io/docs/product/voices/default-voices, time taken: 0.39 seconds.
Results for https://elevenlabs.io/docs/product/voices/default-voices saved to output\elevenlabs-io-docs-product-voices-default-voices.md
[LOG] 🚀 Content extracted for https://elevenlabs.io/docs/product/voices/voice-lab/professional-voice-cloning, success: True, time taken: 0.19 seconds
[LOG] 🚀 Extraction done for https://elevenlabs.io/docs/product/voices/voice-lab/professional-voice-cloning, time taken: 0.19 seconds.
Results for https://elevenlabs.io/docs/product/voices/voice-lab/professional-voice-cloning saved to output\elevenlabs-io-docs-product-voices-voice-lab-professional-voice-cloning.md
[LOG] 🚀 Content extracted for https://elevenlabs.io/docs/product/workspace/sso_setup, success: True, time taken: 0.19 seconds
[LOG] 🚀 Extraction done for https://elevenlabs.io/docs/product/workspace/sso_setup, time taken: 0.19 seconds.
Results for https://elevenlabs.io/docs/product/workspace/sso_setup saved to output\elevenlabs-io-docs-product-workspace-sso_setup.md
```

The output will be saved in the `output` directory in markdown format.
