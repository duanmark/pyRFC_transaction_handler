from pyrfc import Server, RCStatus

def handle_idoc(request_context=None, IDOC_CONTROL_REC_40=None, IDOC_DATA_REC_40=None):
    print("IDOC_INBOUND_ASYNCHRONOUS invoked")
    print("request_context", request_context)

    print("IDOC Control record:", IDOC_CONTROL_REC_40)
    print("IDOC Data record:", IDOC_DATA_REC_40)

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
server.add_function("IDOC_INBOUND_ASYNCHRONOUS", handle_idoc)

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