import asyncio
import os
from aiogram import Router, Bot
from playwright.async_api import async_playwright
from dotenv import load_dotenv
from logs import log

router = Router()

load_dotenv()
channel = os.getenv("CHANNEL")
url = os.getenv("URL")
token = os.getenv("TOKEN")
bot = Bot(token)

async def getprice():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox"]
        )

        page = await browser.new_page()

        try:
            await page.goto(url)
            await page.wait_for_selector(".js-symbol-last")

            element = await page.query_selector(".js-symbol-last")
            ton = await element.inner_text()

            if not ton:
                print("FIND ERROR")
                return None
            
            return ton
        except Exception as err:
            log.error(err)
        finally:
            await browser.close()

async def send():
    try:
        ton = await getprice()

        if ton is None:
            log.price_error("TON")
            return
        
        await bot.send_message(chat_id=channel, text=f"💎 {ton}$")
        log.price("TON", ton)
    except Exception as err:
        log.error(err)

async def start():
    while True:
        await send()
        await asyncio.sleep(57)