import asyncio
from pyppeteer import launch


async def main():
    browser = await launch(args=['--no-sandbox'])
    page = await browser.newPage()
    await page.goto('https://github.com/')
    await page.screenshot({'path': 'example.png'})
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())