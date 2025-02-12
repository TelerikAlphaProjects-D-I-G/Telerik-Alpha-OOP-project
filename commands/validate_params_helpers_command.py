
def validate_params_count(params, count):
	if len(params) != count:
		raise ValueError(f"Invalid number of arguments. Received:{len(params)}")

def try_parse_int(weight):
	try:
		return int(weight)
	except:
		raise ValueError('Invalid value for weight')