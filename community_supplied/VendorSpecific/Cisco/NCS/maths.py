from __future__ import division

def used_percentage(total, used, **kwargs):
	return int(int(float(used))/int(float(total))*100)

def percentage_string_vector(vector, total, separator=None,precision=2, **kwargs):
	values = vector.split(separator)
	print(values)
	percentages = []
	for value in values:
		percentage = round(float(value)/total*100,precision)
		percentages.append(percentage)
	return percentages

def threshold_in_vector(vector, threshold, **kwargs):
	threshold_reached = 0
	if isinstance(vector,str):
		vector_ = vector.replace('[','').replace(']','').split(',')
		vector = [float(element) for element in vector_]
	for element in vector:
		if element > threshold:
			threshold_reached = 1
	return threshold_reached