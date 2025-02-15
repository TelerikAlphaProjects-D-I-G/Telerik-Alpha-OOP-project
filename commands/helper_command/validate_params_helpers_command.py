
def validate_params_count(params, count):
	if len(params) != count:
		raise ValueError(f"Invalid number of arguments. Received:{len(params)}")

def try_parse_int(value):
	try:
		return int(value)
	except ValueError:
		return None