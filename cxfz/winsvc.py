import sys
import os
import time
import win32.lib.winerror as werr
import win32.win32event as w32e
import win32.win32service as w32s
import win32.servicemanager as w32sm
import win32.lib.win32serviceutil as w32su
from loguru import logger
from win32.win32service import error

class CxfzPyService(w32su.ServiceFramework):
    '''
    '''

    _svc_name_ = 'CxfzPyService'
    _svc_display_name_ = 'Cxfz Python Service'
    _svc_description_ = 'Cxfz Python Service is a Demo.'

    def __init__(self, args):
        '''
        '''
        w32su.ServiceFramework.__init__(self, args)
        self.hWaitStop = w32e.CreateEvent(None, 0, 0, None)
        self.is_alive = True

    def SvcDoRun(self):
        while self.is_alive:
            logger.info('cxfz alive.')
            time.sleep(2.0)

    def SvcStop(self):
        self.ReportServiceStatus(w32s.SERVICE_STOP_PENDING)
        w32e.SetEvent(self.hWaitStop)
        self.is_alive = False


def main():
    '''
    '''

    try:
        dll_path = os.path.abspath(w32sm.__file__)
        logger.info(dll_path)
        w32sm.PrepareToHostSingle(CxfzPyService)
        logger.info('initialize')
        w32sm.Initialize(CxfzPyService._svc_name_, dll_path)
        logger.info('start begin')
        w32sm.StartServiceCtrlDispatcher()
        logger.info('start end')
    except error as es:
        logger.error(es)
        if es[0] == werr.werr.ERROR_FAILED_SERVICE_CONTROLLER_CONNECT:
            w32su.usage()
    except Exception as e:
        logger.error(e)

if __name__ == '__main__':
    folder = os.path.dirname(sys.argv[0])
    logger.remove()
    logger.add(
        folder + '\logs\cxfzsvc-{time}.log',
        level='INFO',
        rotation='00:00',
        retention='7 days',
    )
    logger.info(f'service, {folder} {sys.argv}')
    w32su.HandleCommandLine(CxfzPyService)
    # if len(sys.argv) == 1:
    #     main()
    # else:
    #     w32su.HandleCommandLine(CxfzPyService)
