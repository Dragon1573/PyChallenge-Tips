FILL, UNCERTAIN, NOTHING = '■', '_', ' '


def inputdata(inputfile):
    '''
    函数：从inputfile读取数据
    输入：@inputfile，字符串，输入文件
    输出：读取到的数据
          @height 矩阵高度
          @width 矩阵长度
          @horizdata 各行数据（Nonogram矩阵左侧数据）
          @verticdata 各列数据（Nonogram矩阵上侧数据）
    '''
    (height, width, horizdata, verticdata) = 0, 0, [], []

    #标识进入到各个步骤的常量
    STEP_NOTHING = 'NOTHING'
    STEP_READDMI = 'READDIM'
    STEP_READHRZ = 'READHRZ'
    STEP_READVRT = 'READVRT'
    currstep = STEP_NOTHING

    #打开文件
    f = open(inputfile, 'r')
    for line in f.readlines():

        #读到空行直接跳过
        if line.strip() == '':
            continue

        #去掉行尾的'\n'
        if line[-1] == '\n':
            line = line[:-1]

        #处理读到的数据
        if line.startswith('# Dimensions'):   #读取维度
            currstep = STEP_READDMI
        elif line.startswith('# Horizontal'): #读取矩阵高度
            currstep = STEP_READHRZ
        elif line.startswith('# Vertical'):   #读取矩阵长度
            currstep = STEP_READVRT
        else:                                 #读取数据
            if currstep == STEP_READDMI:      #读取维度
                elements = line.split(' ')
                if elements[0].isdigit() and elements[1].isdigit():
                    height = int(elements[0])
                    width = int(elements[1])
                else:
                    raise Exception("CANNOT READ DIMENSION")
            elif currstep == STEP_READHRZ:    #读取各行数据
                elements = line.split(' ')
                horizdata.append(
                    [int(ele) for ele in elements if ele != '0' and ele.isdigit()])
            elif currstep == STEP_READVRT:    #读取各列数据
                elements = line.split(' ')
                verticdata.append(
                    [int(ele) for ele in elements if ele != '0' and ele.isdigit()])
 
    #关闭文件   
    f.close()
    
    return (height, width, horizdata, verticdata)


def outputdata(outputfile, matrix):
    '''
    函数：将matrix内容输出到文件outputfile
    输入 @ouputfile：字符串，保存到的文件
    输入 @matrix：一个二维列表
    '''

    f = open(outputfile, 'w')
    output = ''
    title = '  | '
    counter = 0
    for row in matrix:
        title += hex(counter + 1).upper()[-1] + ' '
        output += hex(counter + 1).upper()[-1] + ' | ' + ' '.join(row) + '\n'
        counter += 1
    f.write(title + '\n' + '-' * (len(title)) + '\n' + output)
    f.close()


def alternatives(data, length):
    '''
    函数：指出某一行或某一列所有可能的填充方案
    输入 @data：列表
    输入 @length：可填充长度
    输出 @result：列表，可能的填充方案
    '''

    datalen = len(data)
    datasum = sum(data)

    #如果一行或一列不需要任何填充，直接返回唯一的全空备选方案
    if datalen == 0:
        return [UNCERTAIN * length]

    j = 0
    result = []
    if datalen == 1:
        j = 1
    for i in range(length - datalen + 1 - datasum + 1):
        header = UNCERTAIN * i + FILL * data[0] + UNCERTAIN * (1 - j)
        if j:
            tails = [UNCERTAIN * (length - len(header))]
        else:
            tails = alternatives(data[1:], (length - len(header)))
        result.extend([header + tail for tail in tails])
    return result


def decide(alterset, idx):
    '''
    函数：根据某行/列备选组合判断改行/列第idx格是否可判定（一定填充或一定不填充）
    输入 @alterset：备选方案集
    输入 @id：（备选方案的）第idx个格子
    输出 @mark：None：不能确定 FILL：一定填充 NOTHING：一定不填充
    '''

    mark = alterset[0][idx]
    for j in range(1, len(alterset)):
        if mark != alterset[j][idx]:
            return None
    return FILL if mark == FILL else NOTHING


def deleteillegal(alterset, idx, mark):
    '''
    函数：去除非法的候选组合
    输入 @alterset：备选方案集
    输入 @id：（备选方案的）第idx个格子
    输入 @mark：标记，指出该格子一定填充或一定不填充，
                如果备选方案与判定结果不符，则是非法方案，应该删掉
    '''    

    if alterset != 'ELIMINATED' and len(alterset) > 1:
        mark = FILL if mark == FILL else UNCERTAIN
        for i in range(len(alterset) - 1, -1, -1): #删除要从后向前删
            if alterset[i][idx] != mark:
                alterset.pop(i)


def drawpic(inputfile, outputfile):
    '''
    函数：绘制题解
    输入 @inputfile：字符串，输入的文件地址
    输入 @outputfile：字符串，输出到的文件地址
    '''

    #读取数据
    (height, width, horizdata, verticdata) = inputdata(inputfile)

    #所有可能的候选组合
    alterh = [alternatives(data, width) for data in horizdata]
    alterv = [alternatives(data, height) for data in verticdata]

    counter = 0             #遍历变量
    total = height * width  #矩阵总元素数
    matrix = []             #结果矩阵

    #初始化矩阵
    for i in range(height):
        matrix.append([UNCERTAIN] * width)

    #循环逐行考虑、逐列考虑
    while counter < total:

        for i in range(height):                             #逐行考虑

            if alterh[i] == 'ELIMINATED':                   #不考虑已经考虑完毕的行
                continue
            if len(alterh[i]) == 0:                         #某行无备选方案，报错
                raise Exception("LACK OF ALTERNATIVES")
            elif len(alterh[i]) == 1:                       #该行只有一种选择的情况
                for j in range(width):                      #逐列筛选可能的组合
                    if matrix[i][j] == UNCERTAIN:           #标记该行剩余未判定信息
                        matrix[i][j] = NOTHING if alterh[i][0][j] != FILL else FILL 
                        counter += 1                        #已判定方格数也要+1
                        deleteillegal(alterv[j], i, matrix[i][j])   
                                                            #删除不可能正确的列组合
                    elif matrix[i][j] != alterh[i][0][j] and alterh[i][0][j] != UNCERTAIN:
                        raise Exception("LACK OF ALTERNATIVES")
                                                            #唯一备选方案与实际不符的情况
                alterh[i] = 'ELIMINATED'                    #该行已经考虑完毕，打上标记
            else:
                for j in range(width):                      #逐列筛选可能的组合
                    if matrix[i][j] != UNCERTAIN:           #只考虑空闲的方格
                        continue
                    mark = decide(alterh[i], j)             #判断第i行第j格是否可判定
                    if mark is not None:                    #该方格可判定的情况
                        matrix[i][j] = mark                 #标记该方格我们判定好的值
                        counter += 1                        #已判定方格数+1
                        deleteillegal(alterv[j], i, mark)   #删除不可能正确的列组合

        for i in range(width):                              #逐列考虑

            if alterv[i] == 'ELIMINATED':                   #不考虑已经考虑完毕的列
                continue
            if len(alterv[i]) == 0:                         #某列无备选方案，报错
                raise Exception("LACK OF ALTERNATIVES")
            elif len(alterv[i]) == 1:                       #该列只有一种选择的情况
                for j in range(height):                     #逐行筛选可能的组合
                    if matrix[j][i] == UNCERTAIN:           #标记该列剩余未判定信息
                        matrix[j][i] = NOTHING if alterv[i][0][j] != FILL else FILL
                        counter += 1                        #已判定方格数也要+1
                        deleteillegal(alterh[j], i, matrix[j][i])   
                                                            #删除不可能正确的行组合
                    elif matrix[j][i] != alterv[i][0][j] and alterv[i][0][j] != UNCERTAIN:   
                        raise Exception("LACK OF ALTERNATIVES")
                                                            #唯一备选方案与实际不符的情况
                alterv[i] = 'ELIMINATED'                    #该列已经考虑完毕，打上标记
            else:
                for j in range(height):                     #逐行筛选可能的组合
                    if matrix[j][i] != UNCERTAIN:           #只考虑空闲的方格
                        continue
                    mark = decide(alterv[i], j)             #判断第i列第j格是否可判定
                    if mark is not None:                    #该方格可判定的情况
                        matrix[j][i] = mark                 #标记该方格我们判定好的值
                        counter += 1                        #已判定方格数+1
                        deleteillegal(alterh[j], i, mark)   #删除不可能正确的行组合

    #输出数据
    outputdata(outputfile, matrix)
