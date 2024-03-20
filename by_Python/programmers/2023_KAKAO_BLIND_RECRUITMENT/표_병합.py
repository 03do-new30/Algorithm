




def solution(commands):
    parents = [x for x in range(2501)]
    cells = ["" for _ in range(2501)]
    answer = []

    def get_address(r, c):
        address = 50 * (r-1) + c
        return address

    def get_ancestor(address):
        if parents[address] == address:
            return address
        return get_ancestor(parents[address])
    
    def update_ancestor(superior, inferior):
        # inferior 값을 가지고 있는 셀들을 superior에 종속되도록 한다
        for i in range(len(parents)):
            if parents[i] == inferior:
                parents[i] = superior
                print(" > {0}는 {1}에 병합됨".format(i, superior))
                # 기존에 가지고 있던 값을 없애고, superior의 값으로 세팅한다
                cells[i] = cells[superior]
                print(" > {0}의 값은 {1}로 됨".format(i, cells[superior]))
    
    def get_addresses_with_value(value):
        ret = []
        for i in range(len(cells)):
            if cells[i] == value:
                ret.append(i)
        return ret


    for command in commands:
        command = command.split()
        job = command[0]

        if job == "UPDATE":
            print(">>> doing UPDATE")
            if len(command) == 4:
                r, c, value = int(command[1]), int(command[2]), command[3]
                address = get_address(r, c)
                ancestor = get_ancestor(address)
                # ancestor에 묶여 있는 모든 셀의 값을 value로 업데이트
                
                for i in range(len(parents)):
                    if parents[i] == ancestor:
                        cells[i] = value
                        print(" > {0}의 값은 {1}".format(i, value))
            elif len(command) == 3:
                value1, value2 = command[1], command[2]

                # value1을 값으로 가지는 모든 셀을 선택
                addresses_1 = get_addresses_with_value(value1)
                ancestors_1 = []
                for addr in addresses_1:
                    ancestor = get_ancestor(addr)
                    if ancestor not in ancestors_1:
                        ancestors_1.append(ancestor)
                
                # 조상이 ancestors_1 에 들어가 있는 셀들의 값을 모두 value2로 바꿈
                change_addresses = []
                for i in range(len(parents)):
                    if parents[i] in ancestors_1:
                        change_addresses.append(i)
                print(" > {0}에 포함된 셀들의 현재 값: {1}".format(change_addresses, value1))
                for addr in change_addresses:
                    cells[addr] = value2
                    print(" > {0}의 값 변경: {1}".format(addr, cells[addr]))
                
            
        elif job == "MERGE":
            r1, c1 = int(command[1]), int(command[2])
            r2, c2 = int(command[3]), int(command[4])
            cell_1 = get_ancestor(get_address(r1, c1))
            cell_2 = get_ancestor(get_address(r2, c2))
            
            print(">>> doing MERGE")
            if cell_1 == cell_2:
                print(" > 선택한 두 위치가 같은 셀이므로 무시")
                continue

            superior = cell_1 # 병합의 기준이 되는 셀
            inferior = cell_2
            if cells[cell_1] == "" and cells[cell_2] != "":
                superior, inferior = cell_2, cell_1
            
            update_ancestor(superior, inferior)
            
        elif job == "UNMERGE":
            r, c = int(command[1]), int(command[2])
            ancestor = get_ancestor(get_address(r, c)) # (r, c)가 병합되어 있던 상위 셀을 구함

            print(">>> doing UNMERGE")
            # 병합을 해제하기 전 셀의 값
            old_value = cells[ancestor]
            print(" > 병합 해제하기 전 셀의 값:", old_value)
            # ancestor에 병합되어 있던 셀들의 병합을 해제한다
            for i in range(len(parents)):
                if parents[i] == ancestor:
                    print(" > {0} 셀 초기화".format(i))
                    parents[i] = i
                    cells[i] = ""
            # 병합을 해제하기 전 셀이 값을 가지고 있었을 경우 (r, c) 위치의 셀이 그 값을 가지게 됨
            if old_value != "":
                print(" > ({0}, {1}) 셀이 {2} 값을 가짐".format(r, c, old_value))
                cells[get_address(r, c)] = old_value
            
        elif job == "PRINT":
            print(" >>> doing PRINT")
            r, c = int(command[1]), int(command[2])
            address = get_address(r, c)
            if cells[address] == "":
                answer.append("EMPTY")
            else:
                answer.append(cells[address])
        print()
    print("answer:", answer)
    return answer

commands = [
    ["UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean", "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle", "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle", "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4", "PRINT 1 3", "PRINT 1 4"],
    ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2", "MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"],
    ["MERGE 1 1 2 2", "MERGE 1 1 3 3", "UPDATE 3 3 A", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3"],
    ["UPDATE 1 1 A", "UPDATE 2 2 B", "UPDATE 3 3 C", "UPDATE 4 4 D", "MERGE 1 1 2 2", "MERGE 3 3 4 4", "MERGE 1 1 3 3", "UNMERGE 1 1", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3", "PRINT 4 4"],
    ["UPDATE 50 50 100", "UPDATE 100 100", "PRINT 50 50"],
    ["UPDATE 1 1 apple", "MERGE 1 1 2 2", "MERGE 2 2 3 3", "UNMERGE 1 1", "UNMERGE 2 2", "PRINT 1 1", "PRINT 2 2", "PRINT 3 3"]
]

result = [
    ["EMPTY", "group"],
    ["d", "EMPTY"],
    ["A", "A", "A"],
    ["A","EMPTY","EMPTY","EMPTY"],
    ["100"],
    ["apple", "EMPTY", "EMPTY"]
]

for i in range(len(result)):
    print('*' * 50, solution(commands[i]) == result[i])
    print('-' * 40)