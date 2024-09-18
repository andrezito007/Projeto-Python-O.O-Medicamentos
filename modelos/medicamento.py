class Medicamentos:
    medicamentos = []

    def __init__(self, nome, nome_cientifico, tarja, local):
        self._nome = nome.upper()
        self._nome_cientifico = nome_cientifico.title()
        self._tarja = tarja
        self._local = local.title()
        self._estoque = False
        Medicamentos.medicamentos.append(self)

    def __str__(self):
        return f'{self._nome} | {self._nome_cientifico} | {self._tarja} | {self._local} | {self._estoque}'

    @classmethod
    def listar_medicamentos(cls):
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
        for medicamento in cls.medicamentos:
            print(f'{medicamento._nome.ljust(20)} | {medicamento._nome_cientifico.ljust(20)} | {medicamento._tarja.ljust(20)} | {medicamento._local.ljust(20)} | {medicamento.estoque}')
            print('-------------------------------------------------------------------------------------------------------------------------')

    @property
    def estoque(self):
        return '❌ estoque' if self._estoque else '✔️ estoque'

    def alterar_estado(self):
        self._estoque = not self._estoque        

Medicamentos.listar_medicamentos()
