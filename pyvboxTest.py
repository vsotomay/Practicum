import virtualbox

def cloneFromSnapshot(machineName, snapshotName):
    """
    Clone from a snapshot and add port forwarding rules
    """
    vbox = virtualbox.VirtualBox()
    vm = vbox.find_machine(machineName)
    newVm = vm.clone(snapshotName)
    tcp = virtualbox.library.NATProtocol(1) #TCP
    vmNatEngine = newVm.get_network_adapter(0).nat_engine #TODO find what slots are
    #!!BREAKS VIRTUALBOX!! (end tasks and processes to fix)
    vmNatEngine.add_redirect('Rule 1', tcp, '', 1000, '', 1194)
    print("rules should have been added")
    print("new vm is called " + newVm.name)
    #vmNatEngine.add_redirect('Rule 2', tcp, '', 2000, '', 22)

cloneFromSnapshot('test_vm', 'testVmSnap1')
