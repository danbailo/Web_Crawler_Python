import os

def create_project_dir(directory):
	if not os.path.exists(directory):
		print('Creating project {}'.format(directory))
		os.makedirs(directory)
	else: print('This project already exists!')		

create_project_dir('ufms')

def create_data_files(project_name, base_url):
	queue = project_name + '/queue.txt'
	crawled = project_name + '/crawled.txt'
	if not os.path.isfile(queue): 
		write_file(queue, base_url)
	if not os.path.isfile(crawled): 
		write_file(crawled, base_url)

#crate a new file
def write_file(path, data):
	with open(path, 'w') as file: file.write(data)

#add data onto an existing file
def	appent_to_file(path, data):
	with open(path, 'a') as file: file.write(data + '\n')

#delete the contents of a file
def delete_file_contents(path): 
	with open(path, 'w'): pass #overwrite

def file_to_set(file_name):
	results = set()
	with open(file_name, 'r') as file:
		for line in file: results.add(line.replace('\n', ''))
	return results

def set_to_file(links, file):
	delete_file_contents(file)
	for link in sorted(links):
		appent_to_file(file, link)