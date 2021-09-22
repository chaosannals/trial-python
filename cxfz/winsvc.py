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

    _one_ = None

    def __init__(self, args):
        '''
        '''
        logger.info(f'cxfz init. start: {args}')
        super().__init__(args)
        # 父类构造函数执行后就突然停止了，下面的语言没有执行。
        logger.info(f'cxfz init ok')
        self.hWaitStop = w32e.CreateEvent(None, 0, 0, None)
        self.is_alive = True
        CxfzPyService._one_ = self
        logger.info(f'cxfz init. end:')

    # def SvcRun(self):
    #     '''
    #     '''

    #     logger.info('svc run.')
    #     self.ReportServiceStatus(w32s.SERVICE_RUNNING)
    #     self.SvcDoRun()
    #     self.ReportServiceStatus(w32s.SERVICE_STOP_PENDING)

    def SvcDoRun(self):
        logger.info('cxfz do run start')
        # 必须设置 RUNNING 状态，不然服务会被认为是没有启动。
        # self.ReportServiceStatus(w32s.SERVICE_RUNNING)
        while self.is_alive:
            logger.info('cxfz alive.')
            time.sleep(2.0)

    def SvcStop(self):
        # 设置 STOP_PENDING 状态。
        logger.info('cxfz stop')
        self.ReportServiceStatus(w32s.SERVICE_STOP_PENDING)
        w32e.SetEvent(self.hWaitStop)
        self.is_alive = False


def main():
    '''
    '''

    try:
        dll_path = os.path.abspath(w32sm.__file__)
        logger.info(dll_path)
        logger.info('initialize')
        # w32sm.Initialize(CxfzPyService._svc_name_, dll_path)
        w32sm.Initialize()
        w32sm.PrepareToHostSingle(CxfzPyService)
        logger.info('start begin')
        w32sm.StartServiceCtrlDispatcher()
        # 启动成功的话，这里在关闭服务前应该不会执行。
        logger.info('start end')

        # if CxfzPyService._one_ != None:
        #     CxfzPyService._one_.SvcRun()
        #     logger.info('has one do run')
        # else:
        #     logger.info('not one do run')
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
    
    if len(sys.argv) == 1:
        main()
    else:
        w32su.HandleCommandLine(CxfzPyService)
