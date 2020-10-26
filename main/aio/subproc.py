import sys
import asyncio

async def run(cmd):
    '''
    '''

    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()

    print(f'[{cmd!r} exited with {process.returncode}]')
    coding = sys.getdefaultencoding()
    print(f'coding: {coding}')
    if stdout:
        print(f'[stdout]\n{stdout.decode("gbk")}')
        pass
    if stderr:
        print(f'[stderr]\n{stderr.decode("gbk")}')
        pass

asyncio.run(run('ls'))