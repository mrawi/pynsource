# test graphs

TEST_GRAPH1 = """
{'type':'node', 'id':'D25', 'x':7, 'y':6, 'width':159, 'height':106}
{'type':'node', 'id':'D13', 'x':6, 'y':119, 'width':119, 'height':73}
{'type':'node', 'id':'m1', 'x':171, 'y':9, 'width':139, 'height':92}
"""

TEST_GRAPH2 = """
{'type':'node', 'id':'D25', 'x':7, 'y':6, 'width':159, 'height':106}
{'type':'node', 'id':'D13', 'x':6, 'y':119, 'width':119, 'height':73}
{'type':'node', 'id':'m1', 'x':146, 'y':179, 'width':139, 'height':92}
{'type':'node', 'id':'D97', 'x':213, 'y':6, 'width':85, 'height':159}
"""

TEST_GRAPH3 = """
{'type':'node', 'id':'D25', 'x':7, 'y':6, 'width':159, 'height':106}
{'type':'node', 'id':'D13', 'x':6, 'y':119, 'width':119, 'height':73}
{'type':'node', 'id':'m1', 'x':246, 'y':179, 'width':139, 'height':92}
{'type':'node', 'id':'D97', 'x':213, 'y':6, 'width':85, 'height':159}
{'type':'node', 'id':'D98', 'x':340, 'y':7, 'width':101, 'height':107}
"""

TEST_GRAPH4 = """
{'type':'node', 'id':'D25', 'x':7, 'y':6, 'width':159, 'height':106}
{'type':'node', 'id':'D13', 'x':6, 'y':119, 'width':119, 'height':73}
{'type':'node', 'id':'m1', 'x':6, 'y':214, 'width':139, 'height':92}
{'type':'node', 'id':'D97', 'x':213, 'y':6, 'width':85, 'height':159}
{'type':'node', 'id':'D98', 'x':305, 'y':57, 'width':101, 'height':107}
{'type':'node', 'id':'D50', 'x':149, 'y':184, 'width':242, 'height':112}
{'type':'node', 'id':'D51', 'x':189, 'y':302, 'width':162, 'height':66}
"""

TEST_GRAPH6 = """
{'type':'node', 'id':'AAAAAAAAAAA', 'x':113, 'y':12, 'width':84, 'height':126}
{'type':'node', 'id':'A', 'x':13, 'y':12, 'width':84, 'height':126}
{'type':'node', 'id':'B', 'x':122, 'y':11, 'width':157, 'height':79}
{'type':'node', 'id':'C', 'x':8, 'y':292, 'width':194, 'height':91}
{'type':'node', 'id':'m1', 'x':102, 'y':95, 'width':123, 'height':144}
{'type':'edge', 'id':'A_to_B', 'source':'A', 'target':'B'}
{'type':'edge', 'id':'A_to_C', 'source':'A', 'target':'C'}
"""

TEST_GRAPH7 = """
{'type':'node', 'id':'A', 'x':10, 'y':10, 'width':250, 'height':250}
{'type':'node', 'id':'c', 'x':265, 'y':90, 'width':60, 'height':60}
{'type':'node', 'id':'m1', 'x':265, 'y':15, 'width':60, 'height':60}
{'type':'edge', 'id':'c_to_m1', 'source':'c', 'target':'m1'}
{'type':'edge', 'id':'A_to_c', 'source':'A', 'target':'c'}
"""

GRAPH_SPRING2 = """
{'type':'node', 'id':'A', 'x':111, 'y':304, 'width':160, 'height':52}
{'type':'node', 'id':'A1', 'x':10, 'y':249, 'width':160, 'height':160}
{'type':'node', 'id':'A2', 'x':15, 'y':365, 'width':160, 'height':160}
{'type':'node', 'id':'B', 'x':257, 'y':85, 'width':160, 'height':160}
{'type':'node', 'id':'B1', 'x':115, 'y':35, 'width':160, 'height':160}
{'type':'node', 'id':'B2', 'x':274, 'y':191, 'width':160, 'height':160}
{'type':'node', 'id':'B21', 'x':172, 'y':144, 'width':160, 'height':160}
{'type':'node', 'id':'B22', 'x':390, 'y':150, 'width':62, 'height':70}
{'type':'node', 'id':'c', 'x':260, 'y':316, 'width':160, 'height':160}
{'type':'node', 'id':'c1', 'x':382, 'y':292, 'width':160, 'height':160}
{'type':'node', 'id':'c2', 'x':375, 'y':366, 'width':160, 'height':160}
{'type':'node', 'id':'c3', 'x':288, 'y':422, 'width':160, 'height':160}
{'type':'node', 'id':'c4', 'x':194, 'y':402, 'width':160, 'height':160}
{'type':'node', 'id':'c5', 'x':194, 'y':250, 'width':56, 'height':50}
{'type':'edge', 'id':'A_to_A1', 'source':'A', 'target':'A1'}
{'type':'edge', 'id':'A_to_A2', 'source':'A', 'target':'A2'}
{'type':'edge', 'id':'B_to_B1', 'source':'B', 'target':'B1'}
{'type':'edge', 'id':'B_to_B2', 'source':'B', 'target':'B2'}
{'type':'edge', 'id':'B2_to_B21', 'source':'B2', 'target':'B21'}
{'type':'edge', 'id':'B2_to_B22', 'source':'B2', 'target':'B22'}
{'type':'edge', 'id':'c_to_c1', 'source':'c', 'target':'c1'}
{'type':'edge', 'id':'c_to_c2', 'source':'c', 'target':'c2'}
{'type':'edge', 'id':'c_to_c3', 'source':'c', 'target':'c3'}
{'type':'edge', 'id':'c_to_c4', 'source':'c', 'target':'c4'}
{'type':'edge', 'id':'c_to_c5', 'source':'c', 'target':'c5'}
{'type':'edge', 'id':'A_to_c', 'source':'A', 'target':'c', 'weight':5}
{'type':'edge', 'id':'B2_to_c', 'source':'B2', 'target':'c'}
{'type':'edge', 'id':'B2_to_c5', 'source':'B2', 'target':'c5'}
{'type':'edge', 'id':'A_to_c5', 'source':'A', 'target':'c5'}
"""

GRAPH_SPRING3 = """
{'type':'node', 'id':'A', 'x':479, 'y':185, 'width':250, 'height':250}
{'type':'node', 'id':'A1', 'x':556, 'y':61, 'width':60, 'height':60}
{'type':'node', 'id':'A2', 'x':449, 'y':57, 'width':60, 'height':60}
{'type':'node', 'id':'B', 'x':109, 'y':89, 'width':60, 'height':60}
{'type':'node', 'id':'B1', 'x':10, 'y':10, 'width':60, 'height':60}
{'type':'node', 'id':'B2', 'x':223, 'y':177, 'width':60, 'height':60}
{'type':'node', 'id':'B21', 'x':262, 'y':50, 'width':60, 'height':60}
{'type':'node', 'id':'B22', 'x':99, 'y':244, 'width':100, 'height':200}
{'type':'node', 'id':'c', 'x':345, 'y':294, 'width':60, 'height':60}
{'type':'node', 'id':'c1', 'x':211, 'y':339, 'width':60, 'height':60}
{'type':'node', 'id':'c2', 'x':457, 'y':440, 'width':60, 'height':60}
{'type':'node', 'id':'c3', 'x':280, 'y':423, 'width':60, 'height':60}
{'type':'node', 'id':'c4', 'x':394, 'y':428, 'width':60, 'height':60}
{'type':'node', 'id':'c5', 'x':348, 'y':169, 'width':60, 'height':120}
{'type':'node', 'id':'D4', 'x':734, 'y':168, 'width':147, 'height':66}
{'type':'node', 'id':'D98', 'x':710, 'y':440, 'width':160, 'height':63}
{'type':'node', 'id':'D33', 'x':734, 'y':269, 'width':135, 'height':109}
{'type':'edge', 'id':'A_to_A1', 'source':'A', 'target':'A1'}
{'type':'edge', 'id':'A_to_A2', 'source':'A', 'target':'A2'}
{'type':'edge', 'id':'B_to_B1', 'source':'B', 'target':'B1'}
{'type':'edge', 'id':'B_to_B2', 'source':'B', 'target':'B2'}
{'type':'edge', 'id':'B2_to_B21', 'source':'B2', 'target':'B21'}
{'type':'edge', 'id':'B2_to_B22', 'source':'B2', 'target':'B22'}
{'type':'edge', 'id':'c_to_c1', 'source':'c', 'target':'c1'}
{'type':'edge', 'id':'c_to_c2', 'source':'c', 'target':'c2'}
{'type':'edge', 'id':'c_to_c3', 'source':'c', 'target':'c3'}
{'type':'edge', 'id':'c_to_c4', 'source':'c', 'target':'c4'}
{'type':'edge', 'id':'c_to_c5', 'source':'c', 'target':'c5'}
{'type':'edge', 'id':'A_to_c', 'source':'A', 'target':'c'}
{'type':'edge', 'id':'B2_to_c', 'source':'B2', 'target':'c'}
{'type':'edge', 'id':'B2_to_c5', 'source':'B2', 'target':'c5'}
{'type':'edge', 'id':'A_to_c5', 'source':'A', 'target':'c5'}
{'type':'edge', 'id':'D33_to_A', 'source':'D33', 'target':'A'}
{'type':'edge', 'id':'D33_to_D98', 'source':'D33', 'target':'D98'}
{'type':'edge', 'id':'D33_to_D4', 'source':'D33', 'target':'D4'}
{'type':'edge', 'id':'D4_to_A', 'source':'D4', 'target':'A'}
"""