class Medicamentos:
    medicamentos = []

    def __init__(self, nome, nome_cientifico, tarja, local):
        self.nome = nome
        self.nome_cientifico = nome_cientifico
        self.tarja = tarja
        self.local = local
        self._estoque = False
        Medicamentos.medicamentos.append(self)

    def __str__(self):
        return f'{self.nome} | {self.nome_cientifico} | {self.tarja} | {self.local} | {self.estoque}'

    def listar_medicamentos():
        print('')
        print('''
              
███╗░░░███╗███████╗██████╗░██╗░█████╗░░█████╗░███╗░░░███╗███████╗███╗░░██╗████████╗░█████╗░░██████╗
████╗░████║██╔════╝██╔══██╗██║██╔══██╗██╔══██╗████╗░████║██╔════╝████╗░██║╚══██╔══╝██╔══██╗██╔════╝
██╔████╔██║█████╗░░██║░░██║██║██║░░╚═╝███████║██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░██║░░██║╚█████╗░
██║╚██╔╝██║██╔══╝░░██║░░██║██║██║░░██╗██╔══██║██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░██║░░██║░╚═══██╗
██║░╚═╝░██║███████╗██████╔╝██║╚█████╔╝██║░░██║██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝╚══════╝╚═════╝░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░╚═════╝░

██████╗░██╗░██████╗██████╗░░█████╗░███╗░░██╗██╗██╗░░░██╗███████╗██╗░██████╗
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗████╗░██║██║██║░░░██║██╔════╝██║██╔════╝
██║░░██║██║╚█████╗░██████╔╝██║░░██║██╔██╗██║██║╚██╗░██╔╝█████╗░░██║╚█████╗░
██║░░██║██║░╚═══██╗██╔═══╝░██║░░██║██║╚████║██║░╚████╔╝░██╔══╝░░██║░╚═══██╗
██████╔╝██║██████╔╝██║░░░░░╚█████╔╝██║░╚███║██║░░╚██╔╝░░███████╗██║██████╔╝
╚═════╝░╚═╝╚═════╝░╚═╝░░░░░░╚════╝░╚═╝░░╚══╝╚═╝░░░╚═╝░░░╚══════╝╚═╝╚═════╝░ ''')
        
        print(f'{'Nome do medicamento'.ljust(20)} | {'Nome científico'.ljust(20)} | {'Tarja'.ljust(20)} | {'Local'.ljust(20)} | {'Estoque'}')
        print('------------------------------------------------------------------------------------------------------------------------------')
        for medicamento in Medicamentos.medicamentos:
            print(f'{medicamento.nome.ljust(20)} | {medicamento.nome_cientifico.ljust(20)} | {medicamento.tarja.ljust(20)} | {medicamento.local.ljust(20)} | {medicamento.estoque}')
            print('-------------------------------------------------------------------------------------------------------------------------')

    @property
    def estoque(self):
        return '❌ estoque' if self._estoque else '✔️ estoque'        

medicamento_tadalafila = Medicamentos('Tadalafila', 'Cialis', 'Vermelha', 'Morumbi')
medicamento_buscopan = Medicamentos('Buscopan', 'butilbrometo', 'Amarela', 'Vila A')
medicamento_paracetamol = Medicamentos('Paracetamol', 'Acetaminofeno', 'Branca', 'Centro')

medicamentos = [medicamento_tadalafila, medicamento_buscopan, medicamento_paracetamol]

Medicamentos.listar_medicamentos()
