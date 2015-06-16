#!/usr/bin/python
import deersrv
import json
import deerconsole
import time
#assert(deersrv.ValidateAddress("TPovjKVAistboRH2Y178wH5NUVEWvQN4HN"))
#assert(deersrv.aliastxid(deersrv.testMoney("TPovjKVAistboRH2Y178wH5NUVEWvQN4HN")))
#print deersrv.proc("{'params': ['CreateAccounts', '02750c2352cd6a52895be14bc9b5399e7362d8071f0d0004223b623f4cd1c15733', 1434114797, '6434b682-5b73-4fa1-b023-3b99f1eec9e1', '3045022100B9860BA6DFFEBFC18F8507E606BF03FBDA5374A6F56D04E4268590163BE6B74F022045BFFFE80A5E3A97ACD05C56895316FB94E49055698CB9821230972C8A1D35CD'], 'id': '1434114797+6434b682-5b73-4fa1-b023-3b99f1eec9e1'}")
#print deersrv.proc('{"params": ["CreateAccount", "04edc9a388beaa6957c49bb34bf627eec73a2dcb98bd7f9752166e9525a0af3678af263889ff55bdd53ed3a5bc3367a487d3ba0ffbafde6d81f881c9c78c91f9ce", 1434455404, "foobar", "G/ELWdLgOsizxJIWUh3PcZA8HZmt5jRj22KJLnOdOPpXWCUqt/wqx/4GH86upaKZrFTxFA9OMs1rvC9pCqGIcso="], "id": "1434455404foobar"}')

pk, pbk, addr = deerconsole.getKeys("foo","somerand"+str(time.time()))
foo = deerconsole.swag(pk, "foobar")
#print foo
#print deersrv.proc(foo)
aa = {"params": ["GetBalance", "04675ee26dc854326e364ecd92de1ce2a9bcf6f5de2a06d27bbfd32d95686117de7e1f7c1dc9c44a3209287d1b89fc63b34a91cddce20a5b02b31bcb847a544ce8", 1434460496, "foobar", "G1Pd4TaqMRNwCCDBJNbsRO3sCOSmY2oJYHBOUHGyNjbkxE+9EvmXOmjcCxqAVx8LZRRTS9qhCat66szPloUVutQ="], "id": "1434460496foobar"}
print deersrv.proc(aa)
#print deersrv.proc('{"params": ["ListTransactions", "04675ee26dc854326e364ecd92de1ce2a9bcf6f5de2a06d27bbfd32d95686117de7e1f7c1dc9c44a3209287d1b89fc63b34a91cddce20a5b02b31bcb847a544ce8", 1434460496, "foobar", "G1Pd4TaqMRNwCCDBJNbsRO3sCOSmY2oJYHBOUHGyNjbkxE+9EvmXOmjcCxqAVx8LZRRTS9qhCat66szPloUVutQ="], "id": "1434460496foobar"}')
#test this module using deerwallet and deerconsole


