import hashlib
import time
import os
import concurrent.futures


#work_dir = "/python/files"
work_dir = "/python/files"


def get_files(target_dir):
	files = os.listdir(target_dir)
	return files


def make_full_path(file_list, work_dir):
	files = []
	for _ in range(50):
		for target_file in file_list:
			target_fullpath_file = os.path.join(work_dir, target_file)
			files.append(target_fullpath_file)
	return files


def get_hash(target_file):
	with open(target_file, "rb") as file_to_hash:
		file_content = file_to_hash.read()
	return hashlib.md5(file_content).hexdigest()


def main():
	start = time.perf_counter()
	files = get_files(work_dir)
	files_full_path = make_full_path(files, work_dir)
	#for file in files_full_path:
	#	print(get_hash(file))
	# Multi-processing
	with concurrent.futures.ThreadPoolExecutor() as execpool:
		execpool.map(get_hash, files_full_path)
	# Thread
	#with concurrent.futures.ThreadPoolExecutor() as execpool:
	#	execpool.map(get_hash, files_full_path)
	end = time.perf_counter()
	run_time = end - start
	print(f'Total time {run_time:.4f}')


if __name__ == '__main__':
	main()
