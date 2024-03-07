from pyrfc import Server, RCStatus

def handle_rfc(request_context=None, RESTART_QNAME=None, TCPICDAT=None):
    print("Handle RFC")
    return RCStatus.OK

def onCheckTransaction(rfcHandle, tid):
    print("Executed onCheckTransaction Python function" ,rfcHandle, tid)
    return RCStatus.OK

def onCommitTransaction(rfcHandle, tid):
    print("Executed  onCommitTransaction Python function", rfcHandle, tid)
    return RCStatus.OK

def onConfirmTransaction(rfcHandle, tid):
    print("Executed onConfirmTransaction Python function", rfcHandle, tid)
    return RCStatus.OK

def onRollbackTransaction(rfcHandle, tid):
    print("Executed onRollbackTransaction Python function", rfcHandle, tid)
    return RCStatus.OK

#Create server
server = Server(server_params={'dest':'gateway'}, client_params={'dest':'server'},config={'debug': True,
                                                                                          'server_log': True } )

#ABAP function used to send IDocs via tRFC/qRFC
server.add_function("STFC_WRITE_TO_TCPIC", handle_rfc)

#Register the RFC transaction handlers.
server.transaction_rfc_init(sysId ='A4H', transactionHandler={ "check": onCheckTransaction,
                                                                "commit": onCommitTransaction,
                                                                "rollback": onRollbackTransaction,
                                                                "confirm": onConfirmTransaction
                                                                })
#Start server
server.start()

#Get server attributes
#print(server.get_server_attributes())

#Check transaction handlers
#print(server.transaction_handlers)
#print(server.transaction_handlers_count)

input("Press Enter to stop server...")

#Shutdown server
server.close()