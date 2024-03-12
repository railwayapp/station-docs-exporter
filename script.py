import subprocess, json
import git

def script():
	repo_path = '/docs/'
	# docs_path = '/docs/src/docs'
	
	# md_suffix = re.compile(".*md$")

	# update railway docs repo
	repo = git.cmd.Git(repo_path)
	repo.pull()

	all_files  = []
	export = []
	values = []
	
	# search through docs, find markdown files, and calculate score
	# for root, _, files in os.walk(docs_path, topdown=False):
	# 	for file in files:
	# 		if re.match(md_suffix, file):
	# 			path = os.path.join(root, file)
	# 			output = pypandoc.convert_file(path, 'plain')
	# 			analysis = Readability(output)
	# 			flesch   = analysis.flesch()
	# 			response = {path: flesch.score} 
	# 			export.append(response)
	# 			values.append(flesch.score)
	# 			all_files.append(flesch)

	args = ['/usr/bin/vale', '/docs/src/docs', '--config=./vale.ini', '--output=JSON']
	p = subprocess.check_output(args)
	data = json.loads(p)
	for key, value in data.items():
		response = {key: value[0]['Message']}
		export.append(response)
		values.append(float(value[0]['Message']))

	# reduce values to one sum, count the docs, find overall average, and append to results
	values_sum = sum(values)
	docs_sum = len(export)
	flesch_average = values_sum / docs_sum
	export.append({'flesch_average': flesch_average})
	export.append({'docs_sum': docs_sum})
 
	return export
