def make_list_of_files(n):
   filenames = []
   for i in range(n):
        filenames.append(f"file_{i}.txt")
   return filenames

print(make_list_of_files(5)) #['file_0.txt', 'file_1.txt', 'file_2.txt', 'file_3.txt', 'file_4.txt']