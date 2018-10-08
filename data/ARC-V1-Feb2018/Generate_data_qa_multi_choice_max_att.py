import json
import ast
dataset = "Easy"  ## "Challenge"

set1 = "dev"

if dataset == "Easy":
    if set1 == "test":
        json_data=open("ARC-Easy/ARC-Easy-Test_just.jsonl","r")
        json_data_write=open("ARC-Easy/ARC-Easy-Test_Good_just.jsonl","w")
        justification_file = open("/Users/vikasy/SEM_5/ARC_EASY_Clark_Just/Easy_BIDAF_test_3_60_explanations_BM25.txt","r")
        cand_rankings = open("/Users/vikasy/SEM_5/ARC_EASY_Clark_Just/Easy_test_ranking.txt","r").readlines()
    elif set1 == "train":
        json_data = open("ARC-Easy/ARC-Easy-Train_just.jsonl", "r")
        json_data_write = open("ARC-Easy/ARC-Easy-Train_Good_just.jsonl", "w")
        justification_file = open("/Users/vikasy/SEM_5/ARC_EASY_Clark_Just/Easy_BIDAF_train_3_60_explanations_BM25.txt","r")
        cand_rankings = open("/Users/vikasy/SEM_5/ARC_EASY_Clark_Just/Easy_train_ranking.txt", "r").readlines()
    elif set1 == "dev":
        json_data = open("ARC-Easy/ARC-Easy-Dev_just.jsonl", "r")
        json_data_write = open("ARC-Easy/ARC-Easy-Dev_Good_just.jsonl", "w")
        justification_file = open("/Users/vikasy/SEM_5/ARC_EASY_Clark_Just/Easy_BIDAF_dev_3_60_explanations_BM25.txt","r")
        cand_rankings = open("/Users/vikasy/SEM_5/ARC_EASY_Clark_Just/Easy_dev_ranking.txt", "r").readlines()

else:

    json_data=open("ARC-Challenge/ARC-Challenge-Test_just.jsonl","r")
    json_data_write=open("ARC-Challenge/ARC-Challenge-Test_Good_just.jsonl","w")

    justification_file = open("/Users/vikasy/SEM_5/ARC_Challenge_BM25/SIGIR_Challenge_test_justification.txt","r")
    # justification_file = open("/Users/vikasy/SEM_5/ARC_Challenge_BM25/Challenge_test_QuestionCand_3_60_explanations_BM25.txt","r")


charInd2Index = {"A":0, "B":1, "C":2, "D":3, "E":4}
numIndex2Index = {"1":0,"2":1,"3":2,"4":3,"5":4}


Good_justifications = []
for line in justification_file:
    all_just = line.strip().split("\t")
    good_just1 = " ".join(all_just[0].split()[1:])
    # good_just1 += " " + " ".join(all_just[1].split()[1:])

    Good_justifications.append(good_just1)

print(len(Good_justifications))

count =0
tot_len = 0
json_line_number = 0
Pval = 1  ## this is P@3
for line in json_data:
    data_dict = json.loads(line)
    ques_cand_ranking = ast.literal_eval(cand_rankings[json_line_number])  ## json line number corresponds to question number

    tot_len+=len(data_dict["question"]["choices"])
    del_list = []
    for choice_ind, choice_text in enumerate(data_dict["question"]["choices"]):
        if choice_text["label"] in charInd2Index.keys():
           lab1 = charInd2Index[choice_text["label"]]
        elif choice_text["label"] in numIndex2Index.keys():
           lab1 = numIndex2Index[choice_text["label"]]

        if lab1 in ques_cand_ranking[Pval:]:
           choice_text["text"] += " " + Good_justifications[count]
        else:
           choice_text["text"] = "dummy"
           del_list.append(choice_ind)
        count+=1
    print(del_list)

    # for index in sorted(del_list, reverse=True):
    #     del data_dict["question"]["choices"][index]


    json.dump(data_dict, json_data_write)
    json_data_write.write('\n')
    json_line_number += 1

print("total len is: ", tot_len)

