import asyncio
from playwright.async_api import async_playwright

FAUCET_URL = "https://testnet.blackhole.xyz"
TESTNET_ADDRESS = "your_testnet_address_here"  # Replace with your actual testnet address

async def claim_blackhole_faucet():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)  # Set to True to run headless
        page = await browser.new_page()

        await page.goto(FAUCET_URL)

        # Wait for the address input field (adjust selector after inspecting the page)
        await page.wait_for_selector('input[type="text"], input[name="address"]')

        # Fill in your testnet address
        await page.fill('input[type="text"], input[name="address"]', TESTNET_ADDRESS)

        # Click the faucet claim button (adjust selector to actual button text or class)
        await page.click('button:has-text("Claim")')

        # Wait for a success or error message (adjust selector/text accordingly)
        try:
            await page.wait_for_selector('text=Success', timeout=10000)
            print("Faucet claim successful!")
        except:
            print("No success message detected. Please verify manually.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(claim_blackhole_faucet())
