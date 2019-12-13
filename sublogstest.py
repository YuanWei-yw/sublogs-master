import asyncio
from aiologs import esHandler
from sublogs import SubLogger
from sublogs import Sublogconfig


async def main():
    Sublogconfig.addConfig({
        "username":'yuan',
        "projectName": "subtest",
        "dbtype": 0,
        "targetDB": ["192.168.88.2:27017"],
        "env": "develop"
    })
    log = SubLogger()


    await log.debug('yuandebug',"m1", "c1", "c2", {"abc": 1}, {"bcd": 1})
    await log.error('yuanerror',"m1", "c1", "c2", {"abc": 1}, {"bcd": 1})
    await log.warning('yuanwarning',"m1", "c1", "c2", {"abc": 1}, {"bcd": 1})
    await log.info('yuaninfo',"m1", "c1", "c2", {"abc": 1}, {"bcd": 1})


if __name__ == "__main__":
    try:
        import uvloop
        asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    except ImportError:
        pass
    asyncio.run(main())
