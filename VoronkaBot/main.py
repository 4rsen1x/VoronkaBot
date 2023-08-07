from handlers import *
import asyncio
import logging


def main():
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    loop.create_task(start_bot(dp))
    loop.run_forever()


if __name__ == "__main__":
    main()
