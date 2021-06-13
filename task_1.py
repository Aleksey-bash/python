with open('nginx_logs.txt') as f:
    result_list = []
    for line in f:
        chunks_line = line.split()
        result_list.append((chunks_line[0], chunks_line[5].replace('"', ''), chunks_line[6]))
print(result_list)


