import json

json_data=open("ARC-Challenge/ARC-Challenge-Test_as_entailment_default.jsonl","r")
# json_data_write=open("ARC-Challenge/ARC-Challenge-Test_as_entailment_default.jsonl","w")

justification_file = open("/Users/vikasy/SEM_5/ARC_Challenge_BM25/Challenge_test_QuestionCand_3_60_explanations_BM25.txt","r")

Good_justifications = []
for line in justification_file:
    all_just = line.strip().split("\t")
    good_just1 = " ".join(all_just[0].split()[1:])
    # good_just1+="."
    good_just1 += " " + " ".join(all_just[1].split()[1:])

    Good_justifications.append(good_just1)


print(len(Good_justifications))

count =0
tot_len = 0
for line in json_data:

    # print(count)
    data_dict = json.loads(line)
    count+=1
    if count==1:
       print(data_dict["question"])
       print(data_dict)
    """
    new_para = ""
    for choice_text in data_dict["question"]["choices"]:
        new_para += " " + Good_justifications[count]
        count+=1
    
    data_dict["para"]=new_para
    json.dump(data_dict, json_data_write)
    json_data_write.write('\n')
    """

print("total len is: ", tot_len)

