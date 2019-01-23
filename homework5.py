"""
Homework 5.

Download a bunch  of files using:
    - aiohttp, asyncio
    - threads
"""

import asyncio
import aiohttp

import threading

from time import time

import urllib.request
import re

PAGE_ADDR = 'https://www.python.org/downloads/source/'


def get_links(url):
    """Return all found links for download."""
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    resp_data = resp.read()
    links = re.findall(r'Download <a href="(.*?)">', str(resp_data))

    return links


def threads_downloader(url):
    """Threads downloader."""
    urllib.request.urlretrieve(url, '/dev/null')


def threads_starter(links):
    threads = []

    for link in links:
        thread = threading.Thread(target=threads_downloader, args=(link,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()


async def asyncio_downloader(url):
    """Asyncio downloader."""
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=None) as r:
            with open('/dev/null', "wb") as f:
                while True:
                    chunk = await r.content.read(8192)
                    if not chunk:
                        break
                    f.write(chunk)


async def asyncio_starter():
    """Asyncio starter."""
    coroutines = []
    tasks = []

    for link in links_list:
        coroutines.append(asyncio_downloader(link))
    for coroutine in coroutines:
        tasks.append(asyncio.create_task(coroutine))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    print("Getting links...")
    links_list = get_links(PAGE_ADDR)
    num_of_files = len(links_list)
    print("Links received.")

    print('Downloading using threads started.')
    threads_start = time()
    threads_starter(links_list)
    threads_duration = time() - threads_start
    print('Downloading using threads finished.')

    print('Downloading using asyncio started.')
    async_start = time()
    asyncio.run(asyncio_starter())
    async_duration = time() - async_start
    print('Downloading using finished started.')

    print('Download time of {} files using threads is about {} seconds'.format(
        num_of_files, int(threads_duration)))
    print('Download time of {} files using asyncio is about {} seconds'.format(
        num_of_files, int(async_duration)))
