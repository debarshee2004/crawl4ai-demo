# Web Scraper with Markdown Save

How to use it? Install the dependencies:

```
pip install crawl4ai crawl4ai[sync] # or pip3 install crawl4ai crawl4ai[sync]
```

Now install

```
playwright install # or python -m playwright install chromium
```

Now you can run the script

```
Code\aiml\crawl4ai> python main.py
Enter the URL to crawl: https://elevenlabs.io/docs/voices/default-voices
Enter the filename to save the results: test.md
[LOG] 🚀 Crawl4AI 0.3.73
[LOG] 🌤️  Warming up the AsyncWebCrawler
[LOG] 🌞 AsyncWebCrawler is ready to crawl
[LOG] 🚀 Content extracted for https://elevenlabs.io/docs/voices/default-voices, success: True, time taken: 0.53 seconds
[LOG] 🚀 Extraction done for https://elevenlabs.io/docs/voices/default-voices, time taken: 0.53 seconds.
Results saved to output\test.md
```
