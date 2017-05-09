import dataset

db = dataset.connect('sqlite:///pagamentos.db?check_same_thread=False')
pagamentos = db['pagamentos']