import logging
from freedictionaryapi.clients.async_client import AsyncDictionaryApiClient
from aiohttp import ClientSession

logging.basicConfig(
    level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

session = ClientSession()

client = AsyncDictionaryApiClient()