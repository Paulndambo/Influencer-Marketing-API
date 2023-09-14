import asyncio

import aiohttp


async def make_request(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    url = 'http://127.0.0.1:8000/analytics/promotion-campaigns/'  # Replace with the API endpoint URL
    num_requests = 1000000

    async with aiohttp.ClientSession() as session:
        tasks = [make_request(session, url) for _ in range(num_requests)]
        responses = await asyncio.gather(*tasks)
        print(responses)

    # Process responses or log them as needed

asyncio.run(main())
