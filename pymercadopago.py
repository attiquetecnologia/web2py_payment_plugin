#-*- coding: utf-8 -*-
__author__ = 'Rodrigo Attique'
__email__ = 'attiquetecnologia@gmail.com'
__copyright__ = 'Copyright(c) 2019-2020 Rodrigo Attique '
__license__ = 'MIT'
__version__ = '0.0.0'
__timestamp__ = '2019-12-3'
# possible options: Prototype, Development, Production
__status__ = 'Prototype'

def mercadopago():
	# Conecta ao mercado pago para fazer o pagamento da fatura
	# Conect at mercadopago
	import mercadopago
	import json
	fatura = db.faturas_cliente(request.args(0))
	# https://www.mercadopago.com.br/developers/en/plugins_sdks/sdks/official/python/
	mp = mercadopago.MP("CLIENT_ID", "CLIENT_SECRET")

	preference = {
		"items": [{
			"back_url": URL('default', 'index'),
			"title": "Fatura #%s, %s" % ("6932", "Toy car"),
			"quantity": 1,
			"currency_id": "BRL",
			"unit_price": 19.9,
			"payer": {
				"name": "Client First Name",
				"surname": "Client Last Name",
				"email": "clientemail@domain.com",
			},
			"back_urls": {
				"success": URL('defautl','index'),
				"failure": URL('default','faturas'),
				"pending": URL('')
			}
		}]
	}

	preferenceResult = mp.create_preference(preference)
	redirect(preferenceResult['response']['init_point'])
	return json.dumps(preferenceResult, indent=4)