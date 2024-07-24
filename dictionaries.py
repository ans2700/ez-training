#which party wins and by how much3*
cong={7:5,18:22,32:8,71:5,66:6}
bjp={7:15,18:20,32:4,71:9,66:2}
cong_sum=0
bjp_sum=0
for age,votes in cong.items():
    if age>=18:
        cong_sum+=votes
print(cong_sum)
for age,votes in bjp.items():
    if age>=18:
        bjp_sum+=votes
print(bjp_sum)
diff=abs(cong_sum-bjp_sum)
if cong_sum>bjp_sum:
    print('congress win:',diff)
else:
    print('bjp win:',diff)
