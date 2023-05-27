import asyncio
import os
import random
import subprocess
import time
from secrets import token_hex

import aiohttp
import pytest


class TestArgs:
    dev = True
    host = "127.0.0.1"
    port = 5000
    
args = TestArgs()
def run_server():
    return subprocess.Popen(["python3", "run.py"], cwd=os.getcwd(), shell=True)

process = run_server()
time.sleep(3)

@pytest.fixture(scope='session')
def my_cleanup_fixture(request):
    if process:
        process.terminate()
        process.wait()
    
ENDPOINT = "http://{}:{}/api/v1/users".format(args.host, args.port)
ENDPOINT_ENTRY = ENDPOINT + "/{}"

# Helper functions
async def getAll(cs: aiohttp.ClientSession):
    async with cs.get(ENDPOINT) as res:
        return await res.json()

async def deleteAll(cs: aiohttp.ClientSession):
    async with cs.delete(ENDPOINT) as res:
        return await res.json()
    
async def create(cs: aiohttp.ClientSession):
    random_hex = token_hex(32)
    async with cs.post(ENDPOINT, data={
        "email": random_hex,
        "username": random_hex,
        "password": random_hex,
    }) as res:
        return await res.json()
    
async def get(cs: aiohttp.ClientSession, id: int):
    async with cs.get(ENDPOINT_ENTRY.format(id)) as res:
        return await res.json()

async def delete(cs: aiohttp.ClientSession, id: int):
    async with cs.delete(ENDPOINT_ENTRY.format(id)) as res:
        return await res.json()
    
async def put(cs: aiohttp.ClientSession, id: int, data: dict):
    async with cs.put(ENDPOINT_ENTRY.format(id), data=data) as res:
        return await res.json()
    
async def patch(cs: aiohttp.ClientSession, id: int, data: dict):
    async with cs.patch(ENDPOINT_ENTRY.format(id), data=data) as res:
        return await res.json()


# Test cases
@pytest.mark.asyncio
async def test_delete_all():
    async with aiohttp.ClientSession() as cs:
        await deleteAll(cs)
        data = await getAll(cs)
        
        assert len(data.get("data", [])) == 0
        
@pytest.mark.asyncio
async def test_create():
    async with aiohttp.ClientSession() as cs:
        created = await asyncio.gather(*[create(cs) for _ in range(100)])
        ids = [c.get("data").get("id") for c in created]
        gotten = await asyncio.gather(*[get(cs, id) for id in ids])
        
        assert len(created) == len(gotten) and all(
            [all(h.get("data").get(key) == c.get("data").get(key) for key in ["email", "username", "password"])
                for h, c in zip(gotten, created)])
        
@pytest.mark.asyncio
async def test_get():
    async with aiohttp.ClientSession() as cs:
        data = await getAll(cs)
        ids = [d.get("id") for d in data.get("data", [])]
        gotten = await asyncio.gather(*[get(cs, id) for id in ids])
        
        assert len(data.get("data", [])) == len(gotten) and all(
            [all(h.get(key) == c.get("data").get(key) for key in ["email", "username", "password"])
                for h, c in zip(data.get("data", []), gotten)])
        
@pytest.mark.asyncio
async def test_delete():
    async with aiohttp.ClientSession() as cs:
        data = await getAll(cs)
        record = random.choice(data.get("data", []))
        
        await delete(cs, record.get("id"))
        data = await getAll(cs)
        
        assert record.get("id") not in [d.get("id") for d in data.get("data", [])]
        
@pytest.mark.asyncio
async def test_put():
    async with aiohttp.ClientSession() as cs:
        data = await getAll(cs)
        record = random.choice(data.get("data", []))
        new_hex = token_hex(32)
        
        await put(cs, record.get("id"), {
            "email": new_hex,
            "username": new_hex,
            "password": new_hex,
        })
        data = await get(cs, record.get("id"))
        
        assert all(data.get("data").get(key) == new_hex for key in ["email", "username", "password"])
        
@pytest.mark.asyncio
async def test_patch():
    async with aiohttp.ClientSession() as cs:
        data = await getAll(cs)
        record = random.choice(data.get("data", []))
        new_hex = token_hex(32)
        
        await patch(cs, record.get("id"), {
            "email": new_hex,
        })
        data = await get(cs, record.get("id"))
        
        assert data.get("data").get("email") == new_hex and all(
            data.get("data").get(key) == record.get(key) for key in ["username", "password"])
        
@pytest.mark.asyncio
async def test_delete_all_finish():
    async with aiohttp.ClientSession() as cs:
        await deleteAll(cs)
        data = await getAll(cs)
        
        assert len(data.get("data", [])) == 0