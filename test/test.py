#!/usr/bin/python
import deersrv
import json

#assert(deersrv.ValidateAddress("TPovjKVAistboRH2Y178wH5NUVEWvQN4HN"))
#assert(deersrv.aliastxid(deersrv.testMoney("TPovjKVAistboRH2Y178wH5NUVEWvQN4HN")))
print deersrv.proc("{'params': ['CreateAccounts', '02750c2352cd6a52895be14bc9b5399e7362d8071f0d0004223b623f4cd1c15733', 1434114797, '6434b682-5b73-4fa1-b023-3b99f1eec9e1', '3045022100B9860BA6DFFEBFC18F8507E606BF03FBDA5374A6F56D04E4268590163BE6B74F022045BFFFE80A5E3A97ACD05C56895316FB94E49055698CB9821230972C8A1D35CD'], 'id': '1434114797+6434b682-5b73-4fa1-b023-3b99f1eec9e1'}")


#test this module using deerwallet and deerconsole