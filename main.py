# 在这个文件中编写代码
def has_duplicates(lst):
    """
    检查列表中是否有重复元素
    参数: lst - 任意列表
    返回: bool - 如果有重复元素返回 True，否则返回 False
    """
    # 学生实现代码区域
 
    seen = set()
    for item in lst:
       
        if item in seen:
            return True
      
        seen.add(item)
   
    return False

if __name__ == "__main__":

    test_cases = [
        [1, 2, 3, 4, 5],         
        [1, 2, 3, 4, 2],          
        ['a', 'b', 'c', 'a'],     
        [],                      
        [True, False, True],      
        [1, '1', 1.0],            
        [5, 5, 5, 5]             
    ]

    print("重复元素判定测试结果：")
    for i, test_list in enumerate(test_cases, 1):
        result = has_duplicates(test_list)
        print(f"测试用例 {i}: {test_list} → {result}")
    
    # 测试每个用例，编写具体测试代码
