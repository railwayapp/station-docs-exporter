import time, re
from prometheus_client.core import GaugeMetricFamily, REGISTRY
from prometheus_client import start_http_server
from script import script

results = script()
print(results)
# iterate over results and add metrics for each url in grafana docs
class CustomCollector(object):
	def __init__(self):
		pass

	def collect(self):
		for result in results:	
			for key, value in result.items():
				if re.match(r'^docs_sum', key):
					gs = GaugeMetricFamily("docs_sum", 'total number of Railway docs', labels=["sum"])
					gs.add_metric([key], value)
					yield gs
				elif re.match(r'^/docs', key):
					g = GaugeMetricFamily("flesch_score", 'flesch reading ease score per URL', labels=["file"])
					g.add_metric([key], value)
					print(g)
					yield g
				elif re.match(r'^flesch_average', key):
					gm = GaugeMetricFamily("average_fre", 'overall FRE for docs repo', labels=["average"])
					gm.add_metric([key], value)
					yield gm


if __name__ == '__main__':
	start_http_server(8000)
	REGISTRY.register(CustomCollector())
	while True:
		time.sleep(30)
