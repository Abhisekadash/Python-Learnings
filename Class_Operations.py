import os
class FileOps:
	def read_data_as_string(self,file_name):
		try:
			f=open(file_name,"r")
			return f.read()
		except Exception as e:
			print("Exception:",e)
	def get_line_count(self,file_name):
		try:
			num_lines=1
			for line in file_name:
				num_lines += 1
				return num_lines
		except Exception as e:
			raise e
	def delete_file(self,file_name):
		try:
			os.remove(file_name)
			print("OK removed")
		except Exception as e:
			print("Not removed")
	def copy_file(self,src_file_name,dest_file_name):
		try:
			with open(src_file_name)as f:
				with open(dest_file_name,"w") as f1:
					for line in f:
						f1.write(line)
			print("Ok Copied")
		except Exception as e:
			print("NOt Copied")
f=FileOps()
data=f.read_data_as_string("novel.txt")
print(data)
file_line_count=f.get_line_count(data)
print(file_line_count)
f.delete_file("novel.txt")
f.copy_file("F:\Python\story.txt","check_file.txt")