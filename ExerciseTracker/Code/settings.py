from multiprocessing import Process, Manager, Value

manager = Manager()
global qu
qu = manager.Queue()
# def init():
#     manager = Manager()
#     global qu
#     qu = manager.Queue()