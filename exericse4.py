
# =============================================================================
# zahlen = range(1,11)
# quad_zahl = []
# 
# for zahl in zahlen: 
#     if zahl%2 == 0:
#         quad_zahl.append(zahl)
#     else: 
#         quad_zahl.append(zahl**2)
#         
# print (quad_zahl)
# =============================================================================

quad_zahl = [zahl**2 if zahl%2 != 0 else zahl for zahl in range(1,11)]

print (quad_zahl)

