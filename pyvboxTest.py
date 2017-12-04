import virtualbox

class WSManager_VPN():

    def __init__(self):
        self.vbox = virtualbox.VirtualBox()

    def clone_vm(self, machine, snapshot_name, machine_name):
        cloned_vm = machine.clone(snapshot_name, name=machine_name)
        self.add_redirect_to_machine(cloned_vm, 1000, 1194)

    def add_redirect_to_machine(self, machine, src_port, dst_port):
        session = machine.create_session()

        machine_name = machine.name
        session.machine.name = machine_name
        print("Cloned machine " + machine_name)

        tcp = virtualbox.library.NATProtocol(1)
        adapter = session.machine.get_network_adapter(0)
        nat_engine = adapter.nat_engine

        nat_engine.add_redirect('', tcp, '', src_port, '', dst_port)

        session.machine.save_settings()
        session.unlock_machine()

        self.start_vm(machine)
        
    def start_vm(self, machine):
        try:
            progress = machine.launch_vm_process(type_p="headless")
            progress.wait_for_completion()
        except Exception:
            print("Error starting VM " + machine.name)

    def remove_redirects(self, machine):
        machine_nat_engine = machine.get_network_adapter(0).nat_engine
        redirects = machine_nat_engine.redirects
        redirect_items = redirects[0].split(',')
        machine_nat_engine.remove_redirect(redirect_items[0])