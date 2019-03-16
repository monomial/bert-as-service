from bert_serving.client import BertClient
bc = BertClient()
bc.encode(['Hello', 'World'])