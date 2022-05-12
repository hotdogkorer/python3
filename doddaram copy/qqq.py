from googletrans import Translator
translator = Translator(service_urls=[
'translate.google.co.kr'
])
tr_results = translator.translate('担当者コメント.', src='ja', dest='ko')
print ('Trans(JA):', tr_results.text, tr_results.pronunciation)
